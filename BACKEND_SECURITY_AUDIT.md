# BACKEND SECURITY AUDIT — MyOwnClone

> Current state of auth, multi-tenancy, and admin access control.

## 1. Stack

- Flask 3 + Flask-RESTX 1.3 + SQLAlchemy 2.0 + Flask-Migrate
- JWT HS256 via PyJWT
- bcrypt for password hashing
- PostgreSQL (Dify base tables + MyOwnClone additions)
- 2 auth paths:
  1. `Authorization: Bearer <jwt>` — user JWT
  2. `X-Admin-Token: <PLATFORM_ADMIN_TOKEN>` — service token from Next.js proxy

## 2. What is solid

- **JWT secret loaded from env**, with a dev default fallback (`dev-secret-change-me`). Production must override.
- **Constant-time token compare** in `_check_service_token` (`hmac.compare_digest`).
- **Password hashing with bcrypt** in `auth.py`.
- **Service token is logged only as the first 8 chars** (`token_str[:8]`) in audit and log lines; raw token is never written to disk.
- **Impersonation token stored as SHA-256(token || pepper)** in `impersonation_tokens.token`, so a DB dump does not leak usable tokens.
- **All admin endpoints require `platform_admin` role**, checked via `_require_platform_admin()` which:
  1. Reads `g.account_role` from JWT claim (fast path).
  2. Falls back to DB `accounts.role` lookup (covers dev path).
  3. Honors `DEV_PLATFORM_ADMIN_BYPASS=true` env override (DEV ONLY).
- **Audit log is append-only** and captures IP + user-agent.
- **`_validate_required_env()` refuses to start** if `DB_PASSWORD` is missing or trivially weak (`postgres`, `changeit`).
- **Sensitive endpoints return specific errors** (e.g. `tenant_not_found` is 404, not 200 with empty body).

## 3. Risks and gaps (action items)

### 3.1 Dev stubs in production path

**File**: `api/api/controllers/console/wraps.py`

```python
def account_initialization_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not hasattr(g, 'account') or g.account is None:
            # DEV STUB: set dummy account so endpoints are reachable
            g.account = type('obj', (object,), {'id': 'dev-account-id'})()
            g.account_id = 'dev-account-id'
        return f(*args, **kwargs)
    return decorated_function


def setup_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not hasattr(g, 'workspace') or g.workspace is None:
            # DEV STUB: set dummy workspace so endpoints are reachable
            g.workspace = type('obj', (object,), {'id': 'dev-workspace-id'})()
        return f(*args, **kwargs)
    return decorated_function
```

**Risk**: If a future bug causes `g.account_id` to be unset, the request is silently treated as a dev account. In production this is a privilege bypass.

**Fix (Phase B2/B3)**: Wrap with an environment check:

```python
import os
IS_DEV = os.getenv("FLASK_ENV", "production") == "development"

def account_initialization_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not getattr(g, 'account_id', None):
            if IS_DEV:
                g.account_id = 'dev-account-id'
                g.account = type('obj', (object,), {'id': 'dev-account-id'})()
            else:
                return {'error': 'account_not_initialized', 'message': '...'}, 401
        return f(*args, **kwargs)
    return decorated_function
```

### 3.2 Circular import risk in `_verify_token`

`api/api/libs/login.py` imports `from api.controllers.console.auth import _verify_token`. Both live in the same package. The order works today because `app_factory.py` imports `auth_bp` first, but a refactor could break this.

**Fix (Phase B4)**: Move `_verify_token` (and `_get_secret_key`) to `api/api/libs/jwt_utils.py`, and have `auth.py` and `login.py` both import from there.

### 3.3 Duplicate tree at `api/`

Two parallel package trees:
- `api/api/` (registered by `app_factory.py`, used at runtime)
- `api/` (root, no registration evidence — appears to be a leftover)

**Risk**: any future refactor that touches the wrong file is silently broken.

**Fix (Phase B1)**: grep first to confirm zero imports, then either:
- Add `pyproject.toml`/`MANIFEST.in` so only `api/api/` is shipped.
- Or delete `api/`.

Document the result.

### 3.4 No automated tests

`pytest` is in `requirements.txt` (indirectly, via Flask) but there is no `tests/` folder and no `pytest.ini`.

**Fix (Phase B5)**: add `api/tests/conftest.py` with a Flask test client, and one smoke test per admin endpoint:
- 401 (no auth)
- 403 (non-admin)
- 200 with empty DB (admin)
- Specific assertions per endpoint shape

### 3.5 `dev-pepper-rotate-in-prod` default for `IMPERSONATION_TOKEN_PEPPER`

If a deployment forgets to set this env var, the pepper is a constant. Token hashes become guessable to anyone with DB access.

**Fix (Phase B6)**:
1. In production (`FLASK_ENV != "development"`), refuse to start if the default value is detected.
2. Document the env var in `.env.example` and the README.

### 3.6 MRR calculation uses Python-side `case()` over a static alias map

If a new plan is added to the DB without updating `PLAN_NAME_ALIASES_DB_TO_API` and `PLAN_PRICES_CENTS`, it silently contributes 0 cents to MRR.

**Fix (Phase B7)**: add a test that asserts every plan in `myownclone_plans.name` has a price entry. Surface unpriced plans in the admin overview as a warning.

### 3.7 `default="member"` on `Account.role` may hide role escalation

If a future migration changes the default, the DB could end up with a mix. Acceptable for now, but document the audit expectation: "every account with `role='platform_admin'` must be reviewed in the audit log".

### 3.8 No CORS allowlist

`CORS(app)` is wide open.

**Fix (Phase B6)**: in production, allow only the known Next.js origin:

```python
CORS(app, resources={r"/console/api/*": {"origins": os.getenv("ALLOWED_ORIGINS", "").split(",")}})
```

## 4. Multi-tenancy

- Every MyOwnClone table except `accounts`, `tenants`, `myownclone_plans`, `admin_audit_log`, `impersonation_log`, `impersonation_tokens`, `cost_tracking` (which has `tenant_id` but is also summed globally in admin) is implicitly tenant-scoped by application convention. **No `tenant_id` is enforced at the ORM level.**
- Admin endpoints (in `admin_platform.py`) explicitly use global queries and bypass tenant scoping — this is by design.
- Non-admin endpoints must use `current_tenant_id` to scope queries. **No automated test verifies this.** Manual review pending.

## 5. Action plan summary

| ID | Item | Phase | Priority |
|---|---|---|---|
| B1 | Confirm/remove duplicate `api/` tree | B | High |
| B2 | Make `account_initialization_required` strict in prod | B | High |
| B3 | Make `setup_required` strict in prod | B | High |
| B4 | Move JWT helpers to `libs/jwt_utils.py` | B | Med |
| B5 | Add `pytest` smoke tests for admin endpoints | B | Med |
| B6 | Document env vars + production guards for `IMPERSONATION_TOKEN_PEPPER` and `CORS` | B | Med |
| B7 | Add a "unpriced plans" warning in overview | C5/C6 | Low |

## 6. Verification checklist

- [ ] `curl -X GET /console/api/myownclone/admin/overview` with no auth → 401
- [ ] Same with valid user JWT but `role=member` → 403
- [ ] Same with `X-Admin-Token` matching `PLATFORM_ADMIN_TOKEN` → 200
- [ ] With DB empty → 200, all numbers 0, `plan_breakdown` has 5 canonical keys
- [ ] `POST /admin/impersonate` with `reason="short"` → 400
- [ ] `POST /admin/impersonate` with non-existent tenant → 404
- [ ] `POST /admin/impersonate/stop` with no token → 400
- [ ] `POST /admin/impersonate/stop` with expired token → 404
- [ ] Impersonation token in DB matches `SHA-256(raw || pepper)`, not raw
- [ ] Audit log has rows for impersonation_started, impersonation_stopped, tenant_updated, tenant_created
- [ ] `PLATFORM_ADMIN_TOKEN` env override is required in production

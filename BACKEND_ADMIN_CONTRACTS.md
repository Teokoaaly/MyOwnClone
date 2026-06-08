# BACKEND ADMIN CONTRACTS — MyOwnClone

> Canonical API contracts for platform-admin endpoints. Source of truth is `api/api/controllers/console/myownclone/admin_platform.py`. This document is the version we promise to clients (Next.js proxy, internal scripts).

## 0. Conventions

- **Base path**: `/console/api/myownclone/admin/*`
- **Content-Type**: `application/json` for all responses
- **Auth**: `Authorization: Bearer <jwt>` OR `X-Admin-Token: <PLATFORM_ADMIN_TOKEN>` (service-to-service from Next.js proxy)
- **Authorization**: every endpoint requires `role == "platform_admin"` on the account. 401 if no session, 403 if not platform_admin.
- **Dates**: ISO-8601 UTC with explicit `Z` suffix (e.g. `2026-06-04T00:00:00Z`).
- **Money**: integer cents. Display formatted with EUR symbol in `*_display` fields.
- **Pagination**: `{ items, pagination: { page, limit, total, pages } }` — never a flat array.
- **Errors**: `{ error: "code", message: "Human readable", details?: ... }` — never just a string.

## 1. Plans and statuses (canonical)

These are the canonical English names. The DB may still store Spanish labels (`básico`, `escala`); the API normalizes at the boundary.

```
plans = ["trial", "basic", "pro", "scale", "enterprise"]
statuses = ["active", "trial", "suspended", "cancelled", "normal"]
```

ACTIVE_TENANT_STATUSES = `("active", "normal", "trial")` — used for "active_tenants" count.

## 2. Price table (cents/month, EUR)

| Plan | Price cents | Display |
|---|---|---|
| trial | 0 | 0.00€ |
| basic | 4900 | 49.00€ |
| pro | 9900 | 99.00€ |
| scale | 19900 | 199.00€ |
| enterprise | 49900 | 499.00€ |

## 3. Endpoints

### 3.1 GET /admin/overview

Returns platform-wide metrics.

**Response 200**

```json
{
  "total_tenants": 42,
  "active_tenants": 38,
  "total_clones": 117,
  "mrr_cents": 124800,
  "mrr_display": "1248.00€",
  "total_costs_cents": 48230,
  "total_costs_display": "482.30€",
  "margin_cents": 76570,
  "margin_display": "765.70€",
  "plan_breakdown": {
    "trial": 8,
    "basic": 12,
    "pro": 14,
    "scale": 6,
    "enterprise": 2
  },
  "generated_at": "2026-06-04T10:23:11Z"
}
```

**Errors**: 401, 403.

**Rules**:
- `mrr_cents` counts only `subscription_status = "active"`.
- `total_costs_cents` is the sum of `cost_tracking.cost_cents` in the last 30 days.
- `margin_cents = mrr_cents - total_costs_cents`.
- `plan_breakdown` always contains the 5 canonical keys, defaulting to 0.

### 3.2 GET /admin/tenants

Paginated tenant list.

**Query params**

| Name | Type | Default | Notes |
|---|---|---|---|
| page | int | 1 | >= 1 |
| limit | int | 20 | max 50 |
| search | string | "" | ilike on name or slug |
| status | string | "" | canonical status (active, trial, suspended, cancelled) |
| plan | string | "" | canonical plan (trial, basic, pro, scale, enterprise) |
| sort | string | "created_at" | one of: created_at, name, plan, status |
| direction | "asc" | "desc" | "asc" or "desc" |

**Response 200**

```json
{
  "items": [
    {
      "id": "tenant-uuid",
      "slug": "my-tenant",
      "name": "My Tenant",
      "plan": "pro",
      "status": "active",
      "subscription_status": "active",
      "clone_count": 3,
      "monthly_cost_cents": 1240,
      "created_at": "2026-06-04T10:00:00Z",
      "updated_at": "2026-06-04T10:00:00Z"
    }
  ],
  "pagination": { "page": 1, "limit": 20, "total": 42, "pages": 3 }
}
```

**Errors**: 401, 403.

### 3.3 GET /admin/tenants/<tenant_id>

**Response 200**

```json
{
  "tenant": {
    "id": "tenant-uuid",
    "slug": "my-tenant",
    "name": "My Tenant",
    "plan": "pro",
    "status": "active",
    "subscription_status": "active",
    "stripe_customer_id": "cus_xxx",
    "stripe_subscription_id": "sub_xxx",
    "created_at": "2026-06-04T10:00:00Z",
    "updated_at": "2026-06-04T10:00:00Z"
  },
  "usage": {
    "clone_count": 3,
    "cost_cents_30d": 1240,
    "tokens_in_30d": 230000,
    "tokens_out_30d": 89000,
    "questions_30d": 412,
    "gaps_open": 7
  },
  "clones": [
    {
      "id": "clone-uuid",
      "name": "Clone name",
      "slug": "clone-slug",
      "is_active": true,
      "language": "es",
      "created_at": "2026-06-04T10:00:00Z"
    }
  ]
}
```

**Errors**: 401, 403, 404 (`{"error":"tenant_not_found"}`).

### 3.4 PATCH /admin/tenants/<tenant_id>

**Body**

```json
{
  "plan": "scale",
  "status": "active"
}
```

Both fields optional but at least one must be present. Pydantic validates:
- `plan` ∈ `trial|basic|pro|scale|enterprise`
- `status` ∈ `normal|active|suspended|cancelled|trial`

**Response 200**

```json
{
  "ok": true,
  "tenant": { "id": "tenant-uuid", "plan": "scale", "status": "active" }
}
```

**Errors**: 400 (`invalid_payload`, `no_op`), 401, 403, 404.

**Side effects**: writes a row to `admin_audit_log` with action `tenant_updated` and metadata `{plan: {from, to}, status: {from, to}}`.

### 3.5 GET /admin/feedback

Paginated feedback list (joins CloneConfig + Tenant).

**Query params**

| Name | Type | Default |
|---|---|---|
| page | int | 1 |
| limit | int | 20 (max 50) |
| search | string | "" |
| rating | "up" | "down" | "" |
| clone_id | string | "" |
| tenant_id | string | "" |

**Response 200**

```json
{
  "items": [
    {
      "id": "fb-uuid",
      "clone_id": "clone-uuid",
      "clone_name": "Clone name",
      "tenant_id": "tenant-uuid",
      "tenant_name": "My Tenant",
      "rating": "up",
      "comment": "Great answer",
      "created_at": "2026-06-04T10:00:00Z"
    }
  ],
  "pagination": { "page": 1, "limit": 20, "total": 12, "pages": 1 }
}
```

**Errors**: 401, 403.

### 3.6 POST /admin/impersonate

**Body**

```json
{ "tenant_id": "tenant-uuid", "reason": "Support ticket #1234" }
```

`reason`: 10-1000 chars, mandatory.

**Response 200**

```json
{
  "impersonation_id": "log-uuid",
  "token": "one-time-token-string",
  "tenant_id": "tenant-uuid",
  "tenant_name": "My Tenant",
  "expires_at": "2026-06-04T10:53:00Z",
  "message": "Impersonation started — use X-Impersonate-Token header. 30 minute timeout."
}
```

**Errors**: 400 (`invalid_payload`), 401, 403, 404 (`tenant_not_found`), 500.

**Security**:
- Token stored as SHA-256(token || IMPERSONATION_TOKEN_PEPPER). Raw token returned ONCE.
- TTL: 30 minutes.
- Audit row written: action `impersonation_started`, metadata includes `token_prefix` (8 chars) for correlation.

### 3.7 POST /admin/impersonate/stop

**Body**: `{ "token": "..." }` OR `X-Impersonate-Token: ...` header.

**Response 200**: `{ "status": "stopped", "tenant_id": "..." }`

**Errors**: 400 (`no_token`), 401, 403, 404 (`no_active_impersonation`), 500.

**Security**:
- Closes the matching `impersonation_log` (not the most recent — matches `admin_id` + `tenant_id` + open).
- Deletes the `impersonation_tokens` row.
- Audit row written: action `impersonation_stopped`.

### 3.8 GET /admin/audit-log

**Query params**: page, limit, action, actor_id, target_id.

**Response 200**

```json
{
  "items": [
    {
      "id": "log-uuid",
      "actor_id": "admin-uuid",
      "action": "impersonation_started",
      "target_type": "tenant",
      "target_id": "tenant-uuid",
      "reason": "Support ticket #1234",
      "metadata": { "impersonation_log_id": "...", "expires_at": "...", "token_prefix": "abcd1234" },
      "ip_address": "1.2.3.4",
      "user_agent": "Mozilla/5.0 ...",
      "created_at": "2026-06-04T10:00:00Z"
    }
  ],
  "pagination": { "page": 1, "limit": 20, "total": 5, "pages": 1 }
}
```

### 3.9 POST /admin/courtesy

Create a tenant + account on behalf of a partner.

**Body**

```json
{
  "email": "partner@example.com",
  "name": "Partner Name",
  "plan": "pro",
  "duration_days": 30
}
```

`plan` ∈ `trial|basic|pro|scale|enterprise`, default `pro`.
`duration_days` ∈ [1, 365], default 30.

**Response 201**

```json
{
  "tenant_id": "new-tenant-uuid",
  "account_id": "new-account-uuid",
  "plan": "pro",
  "trial_ends_at": "2026-07-04T10:00:00Z"
}
```

**Errors**: 400, 401, 403, 500.

**Side effects**: writes a row to `admin_audit_log` with action `tenant_created`.

## 4. Standard error codes

| Code | Status | When |
|---|---|---|
| `unauthorized` | 401 | No session, invalid token, missing Bearer |
| `platform_admin_required` | 403 | Authenticated but not platform_admin |
| `invalid_payload` | 400 | Pydantic validation failed |
| `no_op` | 400 | PATCH with no fields to update |
| `tenant_not_found` | 404 | tenant_id does not exist |
| `no_token` | 400 | stop-impersonate with no token |
| `no_active_impersonation` | 404 | stop-impersonate token not found or expired |
| `impersonation_failed` | 500 | impersonate DB error |
| `stop_failed` | 500 | stop DB error |
| `courtesy_failed` | 500 | courtesy DB error |

## 5. Audit log actions

```
impersonation_started
impersonation_stopped
tenant_updated          # metadata: {plan: {from, to}, status: {from, to}}
tenant_created          # courtesy signup
```

## 6. Env vars expected

```
PLATFORM_ADMIN_TOKEN         service-to-service token from Next.js proxy
IMPERSONATION_TOKEN_PEPPER   pepper for SHA-256 hash of impersonation tokens
JWT_SECRET_KEY               HS256 secret for user JWT
```

## 7. Versioning

We do not yet prefix routes with `/v1/`. When the contract changes incompatibly, add `/v1/` and keep `/admin/*` as a 6-month deprecation shim.

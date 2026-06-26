# AI Costs Endpoint 500 Fix - 2026-06-26

## Problem

`GET /console/api/myownclone/ai-models/costs` returns HTTP 500 when the live
`cost_daily_rollup` table does not exist in the production Postgres database
(most likely because the `2026_06_23_0003_cost_daily_rollup` Alembic migration
was not applied during the last backend deployment).

All other admin AI endpoints respond normally:

| Endpoint | Status | Source |
| --- | --- | --- |
| `/console/api/myownclone/ai-models` | 200 | `[]` (table empty) |
| `/console/api/myownclone/ai-models/assignments` | 200 | `[]` (table empty) |
| `/console/api/myownclone/ai-models/registry-status` | 200 | cache + tasks ok |
| `/console/api/myownclone/ai-models/embedding-status` | 200 | config ok |
| `/console/api/myownclone/ai-models/costs` | **500** | **table missing** |

## Root Cause

`api/controllers/console/myownclone/ai_models.py::AIModelCostsApi.get` issues
`select(CostDailyRollup)` with no error handling. If the underlying
`cost_daily_rollup` table does not exist in the live database, SQLAlchemy
raises `sqlalchemy.exc.ProgrammingError: relation "cost_daily_rollup" does
not exist`, which propagates to Flask as an uncaught 500.

The handler does include an `else:` branch that falls back to querying
`AIInvocation` (line 397 of the M14 handler), but it only reaches that branch
when `select(CostDailyRollup).scalars().all()` returns an empty list — it
does not survive the exception thrown when the table itself is missing.

A secondary issue: the same handler accesses `row.model_id` when computing
`by_model`, but the existing test (`test_ai_model_costs_aggregates_rows`) fed
`SimpleNamespace` rows without `model_id`, so the test was already red on
the M14 baseline.

## Fix Strategy

Defensive degradation: catch `ProgrammingError` around the rollup query and
treat it as "no rollup data available", letting the existing fallback path
aggregate from `AIInvocation` instead. A second try/except protects the
per-model breakdown query so the endpoint stays 200 even if both rollup and
invocations are unavailable (returns empty series).

This approach:

- **Does not require** running `flask db upgrade` to start returning 200.
- **Does not change** the handler behavior when `cost_daily_rollup` IS
  present and populated (fast-path is unchanged).
- **Preserves** the existing `AIInvocation` fallback when the rollup is
  present but empty.
- **Logs** a warning with the SQLAlchemy exception for ops visibility.

## Files Touched

| File | Change |
| --- | --- |
| `api/controllers/console/myownclone/ai_models.py` | Added `from sqlalchemy.exc import ProgrammingError` and wrapped rollup + invocation queries in try/except. |
| `api/tests/test_ai_models_endpoints.py` | Added two regression tests for the missing-rollup case (fallback to `AIInvocation`, and full degradation). Fixed the pre-existing red test `test_ai_model_costs_aggregates_rows` to include `model_id` in its mock rows and assert `by_model`. |

## Tests

RED → GREEN cycle verified locally:

```
$ pytest api/tests/test_ai_models_endpoints.py -v

api/tests/test_ai_models_endpoints.py::test_ai_models_requires_auth PASSED
api/tests/test_ai_models_endpoints.py::test_ai_models_list_is_tenant_scoped PASSED
api/tests/test_ai_models_endpoints.py::test_ai_models_create_encrypts_plaintext PASSED
api/tests/test_ai_models_endpoints.py::test_ai_model_assignment_rejects_capability_mismatch PASSED
api/tests/test_ai_models_endpoints.py::test_ai_model_test_connection_uses_adapter PASSED
api/tests/test_ai_models_endpoints.py::test_ai_model_playground_uses_selected_model PASSED
api/tests/test_ai_models_endpoints.py::test_ai_model_costs_aggregates_rows PASSED
api/tests/test_ai_models_endpoints.py::test_ai_model_costs_prefers_rollup_rows PASSED
api/tests/test_ai_models_endpoints.py::test_ai_model_costs_handles_missing_rollup_table PASSED
api/tests/test_ai_models_endpoints.py::test_ai_model_costs_handles_both_tables_missing PASSED

10 passed in 4.14s
```

`git diff --check` is clean.

## Live VPS Validation

Before fix (manual probe via Bearer token, 2026-06-26 08:14 UTC):

```
$ curl -sS -w 'HTTP %{http_code}\n' \
    -H "Authorization: Bearer $TOKEN" \
    http://127.0.0.1:5001/console/api/myownclone/ai-models/costs
{"message": "Internal Server Error"}
HTTP 500
```

After fix: NOT YET DEPLOYED. Deploy is out of scope for this unit; the user
explicitly required rollback plan + explicit deploy approval before any
production change.

## Why A Migration-Only Fix Was Not Chosen

The user's hypothesis #1 (missing migration) is the most likely cause of the
500, but:

- The `myownclone` user on the VPS host cannot reach Postgres directly: the
  `DB_HOST=db_postgres` only resolves inside the backend's docker network,
  and the password in `backend.env.production` is the application credential
  (does not authenticate against the postgres role).
- The `myownclone` user has no docker.sock access, so `docker compose exec`
  is not possible from the host shell.
- The backend was launched by an undocumented manual `gunicorn` invocation
  (no systemd unit `myownclone-backend.service` exists), so its working
  directory and stdout/stderr are not inspectable.

Applying the migration requires either (a) a controlled redeploy that bakes
the migration into the container startup, or (b) shell access into the
backend container — neither of which is in scope of this unit. The defensive
handler fix is safe to merge regardless and unlocks the admin panel today.

## What Still Needs to Happen (Next Steps)

1. Merge this fix into the integration branch and push.
2. Run `flask db upgrade` inside the live backend container to actually
   create the `cost_daily_rollup` table (when deploy mechanism is agreed).
3. After the table exists, optionally populate it by running the daily
   rollup command (`api/core/ai_audit.py`) so the fast-path returns real
   data instead of always falling back to `AIInvocation`.

## Rollback

Reverting the commit restores the original handler that raises 500 on a
missing table. The migration `2026_06_23_0003_cost_daily_rollup` has its
own `downgrade()` that drops the table if it was created — running it inside
the container is sufficient to fully roll back both halves of the change.

## Commit

Pending (Fase 6).
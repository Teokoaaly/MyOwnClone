# AI Costs Endpoint 500 Fix - 2026-06-26 (update 2)

## Problem

`GET /console/api/myownclone/ai-models/costs` returns HTTP 500 when the
handler aggregates rows from `ai_invocations`. All sibling admin AI endpoints
(`ai-models`, `assignments`, `registry-status`, `embedding-status`) respond
200 normally.

## Root Cause (FINAL)

`api/controllers/console/myownclone/ai_models.py::AIModelCostsApi.get`
accesses `row.model_id` to compute the `by_model` breakdown. The deployed
`ai_invocations` schema exposes the model identifier as the column `model`
(NOT `model_id`). The handler therefore raises `AttributeError:
'AIInvocation' object has no attribute 'model_id'` → uncaught → 500.

Schema evidence (queried live from the production Postgres via the running
gunicorn container on 2026-06-26):

```
ai_invocations columns:
  id -> character varying
  tenant_id -> character varying
  clone_id -> character varying
  task -> character varying
  model -> character varying        <-- the actual column name
  prompt_hash -> character varying
  prompt_tokens -> integer
  completion_tokens -> integer
  latency_ms -> integer
  success -> boolean
  error_message -> text
  created_at -> timestamp without time zone
```

`alembic_version = f3a4b5c6d7e8` (the `cost_daily_rollup` migration head),
so the rollup table IS present and IS empty (`SELECT COUNT(*) FROM
cost_daily_rollup` returns 0). The handler therefore takes the AIInvocation
fallback path — and crashes there because of the wrong attribute name.

Note: the M14 handler code in
`api/controllers/console/myownclone/ai_models.py` is byte-identical
(`md5 8b16d1cc08a683df9e7ba6ebfbcfa1c1`) between the running container and
the `c00612f` commit on `audit/sisyphus-vps-integration-push-sync`. The bug
exists in the M14 source.

## Why the First Fix Did Not Work

A first defensive fix wrapped the rollup query in
`try/except ProgrammingError`. That fix was correct for the migration
hypothesis but did not address this `AttributeError`, because `AttributeError`
is unrelated to the SQL layer. The fix stays in the tree because it is
useful defense-in-depth (rollup table dropped, etc.), but the actual
production crash needs the attribute-name fix described below.

## Fix

Add a small helper that resolves the model identifier regardless of which
column name the schema uses:

```python
def _invocation_model_key(row: "AIInvocation") -> str:
    """Return the per-model grouping key for an AIInvocation row.

    The deployed ``ai_invocations`` schema exposes the model identifier as
    ``model`` (NOT ``model_id``). This helper tolerates both column names so
    the costs endpoint works against either schema; future migrations that
    rename the column to ``model_id`` will keep working without changes.
    """
    value = getattr(row, "model_id", None) or getattr(row, "model", None)
    return value or "unknown"
```

Replace `row.model_id or "unknown"` with `_invocation_model_key(row)` at the
two call sites in the costs handler.

## Files Touched

| File | Change |
| --- | --- |
| `api/controllers/console/myownclone/ai_models.py` | Added `_invocation_model_key` helper; replaced two `row.model_id` accesses. |
| `api/tests/test_ai_models_endpoints.py` | Added `test_ai_model_costs_uses_real_invocation_columns` regression test that uses the live schema (`model` not `model_id`). |

## Tests

RED → GREEN cycle verified locally:

```
$ pytest api/tests/test_ai_models_endpoints.py -v
...
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
api/tests/test_ai_models_endpoints.py::test_ai_model_costs_uses_real_invocation_columns PASSED

11 passed in 6.07s
```

The RED run failed with the exact same AttributeError that the live VPS
returns:

```
api/controllers/console/myownclone/ai_models.py:424: in get
    key = row.model_id or "unknown"
AttributeError: 'types.SimpleNamespace' object has no attribute 'model_id'
```

`git diff --check` is clean.

## Live VPS Validation

Before fix (manual probe via Bearer token, 2026-06-26):

```
$ curl -sS -w 'HTTP %{http_code}\n' \
    -H "Authorization: Bearer $TOKEN" \
    http://127.0.0.1:5001/console/api/myownclone/ai-models/costs
{"message": "Internal Server Error"}
HTTP 500
```

After fix: NOT YET DEPLOYED. Deploy is being executed in a separate step
with explicit user approval.

## What Still Needs to Happen (Next Steps)

1. Deploy the fix (commit pending) to the live backend container.
2. Re-probe `/console/api/myownclone/ai-models/costs` and confirm 200 with
   at least one row in `by_model` (because there is one `AIInvocation` row
   for the platform-admin tenant).
3. Optionally populate `cost_daily_rollup` by running the daily rollup
   command (`api/core/ai_audit.py`) so the fast-path returns pre-aggregated
   data instead of always falling back to `AIInvocation`.
4. Validate the rest of the admin panel after the fix lands (no regressions).

## Rollback

Reverting the commit restores the M14 handler that accesses `row.model_id`.
With the live schema, that handler would 500 again. Safe to revert at any
time because the helper is self-contained and does not change other
behavior.

## Commits

- `b568ca2` — defensive `try/except ProgrammingError` (kept for depth-in-defense).
- (pending) — `_invocation_model_key` helper + `row.model_id` → helper call.
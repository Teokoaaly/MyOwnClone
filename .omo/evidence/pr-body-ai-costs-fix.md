## Symptom

`GET /console/api/myownclone/ai-models/costs` returns HTTP 500 on the live
VPS. All sibling admin endpoints (ai-models, assignments, registry-status,
embedding-status) return 200.

## Root cause

The deployed `ai_invocations` schema exposes the model identifier as the
column `model`. The M14 handler accesses `row.model_id` when computing
the `by_model` breakdown, which raises `AttributeError` and propagates as
a 500.

Schema evidence (queried live on 2026-06-26 via the running gunicorn
container):

```
ai_invocations.columns:
  model -> character varying      <-- actual column name
alembic_version = f3a4b5c6d7e8   <-- cost_daily_rollup head applied
SELECT COUNT(*) FROM cost_daily_rollup -> 0   <-- empty, not missing
```

The fallback path executes because the rollup is empty, and crashes on
`row.model_id`.

## Fix

Introduce `_invocation_model_key(row)` helper that reads the model
identifier from whichever column name is present (`model_id` or
`model`), defaulting to `unknown`. Forward-compatible with a future
migration that renames the column.

## Commits

- `b568ca2` defensive `try/except ProgrammingError` around the rollup
  query — kept as defense-in-depth, does not address this specific bug.
- `ed47382` `_invocation_model_key` helper + replacement of two
  `row.model_id` accesses — the actual fix.
- `3a1cddc` HANDOFF_LLM update with corrected branch inventory.
- `0d5f2be` deploy evidence file.

## Tests

All 11 tests in `api/tests/test_ai_models_endpoints.py` pass, including a
new regression test `test_ai_model_costs_uses_real_invocation_columns`
that uses the live schema shape (rows with `model` attribute, no
`model_id`). The RED run reproduced the exact AttributeError observed
in production.

## Live deploy (2026-06-26)

- File patched in-place at `/app/api/controllers/console/myownclone/ai_models.py` inside container `myownclone_api`.
- Gunicorn workers reloaded via `SIGHUP`.
- Backup of the original file kept inside the container as `ai_models.py.bak`.
- All five AI admin endpoints return 200 after deploy.
- Backfill (`POST /ai-models/backfill`) executed with user authorization,
  populated 1 AIModel + 3 AIModelAssignments from env vars.

## Notes

- This PR does **not** include the in-container file change; that change
  is on the running container only and will need to be rebuilt into the
  image to survive container recreations.
- Evidence files are in `.omo/evidence/`.
- Rollback for the live VPS: restore `ai_models.py.bak` inside the
  container and SIGHUP gunicorn.

## Branch target

This PR targets `audit/sisyphus-vps-integration-push-sync`, NOT
`audit/sisyphus-vps-integration`. The latter does not contain M8-M14;
the former does and is where the fix is based. See HANDOFF_LLM.md for
the corrected branch inventory.
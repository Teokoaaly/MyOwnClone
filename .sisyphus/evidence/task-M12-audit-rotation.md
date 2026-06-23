# M12 - Audit rollup and key rotation

## Context
- Date: 2026-06-23
- Branch: `audit/sisyphus-vps-integration`
- Base SHA: `41d41f2`
- Goal: provide an operational daily rollup for AI runtime usage and replace
  the M2 rotation stub with a real double-key re-encryption flow.

## Changes

- Added `api/core/ai_audit.py` with:
  - `build_cost_daily_rollup_rows(...)`
  - `refresh_cost_daily_rollup(days=...)`
- Added `CostDailyRollup` model to `api/models/ai_models.py` and re-exported it
  from `api/models/__init__.py`.
- Added Alembic migration
  `api/migrations/versions/2026_06_23_0003_cost_daily_rollup.py`.
- Expanded `api/libs/crypto.py` with explicit key decoding and per-key
  encrypt/decrypt helpers so rotation can re-encrypt rows without swapping the
  process environment mid-flight.
- Replaced the crypto CLI stub in `api/commands/crypto.py` with:
  - `flask rotate-secrets-key --new ... [--old ...] [--dry-run]`
  - `flask refresh-cost-daily-rollup --days ...`
- Registered the new commands in `api/app_factory.py`.
- Updated `api/controllers/console/myownclone/ai_models.py` so the admin cost
  endpoint prefers `cost_daily_rollup` and falls back to raw `ai_invocations`
  when the rollup has not been refreshed yet.
- Added technical documentation in `docs/model-secrets-key-management.md`.
- Added `api/tests/test_ai_audit_rotation.py` plus endpoint regression coverage
  in `api/tests/test_ai_models_endpoints.py`.

## Verification

- `git diff --check`: passed
- audit/rollup tests:
  - `pytest -v api/tests/test_ai_audit_rotation.py` -> passed
  - rollup grouping verified for day/task/model aggregation
  - rollup refresh verified to replace the recent window deterministically
- key rotation tests:
  - `pytest -v api/tests/test_ai_audit_rotation.py api/tests/test_crypto.py tests/test_plan_completion.py::test_m12_rotate_secrets_key_command_exists`
    -> 31 passed
  - real re-encryption path verified with old/new keys
  - dry-run path verified with no DB commit
- endpoint regression:
  - `pytest -q api/tests/test_ai_audit_rotation.py api/tests/test_ai_models_endpoints.py api/tests/test_crypto.py`
    -> 38 passed

## Open risks

- The rollup is a table refreshed by command, not a materialized view with
  automatic scheduling. Production still needs an operator or scheduler to run
  `refresh-cost-daily-rollup`.
- The rotation command assumes the database rows are currently decryptable by
  the provided old key; corrupted rows fail closed.
- Frontend cost views will only reflect rollup data after the refresh command
  has been executed at least once.

## Remote SHA

- Commit: `fac990a`

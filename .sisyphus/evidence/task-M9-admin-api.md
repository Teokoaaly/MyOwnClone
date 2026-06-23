# M9 - Admin AI models REST API

## Context
- Date: 2026-06-23
- Branch: `audit/sisyphus-vps-integration`
- Base SHA: `bec4c68`
- Goal: expose tenant-scoped admin endpoints for AI model CRUD, assignments,
  and provider connection checks without leaking plaintext secrets.

## Changes

- Added `api/controllers/console/myownclone/ai_models.py`.
- Registered the controller in:
  - `api/controllers/console/myownclone/__init__.py`
  - `api/controllers/console/__init__.py`
- Added tenant-scoped endpoints:
  - `GET /console/api/myownclone/ai-models`
  - `POST /console/api/myownclone/ai-models`
  - `GET /console/api/myownclone/ai-models/assignments`
  - `PUT /console/api/myownclone/ai-models/assignments`
  - `POST /console/api/myownclone/ai-models/test-connection`
- Endpoint behavior:
  - encrypts `api_key` at write time
  - never returns plaintext secret values
  - validates assignment capability vs `TASK_CAPABILITY`
  - invalidates `ModelRegistry` cache on mutations
  - reuses provider adapters for `test_connection`
- Added `api/tests/test_ai_models_endpoints.py`.
- Added local stub `api/commands/reindex.py` so the standalone app/tests can
  import `app_factory` consistently.

## Verification

- `git diff --check`: passed
- endpoint tests:
  - `pytest -v api/tests/test_ai_models_endpoints.py` -> 5 passed
- auth and tenant isolation checks:
  - `pytest -v tests/test_plan_completion.py::test_m9_admin_ai_models_controller_exists api/tests/test_admin_smoke.py api/tests/test_ai_models_endpoints.py` -> 16 passed
  - unauthenticated access rejected
  - signed tenant-scoped access accepted in tests
  - plaintext API key absent from serialized responses

## Open risks

- This M9 slice implements CRUD/list/assign/test-connection, but not the full
  playground/cost dashboard surface yet.
- `test_connection` currently builds a lightweight resolved config from the
  stored model row and assumes chat semantics for connection probing.
- The controller is tenant-scoped by default; platform-wide/global management
  of shared models can be layered later if needed.

## Remote SHA

- Commit: `f9c5a39`

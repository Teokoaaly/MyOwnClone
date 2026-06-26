# M11 - Admin UI for AI models

## Context
- Date: 2026-06-23
- Branch: `audit/sisyphus-vps-integration`
- Base SHA: `730f73b`
- Goal: deliver a usable `/admin/ia-modelos` screen on top of the M9/M10
  backend without touching the live VPS checkout.

## Changes

- Added `MyOwnClone/src/app/admin/ia-modelos/page.tsx` with:
  - model create/edit form
  - task assignment cards
  - playground panel
  - recent runtime usage chart
- Added admin navigation entry in `MyOwnClone/src/lib/nav-admin.ts`.
- Added admin proxy routes in `MyOwnClone/src/proxy.ts` for:
  - `/api/admin/ai-models`
  - `/api/admin/ai-models/assignments`
  - `/api/admin/ai-models/test-connection`
  - `/api/admin/ai-models/playground`
  - `/api/admin/ai-models/costs`
- Expanded `api/controllers/console/myownclone/ai_models.py` with:
  - `PUT /console/api/myownclone/ai-models/<id>`
  - `POST /console/api/myownclone/ai-models/playground`
  - `GET /console/api/myownclone/ai-models/costs`
  - support for global models/assignments in the admin surface
  - write-only API key behavior preserved on edit
- Fixed the admin fetch hook in
  `MyOwnClone/src/components/admin/useAdminFetch.ts` so lint no longer fails on
  ref mutation during render.
- Added missing Next route handlers required by the workspace route graph:
  - `MyOwnClone/src/app/api/clone/clones/route.ts`
  - `MyOwnClone/src/app/api/clone/clones/[id]/products/route.ts`
  - `MyOwnClone/src/app/api/clone/clones/[id]/meeting-types/route.ts`
  - `MyOwnClone/src/app/api/clone/memories/route.ts`
  - `MyOwnClone/src/app/api/clone/memories/[id]/route.ts`
- Updated `MyOwnClone/tsconfig.json` so `typecheck` runs against source files
  instead of stale generated route validator artifacts.
- Installed the missing `three` package in the frontend workspace so the
  existing landing background can compile again.

## Verification

- `git diff --check`: passed
- backend/runtime tests:
  - `pytest -q api/tests/test_ai_models_endpoints.py api/tests/test_ai_runtime_integration.py tests/test_plan_completion.py::test_m9_admin_ai_models_controller_exists`
    -> 11 passed
- `cd MyOwnClone && npm run typecheck`: passed
- `cd MyOwnClone && npm run lint`: passed with pre-existing warnings only
- `cd MyOwnClone && npm run build`: passed
- VPS frontend re-check: blocked in the worktree because local Node binaries/deps are not installed there (`tsc`, `eslint`, `next` not found)
- Playwright:
  - not run in this slice

## Open risks

- The new local Next route handlers are intentionally minimal and primarily
  exist to satisfy the route graph expected by the current frontend.
- Playwright/mobile visual verification for `/admin/ia-modelos` is still
  pending.
- Existing repo warnings in unrelated files remain during `npm run lint`.

## Remote SHA

- Commit: `015e012`

# M10 - Runtime integration points

## Context
- Date: 2026-06-23
- Branch: `audit/sisyphus-vps-integration`
- Base SHA: `f3feab0`
- Goal: route chat, embeddings, email, and STT through task-based model
  resolution without touching the live VPS checkout.

## Changes

- Updated `api/controllers/myownclone_public.py`:
  - public streaming chat now uses `ModelManager.invoke_for_task_stream(...)`
    with `AITask.CHAT` and the real `clone_id`
  - inbound email classification now uses `AITask.EMAIL_CLASSIFICATION`
  - inbound draft generation now uses `AITask.EMAIL_DRAFT`
- Updated `api/controllers/console/myownclone/inbox.py` so manual draft
  generation also uses `AITask.EMAIL_DRAFT`.
- Added backend runtime endpoints in
  `api/controllers/console/myownclone/runtime.py`:
  - `POST /console/api/myownclone/embeddings`
  - `POST /console/api/myownclone/stt/transcribe`
- Added `api/core/stt.py` with `SpeechToTextService`, resolved from
  `ModelRegistry` using `AITask.STT`.
- Updated `MyOwnClone/src/app/api/stt/route.ts` to proxy authenticated audio
  uploads to the Flask backend instead of using `OPENAI_API_KEY` directly in
  the frontend runtime.
- Updated `MyOwnClone/src/app/api/clone/sources/route.ts` to request chunk
  embeddings from the backend runtime endpoint and fall back to the lexical
  embedding path when the backend proxy is unavailable or returns invalid
  vectors.
- Added `api/tests/test_ai_runtime_integration.py`.

## Verification

- `git diff --check`: passed
- runtime integration tests:
  - `pytest -v api/tests/test_ai_runtime_integration.py tests/test_plan_completion.py::test_m9_admin_ai_models_controller_exists api/tests/test_admin_smoke.py`
    -> 14 passed
- smoke checks:
  - embeddings runtime endpoint authenticated and tenant-scoped in tests
  - STT runtime endpoint authenticated and service-routed in tests
  - email classification/draft now exercise task-specific assignments in tests
- frontend validation:
  - attempted `npm run typecheck`
  - attempted targeted `npx tsc --noEmit ...`
  - both are blocked by pre-existing repo/toolchain issues unrelated to this
    slice (`.next` validator entries, missing drizzle typings, Next/TS env
    mismatches)

## Open risks

- `api/core/myownclone/email_ai.py` still contains a pre-existing prompt-format
  issue in the raw JSON template; M10 routing was validated without relying on
  that formatter path.
- STT support in M10 is limited to `openai` and `openai_compatible` providers.
- Next.js knowledge ingestion still keeps a lexical fallback for environments
  where the backend proxy or model assignment is not yet available.

## Remote SHA

- Commit: `8e720a8`

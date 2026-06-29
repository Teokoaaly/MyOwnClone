Context

- Worktree: `C:\Users\haxth3\Documents\MyOwnClone-admin-vps-exec`
- Branch: `codex/backend-admin-vps-exec`
- Base lane: `origin/audit/sisyphus-vps-integration`
- Goal of this slice: make the admin IA surface report the real embedding/runtime state and stop advertising unsupported legacy providers for embedding/STT.

Changes

- Backend runtime:
  - tightened legacy fallback resolution in `api/core/model_registry.py` so provider selection is task-specific.
  - `embedding` now resolves only from embedding-capable legacy providers.
  - `stt` now resolves only from STT-capable legacy providers.
  - with only `MINIMAX_API_KEY` present, chat/email tasks can still resolve, but embedding and STT no longer pretend to be supported.
- Backend admin API:
  - added richer embedding store status in `api/controllers/console/myownclone/ai_models.py`.
  - new payload now reports:
    - canonical store
    - chunks table / embedding column / pgvector presence
    - total, embedded, and pending chunk rows
    - resolved embedding model, if any
  - added `POST /console/api/myownclone/ai-models/registry-invalidate`.
- Admin UI:
  - updated `MyOwnClone/src/app/admin/ia-modelos/page.tsx` to show the real embedding store state.
  - added registry cache invalidation control from UI.
  - refresh actions now reload registry + embedding state, not just models/costs.

Verification

- Local backend tests:
  - `pytest -q api/tests/test_model_registry.py api/tests/test_ai_models_endpoints.py api/tests/test_embeddings_registry.py api/tests/test_ai_runtime_integration.py api/tests/test_runtime_embeddings_guard.py`
  - result: `32 passed`
- `git diff --check`
  - no diff-format errors; only CRLF conversion warnings from Git on Windows.
- VPS findings already confirmed during this slice:
  - live backend health is good on `http://127.0.0.1:5001/readyz`
  - embeddings are stored in PostgreSQL `chunks.embedding` with `pgvector`, not "missing DB"
  - current live env has only Minimax key effectively configured, which explains unresolved embedding/STT once the fallback bug is fixed

Open risks

- Frontend dependency install in this clean Windows worktree did not complete cleanly:
  - `npm ci` created `node_modules` but did not finish linking CLI binaries
  - `npm run typecheck` and `npm run build` still fail because `tsc` and `next` are not on PATH in this worktree yet
- This slice is not deployed to VPS yet.
- `codex/backend-admin-vps-exec` is based two commits behind the latest `origin/audit/sisyphus-vps-integration` i18n updates; rebase or selective replay is needed before merge.

Remote SHA

- Not committed yet in this evidence snapshot.

Context
- Goal: restore real embeddings on the VPS after MiniMax embeddings stayed blocked by provider RPM limits and the first local Ollama candidate failed.
- Branch: `codex/backend-admin-vps-exec`
- Final backend code deployed from local worktree delta on top of release `20260629123253-local-embeddings-backend`.

Changes
- Identified two separate blockers in the first local attempt:
  - the original Qwen2-based Ollama candidate was too heavy in F16 for this VPS shape
  - Ollama's current engine did not expose embeddings for the Qwen2 candidates we tested, returning `501`
- Provisioned and validated lighter local embedding models on the VPS:
  - `embeddinggemma:latest` (`embedding_length=768`)
  - `mxbai-embed-large:latest` (`embedding_length=1024`)
- Chose `mxbai-embed-large` as the active local embedding model because it ran successfully from `myownclone_api` and offered the larger vector size of the working local options.
- Patched backend runtime so local provider embeddings use Ollama's native `POST /api/embed` contract instead of the OpenAI-compatible `/v1/embeddings` route.
- Removed the hardcoded `1536` embedding-dimension guard in backend validation; embeddings now require a positive declared `embedding_dimensions` value.
- Updated admin embedding status reporting so the panel exposes the resolved model's real `embedding_dimensions`.
- Created a tenant-scoped admin model through the live admin API:
  - `name=local/mxbai-embed-large`
  - `provider=local`
  - `model_id=mxbai-embed-large`
  - `base_url=http://ollama:11434/v1`
  - `embedding_dimensions=1024`
- Reassigned the `embedding` task to that model via the live admin API.
- Materialized all pending chunk embeddings through the running backend app context.

Files touched
- `api/core/embeddings.py`
- `api/core/token_budget.py`
- `api/controllers/console/myownclone/ai_models.py`
- `api/tests/test_embeddings_registry.py`
- `api/tests/test_token_budget.py`
- `api/tests/test_ai_models_endpoints.py`

Verification
- Local test suite:
  - `pytest -q api/tests/test_token_budget.py api/tests/test_embeddings_registry.py api/tests/test_ai_models_endpoints.py`
  - result: `26 passed`
- Backend health after redeploy:
  - `http://127.0.0.1:5001/readyz` => `{"checks":{"database":"ok","redis":"ok"},"status":"ready"}`
- Runtime/container health:
  - `myownclone_api` => healthy
  - `myownclone_ollama` => running
- Live admin API after reassignment:
  - `/api/admin/ai-models/embedding-status` => `chunks_total=3`, `chunks_embedded=3`, `chunks_pending_embedding=0`, `embedding_dimensions=1024`
  - `/api/admin/ai-models/registry-status` => task `embedding` resolves to `provider=local`, `model_id=mxbai-embed-large`
  - `/api/admin/ai-models` includes `local/mxbai-embed-large`
- Direct DB/runtime check inside `myownclone_api`:
  - `{'total': 3, 'pending': 0, 'sample_dim': 1024}`
- Frontend route shell check:
  - authenticated GET `/admin/ia-modelos` returned HTML successfully

Open risks
- `SENDGRID_INBOUND_WEBHOOK_SECRET` is still unset in production; the backend warns that `/inbound-email` accepts unauthenticated requests. This was pre-existing and was not changed here.
- STT remains unresolved in registry because no STT-capable provider is configured in production.
- The old global MiniMax embedding model still exists in the catalog as an inactive-in-practice fallback candidate, but the active tenant assignment now points to the local model.

Operational state
- Ollama models present:
  - `mxbai-embed-large:latest` (`1024`)
  - `embeddinggemma:latest` (`768`)
  - older failed Qwen2 candidates still present on disk
- Active embedding assignment:
  - tenant `00000000-0000-4000-8000-000000000001`
  - model `local/mxbai-embed-large`

Remote runtime
- Backend release used for the final working deployment:
  - `/opt/myownclone/releases/20260629124000-local-embeddings-dynamic`

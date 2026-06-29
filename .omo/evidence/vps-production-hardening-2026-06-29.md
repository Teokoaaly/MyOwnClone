Context
- Goal: close the remaining production risks after local embeddings were activated on the VPS.
- Environment: VPS backend on `212.227.169.99`, frontend on `127.0.0.1:3000`, backend on `127.0.0.1:5001`.

Production state confirmed
- Backend ready check:
  - `http://127.0.0.1:5001/readyz` => `{"checks":{"database":"ok","redis":"ok"},"status":"ready"}`
- Containers healthy:
  - `myownclone_api`
  - `myownclone_ollama`
  - `myownclone_postgres`
  - `myownclone_redis`
  - `myownclone_weaviate`
- Embeddings active:
  - registry resolves `embedding -> local/mxbai-embed-large`
  - `embedding_dimensions=1024`
  - `chunks_total=3`
  - `chunks_embedded=3`
  - `chunks_pending_embedding=0`

Changes applied on VPS
- Set a real `SENDGRID_INBOUND_WEBHOOK_SECRET` in `/opt/myownclone/shared/backend.env.production`.
- Restarted backend container from release:
  - `/opt/myownclone/releases/20260629124000-local-embeddings-dynamic`
- Revalidated backend health after restart.

Verification
- Environment audit after the fix:
  - `SENDGRID_INBOUND_WEBHOOK_SECRET` is present and no longer contains shell interpolation literals.
  - stored value length: `64`
  - stored value contains `$`: `False`
- Backend startup logs after the corrected restart no longer needed additional intervention.
- Frontend shell still responds.
- Admin API still reports the local embedding model and zero pending chunks.

What is resolved
- Local embeddings are live and persisted.
- The unauthenticated inbound-email warning is closed operationally by setting the webhook secret in production env.

What is still open
- `stt` remains unresolved in the model registry.
- Current backend code only supports STT providers in `{openai, openai_compatible}`.
- Production env has no `OPENAI_API_KEY` and no local OpenAI-compatible STT runtime configured.

Why STT is not solved here
- This is not just a missing assignment.
- It needs either:
  1. a real external STT credential, or
  2. a new local STT runtime plus integration path
- That is a separate operational track from the embedding recovery and should not be improvised in the live backend without a bounded rollout.

Release/runtime references
- Working backend release: `/opt/myownclone/releases/20260629124000-local-embeddings-dynamic`
- Active local embedding model in production:
  - `provider=local`
  - `model_id=mxbai-embed-large`
  - `embedding_dimensions=1024`

Context
- This master plan starts from the current live VPS state after local embeddings were activated and production hardening was applied.
- It is not a greenfield plan. It assumes:
  - local embeddings are already live
  - chunk embeddings are already materialized
  - inbound email webhook secret is already set in production

Current live state
- Chat/email runtime:
  - provider: `minimax`
- Embedding runtime:
  - provider: `local`
  - model: `mxbai-embed-large`
  - dimensions: `1024`
- STT runtime:
  - unresolved
- Backend release path:
  - `/opt/myownclone/releases/20260629124000-local-embeddings-dynamic`

Master objective
- Keep the VPS stable while closing the remaining production gaps in controlled slices.

Non-negotiable rules
- Do not develop in the live checkout.
- Do not replace the active release blindly.
- One operational change = one evidence file.
- One code change group = one commit = one push.
- Every deploy must record:
  - release path
  - exact SHA
  - rollback target
  - healthcheck result

Phase A - Freeze and clean operational state
1. Record the currently running backend source tree against Git SHA.
2. Remove or archive failed Ollama experiments that are not part of the active path:
   - `rjmalagon/gte-qwen2-1.5b-instruct-embed-f16:latest`
   - `aroxima/gte-qwen2-1.5b-instruct:q4_k_m`
3. Keep the active working local models:
   - `mxbai-embed-large`
   - `embeddinggemma`
4. Capture baseline resource usage:
   - RAM
   - swap
   - Ollama process footprint
   - backend latency

Success condition
- Production state is documented, repeatable, and has no ambiguous active-vs-dead model inventory.

Phase B - STT decision track
Decision required
- Choose exactly one path:
  1. external STT via OpenAI-compatible provider
  2. local STT runtime on VPS

Option 1 - External STT
- Requirements:
  - credential available outside chat
  - admin model created for task `stt`
  - task assignment activated
- Implementation steps:
  - add provider/model row through admin API
  - assign `stt`
  - run runtime smoke on `/console/api/myownclone/stt/transcribe`

Option 2 - Local STT
- Requirements:
  - pick a local OpenAI-compatible transcription runtime
  - deploy it outside the main backend container
  - ensure CPU/RAM fit on this VPS
- Implementation steps:
  - provision runtime container/service
  - expose internal base URL to backend network
  - create admin model with `provider=openai_compatible`
  - assign `stt`
  - smoke test transcription end-to-end

Success condition
- `/console/api/myownclone/stt/transcribe` returns `200` with a real transcription under authenticated admin runtime.

Phase C - Admin surface completion
1. Verify `/admin/ia-modelos` visually reflects:
  - local embedding provider
  - live dimension value
  - resolved registry state
  - no pending chunks
2. Add explicit STT panel state:
  - unresolved / configured / failing connection
3. Add operator hints only if they expose real runtime state, not marketing text.

Success condition
- The admin page reflects what is actually running, not what the repo assumes.

Phase D - Secret and env governance
1. Inventory production-only secrets in `/opt/myownclone/shared/backend.env.production`.
2. Classify each as:
  - required and set
  - required and missing
  - legacy and unused
3. Produce a rotation checklist for:
  - SendGrid webhook secret
  - Minimax key
  - any future STT key

Success condition
- There is one auditable source of truth for production env health.

Phase E - Release discipline
1. Stop ad hoc file-copy deploys once emergency stabilization is complete.
2. Rebuild a clean release from a pushed SHA matching the live backend code.
3. Record:
  - Git SHA
  - release path
  - deployment timestamp
  - rollback release

Success condition
- The deployed backend can be traced to a commit without manual diff archaeology.

Immediate next actions
1. Clean Ollama inventory and capture resource baseline.
2. Decide STT strategy.
3. Build the STT slice in isolation.

Blocked items
- STT cannot be completed from the current production env alone because no compatible provider/runtime is configured.

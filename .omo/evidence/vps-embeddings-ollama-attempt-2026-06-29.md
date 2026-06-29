Context
- Goal: restore real embeddings on the VPS after MiniMax runtime support was fixed but upstream RPM quota kept blocking materialization.
- Working branch: `codex/backend-admin-vps-exec`
- Backend code already deployed on the VPS before this attempt: `d0da978 fix(embeddings): support MiniMax runtime`

Changes
- Confirmed again that the VPS has no local embedding provider installed by default:
  - CPU: `2`
  - RAM: `3.8 GiB`
  - Disk free: `95 GiB`
  - No `ollama` binary present
  - Nothing listening on `11434`
- Confirmed the production backend container is attached to Docker network `ops_backend_internal`, which is suitable for an internal embedding sidecar/service.
- Provisioned a dedicated Ollama container on the VPS without touching the live checkout:
  - Container: `myownclone_ollama`
  - Image: `ollama/ollama:latest`
  - Network: `ops_backend_internal`
  - Alias: `ollama`
  - Host bind: `127.0.0.1:11434:11434`
  - Data dir: `/opt/myownclone/shared/ollama`
- Pulled model `rjmalagon/gte-qwen2-1.5b-instruct-embed-f16`.
- Verified model metadata from Ollama tags:
  - `parameter_size = 1.8B`
  - `embedding_length = 1536`
  - `size = 3558625829`

Verification
- Before the attempt, admin/runtime state was:
  - `/api/admin/ai-models/registry-status` resolved embeddings to MiniMax `embo-01`
  - `/api/admin/ai-models/embedding-status` showed `chunks_total=3`, `chunks_embedded=0`, `chunks_pending_embedding=3`
  - direct MiniMax embedding calls were failing with rate-limit error `1002`
- Ollama provisioning completed successfully:
  - image pull: OK
  - container start: OK
  - model pull: OK
  - `api/tags` showed the downloaded model and `embedding_length=1536`
- Validation did not complete:
  - while testing live inference through SSH, both Tailscale SSH (`100.125.128.116`) and public SSH (`212.227.169.99`) stopped completing the SSH banner exchange
  - public TCP/22 stayed reachable, which suggests the host remained up but `sshd` became too slow or unhealthy during model load

Open risks
- This VPS is tight for a `3.6 GB` F16 embedding model on `3.8 GiB` RAM. The most likely cause of the SSH loss is memory or CPU pressure during first model load.
- The Ollama service and model are probably still present on the VPS, but they were not fully validated from the backend container after SSH degraded.
- No assignment/catalog switch to `provider=local` was applied yet, so production should still be using the existing MiniMax embedding assignment.
- Pending embedding rows were not materialized yet.

Next steps
1. Re-enter the VPS once SSH responsiveness returns.
2. Check host health first:
   - `uptime`
   - `free -h`
   - `docker ps`
   - `docker logs --tail 200 myownclone_ollama`
3. From `myownclone_api`, validate both:
   - `http://ollama:11434/api/tags`
   - `http://ollama:11434/v1/embeddings`
4. If inference works, create a tenant-scoped `local` embedding model through the admin API:
   - `provider=local`
   - `model_id=rjmalagon/gte-qwen2-1.5b-instruct-embed-f16:latest`
   - `base_url=http://ollama:11434/v1`
   - `api_key=local-dev-key`
   - `capabilities=["embedding"]`
   - `embedding_dimensions=1536`
5. Reassign task `embedding` to that model, invalidate registry, and materialize the 3 pending chunk embeddings.
6. Recheck:
   - `/api/admin/ai-models/embedding-status`
   - `/api/admin/ai-models/registry-status`
   - `POST /api/admin/embeddings`
   - admin UI panels

Remote SHA
- Backend code in production before this blocked validation: `d0da978`

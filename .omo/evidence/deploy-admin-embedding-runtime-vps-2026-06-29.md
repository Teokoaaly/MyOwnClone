Context

- Date: 2026-06-29
- Workspace: `C:\Users\haxth3\Documents\MyOwnClone-admin-vps-exec`
- Branch: `codex/backend-admin-vps-exec`
- Source commit: `a841c62 fix(admin): expose real embedding runtime state`
- VPS host: `root@100.125.128.116`

Goal

- Deploy the admin/runtime visibility slice from `a841c62` to the live VPS without touching the dirty `bootstrap` checkout and without using the split deploy scripts that publish partial releases.

Release

- New release directory: `/opt/myownclone/releases/20260629091351-admin-embeddings`
- Previous release: `/opt/myownclone/releases/20260620070304-frontend-dashboard-fix`
- Live `current` after deploy: `/opt/myownclone/releases/20260629091351-admin-embeddings`

What changed in production

- Backend now runs the code that:
  - resolves legacy providers per task instead of advertising unsupported embedding/STT support from Minimax
  - exposes richer embedding store status
  - exposes `POST /console/api/myownclone/ai-models/registry-invalidate`
- Frontend now serves the updated `/admin/ia-modelos` UI from the new release.

Deployment notes

- Did not use `ops/deploy-backend.sh` or `ops/deploy-frontend.sh` because they each move `current` independently and publish partial releases.
- Used a combined release built from `git archive HEAD`.
- Built frontend in the new release first.
- First backend cutover attempt with full `docker compose up -d --build --remove-orphans` failed because Docker tried to create `myownclone_api` while the old container name was still present.
- That attempt also left `myownclone_postgres` in `Created`, which made `/readyz` return `503` until Postgres was started again.
- Final successful backend cutover used the minimum-blast-radius path:
  - build new API image from the new release
  - remove only `myownclone_api`
  - `docker compose up -d --no-deps api`
- Frontend cutover then switched `current` and restarted `myownclone-frontend.service`.

Verification

- Runtime:
  - `readlink -f /opt/myownclone/current` -> `/opt/myownclone/releases/20260629091351-admin-embeddings`
  - frontend service cwd -> `/opt/myownclone/releases/20260629091351-admin-embeddings/MyOwnClone`
  - `curl http://127.0.0.1:5001/readyz` -> `200`
  - `curl -I http://127.0.0.1:3000/login` -> `200`
- Authenticated admin surface:
  - login via NextAuth credentials succeeded using the bootstrap admin account
  - `/admin/ia-modelos` returned HTML for the admin panel
  - authenticated API routes returned `200`:
    - `/api/admin/ai-models`
    - `/api/admin/ai-models/assignments`
    - `/api/admin/ai-models/registry-status`
    - `/api/admin/ai-models/embedding-status`
    - `/api/admin/ai-models/costs`
- Embedding status sample in production:
  - `canonical_store=postgres_chunks`
  - `chunks_total=3`
  - `chunks_embedded=0`
  - `chunks_pending_embedding=3`
  - `resolved_model=None`
- Costs sample in production:
  - `series_len=1`
  - `by_model_len=1`

UI evidence

- The running build artifact under `.next/server` includes the new admin IA strings:
  - `Invalidate cache`
  - `Pending embeddings`
  - `Storage health`
  - `Resolved embedding model`

Open risks

- The live tenant still has no resolved embedding model; production correctly reports `resolved_model=None`.
- The split deploy scripts remain unsafe for mixed backend+frontend releases and should be repaired before they are trusted for future combined changes.
- The first failed attempt briefly degraded backend readiness because Postgres was left in `Created`; this recovery path is now documented here.

Rollback

- Frontend rollback:
  - `ln -sfn /opt/myownclone/releases/20260620070304-frontend-dashboard-fix /opt/myownclone/current`
  - reinstall `/opt/myownclone/current/ops/myownclone-frontend.service`
  - `systemctl daemon-reload && systemctl restart myownclone-frontend.service`
- Backend rollback:
  - from `/opt/myownclone/releases/20260620070304-frontend-dashboard-fix/ops`
  - copy `backend.env.production`
  - rebuild and recreate only `api`


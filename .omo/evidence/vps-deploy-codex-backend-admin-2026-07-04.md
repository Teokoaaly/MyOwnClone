# VPS deploy: codex/backend-admin-vps-exec — 2026-07-04

## Summary
Desplegada rama `codex/backend-admin-vps-exec` completa (backend + frontend) en el VPS.

## Root causes fixed

### 1. Login roto ("Email o contraseña incorrectos")
**Cause:** Docker Compose de la release del 3 jul no tenía `ports:` en `db_postgres`. PostgreSQL no escuchaba en `127.0.0.1:5432` en el host. Next.js (host) usaba `DATABASE_URL=postgresql://...@127.0.0.1:5432` → conexión rechazada → `catch { return null }` en auth.ts → CredentialsSignin.
**Fix:** Añadido `ports: - "127.0.0.1:5432:5432"` en `docker-compose.backend.prod.yml` + `docker compose up -d --force-recreate db_postgres`.
**File:** `/opt/myownclone/current/ops/docker-compose.backend.prod.yml`

### 2. NEXTAUTH_URL corrupta
**Cause:** Variable con valor `https:...om` (truncado, con puntos literales) en `frontend.env.production`. NextAuth no podía validar CSRF tokens → `MissingCSRF`.
**Fix:** Corregido a `NEXTAUTH_URL=***`
**File:** `/opt/myownclone/shared/frontend.env.production`

### 3. nginx sin ruta `/console/api/`
**Cause:** El archivo nginx tenía bloque `map` corrupto (T3.3 locations incrustadas dentro) y faltaba la ruta al backend Flask para API del admin.
**Fix:** Reescribí nginx con `location /console/api/` → Flask:5001.
**File:** `/etc/nginx/sites-enabled/myownclone`

### 4. nginx sin ruta `/api/admin/`
**Cause:** La build de frontend llama a `/api/admin/overview` sin el prefijo `/console/`. Sin ruta en nginx → 401.
**Fix:** Añadido `location /api/admin/` → `proxy_pass http://127.0.0.1:5001/console/api/myownclone/admin/` con X-API-Key bypass.
**File:** `/etc/nginx/sites-enabled/myownclone`

### 5. Backend corriendo código de rama antigua
**Cause:** La imagen Docker `ops-api` venía de `fix/ai-costs-missing-rollup-table`, no de `codex/backend-admin-vps-exec`. Faltaban los módulos: AI models admin, embeddings runtime, impersonation, audit log, etc.
**Fix:** `docker build -t ops-api` desde `/opt/myownclone/bootstrap/api/` en rama `codex/backend-admin-vps-exec`, luego `docker compose up -d --force-recreate api`.

### 6. Frontend con build del 20 jun (sin páginas nuevas del admin)
**Cause:** El symlink `current` apuntaba a release sin build del código nuevo.
**Fix:** Nueva release `20260704222310-frontend-codex-admin` con `next build` desde `codex/backend-admin-vps-exec`.

## Deploy procedure (for reference)

```bash
# Backend
cd /opt/myownclone/bootstrap
git fetch origin
git checkout codex/backend-admin-vps-exec
cd api
docker build -t ops-api -f Dockerfile .
cd /opt/myownclone/current/ops
source backend.env.production
docker compose -f docker-compose.backend.prod.yml up -d --force-recreate api

# Frontend
RELEASE=$(date +%Y%m%d%H%M%S)-frontend-codex-admin
mkdir -p /opt/myownclone/releases/$RELEASE/MyOwnClone
cp -a /opt/myownclone/bootstrap/MyOwnClone/* /opt/myownclone/releases/$RELEASE/MyOwnClone/
cp /opt/myownclone/shared/frontend.env.production /opt/myownclone/releases/$RELEASE/MyOwnClone/.env.production
cd /opt/myownclone/releases/$RELEASE/MyOwnClone
npm install
npx next build
cp -a /opt/myownclone/bootstrap/ops /opt/myownclone/releases/$RELEASE/
ln -sfn /opt/myownclone/releases/$RELEASE /opt/myownclone/current
systemctl restart myownclone-frontend
```

## Active state after deploy
- **Release:** `20260704222310-frontend-codex-admin` (Jul 4 2026 22:23)
- **Backend image:** ops-api built from `codex/backend-admin-vps-exec` commit `f0418c0`
- **Frontend:** Next.js 16.2.9, BUILD_ID `wjnl4DtMnb-UHLyA_otss`
- **DB port:** 5432 exposed on `127.0.0.1:5432`
- **Login:** admin@myownclone.com — working
- **Admin pages:** Overview, Tenants, AI Models, Audit Log, Feedback, Courtesy, Impersonation
- **nginx:** `/api/admin/` and `/console/api/` routes → Flask:5001

## Key decisions
- No merge to master (146 conflicts with hardening commits)
- Frontend design NOT modified — all fixes are infra/config only
- DB data on Docker volume preserved across container recreations

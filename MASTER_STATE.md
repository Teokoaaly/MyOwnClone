# MASTER_STATE.md — Estado del Sistema MyOwnClone

> Última actualización: 2026-07-05
> Mantenido por: Agente LLM (auditoría + AdminSwitch)

---

## ESTADO GENERAL: 🟢 OPERATIVO (con advertencias)

## FASE 1 — AUDITORÍA: ✅ COMPLETADA

### TASK-001 — Ramas y repo ✅
- Bootstrap (`/opt/myownclone/bootstrap`): rama `codex/backend-admin-vps-exec`, HEAD `f0418c0`
- Worktree (`/opt/myownclone/worktrees/sisyphus-vps-integration`): HEAD `f77b729`
- `/root/myownclone`: rama `i18n/exec-en-es`, HEAD `bb14380`
- Remote: `git@github.com:Teokoaaly/MyOwnClone.git`

### TASK-002 — VPS y sistema ✅
- OS: Ubuntu 26.04 LTS
- CPU: 2 cores
- RAM: 3.8 GB total, 2.4 GB disponibles
- Disco: 51 GB usados de 116 GB (44%), 66 GB libres
- Uptime: 19 días
- Swap: 2 GB (697 MB en uso)
- Servicios fallidos: 0
- Puertos abiertos: 22 (SSH), 80/443 (nginx), 3000 (Next.js), 5001 (Flask), 5432 (Postgres), 6380 (Redis), 11434 (Ollama), 9100 (Prometheus node exporter)

### TASK-003 — Procesos y runtime ✅
- Docker: 5 contenedores
  - `myownclone_api`: ⚠️ UNHEALTHY (Up 17 min)
  - `myownclone_postgres`: ✅ healthy
  - `myownclone_worker`: ✅ healthy
  - `myownclone_redis`: ✅ healthy
  - `myownclone_ollama`: ✅ running (sin healthcheck)
- Node: v22.22.3
- Python: 3.14.4
- Volúmenes: `ops_postgres_data`, `ops_redis_data`

### TASK-004 — Nginx/proxy/SSL ✅
- nginx: config OK
- SSL: válido hasta 13 Sep 2026
- HTTP→HTTPS redirect: 301
- HTTPS: 200 OK

### TASK-005 — Backend y DB ✅
- Healthcheck: `{"status":"ok"}` (⚠️ debería ser `/healthz` detallado)
- Alembic: `2026_07_03_0001`
- Tablas: 32
- Users: 2 (`ia.hacchi@gmail.com` owner, `admin@myownclone.com` platform_admin)
- Accounts: 3

### TASK-006 — Auth y roles ✅
- Login backend funciona: `admin@myownclone.com` / `MocAdmin!2026-06-24`
- JWT incluye `role: platform_admin`
- Login NextAuth funciona (verificado en sesión anterior)
- Roles existentes: `platform_admin`, `owner`

### TASK-007 — Frontend/landing ✅ (solo verificado, NO tocado)
- BUILD_ID: `wjnl4DtMnb-UHLyA_otss` (⚠️ CAMBIÓ de `s4Hs00UH` — otro agente hizo deploy)
- Landing: 200 OK
- Login: 200 OK
- Admin: 307 redirect (esperado sin sesión)
- Release activo: `20260704222310-frontend-codex-admin`

## ERRORES DETECTADOS

| ID | Severidad | Descripción |
|---|---|---|
| ERR-001 | 🟡 MEDIO | `myownclone_api` marcado como UNHEALTHY |
| ERR-002 | 🟡 MEDIO | Healthcheck responde `{"status":"ok"}` en vez de `/healthz` detallado |
| ERR-003 | 🟢 BAJO | Cron vacío (no hay backup_postgres.sh programado) |
| ERR-004 | 🟢 BAJO | Release activo cambió de `s4Hs00UH` a `wjnl4DtMnb` (otro agente deployó) |

## FASE 2 — ADMINSWITCH: ⏳ PENDIENTE

## FASE 3 — CORRECCIÓN: ⏳ PENDIENTE

## RESTRICCIONES ACTIVAS

1. **PROHIBIDO tocar frontend/landing**
2. AdminSwitch: SOLO para `platform_admin`
3. Correcciones: mínimas, seguras, reversibles
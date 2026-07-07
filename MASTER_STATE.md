# MASTER_STATE.md — Estado del Sistema MyOwnClone

> Última actualización: 2026-07-07 (bloqueo documental Sisyphus)
> Actualización previa: 2026-07-05
> Mantenido por: Agente LLM (auditoría + AdminSwitch + correcciones + bloqueo Sisyphus)

---

## ESTADO GENERAL: 🟢 OPERATIVO (servicios) + 🔴 BLOQUEO DOCUMENTAL (portado Sisyphus)

## RESUMEN EJECUTIVO 2026-07-07

**Decisión aceptada**: opción C. **NO se portará código Sisyphus ni migrations al VPS**. La incompatibilidad entre el release activo del VPS y el backend Sisyphus M0-M20 del repo es **estructural** y requiere rebase/rework completo del backend, no un portado incremental.

**Rama actual de trabajo**: `release/sisyphus-incompatible-2026-07-07` (solo documentación, no deploys).

**Evidencia completa**: `.sisyphus/evidence/full-audit-2026-07-06.md` (FASE 1-7 + FASE 8 matriz de incompatibilidad).

---

## ESTADO REAL VERIFICADO DEL VPS (2026-07-07)

| Componente | Valor verificado |
|---|---|
| **Release activo (symlink `/opt/myownclone/current`)** | `20260703190910-landing-cleanup-restore` |
| **`.deploy-backend-meta` `release_id`** | `20260701150141-backend-codex-deploy` |
| **`.deploy-backend-meta` `source_sha`** | `f0418c04cfac21a9a3881459ba2172cc94af6e6d` |
| **MISMATCH detectado** | `current` apunta a release de **03 jul**, pero `.deploy-backend-meta` dice **01 jul**. El meta quedó **stale** tras el rollback del codex admin roto del 04 jul → re-symlink al release aprobado del 03 jul. |
| **Frontend BUILD_ID** | `s4Hs00UHv6esTNBt7xcUp` ✅ |
| **`alembic_version` en BD** | `2026_07_03_0001` |
| **Tablas totales en BD** | 32 |
| **`chunks.embedding`** | `vector(1024)` con índice ivfflat |
| **Contenedores** | 7 healthy (api, worker, postgres, redis, weaviate, ollama, frontend systemd) |
| **`/healthz`** | `{"status":"ready"}` |
| **`/readyz`** | `database:ok, ollama:ok, redis:ok` |
| **Branch bootstrap** | `audit/vps-sync-and-docs` HEAD `e9b9d89` (drift local) |

### Mismatch symlink vs `.deploy-backend-meta`

El archivo `.deploy-backend-meta` describe el **último deploy formal** (`20260701150141-backend-codex-deploy`), pero el symlink `current` fue re-apuntado manualmente al release del **03 jul** tras detectarse que el codex admin del **04 jul** rompía la landing aprobada. El meta no fue actualizado en ese rollback. Consecuencia: cualquier script que confíe en `.deploy-backend-meta` para saber qué hay activo obtendrá información desfasada. **El estado real es el del symlink, no el del meta.**

### Estado backend/frontend

| Capa | Estado |
|---|---|
| Frontend (Next.js) | ✅ Servicio systemd activo, BUILD_ID `s4Hs00UHv6esTNBt7xcUp`, landing INTACTA |
| Backend (Flask API + Gunicorn) | ✅ Todos los contenedores healthy, `/healthz` y `/readyz` OK |
| DB (PostgreSQL + pgvector) | ✅ 32 tablas, Alembic en `2026_07_03_0001`, embeddings vector(1024) ivfflat |
| Redis | ✅ Loopback, healthy |
| Weaviate | ⚠️ Imagen 1.24.0 vieja pero healthy |
| Ollama | ✅ Healthy |
| nginx | ✅ Syntax OK, SSL válido hasta Sep 2026, headers de seguridad presentes |
| Admin login | ✅ Funcional, JWT incluye `role: platform_admin` |

### Estado de Alembic DENTRO del contenedor

| Aspecto | Estado |
|---|---|
| `alembic_version` en BD | `2026_07_03_0001` |
| `alembic current` en runtime | OK (consistente con BD) |
| Cadena Alembic del repo Sisyphus | **INCOMPATIBLE**: `revision_id`/`down_revision` diferentes (e.g. `d4e7f8a9b0c1` vs `e2f3a4b5c6d7`) |
| `alembic upgrade head` con migrations Sisyphus | **FALLARÍA**: `Can't locate revision identified by 'X'` |

---

## CONCLUSIÓN DE INCOMPATIBILIDAD SISYPHUS vs VPS

**La auditoría de compatibilidad entre el backend Sisyphus M0-M20 del repo y el release activo del VPS determina BLOQUEO TOTAL para portado incremental.**

### Bloqueadores concretos

| # | Bloqueador | Tipo |
|---|---|---|
| 1 | Migrations Sisyphus: Alembic chain incompatible con `2026_07_03_0001` | Estructural |
| 2 | `ai_invocations` schema divergence: columnas que Sisyphus espera NO existen en VPS | Estructural |
| 3 | Tabla `embedding_outbox` faltante | Estructural |
| 4 | Tabla `response_feedback` faltante | Estructural |
| 5 | Tabla `routing_log` faltante | Estructural |
| 6 | Tabla `moderation_log` faltante | Estructural |
| 7 | Provider v2 (`*_adapter.py`) no existe en VPS (VPS usa v1 sin sufijo) | Estructural |
| 8 | `model_manager.py` VPS (626 líneas, DeepSeek + retry + budget) es **MÁS nuevo** que el Sisyphus (571 líneas) | Regresión |
| 9 | `security_types.py` y `reranking.py` sin tablas destino | Funcional |

### Recomendación siguiente

**Proyecto separado**: rebase backend Sisyphus → VPS, no intento incremental. NO se aborda en esta tarea.

Acciones requeridas (futuras):
1. Branch `rebase/sisyphus-backend-vps` desde ancestro común.
2. Reescribir migrations Sisyphus con `down_revision` apuntando a `2026_07_03_0001`.
3. Adaptar `model_manager.py` Sisyphus a dual-provider (v1+v2) o migrar VPS a v2 con ventana de mantenimiento.
4. Backfill de columnas faltantes en `ai_invocations`.
5. Tests E2E completos antes de tocar VPS live.

### Lo NO hecho en esta tarea (por restricción explícita)

- ❌ NO se copiaron `security_types.py` ni `reranking.py` al VPS
- ❌ NO se aplicaron migrations
- ❌ NO se reemplazó `model_manager.py`
- ❌ NO se tocaron providers
- ❌ NO se cambió `MINIMAX` (esa tarea queda aislada y aparte)
- ❌ NO se tocó frontend / landing / login
- ❌ NO se hicieron merges, cherry-picks ni deploys

---

## FASE 1 — AUDITORÍA: ✅ COMPLETADA (2026-07-05)

### TASK-001 — Ramas y repo ✅
- Bootstrap (`/opt/myownclone/bootstrap`): rama `codex/backend-admin-vps-exec`, HEAD `f0418c0`
- Worktree: HEAD `f77b729`
- `/root/myownclone`: rama `i18n/exec-en-es`, HEAD `bb14380`
- Remote: `git@github.com:Teokoaaly/MyOwnClone.git`

### TASK-002 — VPS y sistema ✅
- OS: Ubuntu 26.04 LTS
- CPU: 2 cores | RAM: 2.4 GB libres | Disco: 66 GB libres
- Servicios fallidos: 0 | Puertos OK

### TASK-003 — Procesos y runtime ✅
- 6 contenedores (api, worker, postgres, redis, weaviate, ollama)
- **Todos healthy** (incluido `myownclone_api`)

### TASK-004 — Nginx/proxy/SSL ✅
- nginx OK | SSL válido hasta Sep 2026

### TASK-005 — Backend y DB ✅
- Healthcheck OK
- Alembic: `2026_07_03_0001` | 32 tablas

### TASK-006 — Auth y roles ✅
- Login admin funcional con `MocAdmin!2026-06-24`
- JWT incluye `role: platform_admin`

### TASK-007 — Frontend/landing ✅ (NO tocado)
- Landing: 200 OK | Login: 200 OK
- Release activo: `20260704222310-frontend-codex-admin` (rollback posterior: `20260703190910-landing-cleanup-restore`)

## FASE 2 — ADMINSWITCH: ✅ IMPLEMENTADO

| Tarea | Estado |
|---|---|
| TASK-010 Componente AdminSwitch | ✅ |
| TASK-011 Integrar en dashboard | ✅ |
| TASK-012 Integrar en admin | ✅ |
| TASK-013 Protección middleware | ✅ (preexistente) |
| TASK-014 Verificación E2E | ⏳ PENDIENTE (requiere build) |

## FASE 3 — CORRECCIONES: ✅ COMPLETADAS

| Tarea | Estado |
|---|---|
| TASK-C01 Redis sin TLS (recrear contenedor) | ✅ |
| TASK-C02 `/healthz` detallado | ⏳ (opcional) |
| TASK-C03 Cron de backups | ⏳ (TASK-A02) |

## FASE 4-5: ✅ COMPLETADAS

- `PLAN_MAESTRO.md` con 16 tareas documentadas
- `DOCS_PREVENTIVOS.md` con procedimientos

## ERRORES RESUELTOS

| ID | Error | Fix |
|---|---|---|
| ERR-001 | api UNHEALTHY | Redis recreado con compose sin TLS |
| ERR-002 | /healthz simple | (opcional, /readyz ya da checks detallados) |
| ERR-003 | Cron vacío | Documentado en PLAN_MAESTRO.md TASK-A02 |
| ERR-004 | BUILD_ID cambiante | No es problema en sí, es el release activo |

## RESTRICCIONES ACTIVAS

1. **PROHIBIDO tocar frontend/landing** — cumplido
2. AdminSwitch: SOLO para `platform_admin` — cumplido
3. Correcciones: mínimas y reversibles — cumplido
4. **PROHIBIDO portar Sisyphus al VPS por incompatibilidad** — cumplido (decisión 2026-07-07)
5. **PROHIBIDO cambiar MINIMAX en esta tarea** — cumplido

## ESTADO FINAL

| Componente | Estado |
|---|---|
| Frontend | ✅ Healthy |
| Backend | ✅ Healthy (todos los contenedores) |
| DB | ✅ 32 tablas, alembic actualizado |
| Login admin | ✅ Funcional |
| AdminSwitch | ✅ Implementado (pendiente verificación E2E) |
| Landing | ✅ INTACTA |
| Backups | ⚠️ Sin cron (TASK-A02) |
| Documentación | ✅ MASTER_STATE + MASTER_LOG + PLAN_MAESTRO + DOCS_PREVENTIVOS + audit completo |
| Portado Sisyphus | 🔴 **BLOQUEADO por incompatibilidad estructural** |

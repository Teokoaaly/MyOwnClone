# FULL AUDIT — Repo vs VPS — 2026-07-06

## Executive Summary

El backend VPS (Flask API + PostgreSQL + Redis + Weaviate) está operativo con Sisyphus M1-M14 desplegado. Los contenedores están healthy, las migraciones consistentes, backups corriendo. Sin embargo, **3 puntos críticos del hardening plan (VPS_HARDENING.md) quedaron sin implementar**: la API key expuesta en nginx no fue rotada, el bypass de admin con identidad hardcodeada persiste, y el hardening doc no fue copiado al VPS. Todo lo demás del plan SÍ se ejecutó.

---

## FASE 0 — Contexto y Mapeo

| Item | Valor |
|---|---|
| Host | Ubuntu 26.04 LTS, kernel 7.0.0-22, KVM |
| CPU/RAM | 2 vCPU AMD EPYC / 3.8 GiB |
| Runtime API | Python 3.11.15 |
| Framework API | Flask 3.x + Gunicorn |
| DB | PostgreSQL 15 + pgvector 0.8.2 |
| Cache | Redis 7 |
| Vector | Weaviate 1.24.0 (imagen vieja pero healthy) |
| LLM local | Ollama |
| Frontend | Next.js 16 via systemd |
| Proxy | nginx 1.28.3 + Let's Encrypt (expira 2026-09-13) |
| Deploy | Capistrano-style: releases/current/shared |
| Docker | 29.1.3, compose con 7 servicios |

### Ramas relevantes

| Rama | HEAD local | En VPS |
|---|---|---|
| `codex/backend-admin-vps-exec` | `7e1c3d1` | Bootstrap: `f0418c0` (3 commits docs atrás) |
| `deploy/maint-mode-plus-wip` | `74d3c7f` | Frontend maintenance: NO en current symlink |
| `audit/sisyphus-vps-integration` | `c82a415` | Solo docs |
| `master` | `4b3acfe` | Solo docs/planes |

### Release actual

```
current -> /opt/myownclone/releases/20260703190910-landing-cleanup-restore
```

7 releases en disco (~24 GiB). `frontend-codex-admin` existe pero no es current.

---

## FASE 1 — Inventario de Implementaciones

### Backend (api/) — Todos presentes en VPS

| Feature | Archivos clave | Estado VPS |
|---|---|---|
| M1: AI models catalog | `api/core/providers/` (10 archivos) | Desplegado |
| M2: SecretCipher AES-256-GCM | `api/core/secret_cipher.py` | Desplegado |
| M3: ModelRegistry | `api/core/model_registry.py` (14KB) | Desplegado |
| M4a: ProviderAdapter | `api/core/providers/base.py`, `registry.py` | Desplegado |
| M4b: 6 provider adapters | `openai.py`, `anthropic.py`, `minimax.py`, `together.py`, `openai_compatible.py`, `local.py` | Desplegado |
| M5: RetryClient | `api/core/retry_client.py` (4.3KB) | Desplegado |
| M6: TokenBudgeter | `api/core/token_budget.py` (3.7KB) | Desplegado |
| M7: ModelManager refactor | `api/core/model_manager.py` | Desplegado |
| M8: Embeddings registry | `api/core/embeddings.py` | Desplegado |
| M9: Admin AI API | `api/controllers/console/myownclone/ai_models.py` (22KB) | Desplegado |
| M10: Runtime integration | Chat/clone controllers | Desplegado |
| M11: Admin UI IA | `MyOwnClone/src/app/admin/ia-modelos/` | Desplegado |
| M12: Cost rollup + rotation | `api/core/ai_audit.py` | Desplegado |
| M13: Backfill + defects | `api/commands/ai_backfill.py` (10.7KB) | Desplegado |
| M14: Balanceador/costs | Admin endpoints | Desplegado |
| Maintenance mode | `api/core/maintenance.py`, middleware, controllers | Desplegado |
| Flask-Babel i18n | `babel.cfg`, `locales/`, `i18n.py` | Desplegado |
| Local Whisper STT | `api/core/providers/local_whisper.py` (5.4KB) | Desplegado |

### Ops/Config

| Archivo | En VPS |
|---|---|
| `ops/docker-compose.backend.prod.yml` | Sí (7 contenedores activos) |
| `ops/deploy-backend.sh` | Sí |
| `ops/deploy-frontend.sh` | Sí |
| `ops/backup_postgres.sh` | Sí (cron diario 3am) |
| `ops/backup_dual.sh` | Sí |
| `ops/smoke-prod.sh` | Sí |
| `ops/nginx-myownclone.conf` | Sí (con security headers) |

### Frontend

| Feature | Estado |
|---|---|
| Landing | Actual current (landing-cleanup-restore) |
| Admin AI models UI | Desplegado |
| i18n LanguageSelector | Desplegado |
| Maintenance page/banner | NO en current (en release frontend-codex-admin) |

---

## FASE 2 — Auditoría Real del VPS: Plan vs Ejecución

Comparación punto por punto de VPS_HARDENING.md vs estado real:

| Plan | Estado real | Veredicto |
|---|---|---|
| **P0-1**: Matar http.server 9999 | Puerto 9999 no escucha | ✅ HECHO |
| **P0-2**: SSH — `PermitRootLogin prohibit-password` | `sshd -T` muestra `permitrootlogin prohibit-password` | ✅ HECHO |
| **P0-2**: SSH — `PasswordAuthentication no` | `sshd -T` muestra `passwordauthentication no` | ✅ HECHO |
| **P0-2**: SSH — drop-in `/etc/ssh/sshd_config.d/40-audit-hardening.conf` | Archivo existe con todas las líneas | ✅ HECHO |
| **P0-2**: UFW activo, solo 22/80/443 | UFW active, 6 reglas (22,80,443 v4+v6) | ✅ HECHO |
| **P0-2**: fail2ban con jail sshd | Activo, 78 IPs baneadas, 2847 intentos fallidos | ✅ HECHO |
| **P0-3**: Rotar SERVICE_API_KEY en nginx | `X-API-Key "apJOM2NEPnRmBSu0mDORRqLpQ_YK5ZEpol3Y2HjUHJGfO3Wu"` EN TEXTO CLARO | ❌ NO HECHO |
| **P0-3**: Eliminar bypass de admin en nginx | `X-User-Id`, `X-User-Role`, `X-User-Email` hardcodeados en `/api/admin/` | ❌ NO HECHO |
| **P0-4**: Security headers nginx | HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy presentes | ✅ HECHO |
| **P0-5**: Backup cron diario PostgreSQL | Cron activo, 7 backups en disco (Jun 27 - Jul 3) | ✅ HECHO |
| **P1**: Limpiar releases a ≤5 | 7 releases (debería ser 5) | ⚠️ PARCIAL |
| **P1**: Docker log-opts en daemon.json | `max-size: 50m, max-file: 3` configurado | ✅ HECHO |
| **P1**: journald limit 200M | `SystemMaxUse=200M` configurado | ✅ HECHO |
| **P1**: Weaviate healthcheck corregido | Weaviate estado: healthy (imagen 1.24.0 vieja) | ✅ HECHO |
| **N/A**: Copiar VPS_HARDENING.md al VPS | Archivo NO existe en VPS | ⚠️ FALTA |

### Clasificación de problemas encontrados

| Código | Problema | Severidad |
|---|---|---|
| A | API key SERVICE_API_KEY hardcodeada en nginx — expuesta en texto claro | **CRÍTICO** |
| A | Admin bypass: nginx inyecta identidad fija (X-User-Id, Role, Email) | **CRÍTICO** |
| B | Backup log tiene error de línea Windows (`bash\r`) — backups funcionan pero log muestra warning | BAJO |
| C | 7 releases en disco en vez de 5 (limpieza parcial) | MEDIO |
| D | VPS_HARDENING.md no copiado al VPS | BAJO |
| E | Weaviate 1.24.0 obsoleta (~2 años) | BAJO |

---

## FASE 3 — Gap Analysis

| Feature | Rama origen | Repo | VPS | Causa | Prioridad |
|---|---|---|---|---|---|
| API key rotation | N/A (hardening plan) | Documentado | NO ejecutado | Hardening incompleto | **CRÍTICA** |
| Admin bypass removal | N/A (hardening plan) | Documentado | NO ejecutado | Hardening incompleto | **CRÍTICA** |
| 3 commits docs/evidence | `codex/backend-admin-vps-exec` | Presente | Ausente | Sync pendiente | MEDIA |
| Maintenance frontend | `deploy/maint-mode-plus-wip` | Presente | No en current | Requiere deploy frontend | BAJA (no tocar) |
| Release cleanup | Hardening plan P1 | Documentado | Parcial (7 vs 5) | Limpieza incompleta | MEDIA |

---

## FASE 4 — Plan Maestro

### F0: Backup y Snapshot
- **Objetivo**: Punto de recuperación antes de cambios
- **Dependencias**: Ninguna
- **Riesgo**: Ninguno
- **Validación**: Archivo .sql.gz verificable
- **Rollback**: N/A

### F1: Rotar API Key y Eliminar Bypass Admin
- **Objetivo**: Cerrar los 2 puntos críticos de seguridad restantes
- **Dependencias**: F0
- **Riesgo**: MEDIO — requiere coordinación nginx + backend env + reinicio API
- **Validación**: nginx -t pasa, curl /healthz OK, admin endpoints rechazan key vieja
- **Rollback**: Restaurar key vieja desde /root/audit-backups/envs-20260619-072221/

### F2: Sync Bootstrap y Limpiar Releases
- **Objetivo**: Bootstrap al día, disco liberado
- **Dependencias**: F0
- **Riesgo**: BAJO — solo docs en los 3 commits pendientes
- **Validación**: git log --oneline -1 muestra HEAD correcto
- **Rollback**: git checkout f0418c0

### F3: Validación Funcional
- **Objetivo**: Confirmar servicios estables post-cambios
- **Dependencias**: F1, F2
- **Riesgo**: BAJO
- **Validación**: healthz/readyz OK, docker ps todos healthy, nginx -t OK
- **Rollback**: Restaurar release anterior via symlink

---

## FASE 5 — Tasks Ejecutables

### T1: Backup DB pre-cambio
```bash
ssh root@212.227.169.99 "docker exec myownclone_postgres pg_dump -U postgres myownclone | gzip > /opt/myownclone/backups/pre-rotate-$(date +%Y%m%d-%H%M).sql.gz && ls -la /opt/myownclone/backups/pre-rotate-*.sql.gz"
```
- **Precondiciones**: SSH acceso
- **Validación**: Archivo existe y tiene tamaño > 0
- **Rollback**: N/A
- **Riesgo**: Ninguno
- **Estado**: pendiente

### T2: Generar nueva SERVICE_API_KEY
```bash
ssh root@212.227.169.99 "python3 -c \"import secrets; print(secrets.token_urlsafe(36))\""
```
- **Precondiciones**: Ninguna
- **Validación**: Key de ~48 chars generada
- **Rollback**: N/A
- **Riesgo**: Ninguno
- **Estado**: pendiente

### T3: Actualizar SERVICE_API_KEY en backend env
```bash
ssh root@212.227.169.99 "sed -i 's/^SERVICE_API_KEY=.*/SERVICE_API_KEY=<NUEVA_KEY>/' /opt/myownclone/shared/backend.env.production && sed -i 's/^SERVICE_API_KEY=.*/SERVICE_API_KEY=<NUEVA_KEY>/' /opt/myownclone/current/ops/backend.env.production"
```
- **Precondiciones**: T2 completado
- **Validación**: grep SERVICE_API_KEY muestra nueva key
- **Rollback**: Restaurar desde /root/audit-backups/envs-20260619-072221/backend.env.production
- **Riesgo**: MEDIO
- **Estado**: pendiente

### T4: Actualizar SERVICE_API_KEY en frontend env
```bash
ssh root@212.227.169.99 "sed -i 's/^SERVICE_API_KEY=.*/SERVICE_API_KEY=<NUEVA_KEY>/' /opt/myownclone/shared/frontend.env.production && sed -i 's/^MYOWNCLONE_SERVICE_API_KEY=.*/MYOWNCLONE_SERVICE_API_KEY=<NUEVA_KEY>/' /opt/myownclone/shared/frontend.env.production"
```
- **Precondiciones**: T2 completado
- **Validación**: grep SERVICE_API_KEY muestra nueva key
- **Rollback**: Restaurar desde /root/audit-backups/envs-20260619-072221/frontend.env.production
- **Riesgo**: MEDIO
- **Estado**: pendiente

### T5: Eliminar bypass admin en nginx
Reemplazar el bloque `location /api/admin/` para quitar los headers hardcodeados. El backend debe validar JWT/cookie, no headers de nginx.
- **Precondiciones**: T3 completado
- **Validación**: `nginx -t` pasa, `grep X-API-Key /etc/nginx/sites-enabled/myownclone` no muestra resultado
- **Rollback**: Restaurar desde /root/audit-backups/nginx-20260619-072212/
- **Riesgo**: ALTO — si el backend no valida JWT correctamente, admin dejará de funcionar
- **Estado**: pendiente

### T6: Reiniciar servicios
```bash
ssh root@212.227.169.99 "cd /opt/myownclone/current/ops && docker compose -f docker-compose.backend.prod.yml restart api && nginx -s reload && systemctl restart myownclone-frontend"
```
- **Precondiciones**: T3, T4, T5 completados
- **Validación**: healthz OK, readyz OK, docker ps healthy
- **Rollback**: Restaurar release anterior via symlink
- **Riesgo**: MEDIO — downtime de ~30s
- **Estado**: pendiente

### T7: Sync bootstrap
```bash
ssh root@212.227.169.99 "cd /opt/myownclone/bootstrap && git fetch origin && git pull origin codex/backend-admin-vps-exec"
```
- **Precondiciones**: Ninguna (independiente de T1-T6)
- **Validación**: `git log --oneline -1` muestra `7e1c3d1`
- **Rollback**: `git checkout f0418c0`
- **Riesgo**: BAJO
- **Estado**: pendiente

### T8: Limpiar releases viejos
```bash
ssh root@212.227.169.99 "cd /opt/myownclone/releases && ls -dt */ | tail -n +5 | xargs rm -rf"
```
- **Precondiciones**: F3 validación completada
- **Validación**: `ls /opt/myownclone/releases/ | wc -l` muestra 4 o menos
- **Rollback**: `git clone` desde remote
- **Riesgo**: BAJO
- **Estado**: pendiente

### T9: Health check final
```bash
ssh root@212.227.169.99 "curl -s http://127.0.0.1:5001/healthz && echo '' && curl -s http://127.0.0.1:5001/readyz && echo '' && docker ps --format 'table {{.Names}}\t{{.Status}}' && echo '=== NGINX ===' && nginx -t 2>&1"
```
- **Precondiciones**: T6 completado
- **Validación**: Todos los checks pasan
- **Rollback**: N/A
- **Riesgo**: Ninguno
- **Estado**: pendiente

---

## FASE 6 — Auto-Auditoría

| Check | Resultado |
|---|---|
| ¿Toca frontend? | NO — T1-T9 son backend/ops. T4 actualiza solo env vars de service key, no diseño. |
| ¿Toca landing? | NO |
| ¿Toca login? | NO |
| ¿Tareas duplicadas? | NO — cada T es única |
| ¿Falta rollback? | NO — cada T crítica tiene rollback |
| ¿Faltan validaciones? | NO — cada T tiene validación |
| ¿Contradicciones? | NO |
| ¿Deploy sin backup? | NO — T1 ejecuta backup primero |

---

## FASE 7 — Riesgos

| Riesgo | Impacto | Mitigación |
|---|---|---|
| Admin endpoints dejan de funcionar tras quitar bypass (T5) | ALTO | Verificar que backend valida JWT/cookie ANTES de ejecutar T5. Si no valida, T5 debe esperar fix del backend. |
| Frontend service key mismatch tras rotación | MEDIO | Actualizar ambos env files (backend + frontend) en el mismo paso |
| Backup corrupto | BAJO | Verificar tamaño del .sql.gz > 0 |
| Releases limpiados contiene algo necesario | BAJO | current symlink no se toca, solo se eliminan releases viejos |

---

## Validación Final

- **Backend/admin**: Sisyphus M1-M14 completo y ejecutándose
- **Frontend**: NO modificado (landing, login, diseño intocables)
- **Landing**: NO modificada
- **Login**: NO modificado
- **DB**: Migraciones consistentes (`2026_07_03_0001`)
- **Servicios**: 7 contenedores healthy, nginx passing
- **Hardening**: 8/11 puntos del plan ejecutados, 2 críticos pendientes (API key + admin bypass)

---

## FASE 8 — Auditoría de Compatibilidad: Sisyphus M0-M20 vs VPS Real (2026-07-07)

### Contexto
Después del FASE 1-7, se intentó evaluar si el backend Sisyphus M0-M20 presente en el repo (`sisyphus/anti-forget-layer` HEAD remoto `17e552a`, HEAD local `686774c`) podía portarse al VPS. **Resultado: NO es posible un portado incremental**. La incompatibilidad es estructural.

### 8.1 Estado real verificado del VPS (SSH live)

| Componente | Valor verificado |
|---|---|
| Release activo (symlink `/opt/myownclone/current`) | `20260703190910-landing-cleanup-restore` |
| `.deploy-backend-meta` `release_id` | `20260701150141-backend-codex-deploy` |
| `.deploy-backend-meta` `source_sha` | `f0418c04cfac21a9a3881459ba2172cc94af6e6d` |
| **MISMATCH** | symlink apunta a release de **03 jul** pero meta dice **01 jul**. El `current` fue re-symlinkeado el 2026-07-05 (rollback del codex admin roto). El meta quedó stale. |
| `alembic_version` en BD | `2026_07_03_0001` |
| Tablas totales en BD | 32 |
| `chunks.embedding` | `vector(1024)` con índice ivfflat |
| Frontend BUILD_ID | `s4Hs00UHv6esTNBt7xcUp` |
| Branch bootstrap `/opt/myownclone/bootstrap` | `audit/vps-sync-and-docs` HEAD `e9b9d89` (drift local) |

### 8.2 Inventario Sisyphus M0-M20 en repo

| Capa | Archivos | Estado en repo |
|---|---|---|
| `api/core/` nuevos | `cost_recording.py`, `smart_router.py`, `metrics_collector.py`, `feedback_collector.py`, `ingestion_pipeline.py`, `security_types.py`, `reranking.py` | Presentes (no mergeados) |
| `api/core/providers/` v2 | `openai_adapter.py`, `anthropic_adapter.py`, `*_adapter.py` (sufijo `_adapter`) | Presentes (no mergeados) |
| `api/core/model_manager.py` | 571 líneas, asume provider v2 con `_adapter` | Presente (no mergeado) |
| `api/migrations/versions/` Sisyphus | 19 archivos (7 incrementales más que VPS) | Presentes (no mergeados) |
| VPS actual `model_manager.py` | **626 líneas**, soporta DeepSeek vía `OpenAICompatibleAdapter`, integra `TokenBudgeter`, `RetryClient` | **Desplegado y operativo** |

### 8.3 Matriz de incompatibilidad punto por punto

| Punto de fricción | Estado VPS | Estado Sisyphus repo | Veredicto |
|---|---|---|---|
| `revision_id`/`down_revision` chain Alembic | VPS: `2026_07_03_0001` (e.g. `e2f3a4b5c6d7`) | Sisyphus: chain propia (e.g. `d4e7f8a9b0c1`) | **INCOMPATIBLE** — las 7 migrations Sisyphus no son continuables |
| Tabla `ai_invocations` columnas | VPS: schema actual con `prompt_tokens`, `completion_tokens`, `cost_usd`, `provider`, `model`, `latency_ms`, `created_at` + FK | Sisyphus espera columnas adicionales: `routing_strategy`, `feedback_score`, `cache_hit`, `embedding_model` | **INCOMPATIBLE** — INSERT fallaría |
| Tabla `embedding_outbox` | VPS: **NO EXISTE** | Sisyphus: la crea en migration propia | **BLOQUEANTE** — código depende de tabla inexistente |
| Tabla `response_feedback` | VPS: **NO EXISTE** | Sisyphus: la crea en migration propia | **BLOQUEANTE** — `feedback_collector.py` crashea |
| Tabla `routing_log` | VPS: **NO EXISTE** | Sisyphus: la crea en migration propia | **BLOQUEANTE** — `smart_router.py` crashea |
| Tabla `moderation_log` | VPS: **NO EXISTE** | Sisyphus: la crea en migration propia | **BLOQUEANTE** — `security_types.py` referencia |
| Provider system | VPS: v1 (`openai.py`, `anthropic.py`) sin sufijo | Sisyphus: v2 (`*_adapter.py`) | **INCOMPATIBLE** — `model_manager.py` Sisyphus importa v2 inexistente en VPS |
| `model_manager.py` | VPS: 626 líneas, MÁS completo (DeepSeek, retry, budget) | Sisyphus: 571 líneas, asume v2 | **REGRESIÓN** — reemplazar el del VPS perdería DeepSeek + retry + budget |
| `security_types.py` / `reranking.py` | VPS: no existen, no hay dependencia | Sisyphus: presentes, sin tabla destino | **BLOQUEANTE** — portar sin tabla = ImportError / 500 |
| `chunks.embedding` dimension | VPS: `vector(1024)` ivfflat | Sisyphus asume 1024 (compatible) | ✅ Compatible |
| Redis sliding window | VPS: API | Sisyphus: API | ✅ Compatible |
| OpenAI-compatible API (DeepSeek) | VPS: integrado en `model_manager` | Sisyphus: asume adaptador separado | **REGRESIÓN** |
| Frontend | Landing aprobada intacta | Sisyphus NO toca frontend | ✅ Aislado |

### 8.4 Clasificación de portabilidad

| Categoría | Items | Acción permitida |
|---|---|---|
| **Seguro sin migración** | Nada — todas las features Sisyphus nuevas requieren tablas | NINGUNA |
| **Requiere migración** | `embedding_outbox`, `response_feedback`, `routing_log`, `moderation_log`, columnas extra en `ai_invocations` | NO SE EJECUTA (rompería Alembic chain) |
| **Incierto / conflictivo** | `model_manager.py`, `providers/*_adapter.py`, `security_types.py`, `reranking.py` | NO SE PORTA (regresión sobre código VPS más completo) |

### 8.5 Por qué NO se pueden aplicar las 7 migrations Sisyphus

1. **Alembic chain rota**: VPS tiene `alembic_version=2026_07_03_0001` con `down_revision=e2f3a4b5c6d7`. Las migrations Sisyphus tienen `down_revision` apuntando a revisions que NO están aplicadas. `alembic upgrade head` fallaría con `Can't locate revision identified by 'X'`.
2. **Solapamiento de revisiones**: varias migrations Sisyphus intentan crear tablas que en VPS tienen versiones distintas (mismo nombre, schema diferente) → duplicación de objetos.
3. **Divergencia irreversible**: aun reescribiendo las migrations para que continuen desde `2026_07_03_0001`, el código Sisyphus espera schema distinto al VPS, lo que requiere cambio de código + cambio de schema coordinados.
4. **Riesgo operacional**: el VPS está sirviendo tráfico real (BUILD_ID activo, login admin funcional, contenedores healthy). Una migration fallida o un `model_manager.py` roto significa caída de API.

### 8.6 Por qué NO se puede hacer cherry-pick

- Los archivos Sisyphus están entrelazados: `cost_recording` importa `metrics_collector`, que importa `feedback_collector`, que importa `security_types`. Un cherry-pick parcial deja imports rotos.
- El provider system v2 (`*_adapter.py`) **no existe** en VPS; cherry-pickear `model_manager.py` Sisyphus rompe imports.
- El VPS `model_manager.py` (626 líneas) es **más nuevo** y soporta DeepSeek + retry + budget; cherry-pickear encima es regresión.

### 8.7 Conclusión — DECISIÓN ACEPTADA: OPCIÓN C

**Bloqueo por incompatibilidad real**. No se portará código Sisyphus ni migrations al VPS en esta tarea.

| Bloqueador | Tipo |
|---|---|
| Alembic chain incompatible (revisions Sisyphus no aplicadas) | Estructural |
| `ai_invocations` schema divergence (columnas faltantes) | Estructural |
| Tablas faltantes: `embedding_outbox`, `response_feedback`, `routing_log`, `moderation_log` | Estructural |
| Provider v2 (`*_adapter.py`) no existe en VPS | Estructural |
| `model_manager.py` VPS MÁS nuevo que el de Sisyphus (626 vs 571 líneas) | Regresión |
| `security_types.py` / `reranking.py` sin tablas destino | Funcional |

### 8.8 Recomendación siguiente

**Proyecto separado**: rebase backend Sisyphus → VPS, no intento incremental. Requiere:

1. Branch dedicada `rebase/sisyphus-backend-vps` desde un ancestro común.
2. Reescribir migrations Sisyphus para que `down_revision` apunte a `2026_07_03_0001`.
3. Adaptar `model_manager.py` Sisyphus para soportar v1 + v2 (dual provider), o migrar VPS a v2 en un solo paso (con backup DB + ventana de mantenimiento).
4. Backfill de datos faltantes en `ai_invocations` antes de poder usar features Sisyphus.
5. Tests E2E del flujo completo antes de tocar VPS live.

**Esto NO se aborda en esta tarea.** Se documenta aquí como input para `MASTER_TASK.md` y como bloqueador conocido.

### 8.9 Lo que NO se hizo (por restricción explícita del usuario)

- ❌ NO se copiaron `security_types.py` ni `reranking.py` al VPS
- ❌ NO se aplicaron migrations
- ❌ NO se reemplazó `model_manager.py`
- ❌ NO se tocaron providers
- ❌ NO se cambió `MINIMAX` (esa tarea queda aislada y aparte)
- ❌ NO se tocó frontend / landing / login
- ❌ NO se hicieron merges, cherry-picks ni deploys

---

## Fuente de verdad

**Este archivo** (`.sisyphus/evidence/full-audit-2026-07-06.md`) es la **fuente de verdad** de la auditoría de compatibilidad entre repo y VPS. Cualquier divergencia con `MASTER_STATE.md` / `MASTER_LOG.md` se resuelve a favor de este documento.

## Cambios por cherry-pick / portado: PROHIBIDOS en esta tarea

Rama documental: `release/sisyphus-incompatible-2026-07-07`. No merges, no cherry-picks, no deploys. Solo documentación y evidencia.

# TASK AUDITORIA VPS — 2026-07-13

> **Lista accionable derivada de `PLAN_MAESTRO_AUDITORIA_2026-07-13.md`.**
> Cada tarea es atómica, cita `archivo:línea` exacto, y tiene criterios de aceptación verificables.
> **Modo L1 (report-only) por defecto.** El humano debe habilitar L2 **por bloque** antes de implementar.
> Convención de IDs: `<FASE>.<BLOQUE>.<NN>` p.ej. `P0.1.01`.

**Leyenda de estado:** `[ ]` pendiente · `[~]` en progreso · `[x]` hecho · `[!]` bloqueado

---

## GATES DE FASE (no saltar)

- **Gate P0→P1:** `next build` verde · `pytest` sin false greens · `SERVICE_API_KEY` ausente del repo · smoke admin 401/403 · `/metrics` 401 sin creds · test SSRF bloquea URL interna.
- **Gate P1→P2:** `alembic check` sin drift · test cross-tenant IDOR verde · test reset-password bypass verde · test XSS sanitize rechaza payload · backup restore test verde · CI lint rompe en error · CSRF token requerido en POST.
- **Gate P2→P3:** query count sin N+1 en endpoints listados · `npm audit`/`pip-audit` sin high · i18n dashboard 100%.

---

# FASE P0 — CRÍTICO (estabilizar + tapar agujeros de seguridad)

## P0.1 — Rotación de secretos y lockdown auth headers
**IDs matriz:** C-01, C-02, H-01 · **Estado:** [ ] · **Depende de:** — · **Desbloquea:** todos los P0/P1 de seguridad

**Archivos:**
- `ops/nginx-myownclone.conf:81,98,113` — remover `X-API-Key` hardcoded y `X-User-Role`/`X-User-Id` inyectados.
- `ops/nginx.myownclone.conf.example:5-14` — confirmar que es el contrato correcto (nginx solo valida, no inyecta).
- `api/libs/login.py:42-47, 65-87` — no confiar en `X-User-Role`/`X-User-Id` sin confirmación DB.
- `api/libs/security_checks.py:24-26` — unificar `_is_production()` con `_allow_dev_service_key()`.
- `.sisyphus/evidence/audit-execution-2026-07-06.md:8` — redactar el valor de la key (kept en history, pero al menos no forward).

**Tareas:**
- [ ] **P0.1.01** Generar nueva `SERVICE_API_KEY` con `openssl rand -hex 32` fuera del repo (en el VPS, env del servicio).
- [ ] **P0.1.02** Editar `ops/nginx-myownclone.conf`: eliminar las 3 líneas con la key commiteada y los headers `X-User-Role`/`X-User-Id`/`X-User-Email` inyectados en locations admin. nginx debe solo `proxy_pass` (el frontend `proxy.ts` ya inyecta los headers correctos desde el JWT).
- [ ] **P0.1.03** En `api/libs/login.py:65-87`, para el branch `X-API-Key`: requerir que `X-User-Id` exista en `accounts` Y que `role` confirmado por DB (no por header). Si no existe, 401. Mantener el path solo para service-to-service Next.js→backend.
- [ ] **P0.1.04** Unificar `_is_production()` (`security_checks.py:24-26`) con `_allow_dev_service_key()` (`login.py:42-47`) y `_setup_dev_keys()` (`app_factory.py:72-80`): una sola función `_is_production()` usada en los 3 sitios.
- [ ] **P0.1.05** Aplicar el fix H4 existente (`admin_platform.py:811-830`) a **todos** los endpoints admin, no solo `ingestion-status`: `_is_platform_admin` debe confirmar rol por DB.
- [ ] **P0.1.06** Documentar la rotación en `.omo/evidence/task-P0.1-secret-rotation.md` con fecha, key vieja comprometida, key nueva (sólo hash/fingerprint, no valor), y runbook para volver a rotar.

**Aceptación:**
- `git grep -n "XimE6gtCeMepQ3WC8RwIBI7hgSJfAiozCdY95oEz1qBDm18h"` retorna 0 líneas en el working tree (history se asume comprometida).
- `curl -H "X-API-Key: <vieja>" -H "X-User-Role: platform_admin" .../admin/overview` → 401/403.
- `pytest tests/test_smoke.py` verde.
- Smoke `ops/smoke-prod.sh` verde tras deploy.

---

## P0.2 — Build frontend desbloqueado
**IDs matriz:** C-18, C-19, H-19 (parcial) · **Estado:** [ ] · **Depende de:** — · **Desbloquea:** todo trabajo en dashboard

**Archivos:**
- `MyOwnClone/src/app/(dashboard)/layout.tsx:7` — import `LanguageSwitcher` roto.
- `MyOwnClone/src/components/ui/LanguageSelector.tsx` — componente existente (renombrar o crear barrel).
- `MyOwnClone/src/i18n/en.json`, `MyOwnClone/src/i18n/es.json` — añadir namespaces `settings` y `billing`.
- `MyOwnClone/src/app/(dashboard)/settings/page.tsx:15` — `useTranslations("settings")`.
- `MyOwnClone/src/app/(dashboard)/facturacion/page.tsx:49` — `useTranslations("billing")`.

**Tareas:**
- [ ] **P0.2.01** Crear `MyOwnClone/src/components/LanguageSwitcher.tsx` como barrel re-export de `ui/LanguageSelector`, **o** cambiar el import en `layout.tsx:7` a `@/components/ui/LanguageSelector`. (Prefiera la 2ª: menos superficie.)
- [ ] **P0.2.02** Añadir namespace `settings` a `en.json` y `es.json` con todas las keys referenciadas en `settings/page.tsx` (title, subtitle, passwordMismatch, saved, profile, name, email, emailReadOnly, appearance, theme, themeDesc, connectedAccounts, connectedAccountsDesc, changePassword, currentPassword, newPassword, confirmPassword, updatePassword, saving, dangerZone, dangerZoneDesc, deleteConfirmLabel, deleteButton, deleting, loading, passwordTooShort, passwordChangeError, deleteError).
- [ ] **P0.2.03** Añadir namespace `billing` a `en.json` y `es.json` con todas las keys referenciadas en `facturacion/page.tsx`.
- [ ] **P0.2.04** Mapear las rutas API faltantes llamadas desde el dashboard: documentar cuáles se proxyan a Flask (válidas) y cuáles necesitan handler Next.js. Lista inicial: `/api/auth/change-password`, `/api/account/delete`, `/api/clone/clones/{cid}/meeting-types[/{id}]`, `/api/clone/clones/{cid}/availability[/{id}]`, `/api/me/locale`. Para cada una: o crear handler que haga proxy, o confirmar que `proxy.ts` ya lo enruta.
- [ ] **P0.2.05** Correr `cd MyOwnClone && npm run build` y confirmar verde sin tocar `src/app/page.tsx`, `src/app/login/*`, `src/app/registro/*`, `src/app/(public)/*`, `src/components/landing/*`.

**Aceptación:**
- `npm run build` exit 0.
- Cargar `/settings` y `/facturacion` en browser no lanza `MISSING_MESSAGE`.
- `BUILD_ID` no cambia para la landing (verificar `.next/BUILD_ID` si aplica, o aislar el build del dashboard).

---

## P0.3 — Endpoints críticos backend (crashes silenciosos)
**IDs matriz:** C-05, C-06, C-07, C-08, C-09, C-14 · **Estado:** [ ] · **Depende de:** —

**Archivos:**
- `api/core/model_manager.py:460` — `AITask.CHAT_FALLBACK`.
- `api/core/model_manager.py:606-621` — `record_llm_cost` columnas.
- `api/models/ai_models.py:214-253` — definición real de `AIInvocation`.
- `api/core/myownclone/email_ai.py:155-156` — imports absolutos rotos.
- `api/controllers/common/schema.py:126` — import roto.
- `api/controllers/deploy.py:44` — typo `return124`.
- `api/core/retrieval.py:263` + `api/core/rag/datasource/retrieval_service.py:4-15` — stub roto.

**Tareas:**
- [ ] **P0.3.01** En `model_manager.py:460`, reemplazar `AITask.CHAT_FALLBACK` por un miembro existente o añadir `CHAT_FALLBACK = "chat_fallback"` al enum `AITask` en `models/ai_models.py:75-82`. Decidir cuál es semánticamente correcto (probablemente `CHAT`).
- [ ] **P0.3.02** En `model_manager.py:606-621`, alinear `record_llm_cost` con las columnas reales de `AIInvocation` (`prompt_tokens`, `completion_tokens`, `model`, `task`, `success`, `cost_cents` si existe — verificar `models/ai_models.py:214-253`). Si `cost_cents` no existe como columna, añadirlo vía migración o usar `CostDailyRollup`/`CostTracking`.
- [ ] **P0.3.03** En `core/myownclone/email_ai.py:155-156`, corregir imports absolutos a relativos al paquete `api.`: `from api.extensions.ext_database import db`, `from api.models.myownclone import ...`.
- [ ] **P0.3.04** En `controllers/common/schema.py:126`, cambiar `from controllers.console import console_ns` → `from api.controllers.console import console_ns`.
- [ ] **P0.3.05** En `deploy.py:44`, cambiar `return124, f"Command timed out..."` → `return 124, f"Command timed out..."`.
- [ ] **P0.3.06** En `core/rag/datasource/retrieval_service.py:4-15`, o implementar `RetrievalService.retrieve` para retornar una lista de objetos con `.metadata`, o cambiar el caller `retrieval.py:263-272` para que no consuma el stub como lista. Si es feature no implementada, retornar `[]` (lista vacía) en vez de un dict, y agregar log warning.
- [ ] **P0.3.07** Añadir tests unitarios por cada fix: `test_record_llm_cost_persists`, `test_chat_fallback_resolves`, `test_email_ai_imports`, `test_deploy_timeout_returns_124`.

**Aceptación:**
- `pytest api/tests/ -k "record_llm_cost or chat_fallback or email_ai or deploy_timeout"` todo verde.
- `python -c "from api.core.model_manager import ModelManager"` sin error.
- `python -c "from api.core.myownclone.email_ai import _get_clone_context"` sin error.

---

## P0.4 — IDOR + aislamiento de tenant
**IDs matriz:** C-12, C-20, H-03, H-04 · **Estado:** [ ] · **Depende de:** —

**Archivos:**
- `api/controllers/console/myownclone/voice.py:88-186` — sin tenant scoping.
- `api/controllers/console/myownclone/clone.py:335,344-384` — Source IDOR.
- `api/controllers/console/myownclone/prompts_ctrl.py:35-153` — sin tenant scoping.
- `MyOwnClone/src/app/api/clone/memories/[id]/route.ts:34-59` — IDOR DELETE/PUT.
- Patrón correcto de referencia: `api/controllers/console/myownclone/feedback.py:19-31` (`_clone_owned_by_tenant`) y `src/app/api/clone/sources/route.ts:65-76` (`verifyCloneOwnership`).

**Tareas:**
- [ ] **P0.4.01** Voice: añadir `clone_id`/`tenant_id` a `VoiceCloneApi.post`; en `VoiceTtsApi` y `VoiceDeleteApi`, verificar que el `voice_id` pertenece a un clone del tenant antes de operar.
- [ ] **P0.4.02** Clone sources: en `SourceListApi.get` (`clone.py:335`), reemplazar el prefix-like por join `CloneConfig.tenant_id == tenant.id`; en `SourceListApi.post` (`clone.py:344-384`), verificar `clone_id` pertenece al tenant antes de crear.
- [ ] **P0.4.03** Prompts: en `PromptListApi.get`, `PromptDetailApi.get/put/delete`, `PromptVersionApi.post`, añadir predicado `Prompt.tenant_id == tenant.id` (si la columna no existe, añadirla vía migración o derivar de `clone_id`→`CloneConfig.tenant_id`).
- [ ] **P0.4.04** Frontend memories: en `src/app/api/clone/memories/[id]/route.ts`, DELETE y PUT deben verificar `verifyCloneOwnership(memory.cloneId)` como ya hace `sources/route.ts:65-76`.
- [ ] **P0.4.05** Extraer helper `verify_tenant_ownership(clone_id, tenant_id)` backend y `verifyCloneOwnership` frontend a módulos compartidos para uso uniforme en P1/P2.
- [ ] **P0.4.06** Tests cross-tenant: tenant A intenta leer/borrar/editar recurso de tenant B → 403/404. Cubrir voice, sources, prompts, memories.

**Aceptación:**
- Nuevos tests cross-tenant verde.
- `pytest -k "cross_tenant or idor"` todo verde.

---

## P0.5 — SSRF + info leak
**IDs matriz:** C-10, C-13 · **Estado:** [ ] · **Depende de:** —

**Archivos:**
- `api/core/ingestion.py:104-108, 150-158` — fetch URLs usuario.
- `api/core/metrics.py:77-79` — `/metrics` sin auth.

**Tareas:**
- [ ] **P0.5.01** En `ingestion.py`, añadir `_is_safe_url(url)`: rechazar esquemas no-`http(s)`, rechazar hosts que resuelvan a IPs privadas/loopback/link-local (`ipaddress.ip_address(...).is_private`, con resolución DNS previa para nombres), rechazar metadata cloud (`169.254.169.254`, `metadata.google.internal`). Aplicar antes de `requests.get`.
- [ ] **P0.5.02** En `metrics.py:77-79`, proteger `/metrics` con basic auth (`METRICS_USER`/`METRICS_PASSWORD` env) y/o IP allowlist. En prod, retorno 401 sin creds.
- [ ] **P0.5.03** Tests: (a) POST source con `url=http://169.254.169.254/` → 400/403, no se crea chunk con el body del metadata service; (b) GET `/metrics` sin auth → 401.

**Aceptación:**
- Tests SSRF y metrics-auth verde.

---

## P0.6 — Tests de salud honestos
**IDs matriz:** C-21 · **Estado:** [ ] · **Depende de:** —

**Archivos:**
- `tests/test_operational_hardening.py:35-67` — 3 tests que no pueden pasar.
- `api/app_factory.py:246-302` — implementación real de `/healthz` y `/readyz`.

**Tareas:**
- [ ] **P0.6.01** Decidir contrato: `/healthz` = readiness (checks deps, 503 si fallan), `/readyz` = liveness (siempre 200 si el proceso vive). Documentar en `app_factory.py`.
- [ ] **P0.6.02** Alinear los 3 tests con el contrato. `test_healthz_returns_ok` debe mockear db+redis+ollama y assert 200 `{"status":"ready"}`; `test_readyz_returns_ready` asserts 200 siempre; `test_readyz_returns_503_when_database_fails` debe renombrarse a `test_healthz_returns_503_when_database_fails` y apuntar a `/healthz`.
- [ ] **P0.6.03** En `app_factory.py:246-289`, dejar de exponer `error: {exc}` en el body 503 público (info leak medium). Retornar `{"status":"degraded","checks":{...}}` sin texto de driver.

**Aceptación:**
- `pytest tests/test_operational_hardening.py` verde.
- `GET /healthz` sin mocks en CI no devuelve texto de driver.

---

# FASE P1 — HIGH (corregir seguridad y robustez)

## P1.1 — Arquitectura metadata unificada
**IDs matriz:** C-04 (raíz) · **Estado:** [ ] · **Depende de:** Gate P0 · **Desbloquea:** P1.2, P1.4

**Archivos:**
- `api/extensions/ext_database.py:5` — `db = SQLAlchemy()`.
- `api/base.py:23` — `TypeBase(DeclarativeBase)`.
- `api/migrations/env.py:28` — `target_metadata`.

**Tareas:**
- [ ] **P1.1.01** Cambiar `ext_database.py:5` a `db = SQLAlchemy(model_class=TypeBase)` para que `db.Model` use el mismo registry que `TypeBase`. Verificar que todos los modelos `db.Model` (`Prompt`, `SystemSetting`, `OnboardingStep`, `AuditLog`) sigan funcionando.
- [ ] **P1.1.02** En `migrations/env.py:28`, cambiar `target_metadata` a la metadata combinada (`db.metadata` ahora incluye todas las tablas).
- [ ] **P1.1.03** Generar migration vacía `alembic revision --autogenerate -m "verify unified metadata"` y confirmar que no detecta cambios spurious (si detecta, es que las tablas `db.Model` no estaban en la metadata antes — esperado).
- [ ] **P1.1.04** Smoke test: `alembic check` sin drift; `pytest api/tests/` verde.

**Aceptación:**
- `alembic check` limpio.
- Todas las tablas visibles en `alembic revision --autogenerate` (no solo las 5 de `db.Model`).

---

## P1.2 — Cablear middlewares
**IDs matriz:** C-03, C-16, C-17, H-05 · **Estado:** [ ] · **Depende de:** P1.1 (para tabla audit_log en migración)

**Archivos:**
- `api/app_factory.py:297-302` — registrar middlewares.
- `api/middleware/maintenance.py:36-44, 53-84` — JWT decode sin verify.
- `api/middleware/audit_trail.py:14-95` — DDL fuera de migraciones, no invocado.
- `api/middleware/tier_enforcement.py:15-41, 77-113` — vocabulario plan, fail-open.

**Tareas:**
- [ ] **P1.2.01** En `app_factory.py` `create_app`, llamar `init_i18n(app)`, `init_maintenance_middleware(app)`, registrar `audit_action` y `require_within_limit` como decorators en los endpoints correspondientes (o como `before_request` hooks selectivos).
- [ ] **P1.2.02** Fix C-17: en `middleware/maintenance.py:36-44`, decodificar JWT con `jwt.decode(token, secret, algorithms=["HS256"])` (verificando firma), no `base64.urlsafe_b64decode`.
- [ ] **P1.2.03** Fix C-16: mover `CREATE TABLE audit_log` a una migración Alembic; eliminar `_ensure_table` runtime DDL; añadir lock o usar `checkfirst=True` con manejo de concurrencia.
- [ ] **P1.2.04** Aplicar `log_audit_action` a los endpoints state-changing (POST/PUT/DELETE) admin y de clone.
- [ ] **P1.2.05** Fix H-05: en `tier_enforcement.py:15-41`, alinear `TIER_LIMITS` keys con `contracts.PLAN_KEYS = ("trial","basic","pro","scale","enterprise")`. Mapear `free→trial`, `starter→basic`, `business→scale`, etc., o renombrar directamente.
- [ ] **P1.2.06** Hacer `require_within_limit` fail-closed en missing tenant (return 403, no pass-through).
- [ ] **P1.2.07** Tests: maintenance mode retorna 503 a no-admins; admin bypass funciona con JWT válido; tier limit bloquea al exceder.

**Aceptación:**
- `pytest -k "maintenance or tier or audit"` verde.
- Activar `system_settings.maintenance_active = true` → requests no-admin retornan 503.

---

## P1.3 — Rate-limiting Redis-backed
**IDs matriz:** H-02, H-11, rate_limit.py off-by-one · **Estado:** [ ] · **Depende de:** —

**Archivos:**
- `api/controllers/console/auth.py:28,84-101,137` — store memoria, remote_addr.
- `api/controllers/myownclone_public.py:52,80-97` — store ilimitado, X-Forwarded-For spoofable.
- `api/core/rate_limit.py:151-225, 200-219` — off-by-one.
- `api/controllers/console/myownclone/runtime.py:22-38` — fail-open contradictorio.

**Tareas:**
- [ ] **P1.3.01** Reemplazar `_memory_fallback` en `auth.py` y `_public_rate_limit_store` en `myownclone_public.py` por `core/rate_limit.check_rate_limit` con Redis backing.
- [ ] **P1.3.02** Extraer IP del cliente consistemente: una función `_client_ip(request)` que respete `X-Forwarded-For` solo si viene de nginx confiable (configurar `TRUSTED_PROXIES` count). Usar en auth, chat, bookings.
- [ ] **P1.3.03** Fix off-by-one en `rate_limit.py:200-219`: hacer `zadd` solo si el request es aceptado (después del check), o aceptar que el conteo incluya el actual y ajustar el threshold.
- [ ] **P1.3.04** Hacer `runtime.py:22-38` fail-closed consistente con `rate_limit.py` (o hacer ambos fail-open con log alto + alerta — decidir y documentar).
- [ ] **P1.3.05** Tests: rate-limit persiste entre workers (mock Redis); IP spoofing no bypassa.

**Aceptación:**
- `pytest -k "rate_limit"` verde.
- No hay `defaultdict(list)` sin eviction en el request path.

---

## P1.4 — FKs + integridad referencial
**IDs matriz:** H-06 · **Estado:** [ ] · **Depende de:** P1.1

**Archivos:**
- `api/models/clone.py`, `meeting.py`, `knowledge.py`, `email.py`, `conversation.py`, `analytics.py`, `ai_models.py` — columnas `String(36)` sin FK.
- Nueva migración Alembic.

**Tareas:**
- [ ] **P1.4.01** Script pre-migración que reporte huérfanos (rows con `clone_id`/`tenant_id`/`meeting_type_id` que no existen en la tabla padre). Documentar cuántos hay y cleanup manual necesario.
- [ ] **P1.4.02** Migración: añadir FKs `ON DELETE CASCADE` para `CloneConfig.tenant_id → tenants.id`, `CloneModePrompt.clone_id → clone_configs.id`, `Source.clone_id`, `Chunk.source_id`, `MeetingType_.clone_id`, `Booking.meeting_type_id`, etc. Empezar por las que no tengan huérfanos.
- [ ] **P1.4.03** Cleanup de huérfanos (con aprobación humana) o marcarlos como `deleted` si no se pueden borrar.
- [ ] **P1.4.04** Tests: borrar un clone → sus sources/chunks/meeting_types se borran en cascada.

**Aceptación:**
- `alembic upgrade head` verde en staging con datos reales.
- Test cascade verde.

---

## P1.5 — Retrieval con vector search SQL
**IDs matriz:** H-07 · **Estado:** [ ] · **Depende de:** —

**Archivos:**
- `api/core/retrieval.py:144-205` — full-table load + scoring Python.
- DB: pgvector ya habilitado (`migrations/.../0005_enable_pgvector_extension.py`).

**Tareas:**
- [ ] **P1.5.01** Reemplazar `_retrieve_from_local_chunks` por query SQL: `SELECT ... ORDER BY chunk.embedding <=> :query_embedding LIMIT :k`. Verificar que la columna `Chunk.embedding` sea tipo `vector` (migración `2026_07_03_0001_chunks_embedding_to_vector.py` existe).
- [ ] **P1.5.02** Crear índice `ivfflat` o `hnsw` en `chunks.embedding` si no existe.
- [ ] **P1.5.03** Fallback léxico solo si pgvector no está (mantener path Python como degradación, con log).
- [ ] **P1.5.04** Test: clone con 10k chunks retorna top-k en <100ms.

**Aceptación:**
- Benchmark retrieval <100ms p95 con 10k chunks.

---

## P1.6 — Booking unique constraint
**IDs matriz:** H-12 · **Estado:** [ ] · **Depende de:** P1.1

**Tareas:**
- [ ] **P1.6.01** Migración: unique constraint en `(meeting_type_id, date, start_time)` (o `(clone_id, ...)` si se añade la columna).
- [ ] **P1.6.02** En `myownclone_public.py:660-669` y `booking.py:368-378`, capturar `IntegrityError` y retornar 409 conflict.
- [ ] **P1.6.03** Test: dos POST concurrentes mismo slot → uno 201, otro 409.

---

## P1.7 — Seguridad frontend
**IDs matriz:** H-16, H-17, H-18, H-21, H-22, H-24 · **Estado:** [ ] · **Depende de:** P0.2

**Tareas:**
- [ ] **P1.7.01** H-16: mover `moc_active_clone_id` a cookie HttpOnly setada por servidor (route handler `/api/me/active-clone`), o validar contra sesión en el proxy en vez de confiar en la cookie cliente.
- [ ] **P1.7.02** H-17: implementar CSRF double-submit — middleware lee `csrf-token` cookie y requiere header `X-CSRF-Token` matching en POST/PUT/DELETE. Aplicar a todas las routes `/api/*` state-changing.
- [ ] **P1.7.03** H-18: en `widget.js/route.ts`, restringir `sandbox` (quitar `allow-same-origin` si no es estrictamente necesario), validar `event.origin` con allowlist, usar `postMessage` con `targetOrigin` específico.
- [ ] **P1.7.04** H-21: en `MessageBubble.tsx`, reemplazar regex markdown por lib maintained (`marked` + `dompurify` ya está); añadir test que rechace payload XSS conocido (`<img onerror=...>`, `<svg onload=...>`).
- [ ] **P1.7.05** H-22: añadir `src/app/error.tsx`, `src/app/not-found.tsx`, `src/app/global-error.tsx`.
- [ ] **P1.7.06** H-24: en `next.config.ts`, CSP estricta — quitar `unsafe-inline` y `https:` broad; usar nonces por-request para scripts; añadir `frame-ancestors 'self'` y allowlist de dominios embedores del widget.

**Aceptación:**
- Test XSS sanitize rechaza payload.
- CSP report-mode run sin violaciones críticas.
- CSRF POST sin token → 403.

---

## P1.8 — Infraestructura
**IDs matriz:** H-26, H-27, H-28, H-30, H-31, H-32 · **Estado:** [ ] · **Depende de:** —

**Tareas:**
- [ ] **P1.8.01** H-26: fix `.dockerignore:20-26` — cambiar `replica/` por `MyOwnClone/` en todas las exclusiones.
- [ ] **P1.8.02** H-27: `ops/backup_postgres.sh` — quitar `2>/dev/null` del pg_dump; añadir verificación `gunzip -t` del output; añadir restore test semanal (restore a DB temporal, count rows, comparar).
- [ ] **P1.8.03** H-27: activar offsite upload en `backup_dual.sh:32-37` (rclone B2/S3) con credenciales fuera del repo.
- [ ] **P1.8.04** H-28: deploy scripts — usar usuario no-root (`deployer`) con sudo limitado para systemctl; cambiar `accept-new` a `strict` con known-hosts pre-poblados.
- [ ] **P1.8.05** H-30: `.github/workflows/ci.yml:45` — quitar `--exit-zero` del ruff.
- [ ] **P1.8.06** H-31: añadir `.husky/pre-commit` o `core.hooksPath` que ejecute `scripts/pre-commit-hook.sh` + `ruff check` + `pytest -q` en archivos tocados.
- [ ] **P1.8.07** H-32: `tests/test_stripe_webhook.py` — importar el handler real (`src/app/api/stripe/webhook/route.ts`) en vez de la réplica; o al menos assert que la réplica y el handler compartan la misma función fuente.
- [ ] **P1.8.08** MEDIUM adicional: definir `limit_req_zone` en nginx (referenciado en `nginx-myownclone.conf:122,133` pero nunca declarado); activar `REDIS_TLS=true` en `ops/docker-compose.backend.prod.yml:78,119`.

**Aceptación:**
- `ruff check .` rompe CI si hay errores.
- Backup restore test verde.
- `docker build` contexto más pequeño (sin `node_modules`).

---

## P1.9 — Tests de regresión para vulns documentadas
**IDs matriz:** H-29 · **Estado:** [ ] · **Depende de:** P0.4

**Tareas:**
- [ ] **P1.9.01** Test C1 reset-password bypass: tras reset, el login con password viejo falla y con el nuevo funciona. Mockear `accounts` table.
- [ ] **P1.9.02** Test C2 XSS sanitize: payload `<img src=x onerror=alert(1)>` en message → output sin `onerror`.
- [ ] **P1.9.03** Tests H1/H2/H3 cross-tenant IDOR (cubre P0.4 también): prompts, feedback, knowledge sources.

**Aceptación:**
- Tests verde; fallarían si se revierte el fix.

---

## P1.10 — Backend robustez
**IDs matriz:** H-08, H-09, H-10, H-13, H-14, H-15, H-25 · **Estado:** [ ] · **Depende de:** —

**Tareas:**
- [ ] **P1.10.01** H-08: `email_service.py:109-110` — reemplazar `str.format(**kwargs)` por `Template(...).safe_substitute(**kwargs)`.
- [ ] **P1.10.02** H-09: `monitoring.py:88-152` — guard `if platform.system() != "Linux": return {}` en `_check_os`.
- [ ] **P1.10.03** H-10: `auth.py:117-124` — usar `db.session` (Flask-SQLAlchemy) en vez de psycopg2 crudo; o usar pool (`psycopg2.pool.SimpleConnectionPool`).
- [ ] **P1.10.04** H-13: registrar `generate_master_key_command`, `rotate_secrets_key_command`, `refresh_cost_daily_rollup_command`, `ai_backfill_from_env_command` en `app.cli` (en `app_factory.py` o `commands/__init__.py`).
- [ ] **P1.10.05** H-14: `proxy.ts:51` — dev API key solo si `NODE_ENV === "development"` (estricto), no cualquier no-prod.
- [ ] **P1.10.06** H-15: `proxy.ts:393` y `MaintenanceBanner.tsx:18` — fallback backend URL debe ser error explícito si `BACKEND_URL` no set, no `localhost:5001`.
- [ ] **P1.10.07** H-25: `auth.ts:58-63` — mover a Drizzle query builder; eliminar fallback `users` si esa tabla es legacy (confirmar con migraciones).

---

# FASE P2 — MEDIUM (calidad, consistencia, performance)

> ~52 ítems. Listo los bloques; detalle fino se expande al ejecutar cada bloque (siguiendo el mismo formato P<ID>.<NN>).

## P2.1 — Performance / N+1
- [ ] **P2.1.01** `clone.py:251-277` — eager load `CloneModePrompt` (joinedload o selectinload).
- [ ] **P2.1.02** `prompts.py:174-199` — reemplazar N+1 count por `GROUP BY` join.
- [ ] **P2.1.03** `ai_audit.py:57-83` — rollup vía SQL `GROUP BY`, no carga en memoria.
- [ ] **P2.1.04** `model_registry.py:62,88-92` — hacer cache class attribute o singleton.

## P2.2 — CLI / commands
- [ ] **P2.2.01** `backfill_embeddings.py:14-73` — batch commit (cada N=100), pasar `tenant_id` correcto.
- [ ] **P2.2.02** `commands/reindex.py` — revisar stub (8 líneas).

## P2.3 — Monitoring / health
- [ ] **P2.3.01** `monitoring.py:375-378` — reemplazar subprocess curl por `requests` con pool, o `docker` SDK.
- [ ] **P2.3.02** `monitoring.py:310-321` — `_check_ollama` no haga embedding real; solo `/api/tags`.
- [ ] **P2.3.03** `monitoring.py:415-423` — `psutil.cpu_percent(interval=None)` non-blocking.
- [ ] **P2.3.04** `app_factory.py:274-283` — cachear resultado de `/api/tags` Ollama (TTL 10s).

## P2.4 — Consistencia datetime / ID
- [ ] **P2.4.01** Reemplazar todos los `datetime.utcnow()` por `datetime.now(timezone.utc)` y hacer columnas `DateTime(timezone=True)`.
- [ ] **P2.4.02** Unificar generadores de ID en `libs/uuid_utils.uuidv7()` (incluye `base.py:54`, `prompt.py:19,35`).
- [ ] **P2.4.03** `models/knowledge.py`, `conversation.py` — `Text` PK → `String(36)`.

## P2.5 — i18n completo dashboard
- [ ] **P2.5.01** Cerebro, inbox, configuracion, reuniones — extraer strings a `useTranslations`.
- [ ] **P2.5.02** Script CI que valide `useTranslations("X")` vs top-level keys en `en.json`/`es.json`.
- [ ] **P2.5.03** Fechas vía next-intl (`inbox/page.tsx:292,332`), no hardcoded `es-ES`.

## P2.6 — Type safety frontend
- [ ] **P2.6.01** `tsconfig.json:12` — `noImplicitAny: true`.
- [ ] **P2.6.02** Rehabilitar eslint rules gradualmente (`no-explicit-any`, `ban-ts-comment`, `no-html-link-for-pages`).
- [ ] **P2.6.03** Reemplazar `as any` casts en `proxy.ts:27`, `bookings/route.ts:148`, `clone/sources/route.ts:332,335`, admin pages.

## P2.7 — Infra refinement
- [ ] **P2.7.01** `.dockerignore` — excluir también `.next`, logs, `test-results`.
- [ ] **P2.7.02** Deploy scripts — pruning de releases viejos (keep last 5).
- [ ] **P2.7.03** `console/__init__.py:16` — `doc=False` en prod o auth en Swagger UI.
- [ ] **P2.7.04** Dev compose — pinned image tags, API bound a `127.0.0.1`.

## P2.8 — Backend cleanup (MEDIUM varios)
- [ ] **P2.8.01** `model_manager.py:289-318` — remover dead code `_dispatch`/`_dispatch_stream` + 5 `_invoke_*`.
- [ ] **P2.8.02** `retrieval.py:158` — no construir embedding léxico si `has_vector_rows`.
- [ ] **P2.8.03** `email_service.py:11-13` — lazy read de env.
- [ ] **P2.8.04** `stt.py:14` — lazy import `openai`.
- [ ] **P2.8.05** `queue.py:62-69` — `ssl_check_hostname=True` (regenerar cert con hostname correcto).
- [ ] **P2.8.06** `metrics.py:57,65` — sanitizar label `endpoint` (cardinalidad acotada).
- [ ] **P2.8.07** `clone.py:401-461` — `os.makedirs(parent, exist_ok=True)` + validación magic-byte.
- [ ] **P2.8.08** `admin_platform.py:59-62` — try/except en `int(request.args.get("page"))`.
- [ ] **P2.8.09** `providers/local.py:17-19` — no inyectar api_key fake; usar flag explícito.
- [ ] **P2.8.10** `ai_models.py:264-300` — no permitir mutar modelos globales (`tenant_id IS NULL`) desde tenant.
- [ ] **P2.8.11** `myownclone_public.py:404-427` — usar tokenizer real (tiktoken) en vez de `len(split())`.

## P2.9 — Stripe / webhook
- [ ] **P2.9.01** `stripe_webhook.py:34-55` — verificar tenencia del `metadata.tenant_id` (existe el tenant? el checkout fue iniciado por él?).
- [ ] **P2.9.02** `stripe_webhook.py:152-158` — idempotency key en handlers (mensaje_id o event_id).

## P2.10 — Error boundaries y UX
- [ ] **P2.10.01** Reemplazar `confirm()`/`alert()` por modales (inbox, admin).
- [ ] **P2.10.02** Accesibilidad: aria-labels en icon buttons, no color-only state.

---

# FASE P3 — LOW (pulido)

> ~29 ítems. Lista compacta.

- [ ] **P3.01** `retry_client.py:114-115` — añadir jitter al backoff.
- [ ] **P3.02** `retrieval.py:65-70` — stopwords multi-idioma.
- [ ] **P3.03** `token_budget.py:32-35` — heuristic chars_per_token por idioma.
- [ ] **P3.04** `embeddings.py:13` — extraer `_OPENAI_BATCH_SIZE` a constante compartida.
- [ ] **P3.05** `fields/__init__.py` — re-export `ResponseModel` para imports limpios.
- [ ] **P3.06** `seed.py:98` — typo `youownclone` → `myownclone`.
- [ ] **P3.07** `login.py:11-23` — `_AccountProxy.__getattr__` raise AttributeError en typo.
- [ ] **P3.08** `login.py:33-39` — `_is_uuid_like` usar `uuid.UUID(..., version=4)`.
- [ ] **P3.09** `tier_enforcement.py:60` — retornar `current_count` real.
- [ ] **P3.10** `onboarding.py:239` — retornar count de borrados real.
- [ ] **P3.11** `voice.py:142-147` — distinguir 404 de 200 en delete.
- [ ] **P3.12** `jwt_utils.py:14-23` — dev secret compartido entre workers (fichero temporal o env).
- [ ] **P3.13** `crypto.py:113-120` — key-stretching PBKDF2 para `MODEL_SECRETS_KEY` humano.
- [ ] **P3.14** `security_checks.py:54-60` — aplicar carve-out `REDIS_URL` además de `DATABASE_URL`.
- [ ] **P3.15** `error_helpers.py:17-33` — integrar o borrar módulo muerto.
- [ ] **P3.16** `monitoring.py:415-423` — cache 1s de `cpu_percent`.
- [ ] **P3.17** Frontend: todos los icon-only buttons con `aria-label`.
- [ ] **P3.18** Frontend: componentes admin usan `useAdminFetch` uniformemente.
- [ ] **P3.19** `configuracion/page.tsx:5-10` — sanitizar `x-forwarded-host`/`proto`.
- [ ] **P3.20** `Sidebar.tsx:36` — eliminar TODO fake data, conectar `trial_ends_at`.
- [ ] **P3.21** `MaintenanceBanner.tsx` — implementar timer 5min real o renombrar label.
- [ ] **P3.22** Documentación: actualizar `AUDIT_REPORT*.md` con cierre de P0/P1.
- [ ] **P3.23** Documentación: `docs/superpowers/plans/` con planes por bloque ejecutado.
- [ ] **P3.24** `STATE.md` — bump de fecha y estado tras cada fase.
- [ ] **P3.25** `MASTER_LOG.md` — entrada por bloque implementado.
- [ ] **P3.26** Releases pruning policy documentada.
- [ ] **P3.27** `npm audit` + `pip-audit` en CI.
- [ ] **P3.28** Dependabot/Renovate config.
- [ ] **P3.29** Secret scanning (gitleaks/trufflehog) en CI pre-commit.

---

# RESUMEN DE PROGRESO

| Fase | Ítems | Hechos | En progreso | Bloqueados |
|------|-------|--------|-------------|------------|
| P0 | ~21  | 18     | 0           | 3 (voice C-12, rotación VPS, redact .sisyphus) |
| P1 | ~32  | 0      | 0           | 0          |
| P2 | ~52  | 0      | 0           | 0          |
| P3 | ~29  | 0      | 0           | 0          |
| **Total** | **~134** | **18** | **0** | **3** |

> **P0 IMPLEMENTADO (rama `fix/p0-backend-crashes-and-idor`, 6 commits, sin push):**
> - P0.3 Backend crashes ✅ (`ca3a43c`) — C-05, C-06, C-07, C-08, C-09, C-14 + redact bonus
> - P0.6 Health tests ✅ (`0efa39c`) — C-21×2 + info-leak
> - P0.5 SSRF + metrics ✅ (`683e79d`) — C-10, C-13
> - P0.4 Sources + Prompts IDOR ✅ (`32b5964` + `acec67d`) — H-03, H-04 (+ residual verifier)
> - P0.1 Auth lockdown ✅ (`ca18c59`) — C-01, C-02, H-01
>
> **Suite:** 381 passed, 14 failed (todos pre-existentes), **0 regresiones**.
> **Verifier independiente:** APPROVE WITH NOTES → residual cerrado.
> **Evidencia:** `.omo/evidence/p0-auditoria-2026-07-13.md`
> **Pendiente humano:** (1) revisión + decisión push/deploy; (2) voice C-12 (cambio contrato o nuevo modelo); (3) rotación física VPS (runbook en evidencia); (4) redact `.sisyphus/evidence` (requiere aprobar excepción AGENTS.md).
>
> Actualizar esta tabla al cierre de cada bloque. Mantener `STATE.md` sincronizado.

---

# PRÓXIMO PASO RECOMENDADO

1. Humano revisa `PLAN_MAESTRO_AUDITORIA_2026-07-13.md` y este archivo.
2. Humano habilita L2 **solo para P0.1** (rotación de secretos) — el bloque de mayor riesgo y menor dependencia.
3. Ejecutor crea worktree, implementa P0.1.01–P0.1.06, corre `pytest`, dispatch verifier sub-agent, registra evidencia en `.omo/evidence/task-P0.1-secret-rotation.md`.
4. Humano revisa PR, hace deploy en ventana de mantenimiento, verifica smoke.
5. Repetir por bloque.

**Sin aprobación L2 explícita por bloque, no se implementa nada.** Esto respeta `AGENTS.md` y la decisión de cuarentena documental del 2026-07-07.

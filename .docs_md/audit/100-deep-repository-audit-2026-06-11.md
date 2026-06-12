# Auditoria profunda del repositorio - 2026-06-11

## Veredicto directo

No, el repositorio no esta al 100%. Tiene una base visual y tecnica importante, pero **no es un producto util end-to-end todavia**. El problema no es un detalle de CSS: hay flujos que parecen completos en la UI pero se cortan entre Next, el proxy, Flask, DB o servicios externos.

Estado global estimado:

| Area | Estado | Lectura |
|---|---|---|
| Landing | Amarillo | Visualmente avanzada, pero pricing debe compartir contrato con billing. |
| Dashboard | Amarillo/Rojo | UI amplia, pero varios widgets no tienen datos reales. |
| Backend Flask | Amarillo/Rojo | Controladores existen, pero hay stubs y endpoints incompletos. |
| RAG/conocimiento | Rojo | No hay ingestion real conectada desde la UI. |
| Billing/Stripe | Rojo | Checkout tiene errores de contrato y rutas antiguas. |
| Admin | Rojo/Amarillo | Hay pantallas que llaman rutas no mapeadas. |
| Tests | Rojo | Typecheck pasa, Vitest falla, pytest raiz no cubre `api/tests`. |
| Produccion | Rojo | Contratos/env/migraciones no estan cerrados. |

## Pruebas ejecutadas

| Comando | Resultado | Implicacion |
|---|---:|---|
| `npm run typecheck` | OK | El frontend compila TypeScript. |
| `npm test` | FAIL | Hay regresiones actuales en `ChatPanel` y `facturacion`. |
| `pytest -q` | OK | Solo ejecuta `tests/`, no todo backend. |
| `pytest api\tests -q` | OK parcial | 14 passed, 12 skipped. Cobertura backend incompleta. |

## P0 - Bloqueadores reales

### P0-01 - El conocimiento no llega al RAG

La UI de biblioteca escribe fuentes en una API local de Next:

- `MyOwnClone/src/app/(dashboard)/biblioteca/page.tsx:53`
- `MyOwnClone/src/app/(dashboard)/biblioteca/nuevo/page.tsx:83`
- `MyOwnClone/src/app/api/clone/sources/route.ts:125`
- `MyOwnClone/src/app/api/clone/sources/route.ts:129`

Pero el backend RAG no lee esas fuentes directamente. El retrieval intenta resolver datasets:

- `api/core/myownclone/silos.py:48`
- `api/core/retrieval.py:64`

y los modelos que usa son stubs:

- `api/models/dataset.py:1`
- `api/models/dataset.py:4`
- `api/models/dataset.py:11`

Resultado: el usuario puede subir contenido y verlo como `ready`, pero eso no garantiza que el clon lo use.

Desarrollo requerido:

1. Definir tablas reales de dataset/segments o usar `sources/chunks`.
2. Crear endpoint backend de ingestion.
3. Cambiar `sources` a estado `processing`.
4. Generar chunks + embeddings.
5. Hacer retrieval por silo real.
6. Test E2E: subir fuente -> preguntar -> respuesta usa esa fuente.

### P0-02 - Billing/Stripe no puede considerarse funcional

Evidencias:

- `api/controllers/console/myownclone/stripe_ctrl.py:29` usa `success_url="/dashboard/resumen"`.
- `api/controllers/console/myownclone/stripe_ctrl.py:30` usa `cancel_url="/dashboard/facturacion"`.
- Las rutas reales del dashboard son `/resumen` y `/facturacion`.
- `api/controllers/console/myownclone/stripe_ctrl.py:72` obtiene `account, tenant_id = current_account_with_tenant()`.
- `api/controllers/console/myownclone/stripe_ctrl.py:96` usa `customer_email=account.email`, pero en auth por proxy `account` puede ser un string/proxy, no un objeto SQLAlchemy con `.email`.

Desarrollo requerido:

1. Normalizar `current_account_with_tenant()` para devolver estructura con `id/email/role/tenant_id`.
2. Cambiar rutas success/cancel a `/resumen` y `/facturacion`.
3. Usar planes reales de backend para checkout.
4. Si hay fallback pricing, no permitir checkout activo.
5. Test: click Upgrade -> crea session -> redirect correcto.

### P0-03 - Contratos DB divergentes

Tenants:

- Drizzle: `MyOwnClone/src/lib/db/schema/tenants.ts:16` define planes `basic/pro/scale/enterprise/trial`.
- SQLAlchemy: `api/models/account.py:67` usa default `"basico"`/`"básico"` segun modelo/migracion.
- Drizzle: `tenant_status` usa valores de trial/active/suspended/cancelled.
- SQLAlchemy: `api/models/account.py:70` usa default `"normal"`.

Clone modes:

- Drizzle: `MyOwnClone/src/lib/db/schema/clones.ts:13` usa `pedagogy`.
- Backend: `api/models/clone.py:16` usa `teach`.

Products:

- Drizzle: `MyOwnClone/src/lib/db/schema/analytics.ts:80` guarda status enum en columna `status`.
- SQLAlchemy: `api/models/meeting.py:70` guarda boolean `active`.

Impersonation:

- SQLAlchemy: `api/models/analytics.py:114` tabla `impersonation_log`.
- Drizzle: `MyOwnClone/src/lib/db/schema/analytics.ts:90` tabla `impersonation_logs`.

Desarrollo requerido:

1. Elegir fuente de verdad: recomendacion, Drizzle schema + SQLAlchemy alineado.
2. Normalizar nombres internos: `basic`, `pro`, `scale`, `enterprise`; `teach`, `support`, `sales`.
3. Migracion de reconciliacion.
4. Tests de lectura/escritura cruzada.

### P0-04 - Admin tiene rutas visuales no conectadas

Frontend llama:

- `MyOwnClone/src/app/admin/audit/page.tsx:93` -> `/api/admin/audit-log`
- `MyOwnClone/src/app/admin/feedback/page.tsx:62` -> `/api/admin/feedback`
- `MyOwnClone/src/app/admin/courtesy/page.tsx:65` -> `/api/admin/courtesy`
- `MyOwnClone/src/components/admin/CourtesyButton.tsx:54` -> `/api/admin/courtesy`

Proxy solo mapea:

- `MyOwnClone/src/proxy.ts:60` -> `/api/admin/courtesy-account`

Backend tiene:

- `api/controllers/console/myownclone/admin_platform.py:273` -> `/myownclone/admin/courtesy-account`
- `api/controllers/console/myownclone/feedback.py:29` -> `/myownclone/feedback`
- `api/controllers/console/myownclone/feedback.py:58` -> `/myownclone/feedback/stats`

No aparece contrato backend/proxy para `/api/admin/audit-log`, `/api/admin/feedback`, `/api/admin/courtesy`.

Desarrollo requerido:

1. Crear rutas proxy correctas o cambiar frontend a las rutas existentes.
2. Implementar audit-log admin si no existe.
3. Separar feedback de clon (`/api/clone/feedback`) y feedback admin (`/api/admin/feedback`).
4. Test admin pages: audit, feedback, courtesy.

## P1 - Flujos importantes incompletos

### P1-01 - Productos/Sales mode no esta cerrado

Frontend:

- `MyOwnClone/src/app/(dashboard)/productos/page.tsx:54` GET `/api/clone/clones/${cid}/products`.
- `MyOwnClone/src/app/(dashboard)/productos/page.tsx:75` POST products.

Backend:

- `api/controllers/console/myownclone/booking.py:127` ruta products.
- `api/controllers/console/myownclone/booking.py:132` solo `post`.

No hay GET/PUT/DELETE auditado para productos. El dashboard no puede listar de forma fiable.

### P1-02 - Analytics no refleja actividad real

Backend:

- `api/controllers/console/myownclone/analytics.py:89` TODO.
- `api/controllers/console/myownclone/analytics.py:93` `total_conversations = 0`.
- `api/controllers/console/myownclone/analytics.py:94` `total_messages = 0`.

El dashboard puede mostrar metricas bonitas pero no reales.

### P1-03 - SearchCommandBar depende de endpoints fragiles

Evidencias:

- `MyOwnClone/src/components/ui/SearchCommandBar.tsx:224` clones.
- `MyOwnClone/src/components/ui/SearchCommandBar.tsx:225` memories.
- `MyOwnClone/src/components/ui/SearchCommandBar.tsx:230` products.
- `MyOwnClone/src/components/ui/SearchCommandBar.tsx:238` meeting-types.

Si products no tiene GET, el buscador global da resultados incompletos.

### P1-04 - Proxy hardcodea backend local

- `MyOwnClone/src/proxy.ts:5` define `BACKEND_URL = "http://127.0.0.1:5001"`.
- `.env.example` si define `MYOWNCLONE_API_URL`.
- `MyOwnClone/src/app/(public)/[slug]/page.tsx:54` si usa `MYOWNCLONE_API_URL`.

Hay dos estrategias distintas de conexion al backend. En deploy puede romperse.

### P1-05 - Variables DB inconsistentes

Backend app factory:

- `api/app_factory.py:182` usa `DB_USER`.
- `api/app_factory.py:185` usa `DB_NAME`.

Auth raw psycopg:

- `api/controllers/console/auth.py:121` usa `DB_USERNAME`.
- `api/controllers/console/auth.py:123` usa `DB_DATABASE`.

`.env.example` usa `DB_USER` y `DB_NAME`:

- `api/.env.example:22`
- `api/.env.example:26`

Riesgo: login puede usar otra DB/config que la app.

### P1-06 - Tests frontend estan rojos

Fallos ya observados:

- `MyOwnClone/src/components/chat/ChatPanel.tsx:70` asume `scrollTo`.
- `MyOwnClone/src/__tests__/app/facturacion.test.tsx:123` espera mensaje anterior.
- `MyOwnClone/src/__tests__/app/facturacion.test.tsx:188` espera badge anterior.

Desarrollo requerido:

1. Guard para `scrollTo`.
2. Actualizar tests de billing al contrato definitivo.
3. Ejecutar Vitest antes de mas cambios visuales.

### P1-07 - Pytest raiz no ejecuta backend completo

- `pytest.ini:2` define `testpaths = tests`.
- `api/tests` queda fuera del comando normal.
- `api/tests/test_tenant_scoping.py:94`, `test_plan_pricing.py:65`, `test_admin_smoke.py:34`, `test_admin_smoke.py:46` tienen skips.

La suite da una falsa sensacion de seguridad.

## P2 - Riesgos de producto y mantenimiento

### P2-01 - Stubs estructurales en backend

Evidencias:

- `api/base.py:3`
- `api/configs/__init__.py:1`
- `api/core/rag/datasource/retrieval_service.py:1`
- `api/core/rag/retrieval/retrieval_methods.py:1`
- `api/models/model.py:4`
- `api/models/types.py:1`
- `api/fields/base.py:1`

No todos son malos, pero deben estar catalogados como compatibilidad temporal, no como core terminado.

### P2-02 - API local sources no valida ownership fuerte

- `MyOwnClone/src/app/api/clone/sources/route.ts:10` lee `moc_active_clone_id`.
- `MyOwnClone/src/app/api/clone/sources/route.ts:12` cae a `DEFAULT_CLONE_ID`.
- `MyOwnClone/src/app/api/clone/sources/route.ts:32` consulta por `cloneId`.

Falta validar que el clone pertenece al tenant/user de la sesion.

### P2-03 - Estado de fuentes falsea progreso

- `MyOwnClone/src/app/api/clone/sources/route.ts:42` `wordCount: 150` stub.
- `MyOwnClone/src/app/api/clone/sources/route.ts:125` `status: "ready"`.

Debe calcularse desde ingestion real.

### P2-04 - E2E superficial

E2E actual:

- `MyOwnClone/e2e/navigation.spec.ts` solo valida carga basica.
- `MyOwnClone/e2e/auth.spec.ts` valida formulario visible.

No hay E2E de:

- crear clone,
- subir fuente,
- chat con contexto,
- billing checkout,
- admin audit,
- products CRUD.

### P2-05 - `api/.venv` esta dentro del repo de trabajo

Aunque no parece trackeado, el inventario de archivos lo incluye y mete ruido enorme. Debe estar ignorado y fuera de auditorias.

- `rg --files` no lo lista, pero `Get-ChildItem api` si muestra `.venv`.

### P2-06 - `api/.flaskenv` esta trackeado

- `git ls-files api/.flaskenv` devuelve `api/.flaskenv`.
- Contiene `FLASK_ENV=development`.

No es secreto, pero produccion no debe depender de un archivo dev trackeado.

## Matriz de utilidad por flujo

| Flujo | UI | API Next/proxy | Backend | DB | Tests | Estado |
|---|---|---|---|---|---|---|
| Landing pricing | Si | N/A | Parcial via billing plans | Planes divergentes | No E2E | Amarillo |
| Login credenciales | Si | NextAuth | Auth Flask/raw DB tambien existe | Users/accounts divergentes | Parcial | Amarillo |
| Crear clone | Si | Proxy `/api/clone/clones` | Si | clone_configs | Parcial | Amarillo |
| Chat clone | Si | Proxy `/api/clone/{slug}/chat` | Si | RAG roto/stub | Unit rojo | Rojo |
| Subir conocimiento | Si | Next local `sources` | No ingestion | sources/chunks no conectados | Parcial | Rojo |
| Memories/cerebro | Si | Proxy memories | Si | creator_memory/memories divergente | No E2E | Amarillo |
| Inbox/email | Si | Proxy inbox | Si | email_inbound/emails divergente | No E2E | Amarillo |
| Products | Si | Proxy products | POST solo | products divergente | No E2E | Rojo |
| Meetings | Si | Proxy meeting-types/availability | GET/POST | booking tables divergentes | No E2E | Amarillo |
| Billing | Si | Proxy stripe | Roto | tenant plan divergente | Unit rojo | Rojo |
| Admin tenants | Si | Proxy tenants | Si | tenants/accounts | Smoke parcial | Amarillo |
| Admin audit | Si | Ruta no mapeada | No claro | impersonation_log/logs divergente | Skipped | Rojo |
| Admin feedback | Si | Ruta no mapeada | Feedback clon, no admin | clone_feedback | No E2E | Rojo |
| Courtesy | Si | Ruta frontend incorrecta | courtesy-account | accounts/tenants | Skipped | Rojo |

## Plan de desarrollo obligatorio

### Fase A - Parar la hemorragia de contratos

1. Cambiar `proxy.ts` a `MYOWNCLONE_API_URL`.
2. Unificar rutas admin:
   - `/api/admin/courtesy` -> `/console/api/myownclone/admin/courtesy-account`, o renombrar frontend.
   - crear/mapping `/api/admin/feedback`.
   - crear/mapping `/api/admin/audit-log`.
3. Normalizar env DB: usar solo `DB_USER`/`DB_NAME` o solo `DB_USERNAME`/`DB_DATABASE`.
4. Arreglar Vitest.

### Fase B - Hacer util el producto principal

1. Redisenar ingestion.
2. Crear modelos/tables reales de RAG.
3. Conectar `sources` con embeddings.
4. Persistir conversaciones y mensajes.
5. Analytics lee conversaciones reales.

### Fase C - Monetizacion

1. Arreglar Stripe checkout.
2. Unificar pricing landing/billing.
3. Definir plan keys internas.
4. Test checkout en modo test.

### Fase D - Gestion completa

1. Products CRUD completo.
2. Meeting CRUD completo.
3. Admin audit/feedback/courtesy funcionales.
4. Settings/API Keys separadas y probadas.

### Fase E - QA real

1. `pytest.ini` incluye `tests` y `api/tests`.
2. Quitar skips o justificar cada skip.
3. Playwright E2E de flujos reales.
4. CI bloquea merge si falla typecheck, vitest, pytest y E2E smoke.

## Criterio de "100% util"

Una pantalla solo puede marcarse terminada si:

1. El boton llama una ruta real.
2. La ruta esta en proxy o API Next documentada.
3. El backend existe y valida tenant/usuario.
4. La DB tiene tabla/migracion real.
5. Hay estado loading/error/empty.
6. Hay test unitario o integracion.
7. Hay al menos un E2E para el flujo principal.

Con ese criterio, hoy el repositorio no esta terminado. La prioridad es desarrollo de interconexion, no mas retoque visual.

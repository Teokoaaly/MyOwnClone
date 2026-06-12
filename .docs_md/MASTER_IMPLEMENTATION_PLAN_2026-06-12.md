# Plan maestro de implementacion - MyOwnClone

Fecha: 2026-06-12  
Fuente base: `.docs_md/audit/100-deep-repository-audit-2026-06-11.md`  
Objetivo: convertir el repositorio en un producto SaaS funcional end-to-end, no solo una UI que compila.

## Regla de oro

Una tarea solo se marca como completada si cumple:

1. UI o flujo visible conectado a una ruta real.
2. Ruta Next/API/proxy correctamente mapeada.
3. Backend Flask real, sin stub/falso exito.
4. Validacion de usuario, tenant, permisos y ownership.
5. Modelo DB y migracion coherentes.
6. Estados loading/empty/error.
7. Tests unitarios o integracion.
8. Al menos un E2E para flujos criticos.
9. Documentacion actualizada si cambia contrato.

## Estado inicial obligatorio

Antes de tocar codigo, ejecutar:

```powershell
git status --short
cd MyOwnClone
npm run typecheck
npm test
cd ..
pytest -q
pytest api\tests -q
```

Registrar resultados en `.docs_md/audit/IMPLEMENTATION_PROGRESS_2026-06-12.md`.

## Orden de ejecucion

No saltar fases salvo que una tarea indique que puede hacerse en paralelo.

| Fase | Objetivo | Severidad | Salida esperada |
|---|---|---|---|
| A | Contratos, rutas, env y tests rojos | P0 | Base estable y rutas reales |
| B | DB y modelos fuente de verdad | P0 | Drizzle/SQLAlchemy alineados |
| C | RAG, conocimiento y chat util | P0 | Fuente subida usada por chat |
| D | Billing/Stripe | P0 | Upgrade funcional en modo test |
| E | Admin, products, meetings, analytics | P1 | Gestion completa sin pantallas rotas |
| F | QA, E2E, CI y produccion | P1/P2 | Suite confiable y deploy-ready |

---

# Fase A - Contratos, rutas, env y tests rojos

## TASK-A01 - Crear registro de progreso

Prioridad: P0  
Owner: Coordinador/agente implementador  
Archivos:

- `.docs_md/audit/IMPLEMENTATION_PROGRESS_2026-06-12.md`

Acciones:

1. Crear documento de progreso.
2. Registrar commit/branch si aplica.
3. Registrar resultados iniciales de typecheck, Vitest, pytest raiz y pytest backend.
4. Mantener tabla de estado por task.

Criterio de cierre:

- Documento creado.
- Cada task posterior puede actualizar estado `pending / in_progress / blocked / ***REMOVED***`.

Tests:

- No aplica.

## TASK-A02 - Arreglar Vitest roto en ChatPanel

Prioridad: P0  
Archivos:

- `MyOwnClone/src/components/chat/ChatPanel.tsx`
- `MyOwnClone/src/__tests__/components/ChatPanel.test.tsx`
- `MyOwnClone/src/test-setup.ts` si hace falta.

Problema:

- `ChatPanel` llama `container.scrollTo`, que no existe en jsdom.

Acciones:

1. Proteger `scrollTo` con guard.
2. No eliminar auto-scroll en navegador real.
3. Mantener tests existentes.

Criterio de cierre:

- `npm test -- ChatPanel` pasa.
- No hay error `scrollTo is not a function`.

Tests:

```powershell
cd MyOwnClone
npm test -- ChatPanel
```

## TASK-A03 - Alinear tests de facturacion con contrato final

Prioridad: P0  
Archivos:

- `MyOwnClone/src/app/(dashboard)/facturacion/page.tsx`
- `MyOwnClone/src/__tests__/app/facturacion.test.tsx`

Problema:

- Tests esperan copy/comportamiento anterior.
- UI tiene fallback pricing que puede parecer accionable.

Acciones:

1. Decidir contrato final:
   - Si planes backend fallan, mostrar pricing informativo.
   - No permitir checkout con planes fallback.
2. Actualizar tests a ese contrato.
3. Asegurar `Popular`/`Recommended` segun copy final elegido.

Criterio de cierre:

- Tests de facturacion pasan.
- Fallback no inicia checkout.

Tests:

```powershell
cd MyOwnClone
npm test -- facturacion
```

## TASK-A04 - Usar `MYOWNCLONE_API_URL` en proxy

Prioridad: P0  
Archivos:

- `MyOwnClone/src/proxy.ts`
- `MyOwnClone/.env.example`
- `ops/frontend.env.production.example`

Problema:

- `proxy.ts` hardcodea `http://127.0.0.1:5001`.

Acciones:

1. Cambiar `BACKEND_URL` para leer `process.env.MYOWNCLONE_API_URL`.
2. Permitir fallback local solo en development/test.
3. Si falta en production, devolver error claro.
4. Documentar variable.

Criterio de cierre:

- No queda backend local hardcodeado en proxy.
- Tests existentes no rompen.

Tests:

```powershell
cd MyOwnClone
npm run typecheck
```

## TASK-A05 - Normalizar variables DB backend

Prioridad: P0  
Archivos:

- `api/app_factory.py`
- `api/controllers/console/auth.py`
- `api/.env.example`
- `ops/backend.env.production.example`

Problema:

- `app_factory.py` usa `DB_USER/DB_NAME`.
- `auth.py` usa `DB_USERNAME/DB_DATABASE`.

Acciones:

1. Elegir canon: `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `DB_NAME`.
2. Actualizar `auth.py`.
3. Mantener compat temporal leyendo alias antiguos con warning, si hay riesgo de entorno existente.
4. Actualizar ejemplos env.

Criterio de cierre:

- App y login usan mismas variables.
- Documentacion env coherente.

Tests:

```powershell
pytest -q
pytest api\tests -q
```

## TASK-A06 - Reparar rutas admin proxy/frontend

Prioridad: P0  
Archivos:

- `MyOwnClone/src/proxy.ts`
- `MyOwnClone/src/app/admin/audit/page.tsx`
- `MyOwnClone/src/app/admin/feedback/page.tsx`
- `MyOwnClone/src/app/admin/courtesy/page.tsx`
- `MyOwnClone/src/components/admin/CourtesyButton.tsx`
- `api/controllers/console/myownclone/admin_platform.py`
- `api/controllers/console/myownclone/feedback.py`

Problema:

- Frontend llama `/api/admin/audit-log`, `/api/admin/feedback`, `/api/admin/courtesy`.
- Proxy/backend no exponen esas rutas exactas.

Acciones:

1. Crear mapping `/api/admin/courtesy` -> `/console/api/myownclone/admin/courtesy-account`.
2. Crear endpoint/mapping `/api/admin/feedback` para listado admin.
3. Crear endpoint/mapping `/api/admin/audit-log` o cambiar UI a ruta existente.
4. Asegurar role `platform_admin`.
5. Crear tests de rutas admin.

Criterio de cierre:

- Ninguna pagina admin llama endpoint inexistente.
- Admin audit, feedback y courtesy cargan datos o empty state real.

Tests:

```powershell
cd MyOwnClone
npm test -- admin
cd ..
pytest api\tests -q
```

---

# Fase B - DB y modelos fuente de verdad

## TASK-B01 - Decidir y documentar fuente de verdad DB

Prioridad: P0  
Archivos:

- `.docs_md/DB_SOURCE_OF_TRUTH_2026-06-12.md`
- `MyOwnClone/src/lib/db/schema/*`
- `api/models/*`
- `api/migrations/versions/*`

Decision recomendada:

- Drizzle como fuente de verdad declarativa.
- SQLAlchemy alineado para backend Flask.
- Alembic mantiene migraciones backend solo si refleja el mismo contrato.

Criterio de cierre:

- Documento con decision.
- Tabla de correspondencia Drizzle vs SQLAlchemy.

## TASK-B02 - Normalizar enums internos

Prioridad: P0  
Archivos:

- `MyOwnClone/src/lib/db/schema/tenants.ts`
- `MyOwnClone/src/lib/db/schema/clones.ts`
- `api/models/account.py`
- `api/models/clone.py`
- migracion nueva.

Valores canon:

- Plan: `trial`, `basic`, `pro`, `scale`, `enterprise`.
- Tenant status: `trial`, `active`, `suspended`, `cancelled`.
- Subscription status: `inactive`, `trialing`, `active`, `past_due`, `cancelled`.
- Clone modes: `teach`, `support`, `sales`.

Acciones:

1. Migrar `basico/básico` a `basic`.
2. Migrar `normal` a `active`.
3. Migrar `pedagogy` a `teach`.
4. Actualizar seeds, UI y tests.

Criterio de cierre:

- No quedan valores divergentes salvo mapeos de compat documentados.

Tests:

```powershell
pytest api\tests -q
cd MyOwnClone
npm run typecheck
```

## TASK-B03 - Alinear products e impersonation

Prioridad: P0  
Archivos:

- `MyOwnClone/src/lib/db/schema/analytics.ts`
- `api/models/meeting.py`
- `api/models/analytics.py`
- migracion nueva.

Problemas:

- Products: Drizzle usa `status`, SQLAlchemy usa `active`.
- Impersonation: `impersonation_logs` vs `impersonation_log`.

Acciones:

1. Elegir contrato final de products.
2. Elegir nombre final de impersonation log.
3. Migrar tablas/columnas sin perder datos.
4. Actualizar queries.

Criterio de cierre:

- Frontend/backend usan mismos campos.
- Tests products/admin pasan.

## TASK-B04 - Validar ownership en APIs locales Next

Prioridad: P0  
Archivos:

- `MyOwnClone/src/app/api/clone/sources/route.ts`
- `MyOwnClone/src/lib/auth.ts`
- helper nuevo opcional `MyOwnClone/src/lib/clone-ownership.ts`

Problema:

- `sources` confia en cookie `moc_active_clone_id` o `DEFAULT_CLONE_ID`.

Acciones:

1. Resolver tenant/user desde sesion.
2. Verificar clone pertenece al tenant/user.
3. Rechazar cloneId no autorizado.
4. Eliminar fallback inseguro si no hay clone activo.

Criterio de cierre:

- Usuario no puede leer/escribir sources de otro tenant.

Tests:

- Crear test unitario/integracion de tenant A/B.

---

# Fase C - RAG, conocimiento y chat util

## TASK-C01 - Disenar contrato de ingestion

Prioridad: P0  
Archivos:

- `.docs_md/RAG_INGESTION_CONTRACT_2026-06-12.md`
- `api/core/ingestion.py`
- `api/core/retrieval.py`
- `api/core/myownclone/silos.py`

Contrato minimo:

```text
source: queued/processing/ready/error
source -> chunks
chunk -> embedding vector
chunk metadata -> silo, clone_id, tenant_id, source_id
chat -> retrieve chunks by tenant+clone+silo
```

Criterio de cierre:

- Documento con payloads, estados y errores.

## TASK-C02 - Sustituir Dataset/DocumentSegment stubs

Prioridad: P0  
Archivos:

- `api/models/dataset.py`
- `api/core/myownclone/silos.py`
- `api/core/retrieval.py`
- migracion nueva o adaptacion a `sources/chunks`.

Acciones:

Opcion preferida:

1. Usar `sources` y `chunks` existentes.
2. No crear `Dataset` si no aporta valor.
3. Actualizar retrieval para buscar chunks por source/clone/silo.

Criterio de cierre:

- Retrieval no importa modelos stub.
- Test de retrieval con chunk fixture pasa.

## TASK-C03 - Implementar ingestion real de sources

Prioridad: P0  
Archivos:

- `MyOwnClone/src/app/api/clone/sources/route.ts`
- `api/controllers/console/myownclone/*` nuevo o existente.
- `api/core/ingestion.py`
- `MyOwnClone/src/lib/db/schema/sources.ts`
- `MyOwnClone/src/lib/db/schema/chunks.ts`

Acciones:

1. POST source crea source `processing`.
2. Extrae texto por tipo: text/web/pdf/youtube segun alcance.
3. Chunking.
4. Embeddings.
5. Guarda chunks.
6. Marca `ready` o `error`.
7. Calcula wordCount real.

Criterio de cierre:

- No hay `wordCount: 150`.
- No hay `ready` falso.

Tests:

- Test backend ingestion text.
- Test Next/API source.

## TASK-C04 - Chat usa conocimiento real y persiste conversacion

Prioridad: P0  
Archivos:

- `MyOwnClone/src/components/chat/ChatPanel.tsx`
- `api/controllers/myownclone_public.py`
- `api/core/retrieval.py`
- `api/core/model_manager.py`
- modelos/migraciones conversations/messages.

Acciones:

1. Unificar ruta publica y dashboard si es posible.
2. Retrieval por tenant+clone+silo.
3. System prompt del clone.
4. Persistir conversation/message.
5. Guardar confidence/sources.
6. Error claro si no hay LLM key.

Criterio de cierre:

- Pregunta sobre fuente subida responde con esa fuente.
- Conversation y messages quedan persistidos.

Tests:

- Integracion chat con source fixture.
- Vitest ChatPanel.

## TASK-C05 - E2E RAG minimo

Prioridad: P0  
Archivos:

- `MyOwnClone/e2e/rag.spec.ts`

Flujo:

1. Login.
2. Crear/seleccionar clone.
3. Subir texto con dato unico.
4. Esperar ready.
5. Preguntar por dato unico.
6. Ver respuesta que contiene dato.

Criterio de cierre:

- E2E pasa en local con modo test.

---

# Fase D - Billing/Stripe

## TASK-D01 - Arreglar Stripe checkout backend

Prioridad: P0  
Archivos:

- `api/controllers/console/myownclone/stripe_ctrl.py`
- `api/libs/login.py`
- `api/models/account.py`

Acciones:

1. `current_account_with_tenant()` debe exponer email/id/role/tenant.
2. Success/cancel URL reales: `/resumen`, `/facturacion`.
3. Validar plan_id existe.
4. Manejar Stripe no configurado sin 500 opaco.

Criterio de cierre:

- Checkout session se crea en modo test.
- Error controlado si Stripe no esta configurado.

## TASK-D02 - Unificar pricing landing/billing

Prioridad: P1  
Archivos:

- `MyOwnClone/src/app/page.tsx`
- `MyOwnClone/src/app/(dashboard)/facturacion/page.tsx`
- componente nuevo opcional `PricingCards.tsx`

Acciones:

1. Crear componente compartido.
2. Modo `marketing`: CTA registro/contacto.
3. Modo `billing`: current plan + upgrade.
4. Sin borde interior no deseado en landing pricing.

Criterio de cierre:

- Landing y billing muestran mismos planes base.
- Billing usa acciones reales.

## TASK-D03 - Stripe webhook actualiza tenant

Prioridad: P0  
Archivos:

- `MyOwnClone/src/app/api/stripe/webhook/route.ts`
- `api/controllers/console/myownclone/stripe_ctrl.py`
- schema tenants.

Acciones:

1. Confirmar webhook source of truth.
2. Actualizar `stripe_customer_id`, `stripe_subscription_id`, `plan`, `subscription_status`.
3. Test con evento fixture.

Criterio de cierre:

- Tenant cambia de plan tras evento test.

---

# Fase E - Admin, products, meetings, analytics

## TASK-E01 - Products CRUD completo

Prioridad: P1  
Archivos:

- `api/controllers/console/myownclone/booking.py`
- `api/models/meeting.py`
- `MyOwnClone/src/app/(dashboard)/productos/page.tsx`
- `MyOwnClone/src/components/ui/SearchCommandBar.tsx`

Acciones:

1. Implementar GET products.
2. Implementar POST.
3. Implementar PUT/PATCH.
4. Implementar DELETE o deactivate.
5. Tenant ownership.
6. Actualizar UI si falta editar/eliminar.

Criterio de cierre:

- Products page lista, crea, edita y elimina/desactiva.
- SearchCommandBar no falla.

## TASK-E02 - Meetings CRUD completo

Prioridad: P1  
Archivos:

- `api/controllers/console/myownclone/booking.py`
- `api/models/meeting.py`
- `MyOwnClone/src/app/(dashboard)/reuniones/page.tsx`

Acciones:

1. Validar GET/POST existentes.
2. Implementar update/delete si UI lo requiere.
3. Validar timezone y formato hora.
4. Ownership tenant/clone.

Criterio de cierre:

- Reuniones permite gestionar tipos y disponibilidad.

## TASK-E03 - Analytics reales

Prioridad: P1  
Archivos:

- `api/controllers/console/myownclone/analytics.py`
- conversations/messages schema/model.
- `MyOwnClone/src/app/(dashboard)/analiticas/page.tsx`
- `MyOwnClone/src/app/(dashboard)/resumen/page.tsx`

Acciones:

1. Sustituir `total_conversations = 0`.
2. Leer conversations/messages reales.
3. Feedback real.
4. Costs reales si existen.
5. No mostrar metricas falsas si no hay datos.

Criterio de cierre:

- Analytics cambia tras enviar mensaje al chat.

## TASK-E04 - Admin audit, feedback y courtesy funcionales

Prioridad: P1  
Archivos:

- `api/controllers/console/myownclone/admin_platform.py`
- `api/controllers/console/myownclone/feedback.py`
- `MyOwnClone/src/app/admin/audit/page.tsx`
- `MyOwnClone/src/app/admin/feedback/page.tsx`
- `MyOwnClone/src/app/admin/courtesy/page.tsx`

Acciones:

1. Audit log endpoint paginado.
2. Feedback admin endpoint paginado.
3. Courtesy list/create endpoint o ajustar UI a create-only.
4. Role check platform_admin.

Criterio de cierre:

- Las 3 pantallas admin no devuelven 404/500 por rutas inexistentes.

## TASK-E05 - Memories afectan respuestas o se documentan como perfil

Prioridad: P1  
Archivos:

- `api/controllers/console/myownclone/creator_memory.py`
- `api/core/retrieval.py`
- `api/controllers/myownclone_public.py`
- `MyOwnClone/src/app/(dashboard)/cerebro/page.tsx`

Acciones:

1. Definir si memories son retrieval, prompt context o solo notas.
2. Incluirlas en chat si producto lo promete.
3. Test de memory -> respuesta.

Criterio de cierre:

- Comportamiento documentado y testeado.

## TASK-E06 - Inbox/email E2E tecnico

Prioridad: P1  
Archivos:

- `api/controllers/myownclone_public.py`
- `api/controllers/console/myownclone/inbox.py`
- `api/core/myownclone/email_processor.py`
- `MyOwnClone/src/app/(dashboard)/inbox/page.tsx`

Acciones:

1. Validar inbound signature.
2. Crear email inbound fixture.
3. Listar inbox.
4. Generar draft.
5. Cambiar status/delete.

Criterio de cierre:

- Flujo inbox funciona sin datos fake.

---

# Fase F - QA, E2E, CI y produccion

## TASK-F01 - Pytest completo por defecto

Prioridad: P1  
Archivos:

- `pytest.ini`
- `api/tests/*`

Acciones:

1. Incluir `tests` y `api/tests` en `testpaths`, o documentar dos comandos en CI.
2. Revisar skips.
3. Convertir skips criticos a tests reales.

Criterio de cierre:

- `pytest -q` cubre backend relevante o CI ejecuta ambos grupos.

## TASK-F02 - Playwright E2E criticos

Prioridad: P1  
Archivos:

- `MyOwnClone/e2e/*.spec.ts`

Crear specs:

1. `auth-dashboard.spec.ts`
2. `rag.spec.ts`
3. `billing.spec.ts`
4. `admin.spec.ts`
5. `products-meetings.spec.ts`

Criterio de cierre:

- E2E no solo carga paginas; valida flujo.

## TASK-F03 - CI gate recomendado

Prioridad: P1  
Archivos:

- `.github/workflows/*` si existe.
- docs ops.

Gate minimo:

```powershell
cd MyOwnClone
npm run typecheck
npm test
cd ..
pytest -q
pytest api\tests -q
```

Gate ampliado:

```powershell
cd MyOwnClone
npx playwright test
```

Criterio de cierre:

- CI bloquea merges si falla gate minimo.

## TASK-F04 - Produccion y env

Prioridad: P1  
Archivos:

- `MyOwnClone/.env.example`
- `api/.env.example`
- `ops/*.env.production.example`
- `ops/*.sh`

Acciones:

1. Quitar contradicciones env.
2. Confirmar CORS.
3. Confirmar secure cookies.
4. Confirmar backend URL.
5. Confirmar Stripe/OpenAI/SendGrid/Whereby en modo prod.
6. Documentar valores obligatorios.

Criterio de cierre:

- Un agente puede levantar local y preparar prod siguiendo docs.

## TASK-F05 - Higiene de repo

Prioridad: P2  
Archivos:

- `.gitignore`
- `api/.flaskenv`
- `api/.venv`

Acciones:

1. Confirmar `.venv` ignorado.
2. Evitar que auditorias incluyan `.venv`.
3. Evaluar si `api/.flaskenv` debe seguir trackeado.

Criterio de cierre:

- Inventario repo no se contamina con entorno virtual.

---

# Tabla de seguimiento para el agente

| Task | Prioridad | Estado | Depende de | Tests obligatorios |
|---|---|---|---|---|
| TASK-A01 | P0 | pending | - | - |
| TASK-A02 | P0 | pending | - | `npm test -- ChatPanel` |
| TASK-A03 | P0 | pending | - | `npm test -- facturacion` |
| TASK-A04 | P0 | pending | - | `npm run typecheck` |
| TASK-A05 | P0 | pending | - | `pytest -q`, `pytest api\tests -q` |
| TASK-A06 | P0 | pending | A04 | admin tests, pytest api |
| TASK-B01 | P0 | pending | A01 | doc review |
| TASK-B02 | P0 | pending | B01 | typecheck, pytest api |
| TASK-B03 | P0 | pending | B01 | products/admin tests |
| TASK-B04 | P0 | pending | B01 | tenant scoping tests |
| TASK-C01 | P0 | pending | B01 | doc review |
| TASK-C02 | P0 | pending | C01 | retrieval tests |
| TASK-C03 | P0 | pending | C02 | ingestion tests |
| TASK-C04 | P0 | pending | C03 | chat integration tests |
| TASK-C05 | P0 | pending | C04 | Playwright RAG |
| TASK-D01 | P0 | pending | A05/B02 | Stripe checkout tests |
| TASK-D02 | P1 | pending | D01 | Vitest billing |
| TASK-D03 | P0 | pending | D01/B02 | webhook tests |
| TASK-E01 | P1 | pending | B03 | products tests |
| TASK-E02 | P1 | pending | B03 | booking tests |
| TASK-E03 | P1 | pending | C04 | analytics tests |
| TASK-E04 | P1 | pending | A06/B03 | admin tests |
| TASK-E05 | P1 | pending | C04 | memory chat test |
| TASK-E06 | P1 | pending | B03 | inbox tests |
| TASK-F01 | P1 | pending | A02/A03 | `pytest -q` |
| TASK-F02 | P1 | pending | C05/D01/E01/E04 | Playwright |
| TASK-F03 | P1 | pending | F01/F02 | CI gate |
| TASK-F04 | P1 | pending | A04/A05/D01 | deploy smoke |
| TASK-F05 | P2 | pending | - | git status/inventory |

## Instrucciones finales para el agente implementador

1. No hacer cambios visuales fuera del alcance de una task.
2. No marcar una pantalla como lista si su endpoint no existe.
3. No usar mocks como exito productivo.
4. Si faltan credenciales externas, crear modo test explicito y error productivo claro.
5. Actualizar este plan o el progress log con cada decision de contrato.
6. Despues de cada fase, ejecutar el gate minimo y registrar resultados.

## Entrega esperada por fase

Cada fase debe cerrar con:

| Campo | Requerido |
|---|---|
| Tasks completadas | Si |
| Archivos tocados | Si |
| Contratos cambiados | Si |
| Migraciones | Si aplica |
| Tests ejecutados | Si |
| Pendientes reales | Solo bloqueos externos |


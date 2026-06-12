# Auditoria 100% - Coordinacion (2026-06-11)

## Resumen ejecutivo

- **Estado real:** Rojo para produccion. El repositorio tiene una base amplia, pero los flujos principales no estan 100% interconectados.
- **Riesgo principal:** frontend, Next API routes, Flask backend y dos modelos de datos trabajan con contratos distintos.
- **Veredicto:** no se debe vender como funcional completo hasta cerrar los P0/P1 de conocimiento/RAG, billing, contratos de datos, productos y tests.
- **Nota:** este documento reemplaza el snapshot anterior del 2026-06-10, que indicaba tests verdes y RAG operativo. En el estado revisado el 2026-06-11 eso ya no es correcto.

## Verificaciones ejecutadas

| Comando | Resultado | Lectura |
|---|---:|---|
| `npm run typecheck` en `MyOwnClone/` | OK | TypeScript compila. |
| `npm test` en `MyOwnClone/` | FAIL | 12 fallos: `ChatPanel` por `scrollTo` en jsdom y tests de `facturacion` desactualizados. |
| `pytest -q` en raiz | OK, 26 tests | Solo ejecuta `tests/`, no `api/tests`. |
| `pytest api\tests -q` | OK, 14 passed / 12 skipped | Hay cobertura backend, pero muchas pruebas criticas estan saltadas. |

## Hallazgos bloqueantes

| ID | Prioridad | Hallazgo | Evidencia | Impacto |
|---|---|---|---|---|
| C11-001 | P0 | El flujo de conocimiento no alimenta RAG. | `MyOwnClone/src/app/api/clone/sources/route.ts:125`, `api/models/dataset.py:4`, `api/core/myownclone/silos.py:48` | El usuario puede subir fuentes que quedan como `ready`, pero el chat no tiene base real fiable. |
| C11-002 | P0 | Billing/Stripe checkout esta roto. | `api/controllers/console/myownclone/stripe_ctrl.py:29`, `:72`, `:96` | Click en upgrade puede fallar o volver a rutas inexistentes (`/dashboard/...`). |
| C11-003 | P0 | Contratos DB/enums divergentes entre Drizzle y SQLAlchemy. | `MyOwnClone/src/lib/db/schema/tenants.ts:16`, `api/models/account.py:67`, `MyOwnClone/src/lib/db/schema/clones.ts:13`, `api/models/clone.py:16` | Datos validos en una capa pueden ser invalidos o invisibles en otra. |
| C11-004 | P1 | Proxy Next hardcodea backend local. | `MyOwnClone/src/proxy.ts:5` | Deploy y entornos reales ignoran `MYOWNCLONE_API_URL`. |
| C11-005 | P1 | Productos no esta interconectado. | `MyOwnClone/src/app/(dashboard)/productos/page.tsx:54`, `api/controllers/console/myownclone/booking.py:127` | Frontend pide GET de productos; backend solo registra la ruta y no hay GET auditado. |
| C11-006 | P1 | Analytics muestra datos falsos/parciales. | `api/controllers/console/myownclone/analytics.py:89-98` | Dashboard puede decir 0 conversaciones/mensajes aunque haya actividad. |
| C11-007 | P1 | Test suite frontend esta roja. | `MyOwnClone/src/components/chat/ChatPanel.tsx:70`, `MyOwnClone/src/__tests__/app/facturacion.test.tsx:123` | No hay confianza para seguir tocando UI sin regresiones. |

## Mapa de interconexion actual

| Flujo | Frontend | Proxy/API Next | Flask backend | DB/servicios | Estado |
|---|---|---|---|---|---|
| Login | NextAuth | N/A | Flask auth parcial | Drizzle users / SQLAlchemy account | Amarillo |
| Onboarding clone | Dashboard | `/api/clone/clones` proxy | `clone.py` | SQLAlchemy clone | Amarillo |
| Chat publico | `[slug]` + `ChatPanel` | proxy/public fetch mixto | `myownclone_public.py` | retrieval/model manager | Rojo |
| Conocimiento | Biblioteca | `/api/clone/sources` local | No ingest real | Drizzle sources, Dataset stub | Rojo |
| Productos | Dashboard products | proxy | `booking.py` ruta products | SQLAlchemy Product | Rojo |
| Reuniones | Dashboard reuniones | proxy | booking/availability | SQLAlchemy booking | Amarillo |
| Billing | Dashboard billing | `/api/clone/stripe/*` | `stripe_ctrl.py` | Stripe + tenant plan | Rojo |
| Admin | Admin pages | proxy | admin_platform | SQLAlchemy | Amarillo |

## Orden recomendado

1. **Cerrar P0 de datos/RAG:** una fuente de verdad DB, modelos Dataset reales, ingestion desde sources y retrieval funcionando con tests.
2. **Arreglar billing:** `current_account_with_tenant`, rutas correctas, planes normalizados y tests de checkout.
3. **Arreglar proxy/env:** `MYOWNCLONE_API_URL`, sin backend local hardcodeado.
4. **Arreglar productos:** GET/POST/PUT/DELETE backend y UI conectada.
5. **Volver tests a verde:** Vitest, pytest raiz + `api/tests`, y smoke E2E de flujos criticos.

## Estado de documentacion

Los documentos de esta carpeta quedan actualizados como fuente de verdad de auditoria:

- `01-db-architecture.md`: contratos de datos y divergencias.
- `02-auth-security.md`: auth, proxy y seguridad.
- `03-frontend.md`: dashboard, landing, billing y UX.
- `04-backend-rag.md`: Flask, RAG, ingestion y negocio.
- `05-i18n.md`: idiomas y textos.
- `06-integrations.md`: Stripe, email, booking y externos.
- `07-testing-ci-prod.md`: pruebas, CI y produccion.
- `99-consolidated-action-plan.md`: plan de ejecucion.

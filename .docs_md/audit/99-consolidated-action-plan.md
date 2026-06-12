# Plan Consolidado de Accion (Auditoria 2026-06-11)

> Auditoria profunda ampliada: `100-deep-repository-audit-2026-06-11.md`.
> Plan maestro implementable: `.docs_md/MASTER_IMPLEMENTATION_PLAN_2026-06-12.md`.

## Diagnostico

El producto tiene interfaz y estructura, pero no esta cerrado como sistema util end-to-end. La prioridad no es seguir retocando pantallas: es conectar correctamente frontend, proxy, backend, DB y servicios.

## P0 - Bloqueadores

| ID | Area | Tarea | Evidencia |
|---|---|---|---|
| P0-01 | RAG | Sustituir Dataset/DocumentSegment stub o adaptar retrieval a tablas reales. | `api/models/dataset.py:4`, `api/core/myownclone/silos.py:48` |
| P0-02 | Knowledge | Hacer que crear fuente dispare ingestion/embeddings y estado real. | `MyOwnClone/src/app/api/clone/sources/route.ts:125` |
| P0-03 | Billing | Arreglar Stripe checkout con proxy account/email y rutas reales. | `api/controllers/console/myownclone/stripe_ctrl.py:29`, `:96` |
| P0-04 | DB contracts | Normalizar enums y nombres entre Drizzle/SQLAlchemy. | `tenants.ts:16`, `account.py:67`, `clones.ts:13`, `clone.py:16` |

## P1 - Criticos

| ID | Area | Tarea | Evidencia |
|---|---|---|---|
| P1-01 | Proxy | Usar `MYOWNCLONE_API_URL` en `proxy.ts`. | `MyOwnClone/src/proxy.ts:5` |
| P1-02 | Productos | Implementar contrato backend completo y tests. | `productos/page.tsx:54`, `booking.py:127` |
| P1-03 | Analytics | Persistir y contar conversaciones/mensajes reales. | `analytics.py:89-98` |
| P1-04 | Tests | Volver `npm test` a verde. | `ChatPanel.tsx:70`, `facturacion.test.tsx:123` |
| P1-05 | CI | Ejecutar `api/tests` en el flujo normal. | `pytest.ini:2` |
| P1-06 | Billing UI | Reutilizar planes de landing con modo upgrade y checkout real. | `facturacion/page.tsx` |

## Roadmap de ejecucion

### Fase 1 - Estabilizacion inmediata

1. Arreglar `ChatPanel` para que Vitest no falle.
2. Alinear tests de facturacion con el comportamiento final.
3. Cambiar proxy a env `MYOWNCLONE_API_URL`.
4. Bloquear checkout cuando los planes son fallback.

### Fase 2 - Producto util

1. Implementar ingestion real de fuentes.
2. Implementar Dataset/segments/chunks reales o unificar sobre las tablas existentes.
3. Unificar chat publico/dashboard con retrieval y prompt del clone.
4. Registrar conversaciones/mensajes para analytics.

### Fase 3 - Monetizacion

1. Arreglar `stripe_ctrl.py`.
2. Crear pricing compartido landing/billing.
3. Billing dashboard debe mostrar plan actual, upgrade/downgrade y errores accionables.

### Fase 4 - Gestion

1. Productos CRUD completo.
2. Reuniones CRUD completo y verificado.
3. Settings y API Keys separados por contenido, ruta y tests.

### Fase 5 - Produccion

1. `pytest.ini` incluye `api/tests` o CI ejecuta ambos comandos.
2. Activar pruebas saltadas con fixtures reales.
3. Health check backend.
4. Rate limit durable para publico.
5. Documentar env vars obligatorias por entorno.

## Criterio de cierre

Un flujo se considera listo solo si cumple:

- UI visible y coherente.
- API contract documentado.
- Backend implementado.
- DB/migracion real.
- Tests unitarios/integracion pasan.
- Error state controlado.
- Sin dependencia silenciosa de stubs.

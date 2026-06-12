# Auditoria 100% - Backend, RAG y Logica de Negocio (2026-06-11)

## Resumen

- **Estado:** Rojo en RAG y billing; amarillo en CRUDs base.
- **Riesgo principal:** el backend tiene controladores, pero algunos modelos/contratos son stubs o no coinciden con lo que pide el frontend.
- **Veredicto:** antes de nuevas pantallas hay que cerrar ingestion, retrieval, productos y Stripe.

## Hallazgos

| ID | Prioridad | Hallazgo | Evidencia | Impacto |
|---|---|---|---|---|
| B11-001 | P0 | `Dataset` y `DocumentSegment` son stubs, pero RAG los consulta como modelos SQLAlchemy. | `api/models/dataset.py:4`, `api/models/dataset.py:11`, `api/core/myownclone/silos.py:48` | Retrieval puede fallar o devolver vacio aunque haya fuentes. |
| B11-002 | P0 | `sources` no dispara ingestion ni embeddings. | `MyOwnClone/src/app/api/clone/sources/route.ts:125-129`, `api/core/ingestion.py` | Base de conocimiento no es util para el clon. |
| B11-003 | P0 | Stripe checkout usa `account.email` cuando `account` sale del proxy como string. | `api/controllers/console/myownclone/stripe_ctrl.py:72`, `:96` | Upgrade puede romper con 500. |
| B11-004 | P0 | Stripe redirige a rutas antiguas `/dashboard/...`. | `api/controllers/console/myownclone/stripe_ctrl.py:29-30` | Flujo post-pago lleva a paginas inexistentes. |
| B11-005 | P1 | Analytics devuelve conversaciones/mensajes a 0 por TODO. | `api/controllers/console/myownclone/analytics.py:89-98` | Dashboard no sirve para monitorizar crecimiento real. |
| B11-006 | P1 | Productos no tiene contrato completo alineado con frontend. | `api/controllers/console/myownclone/booking.py:127`, frontend `productos/page.tsx:54` | Sales mode no puede gestionar catalogo de forma fiable. |
| B11-007 | P1 | `chat-simple` usa model manager sin retrieval/prompt del clone. | `api/controllers/myownclone_public.py:373`, `api/core/model_manager.py:333-348` | Una ruta de chat puede responder sin personalidad ni conocimiento. |
| B11-008 | P2 | Rate limit publico en memoria. | `api/controllers/myownclone_public.py:50`, `:86-99` | No es suficiente para varios workers ni reinicios. |

## Flujo RAG esperado

```
Dashboard source upload
  -> valida tenant/clone
  -> crea Source en estado processing
  -> backend ingestion extrae texto
  -> crea Dataset/DocumentSegment/embeddings por silo
  -> marca Source ready/error
  -> chat retrieve_from_silo
  -> LLM con system prompt + contexto + citas
```

## Flujo RAG actual observado

```
Dashboard source upload
  -> Next API local valida sesion
  -> toma cloneId de cookie o DEFAULT_CLONE_ID
  -> inserta Source Drizzle en ready
  -> no ingestion
  -> retrieval consulta Dataset stub
```

## Acciones backend

1. Crear modelos/migraciones reales para Dataset y DocumentSegment o cambiar retrieval para usar las tablas Drizzle actuales (`sources/chunks`).
2. Exponer endpoint backend para crear fuentes y procesarlas por silo.
3. Cambiar Next `/api/clone/sources` para que sea proxy o job starter, no almacenamiento final aislado.
4. Arreglar `stripe_ctrl.py`: usuario proxy, email, tenant, rutas `/resumen` y `/facturacion`.
5. Implementar GET/POST/PUT/DELETE de productos con tests.
6. Registrar conversaciones y mensajes para analytics.
7. Unificar chat publico y chat dashboard en una sola ruta RAG-aware.

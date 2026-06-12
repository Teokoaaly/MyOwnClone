# Auditoria 100% - Integraciones (2026-06-11)

## Resumen

- **Estado:** Rojo en Stripe/RAG ingestion, amarillo en email/booking.
- **Riesgo principal:** hay botones y endpoints, pero los servicios externos no tienen contrato end-to-end validado.

## Hallazgos

| ID | Prioridad | Integracion | Hallazgo | Evidencia |
|---|---|---|---|---|
| G11-001 | P0 | Stripe | Checkout puede romper por `account.email` y rutas antiguas. | `api/controllers/console/myownclone/stripe_ctrl.py:29-30`, `:96` |
| G11-002 | P1 | Stripe | Fallback pricing puede permitir accion no real. | `facturacion/page.tsx:64`, `:240` |
| G11-003 | P0 | RAG/OpenAI | Fuentes no generan embeddings ni dataset real. | `sources/route.ts:125`, `dataset.py:4` |
| G11-004 | P1 | Products/Sales | Catalogo no tiene CRUD completo auditado. | `productos/page.tsx:54`, `booking.py:127` |
| G11-005 | P2 | Public chat | Rate limit local en memoria. | `myownclone_public.py:50` |
| G11-006 | P2 | Email inbound | Firma existe, pero flujo inbox/draft necesita E2E. | `myownclone_public.py`, `inbox.py` |
| G11-007 | P2 | Booking | Reuniones existen, falta validacion completa de Whereby/calendario. | `booking.py` |

## Acciones

1. Stripe test mode E2E: plan -> checkout -> success -> tenant plan actualizado.
2. RAG E2E: fuente -> segmentacion -> embedding -> retrieval -> respuesta con contexto.
3. Products E2E: crear producto -> chat sales lo usa.
4. Email E2E: inbound firmado -> inbox -> draft.
5. Booking E2E: disponibilidad -> reserva -> confirmacion.

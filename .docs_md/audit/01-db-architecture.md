# Auditoria 100% - DB y Arquitectura de Datos (2026-06-11)

## Resumen

- **Estado:** Rojo por divergencia de contratos.
- **Riesgo principal:** Drizzle y SQLAlchemy no describen el mismo producto.
- **Veredicto:** elegir una fuente de verdad antes de ampliar features.

## Hallazgos

| ID | Prioridad | Hallazgo | Evidencia | Impacto |
|---|---|---|---|---|
| D11-001 | P0 | Plan/status de tenant no coinciden entre frontend DB y backend. | `MyOwnClone/src/lib/db/schema/tenants.ts:16-39`, `api/models/account.py:67-71` | `basic/trial/active` vs `basico/normal` rompe billing, admin y filtros. |
| D11-002 | P0 | Modos del clone no coinciden. | `MyOwnClone/src/lib/db/schema/clones.ts:13`, `api/models/clone.py:16-18` | `pedagogy` vs `teach`; prompts/conversations pueden quedar fuera. |
| D11-003 | P0 | Dataset/DocumentSegment no son modelos reales. | `api/models/dataset.py:4`, `api/models/dataset.py:11` | RAG no tiene base relacional consistente. |
| D11-004 | P1 | `sources` se escribe en Drizzle, retrieval lee otros modelos. | `MyOwnClone/src/app/api/clone/sources/route.ts:129`, `api/core/myownclone/silos.py:48` | El conocimiento no fluye de UI a chat. |
| D11-005 | P1 | Cookie/default clone id puede saltarse verificacion fuerte de propiedad en API local. | `sources/route.ts:10-12`, `:32` | Riesgo multi-tenant si un usuario fuerza cloneId. |

## Decision requerida

Opcion recomendada: **Drizzle como fuente de verdad para Next + migraciones**, y SQLAlchemy alineado exactamente con esas tablas para Flask.

Tareas:

1. Crear matriz de tablas compartidas.
2. Normalizar enums.
3. Crear migracion de reconciliacion.
4. Eliminar stubs de Dataset o apuntar RAG a tablas reales.
5. Anadir tests DB cross-layer.

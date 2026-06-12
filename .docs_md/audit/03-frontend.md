# Auditoria 100% - Frontend, Dashboard y UX (2026-06-11)

## Resumen

- **Estado:** Amarillo/Rojo. La UI existe y visualmente esta avanzada, pero hay flujos que no estan respaldados por backend real.
- **Riesgo principal:** se muestran acciones utiles (`sources`, `products`, `billing`, chat) que pueden fallar o no persistir en el sistema correcto.
- **Veredicto:** se puede seguir iterando, pero hay que congelar cambios visuales hasta cerrar contratos de API y tests.

## Hallazgos

| ID | Prioridad | Hallazgo | Evidencia | Recomendacion |
|---|---|---|---|---|
| F11-001 | P0 | Biblioteca/sources usa API local y no backend RAG. | `MyOwnClone/src/app/api/clone/sources/route.ts:32`, `:125`, `:129` | Reemplazar por backend ingestion o hacer que Next dispare ingestion y estado real `processing/ready/error`. |
| F11-002 | P1 | `ChatPanel` rompe Vitest por `scrollTo` no protegido. | `MyOwnClone/src/components/chat/ChatPanel.tsx:70` | Comprobar `typeof container.scrollTo === "function"` o usar `scrollTop`. |
| F11-003 | P1 | Facturacion UI y tests estan desalineados. | `MyOwnClone/src/app/(dashboard)/facturacion/page.tsx:240`, `:292`; test en `facturacion.test.tsx:123`, `:188` | Decidir copy final y actualizar tests junto al comportamiento. |
| F11-004 | P1 | Plan fallback puede iniciar checkout con IDs inexistentes. | `MyOwnClone/src/app/(dashboard)/facturacion/page.tsx:64` | Si la API de planes falla, mostrar planes informativos sin checkout activo. |
| F11-005 | P1 | Productos llama GET a un endpoint que no esta completo. | `MyOwnClone/src/app/(dashboard)/productos/page.tsx:54` | Implementar contrato backend completo antes de cerrar la pagina. |
| F11-006 | P1 | Pagina publica `[slug]` llama backend directo, mientras dashboard usa proxy. | `MyOwnClone/src/app/(public)/[slug]/page.tsx:54` | Centralizar cliente API/env y evitar rutas diferentes por tipo de pagina. |
| F11-007 | P2 | Mucho dashboard depende de client components y fetch en cliente. | Rutas en `MyOwnClone/src/app/(dashboard)/...` | Mantener solo interactividad como cliente; mover datos base a server components o loaders. |
| F11-008 | P2 | Textos mezclan ingles/espanol y no usan i18n. | Landing/dashboard/settings/sidebar | Definir idioma base por usuario/clone y extraer strings a mensajes. |

## Puntos revisados de dashboard

| Area | Estado | Notas |
|---|---|---|
| Overview / resumen | Amarillo | UI ajustada, pero analytics no refleja conversaciones reales. |
| Sidebar | Amarillo | Ya separa Settings y API Keys, pero debe validarse contra rutas reales. |
| Upgrade card | Amarillo | Debe apuntar a billing funcional y no moverse por animaciones de contenido. |
| Facturacion | Rojo | La pantalla debe usar los mismos planes de landing, pero con acciones de upgrade reales. |
| Settings | Amarillo | Identidad del clone visible; hay que separar settings de API keys correctamente en contenido y rutas. |
| API Keys | Amarillo | Debe ser pagina propia, no contenido de settings. |
| Public clone chat | Rojo | UI existe, pero depende de RAG/backend roto. |

## Acciones frontend

1. Volver `npm test` a verde.
2. Bloquear checkout en fallback plans.
3. Unificar componentes de pricing entre landing y billing, con modo `marketing` y modo `upgrade`.
4. Mover `/api/clone/sources` a contrato backend real o documentarlo como stub visible.
5. Crear tests de navegacion dashboard: Overview -> API Keys, Settings, Billing, Upgrade.
6. Revisar layout para evitar scrolls internos no deseados; solo pagina o panel explicito deben scrollear.

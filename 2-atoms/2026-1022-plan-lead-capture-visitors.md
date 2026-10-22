---
id: 2026-1022-plan-lead-capture-visitors
type: atom
certainty: tentative
sources: [raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md]
links: ["[[2026-1022-myclone-chat-streaming-sse]]", "[[2026-1022-instancia-como-captador-de-leads]]", "[[2026-1022-plan-workflows-nuestro]]"]
---
## Claim
El paso 2 del handoff (prioridad 🔴 ALTA, esfuerzo **bajo**) es añadir gestión de leads sobre lo que [[myownclone]] ya tiene: hoy existe `visitorId` en la tabla `conversations` (Drizzle) y solo falta crear la tabla `visitors` (`clone_id`, `email`, `first_name`, `last_name`, `session_token`, `metadata JSONB`, `created_at`, `last_seen_at`), un endpoint público `POST /api/myownclone/public/clones/{slug}/capture-lead`, un proxy `GET /api/visitors`, y la UI: en `resumen/page.tsx` mostrar un popup "Ingresa tu email para continuar" **después de 3 mensajes del usuario**.

## Why It Matters
Es el mismo patrón post-chat que usa MyClone.is (`POST /api/v1/sessions/{session_token}/capture-lead`, ver [[2026-1022-myclone-chat-streaming-sse]]): el visitante no da su email antes de hablar, se lo pide el clon cuando ya ha hablado. En el vault, [[2026-1022-instancia-como-captador-de-leads]] ya describe a [[myownclone]] como captador de leads por definición — lo que falta aquí es la **infraestructura de captura**, no la intención de producto.
El handoff ordena explicitamente "bajo esfuerzo, alto impacto" y lo coloca segundo en la roadmap, por delante de workflows: es la pieza que convierte tráfico en leads contactables con muy poco código nuevo (una tabla + dos endpoints + un popup).
El trigger de los 3 mensajes es una decisión de producto arbitraria pero replicable: define el momento de mayor compromiso antes de pedir el email. Marcar `tentative`: es plan, no implementación verificada.

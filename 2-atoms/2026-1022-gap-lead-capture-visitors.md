---
id: 2026-1022-gap-lead-capture-visitors
type: atom
certainty: solid
sources: [raw/articles/myownclone-osint-implementation-plan-2026-06-24.md]
links: ["[[2026-1022-instancia-como-captador-de-leads]]", "[[2026-1022-myclone-vs-myownclone-gaps-api]]", "[[2026-1022-myclone-access-control-por-persona]]", "[[2026-1022-plan-lead-capture-visitors]]"]
---
## Claim
[[myownclone]] **no sabe quién visita sus clones**: no hay captura de leads post-chat, ni visitor tracking, ni tabla de visitantes. Lo único disponible es un modelo `Feedback` en `analytics.py` que solo guarda un rating. MyClone.is, en cambio, expone `POST /sessions/{token}/capture-lead` con email y nombre tras la conversación, `GET /personas/{id}/visitors` con `PersonaVisitorResponse` (id, email, firstName, lastName, addedAt, lastAccessedAt) y un lead scoring con `OutputTemplate` de secciones `profile, situation, need, score, key_context, follow_up_questions`.

## Why It Matters
El gap no es "falta un formulario": es que **no existe la tabla de visitantes**, así que cualquier analítica de audiencia o funnel se apoya hoy en datos que el producto no captura. El lead scoring con secciones fijas (situación, necesidad, score, preguntas de seguimiento) convierte una conversación en una ficha accionable para el creator, no solo en un email.
El plan de implementación propone `Visitor` (id, persona_id, email, first_name, last_name, created_at, last_accessed_at) y `LeadCapture` (id, session_token, visitor_id, captured_at, source), guardar el `session_token` en `chat_public`, y exponer `/visitors` y `/analytics/visitors`, con un popup de email tras 3 mensajes.
Relacionado: [[2026-1022-myclone-access-control-por-persona]] muestra que MyClone.is gestiona visitantes tanto por persona como por usuario, es decir, el lead es un objeto de plataforma, no un añadido del chat.
El detalle de diseño (tabla `visitors` en Drizzle, proxy `GET /api/visitors`, popup a los 3 mensajes) está en [[2026-1022-plan-lead-capture-visitors]], derivado del handoff complementario.

## [FRICTION]
> [[2026-1022-instancia-como-captador-de-leads]] (fundador) afirma que en [[myownclone]] "dependiendo de cada instancia [...] hay una que quieres que [...] tengan que dejarte el email para hablar", con base de datos exportable a CRM.
> Este átomo presiona esa creencia porque el plan de implementación, basado en el código, afirma que no existe captura de leads ni visitor tracking en el producto: el único registro de interacción es un `Feedback` con rating.
> Ambas no pueden ser completamente correctas: o el email-gate por instancia existe solo en el producto servido en producción y no en este repo, o es una capacidad prometida pero no implementada. Marcado para juicio humano, no auto-resuelto.

> [[2026-1022-myclone-vs-myownclone-gaps-api]] lista "captura de leads" entre lo que [[myownclone]] **sí puede replicar** de MyClone.is, mientras este átomo la lista como lo que **no tiene**.
> La fricción es de granularidad: replicable ≠ implementado. Marcado para juicio humano, no auto-resuelto.

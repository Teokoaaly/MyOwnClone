---
id: 2026-10-27-gmail-api-filters
type: atom
certainty: solid
sources: [sources/2026-10-27-gmail-api-overview.md]
links: ["[[2026-10-27-gmail-api-drafts]]", "[[2026-10-27-gmail-api-forwarding]]"]
---

## Claim
Filters are advanced rules configured for an account that evaluate incoming messages against specific matching criteria (such as sender, subject, or size); when a message matches, filters automatically trigger actions such as adding or removing labels, or forwarding the email to a specified address.

## Why It Matters
Filters enable automated email triage and organization without requiring polling or constant API calls, as the server applies rules in real-time upon message arrival.

## [FRICTION]
> [[2026-10-27-gmail-api-forwarding]] (escrita hoy) afirma que los filtros solo pueden añadir etiquetas o reenviar, pero no pueden mover mensajes entre carpetas. Esta nota presiona eso porque el sistema de etiquetas de Gmail funciona como carpetas virtuales, lo que hace que esa distinción sea falsa. Ambas pueden ser completamente correctas. Marcado para juicio humano, no auto-resuelto.
---
id: 2026-10-27-gmail-api-drafts
type: atom
certainty: solid
sources: [sources/2026-10-27-gmail-api-overview.md]
links: ["[[2026-10-27-gmail-api-messages]]", "[[2026-10-27-gmail-api-filters]]"]
---

## Claim
A draft is an unsent message that can be replaced; sending a draft automatically deletes the draft and creates a message with the SENT system label.

## Why It Matters
The draft model allows applications to build unsent messages incrementally and send them atomically, simplifying workflows that need to compose and send email programmatically.

## [FRICTION]
> [[2026-10-27-gmail-api-messages]] (escrita hoy) afirma que el mensaje no puede cambiarse después de crearlo. Esta nota presiona eso porque los borradores sí pueden reemplazarse, lo que crea una tensión entre la inmensajeidad y la maleabilidad de los borradores. Ambas pueden ser completamente correctas. Marcado para juicio humano, no auto-resuelto.
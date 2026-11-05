---
id: 2026-10-27-gmail-api-messages
type: atom
certainty: solid
sources: [sources/2026-10-27-gmail-api-overview.md]
links: ["[[2026-10-27-gmail-api-threads]]", "[[2026-10-27-gmail-api-drafts]]"]
---

## Claim
A Gmail message is an email containing sender, recipients, subject, and body; after creation, the message cannot be changed.

## Why It Matters
Messages are the fundamental unit of data in the Gmail API; understanding their immutable nature affects how drafts, sends, and forwards are handled in application logic.

## [FRICTION]
> [[2026-10-27-gmail-api-drafts]] (escrita hoy) afirma que los borradores pueden modificarse después de crear el mensaje. Esta nota presiona eso porque el claim dice que el mensaje no puede cambiarse después de crearlo, mientras que los borradores sí pueden reemplazarse. Ambas pueden ser completamente correctas. Marcado para juicio humano, no auto-resuelto.
---
id: 2026-10-27-gmail-api-labels
type: atom
certainty: solid
sources: [sources/2026-10-27-gmail-api-overview.md]
links: ["[[2026-10-27-gmail-api-restful]]", "[[2026-10-27-gmail-api-threads]]"]
---

## Claim
The Gmail API uses two types of labels: system labels ( internally created, such as INBOX, TRASH, or SPAM, which cannot be deleted or modified but can be applied or removed from messages and threads) and user labels (created by a user or application, which can be deleted or modified).

## Why It Matters
Understanding the label distinction is essential for correctly organizing messages, as system labels provide fixed organizational categories while user labels allow custom categorization and persistence across sessions.

## [FRICTION]
> [[2026-10-27-gmail-api-threads]] (escrita hoy) afirma que los hilos solo usan etiquetas de usuario. Esta nota presiona eso porque las etiquetas del sistema (INBOX, TRASH, SPAM) se aplican automáticamente y son fundamentales para la arquitectura de hilos. Ambas pueden ser completamente correctas. Marcado para juicio humano, no auto-resuelto.
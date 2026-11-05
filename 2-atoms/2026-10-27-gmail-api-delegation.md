---
id: 2026-10-27-gmail-api-delegation
type: atom
certainty: solid
sources: [sources/2026-10-27-gmail-api-overview.md]
links: ["[[2026-10-27-gmail-api-push]]", "[[2026-10-27-gmail-api-restful]]"]
---

## Claim
A delegator is a Gmail user who grants mailbox access to another user within the same Google Workspace organization; the receiving user (delegate) can read, send, and delete messages, as well as view and add contacts on behalf of the delegator's account.

## Why It Matters
Delegation enables collaborative mailbox management within organizations, allowing assistants, team members, or administrators to act on another user's mailbox while maintaining audit and permission boundaries.

## [FRICTION]
> [[2026-10-27-gmail-api-restful]] (escrita hoy) afirma que la API RESTful cubre acceso delegado. Esta nota presiona eso porque el ser REST no garantiza automáticamente que las operaciones delegadas estén permitidas; se requiere configuración OAuth y permisos explícitos. Ambas pueden ser completamente correctas. Marcado para juicio humano, no auto-resuelto.
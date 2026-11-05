---
id: 2026-1028-newapi-group-isolation
type: atom
certainty: solid
sources: [sources/2026-10-28-newapi-group-management.md]
links: ["[[2026-1028-newapi-token-group]]", "\"[[2026-1028-newapi-channel-group]]\""]
---

## Claim

Groups isolate channel access permissions and billing multipliers for different users — users in different groups can only access channels assigned to their group.

## Why It Matters

This permission isolation is the foundational access control mechanism of New API: it ensures that users, tokens, and channels are logically separated by group, preventing cross-group channel access and enabling tiered billing through group-specific multipliers. Without group isolation, all users would share the same channel access, making per-user billing and access control impossible.

## [FRICTION]

> [[2026-1028-newapi-token-group]] (escrita hace pocas semanas) afirma que los tokens heredan el grupo del usuario por defecto. Esta nota presiona porque la fuente original indica que el grupo del token se puede establecer de forma independiente al del usuario, no necesariamente heredado — y el modo `auto` selecciona grupos en orden de prioridad, no por herencia. Ambas pueden ser ciertas dependiendo de la configuración inicial, pero la fuente no aclara el comportamiento por defecto. Marcado para juicio humano, no auto-resuelto.
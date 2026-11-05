---
id: 2026-1028-newapi-token-group
type: atom
certainty: solid
sources: [sources/2026-10-28-newapi-group-management.md]
links: ["[[2026-1028-newapi-group-isolation]]", "\"[[2026-1028-newapi-channel-group]]\""]
---

## Claim

A token's group determines which channel group it can access when making API calls — the group can be set explicitly or set to `auto` for priority-ordered automatic selection.

## Why It Matters

The token-group assignment is the primary access control mechanism for API calls: each token carries a group identifier that the gateway uses to route the request to an authorized channel. When set to `auto`, the system selects an available group in priority order, enabling cross-group failover scenarios where a token can automatically use an alternative group if its primary group is at capacity or unavailable. This dual-mode (explicit + auto) provides both predictable access control and resilience.

## [FRICTION]

> [[2026-1028-newapi-group-isolation]] (escrita hace pocas semanas) afirma que los grupos aíslan tanto los permisos de canal como los multiplicadores de facturación. Esta nota presiona porque, aunque el aislamiento de permisos es claro, la fuente original no especifica si los multiplicadores de facturación también se heredan por grupo o se aplican a nivel de token. La distinción es práctica: si los multiplicadores son a nivel de grupo, todos los usuarios del grupo comparten la misma escala de precios; si son a nivel de token, la variación es por token dentro del mismo grupo. Falta claridad en la documentación original. Marcado para juicio humano, no auto-resuelto.
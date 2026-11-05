---
id: 2026-1028-newapi-channel-group
type: atom
certainty: solid
sources: [sources/2026-10-28-newapi-group-management.md]
links: ["[[2026-1028-newapi-group-isolation]]", "\"[[2026-1028-newapi-token-group]]\""]
---

## Claim

Channels can be restricted to specific groups via the "Group" field when adding a channel, limiting which tokens (and thus which users) can access that channel.

## Why It Matters

Channel group restriction is the complementary access control point to token group assignment: while tokens determine which group they belong to, channels declare which groups are allowed to access them. This bidirectional constraint (token group + channel group) creates a double-gate access control model. A token can only access a channel if the token's group matches (or is auto-selected) the channel's allowed groups. This prevents scenarios where a token has access to a channel it shouldn't, or where a channel receives requests from tokens outside its intended audience. Configuration happens in the admin panel or System Settings under the "Groups" entry.

## [FRICTION]

> [[2026-1028-newapi-token-group]] (escrita hace pocas semanas) afirma que el modo `auto` en el grupo del token selecciona grupos en orden de prioridad. Esta nota presiona porque la fuente original describe el modo `auto` como "útil para escenarios de fallo entre grupos", pero no especifica qué sucede cuando ningún grupo disponible coincide con los grupos permitidos del canal. Si el token auto-selecciona un grupo que el canal no permite, la llamada fallará — pero la fuente no aclara si el error es inmediato o si el sistema intenta el siguiente grupo en la lista. Falta documentación del comportamiento de fallo cruzado. Marcado para juicio humano, no auto-resuelto.
---
id: 2026-1028-newapi-user-group
type: atom
certainty: solid
sources: [sources/2026-10-28-newapi-group-management.md]
links: ["[[2026-1028-newapi-group-isolation]]", "\"[[2026-1028-newapi-token-group]]\""]
---

## Claim

Users can be assigned to a specific group when editing them in User Management, restricting which channels they can access based on their group membership.

## Why It Matters

User group assignment is the human-facing side of New API's access control: administrators assign users to groups in the User Management interface, and those group memberships directly determine channel access. This is the most direct way to control which users see which channels — by assigning a user to "Group A", they can only access channels restricted to "Group A". Group assignment can be modified at any time, instantly changing the user's channel access without requiring token recreation or reconfiguration. This makes group-based access control flexible for dynamic team structures and role changes.

## [FRICTION]

> [[2026-1028-newapi-token-group]] (escrita hace pocas semanas) afirma que los tokens pueden tener su grupo establecido de forma independiente al del usuario. Esta nota presiona porque la fuente original no aclara si la asignación de grupo de usuario y grupo de token son totalmente independientes o si existe una relación de herencia o sincronización. En la práctica, es posible que un usuario pertenezca al Grupo A pero su token esté configurado en el Grupo B, o que el modo `auto` del token seleccione un grupo distinto al del usuario. La relación entre el grupo de usuario y el grupo de token no está documentada en la fuente original, creando incertidumbre sobre el comportamiento esperado en configuraciones mixtas. Marcado para juicio humano, no auto-resuelto.
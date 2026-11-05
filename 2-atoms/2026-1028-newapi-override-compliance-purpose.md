---
id: 2026-1028-newapi-override-compliance-purpose
type: atom
certainty: solid
sources: [sources/2026-10-28-newapi-project-introduction.md]
links: ["[[2026-1028-newapi-channel-management-operation-modes]]", "[[2026-1028-newapi-channel-management-conditional-logic]]"]
---

## Claim

The New API parameter override feature has a restricted purpose: it can only be used for compatibility with legal upstream interface formats, enterprise network compatibility, and request normalization. This limitation gates how the 15 operation modes may be applied in practice.

## Why It Matters

Understanding the permissible use cases prevents overreach — applying parameter overrides beyond these sanctioned purposes may violate upstream terms, break enterprise contracts, or produce unintended request transformations. The simple override mode (backward compatible) and advanced operation mode (conditional logic) each serve these compliance boundaries differently.

## [FRICTION]

> The documentation states the parameter override feature \"can only be used for compatibility with legal upstream interface formats, enterprise network compatibility, and request normalization,\" but does not define what constitutes a valid \"compatibility\" use case versus an invalid one. Operators may uncertain whether their intended transformation falls within the sanctioned purpose, risking unintended compliance violations.

> [[2026-1028-newapi-channel-management-operation-modes]] distinguishes between simple and advanced modes, but the friction notes that \"the overlap and migration path between them is not explicitly defined.\" Operators may uncertainty about when to use which mode for equivalent transformations within the permitted compliance boundary.
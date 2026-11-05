---
id: 2026-1028-newapi-channel-management-path-syntax
type: atom
certainty: solid
sources: [raw/sources/2026-10-28-newapi-channel-management.md]
links: ["[[2026-1022-api-privada-sin-documentacion]]", ["[[2026-1022-arquitectura-rac-tres-modos-por-clon]]"]]
---
## Claim
NewAPI's channel management uses JSON path syntax for field access, supporting root-level fields, nested objects, array indexing with `0`, `-1` (last element), and built-in variables `model`, `upstream_model`, and `original_model` for conditional logic — enabling path-based targeting across nested request structures.

## Why It Matters
Path syntax is the mechanism through which all 15 operation modes and conditional logic address specific fields in the request payload. Support for negative indexing (`messages.-1.content` for last element), built-in variables (model, upstream_model, original_model), and nested object access (`metadata.user.name`) makes the system capable of targeting virtually any parameter in complex request structures — essential for the practical examples like dynamically adjusting parameters based on model type.

## [FRICTION]
> Built-in variables (`model`, `upstream_model`, `original_model`) can be used directly in paths without being explicitly present in the request body, but the documentation does not clarify the fallback behavior when these variables are undefined or redirect to unexpected values. Operators may assume these are always available.

> Negative array indexing (`messages.-1.content`) is a convenient shortcut, but its interaction with other path modifiers (like `trim_prefix`, `ensure_suffix`, or operation chaining) is not documented. Earlier operations in the array may modify the structure that later operations reference.

> The path syntax documentation mentions `.` notation for nested objects but does not address bracket notation (`['key']`) or array filter syntax that may exist in the underlying JSON patch implementation. Operators with JSON Patch experience may assume additional syntax is supported.

> Conditional paths that reference model-dependent fields create circular dependency risk: a condition checking `model` prefix may trigger an operation that changes the effective `model` value, potentially affecting subsequent conditions in the same `operations` array execution order.
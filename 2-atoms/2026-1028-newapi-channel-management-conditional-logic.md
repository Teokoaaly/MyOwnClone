---
id: 2026-1028-newapi-channel-management-conditional-logic
type: atom
certainty: solid
sources: [raw/sources/2026-10-28-newapi-channel-management.md]
links: ["[[2026-1022-api-privada-sin-documentacion]]", ["[[2026-1022-arquitectura-rac-tres-modos-por-clon]]"]]
---
## Claim
NewAPI's channel management supports conditional logic through a `conditions` array per operation, with matching modes (full, prefix, suffix, contains, gt, gte, lt, lte), invert capability, and `pass_missing_key` behavior — enabling sophisticated context-aware parameter adjustments.

## Why It Matters
Conditional logic transforms the parameter override system from static overrides into dynamic, context-aware adjustments. By specifying conditions on paths like `messages.0.content`, `model`, or `max_tokens`, operators can automatically adjust temperature, max_tokens, or stream settings based on message content, model type, or numeric thresholds — critical for routing different message types to appropriate model configurations.

## [FRICTION]
> The documentation lists 9 condition matching modes (full, prefix, suffix, contains, gt, gte, lt, lte) but does not clearly specify type coercion rules for string-to-number comparisons or edge cases when mixing types within a single conditions array.

> `pass_missing_key` behavior inverts the condition logic: `true` means the condition passes if the path is missing, `false` (default) means it fails. This inverted logic is easy to misconfigure, especially in AND combinations where one missing key could block an entire operation set.

> The `invert` flag on individual conditions negates that condition's result, but the interaction between `invert` and `pass_missing_key` is not documented. A condition with `invert: true` and `pass_missing_key: true` has counterintuitive behavior that may surprise operators.

> Logical relationship (`AND` vs `OR`) at the operation level is clear, but nested conditions within an `operations` array and their cumulative effect are not illustrated with end-to-end examples showing how multiple operations with different condition configurations interact.
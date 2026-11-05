---
id: 2026-1028-newapi-channel-management-execution-order
type: atom
certainty: solid
sources: [raw/sources/2026-10-28-newapi-channel-management.md]
links: ["[[2026-1022-api-privada-sin-documentacion]]", ["[[2026-1022-arquitectura-rac-tres-modos-por-clon]]"]]
---
## Claim
NewAPI's channel management executes operations sequentially in the order they appear in the `operations` array, with earlier operations potentially affecting subsequent ones through path modification, value alteration, or structural changes to the request payload — making execution order a critical design consideration.

## Why It Matters
The sequential execution model means that the `operations` array is not just a configuration list but a program whose behavior depends on ordering. Two operations that would be independent in isolation may interact when reordered. This is especially relevant for: chained `trim_prefix`/`ensure_prefix` combinations, `append`/`prepend` operations that modify array structure before subsequent operations reference it, and conditions that reference paths modified by earlier operations. Understanding execution order is essential for reliable channel configurations.

## Key Execution Principles
- **Order matters**: The `operations` array is processed from first to last; reordering can change which values are set, appended, or deleted
- **Cumulative effects**: Earlier operations modify the payload that later operations see; a `set` on `temperature` early in the array may make a later conditional `set` redundant or conflicting
- **Condition timing**: Conditions are evaluated against the current state of the payload at each operation's turn, not against the original payload
- **No implicit rollback**: If an operation fails or is skipped (e.g., `keep_origin: true` with existing value), later operations still execute against the modified payload

## [FRICTION]
> The documentation explicitly states "Operations are executed sequentially according to their order in the `operations` array; earlier operations may affect subsequent ones" but provides no tooling or visualization to help operators predict the outcome of a given ordering. Operators must reason through the execution trace mentally, which is error-prone for arrays with 4+ operations.

> Chained trim operations are a common friction point: `trim_prefix` removing "openai/" followed by `ensure_prefix` also adding "openai/" may seem redundant, but the `keep_origin` parameter on `set` mode changes behavior — with `keep_origin: true`, the set is skipped if the target already has a value, creating conditional behavior that depends on prior operations.

> `append`/`prepend` operations that modify array structure (e.g., adding to `messages`) can change indices for subsequently referenced paths like `messages.0.content` or `messages.-1.content`. The documentation shows these patterns in examples but does not provide a runtime index-tracking aid.

> Conditional logic with path references that earlier operations modify creates subtle bugs. For example, a condition checking `messages.0.content` for "code" may pass on the first operation but by the time a second operation runs, the first operation may have shifted or restructured the messages array.

> No built-in dry-run or simulation mode is documented. Operators must test configurations in staging environments to verify execution order effects, increasing iteration time for complex channel setups.
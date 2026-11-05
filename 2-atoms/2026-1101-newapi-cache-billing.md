---
id: 2026-1101-newapi-cache-billing
type: atom
certainty: solid
sources: [sources/2026-10-28-newapi-features-introduction.md]
links: ["[[2026-1101-newapi-reasoning-effort-suffix]]", "[[2026-1101-newapi-model-rate-limiting]]"]
---
## Claim

New API supports cache billing when enabled: billing is performed according to a set ratio upon cache hit. Two configuration options exist: (1) `Prompt Cache Ratio` in System Settings - Operations Settings, and (2) `Prompt Cache Ratio` per-channel (range 0-1). When set to 0.5, billing occurs at 50% of the normal rate upon cache hit. Supported channels include OpenAI, Azure, and DeepSeek; Claude is not yet supported.

## Why It Matters

Cache billing reduces costs for repeated prompts by applying a discounted ratio on cache hits. This is especially valuable for high-volume workloads with repetitive query patterns. The per-channel ratio allows fine-grained control — some channels can have higher cache discounts than others. Enabling this feature without per-channel configuration defaults to the system-wide ratio.

## [FRICTION]

> Claude is listed as not supported for cache billing, but no migration path or alternative is documented — operators with Claude-dependent workloads cannot apply cache discounts and may face unexpected full billing charges.

> The per-channel ratio overrides the system-wide ratio, but the interaction between the two is not explained: if the system ratio is 0.5 and a channel sets 0.2, does the channel ratio take full effect or is it capped at the system level?

> Billing ratio applies "upon cache hit" but no definition of a "cache hit" boundary exists — it is unclear whether partial matches, token-range overlaps, or prompt embedding similarities affect what counts as a hit, creating ambiguity in cost tracking.

> OpenAI and Azure are supported, but DeepSeek's cache billing behavior may differ from OpenAI's implementation since DeepSeek's cache model may not use the same token-reuse mechanism; operators moving from OpenAI to DeepSeek may see different billing outcomes despite identical ratios.

> No audit or visibility mechanism is documented for tracking which prompts benefited from cache billing vs. full-price billing, making it difficult to validate cost savings claims or reconcile billed amounts with actual usage.

---
[[2026-1101-newapi-reasoning-effort-suffix]]
[[2026-1101-newapi-model-rate-limiting]]
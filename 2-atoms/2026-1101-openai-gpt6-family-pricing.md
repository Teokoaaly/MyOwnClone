---
id: 2026-1101-openai-gpt6-family-pricing
type: atom
certainty: solid
sources: [sources/2026-10-28-openai-api-pricing.md]
links: ["[[2026-1101-openai-prompt-caching-pricing]]", "[[2026-1101-openai-regional-residency-pricing]]", "[[2026-1101-openai-batch-processing-pricing]]"]
---
## Claim
OpenAI's gpt-6 family consists of four model variants — gpt-6-astra, gpt-6.1-sol, gpt-6.1-terra, and gpt-6-luna — each offered across four pricing tiers: Standard, Batch, Fast, and Ultrafast. Input and output prices scale significantly across tiers, with Ultrafast costing 6× the Standard rate for input and 6× for output.

## Why It Matters
The tier structure creates a cost-performance tradeoff: Standard tier is suitable for batch workflows and cost-sensitive use cases, Fast mode (formerly Priority) serves real-time interactive needs, and Ultrafast commands a premium for latency-critical applications. The 4×–6× price gap between tiers means tier selection has a larger financial impact than model variant selection within the same tier.

## [FRICTION]
> [[2026-1101-openai-prompt-caching-pricing]] notes that prompt caching carries its own separate pricing per tier, which means a model's cached input rate depends on the chosen tier — a detail not always visible when comparing base input/output rates alone. Additionally, the gpt-6.1-sol model appears across all four tiers with consistent relative pricing, but the gpt-6-luna entry-level model's 10% regional data residency uplift (see [[2026-1101-openai-regional-residency-pricing]]) applies uniformly, making the effective floor price tier-dependent rather than model-dependent.
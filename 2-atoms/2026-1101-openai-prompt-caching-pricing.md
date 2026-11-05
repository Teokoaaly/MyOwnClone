---
id: 2026-1101-openai-prompt-caching-pricing
type: atom
certainty: solid
sources: [sources/2026-10-28-openai-api-pricing.md]
links: ["[[2026-1101-openai-gpt6-family-pricing]]", "[[2026-1101-openai-regional-residency-pricing]]", "[[2026-1101-openai-batch-processing-pricing]]"]
---
## Claim
OpenAI applies per-tier prompt caching pricing across all gpt-6 family models and gpt-6.1 variants. Cached input is always cheaper than fresh input, with the discount ratio preserved across tiers: 10× cheaper than standard input in Standard tier, 5× in Batch, 5× in Fast, and 6× in Ultrafast. The 30-minute write window and 12-hour write window pricing also scales tier-proportionally.

## Why It Matters
For workloads with repetitive prompt patterns, enabling prompt caching can reduce effective input costs by 5×–10× depending on the tier. However, the caching discount interacts with tier selection: choosing Ultrafast for latency while relying on caching produces the highest absolute savings but at a higher base rate, whereas Standard tier with caching offers the lowest effective cost for batch-visible prompts. The 30-minute and 12-hour write optimizations are most valuable when paired with the appropriate tier for the workload pattern.

## [FRICTION]
> [[2026-1101-openai-gpt6-family-pricing]] lists base input/output rates per tier, but the cached input rates are published in a separate pricing matrix that requires cross-referencing the tier column. This separation creates friction when estimating total cost for cached workloads: a user comparing Ultrafast vs Standard must mentally adjust both the base rate and the cached discount, and the 30m/12h write window prices add a third dimension. The friction is amplified because the cached input row does not always align visually with the base input row in the published tables.
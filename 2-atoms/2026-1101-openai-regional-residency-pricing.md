---
id: 2026-1101-openai-regional-residency-pricing
type: atom
certainty: solid
sources: [sources/2026-10-28-openai-api-pricing.md]
links: ["[[2026-1101-openai-gpt6-family-pricing]]", "[[2026-1101-openai-prompt-caching-pricing]]", "[[2026-1101-openai-batch-processing-pricing]]"]
---
## Claim
OpenAI charges a 10% uplift for regional processing (data residency) endpoints on models released on or after March 5, 2026. This applies to gpt-6 family models (gpt-6-astra, gpt-6.1-sol, gpt-6.1-terra, gpt-6-luna) as well as gpt-6.1-sol, gpt-6.1-terra, and gpt-6-luna. The uplift is applied to both input and output rates when using a data residency endpoint in a supported region.

## Why It Matters
For global applications requiring data to remain within specific jurisdictions, the 10% uplift is an additional cost factor on top of the base tier pricing. This is particularly relevant for enterprises with compliance requirements in regions like the EU, where data residency is mandated. The uplift applies uniformly across all four gpt-6 tiers, meaning the percentage hit is constant but the absolute dollar impact scales with the tier's base rate.

## [FRICTION]
> [[2026-1101-openai-gpt6-family-pricing]] presents base rates without the regional uplift, so cost comparisons across regions require mentally adding 10% to the endpoint price. The friction increases when mixing regional and non-regional endpoints in the same workflow, as the pricing calculator must track which tier×region combination applies at each step. Additionally, the uplift announcement references "models released on or after March 5, 2026," which creates a cutoff boundary — gpt-6-luna (released before that date) may avoid the uplift while gpt-6-astra (released after) incurs it, unless the capture date and model release dates are verified explicitly.
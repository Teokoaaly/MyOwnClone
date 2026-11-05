---
id: 2026-10-28-xai-regional-endpoint-pricing
type: atom
certainty: solid
sources: [sources/2026-10-28-xai-api-pricing.md]
links: ["[[2026-1101-openai-regional-residency-pricing.md]]", "[[2026-1023-priceai-grok-x-subscription-cuatro-escalones]]"]
---

## Claim
xAI's US Regional Endpoint pricing is 1.1x the global token rates, applying to input, output, and cached input tokens including long-context rates, but only for grok-4.7 and grok-4.6; the global endpoint https://api.x.ai/v1 serves all models while the US endpoint https://us.api.x.ai/v1 is limited to grok-4.7 and grok-4.6 only, and prompt caching discounts are applied before the 1.1x multiplier.

## Why It Matters
The 1.1x regional premium is modest but non-trivial for high-volume workloads, and the model restriction (only grok-4.7 and grok-4.6 on US endpoint) forces users needing other models to use the global endpoint. For US-based workloads requiring low latency, the tradeoff is between the 1.1x cost premium and reduced latency; for other models, the global endpoint is the only option regardless of location. Compared to OpenAI's regional residency pricing which varies by country and can offer discounts, xIA's US-specific 1.1x surcharge is simpler but less flexible.

[[2026-1101-openai-regional-residency-pricing.md]]
[[2026-1023-priceai-grok-x-subscription-cuatro-escalones]]
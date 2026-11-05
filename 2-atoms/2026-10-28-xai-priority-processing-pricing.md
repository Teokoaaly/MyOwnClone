---
id: 2026-10-28-xai-priority-processing-pricing
type: atom
certainty: solid
sources: [sources/2026-10-28-xai-api-pricing.md]
links: ["[[2026-1101-openai-batch-processing-pricing.md]]", "[[2026-1023-priceai-grok-x-subscription-cuatro-escalones]]"]
---

## Claim
xAI Priority Processing charges a 2x premium over standard token rates for text requests, applied after prompt caching discounts, with higher scheduling priority and lower latency; requests confirmed at the priority tier are billed at 2x, while those served at the default tier revert to standard rates, and priority is only available for Chat Completions and Responses endpoints, not image/video or Batch API.

## Why It Matters
The 2x multiplier means latency-sensitive applications can pay significantly more to reduce wait time, but the fallback to standard rates if the default tier serves means cost predictability requires monitoring the service_tier field. For caching users, the order matters: prompt caching discounts apply before the 2x multiplier, so cached priority requests pay less than 2x the discounted standard rate. Compared to OpenAI's priority pricing (which also uses a multiplier model), xAI's approach is simpler but the 2x flat rate is higher than OpenAI's variable premiums.

[[2026-1101-openai-batch-processing-pricing.md]]
[[2026-1023-priceai-grok-x-subscription-cuatro-escalones]]
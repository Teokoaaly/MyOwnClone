---
id: 2026-1028-anthropic-models-usage
type: atom
certainty: solid
sources: [raw/2026-10-28-anthropic-plans-pricing.md]
links: ["[[2026-1028-anthropic-free-pro-max]]"]
---

## Claim

The models and usage section outlines model availability by plan: Free includes Haiku and Sonnet via usage credits (no credits listed), Pro adds usage credits and $0 New API credits, Max adds $100/month (5x) or $200/month (20x) in API credits, and Team adds up to $500/month in pooled API credits. All plans include Haiku, Sonnet, and Opus (via usage credits or API credits). Context window is "Up to 1M varies by model" across all plans. Usage credits and API credits are the mechanism through which higher-tier plans deliver increased capacity.

## Why It Matters

The credit-based system ties dollar value to token consumption, making cost planning dependent on expected usage patterns. The distinction between "usage credits" (internal platform usage) and "API credits" (external platform access) is not consistently clarified across plans. The $100–$200 API credits included with Max and $500 with Team represent significant added value for developers building on the platform, but the conversion rate or quota mechanism between credits and actual token throughput is not described.

## [FRICTION]

> The "Fable" entry in the models table shows "$0.25/MTok Read, $12.50/MTok Write" for Max 5x and "$0.20/MTok Read, $5/MTok Write" for Max 20x — the pricing difference between 5x and 20x tiers is marginal on write operations ($12.50 vs $5) but significant on read operations ($0.25 vs $0.20). This pricing granularity suggests the 5x/20x distinction is primarily about usage quotas, not per-token pricing, yet the table does not explicitly state this.

> "Usage creditsMore information" appears as a yes/no feature with "More information" links, but the actual content behind those links (how credits are earned, converted, or capped) is not accessible from the pricing page. A user cannot determine their effective per-token cost without external research.

> The context window "Up to 1M varies by model" claim is technically true but practically unhelpful: a user needs to know which model supports how much of the 1M tokens, whether context windows count across sessions, and what happens when the window is exceeded. None of these boundaries are on the pricing page.

> Free plan includes Haiku and Sonnet but provides "No" for usage credits — yet the feature comparison also shows "Yes" for usage credits under Pro. The transition from "no credits" to "yes credits" with no dollar amount listed for Free creates a gap: does Free have a credit system at all, and if so, what is the budget?
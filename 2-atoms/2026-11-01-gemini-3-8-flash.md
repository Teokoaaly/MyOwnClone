---
id: 2026-11-01-gemini-3-8-flash
type: atom
certainty: solid
sources: [sources/2026-10-28-gemini-api-pricing.md]
links: [[2-atoms/2026-11-01-gemini-pricing-features]]
---

## Claim
Gemini 3.8 Flash is Google's most intelligent Flash model, engineered for long-horizon software engineering, autonomous agents, and complex enterprise workflows. It slots below Gemini 4 Argon as the most capable Flash model but above Gemini 3.6 Flash and the 3.5 series.

## Pricing
- Input: Free of charge (Free Tier); Paid Tier: $0.75 per 1M tokens through December 31, 2026; $1.50 starting January 1, 2027
- Output (including thinking tokens): Free of charge (Free Tier); Paid Tier: $3.75 per 1M tokens through December 31, 2026; $7.50 starting January 1, 2027
- Context caching: $0.075 per 1M tokens through December 31, 2026; $0.15 starting January 1, 2027; $0.50 / 1M tokens/hour (storage) through December 31, 2026; $1.00 starting January 1, 2027
- Grounding with Google Search*: 5,000 free search requests per month (shared across all Gemini 3+ models), then $14 per 1,000 requests
- Grounding with Google Maps*: 5,000 requests per month (free, shared), then $14 / 1,000 search queries
- Used to improve products: Yes (contributor tier); Used to improve products (output): No

## Free Tier limits
- Input: Free of charge
- Output: Free of charge
- Context caching: Free of charge (up to implied limits)

## Why It Matters
Flash sits at the sweet spot of capability/cost for most enterprise agentic workloads. Its thinking token support and batch/flex/priority pricing tiers make it versatile. The free tier makes it accessible for development and low-volume production. The December 2026 price increase signals Google's confidence in the model's market position.

## [FRICTION]
> The 5,000 free grounding search requests per month are shared across ALL Gemini 3+ models (Argon, Flash, Pro, Nano, etc.). In a mixed-model workflow where Argon handles reasoning and Flash handles retrieval/grounding, the rate limit is a pooled resource. Heavy Argon usage for grounded queries could starve Flash of grounding capacity, creating an implicit coordination friction between models in the same organization.
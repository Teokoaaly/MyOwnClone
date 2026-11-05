---
id: 2026-11-01-gemini-2-5-flash
type: atom
certainty: solid
sources: [sources/2026-10-28-gemini-api-pricing.md]
links: [[2-atoms/2026-11-01-gemini-pricing-features]]
---

## Claim
Gemini 2.5 Flash is the first hybrid reasoning model from Google which supports a 1M token context window and thinking budgets. It balances speed and multimodal capabilities across general agentic and everyday tasks.

## Pricing
- Input: Free of charge (Free Tier); Paid Tier: $0.30 per 1M tokens (text/image/video); $1.00 per 1M tokens (audio)
- Output (including thinking tokens): Free of charge (Free Tier); Paid Tier: $2.50 per 1M tokens
- Context caching: $0.03 per 1M tokens (text/image/video); $0.10 per 1M tokens (audio); $1.00 / 1M tokens/hour (storage) 
- Grounding with Google Search: Free of charge, up to 500 RPD (limit shared with Flash-Lite RPD); 1,500 RPD (free, limit shared with Flash-Lite RPD), then $35 / 1,000 grounded prompts
- Grounding with Google Maps: 500 RPD; 1,500 RPD (free), then $25 / 1,000 grounded prompts
- Used to improve products: Yes (contributor tier); Used to improve products (output): No

## Key Features
- 1M token context window
- Thinking budgets (controlled reasoning)
- First Gemini model with Google Search grounding at no cost up to 500 RPD
- Shared rate limits with Flash-Lite (500 RPD limit)

## Why It Matters
Flash's 1M context window and thinking budgets make it the first Gemini model capable of truly long-horizon reasoning workloads. The free-tier grounding (up to 500 RPD) is a unique differentiator among Gemini models. The shared RPD limit with Flash-Lite creates a coordination friction: users grounding at >500 RPD must upgrade from Flash-Lite to Flash, creating an explicit upgrade path based on retrieval needs.

## [FRICTION]
> The 500 RPD free grounding limit is shared between Gemini 2.5 Flash and Gemini 3.5 Flash-Lite. In mixed-workflows, grounding heavy use on Flash depletes the shared pool, leaving Flash-Lite without grounding capability until the next monthly reset. This creates an explicit dependency: any application needing >500 RPD of Google Search grounding must use Flash (not Flash-Lite), increasing minimum monthly costs by ~$35 per 1,000 grounded prompts beyond the free limit.
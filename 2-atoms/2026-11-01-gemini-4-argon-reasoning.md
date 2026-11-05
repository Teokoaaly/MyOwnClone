---
id: 2026-11-01-gemini-4-argon-reasoning
type: atom
certainty: solid
sources: [sources/2026-10-28-gemini-api-pricing.md]
links: [[2-atoms/2026-11-01-gemini-pricing-features]]
---

## Claim
Gemini 4 Argon is the flagship reasoning model built for complex software engineering, deep mathematical and scientific problem solving, autonomous multi-step agents, and long-decode generation up to 1M tokens. It is Google's most capable model for agentic workflows and multi-step reasoning.

## Pricing
- Input: Not available (Free Tier: limited access); Paid Tier: $2.00 per 1M tokens through November 30, 2026; $4.00 starting December 1, 2026
- Output (including thinking tokens): Not available (Free Tier: limited access); Paid Tier: $10.00 per 1M tokens through November 30, 2026; $20.00 starting December 1, 2026
- Context caching: $0.10 per 1M tokens through November 30, 2026; $0.20 starting December 1, 2026 (implicit caching only, explicit caching not supported)
- Grounding with Google Search*: 5,000 free search requests per month (shared across all Gemini 3+ models), then $14 per 1,000 requests
- Grounding with Google Maps*: 5,000 requests per month (free, shared), then $14 / 1,000 search queries
- Used to improve products: No

## Why It Matters
Argon replaces Gemini 2.5 Pro as Google's top-tier reasoning model. Its 1M token context window and agentic capabilities make it suitable for autonomous multi-step agents and complex code generation. The pricing positions it above Gemini 3.8 Flash in the reasoning hierarchy, with input/output costs reflecting its superior capabilities. The lack of free tier for input/output suggests it's targeted at production workloads from the start.

## [FRICTION]
> The "Not available" Free Tier status for Argon creates a gap with Gemini 3.8 Flash which offers Free Tier access to certain models. Users upgrading from Flash to Argon for reasoning workloads face an immediate cost floor of $2.00/1M input tokens, whereas Flash had free access. This may slow adoption for experimental developers. The context caching model (implicit only, no explicit) also differs from Flash's more flexible caching options, requiring workflow adjustments for long-context applications.
>
> *Grounding with Google Search* shared across all Gemini 3+ models creates a friction point: rate limits are pooled model-wide, so heavy Argon usage for grounded reasoning may deplete the 5,000 free search requests needed for other models like Flash or Pro.
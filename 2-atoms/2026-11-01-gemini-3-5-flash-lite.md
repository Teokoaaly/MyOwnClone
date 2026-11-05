---
id: 2026-11-01-gemini-3-5-flash-lite
type: atom
certainty: solid
sources: [sources/2026-10-28-gemini-api-pricing.md]
links: [[2-atoms/2026-11-01-gemini-pricing-features]]
---

## Claim
Gemini 3.5 Flash-Lite is a cost-efficient model optimized for high-volume agentic tasks, translation, and simple data processing. It is the most affordable entry point into the Gemini API family.

## Pricing
- Input: Free of charge (Free Tier); Paid Tier: $0.10 per 1M tokens (text/image/video/audio) 
- Output (including thinking tokens): Free of charge (Free Tier); Paid Tier: $0.25 per 1M tokens
- Context caching: Not available
- Grounding with Google Search*: Not available (blocked for Flash-Lite)
- Grounding with Google Maps*: Not available (blocked for Flash-Lite)
- Used to improve products: Yes (contributor tier); Used to improve products (output): No

## Why It Matters
Flash-Lite's ultra-low price makes it viable for mass-scale agentic workflows, batch processing, and applications where token volume drives costs. The lack of context caching and grounding grounding limits its use to simple, non-retrieval tasks. Its audio pricing (same rate as text/image/video) simplifies billing for multimodal applications.

## [FRICTION]
> Flash-Lite completely lacks both context caching and Google Search grounding — a significant friction point for RAG (Retrieval-Augmented Generation) workloads. Applications that need grounding must either upgrade to Flash (which includes both features) or accept that Flash-Lite is strictly for stateless, non-retrieval generation. This forces a model-tier decision boundary: any application requiring grounding must run at a higher cost tier than Flash-Lite's price point would suggest.
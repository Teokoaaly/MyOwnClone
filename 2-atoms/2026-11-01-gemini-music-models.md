---
id: 2026-11-01-gemini-music-models
type: atom
certainty: solid
sources: [sources/2026-10-28-gemini-api-pricing.md]
links: [[2-atoms/2026-11-01-gemini-pricing-features]]
---

## Claim
Gemini Lyria models are Google's music generation family: Lyria 3.5 (full song) and Lyria 3 (clip preview/pro preview). Pricing is per request/song rather than per token.

## Pricing — Lyria 3.5
- Full Song: Not available; $0.08 per song (Paid Tier, per request in USD)
- Used to improve products: Yes; output: No

## Pricing — Lyria 3 Clip Preview (30s)
- Not available; $0.04 per song (Per request in USD)

## Pricing — Lyria 3 Pro Preview (Full Song)
- Not available; $0.08 per song (Per request in USD)

## Why It Matters
Lyria models price per complete song regardless of length, making them predictable for music generation workloads. The per-request pricing model is distinct from the per-token model used by text/voice generations. Lyria 3.5 at $0.08/song is positioned as a premium music generation API, suitable for content creation, background music, and AI-assisted composition.

## [FRICTION]
> The per-song pricing model creates cost uncertainty for longer compositions: a 5-minute song and a 2-minute song both count as "one song" at $0.08, but the token consumption and generation compute cost differ significantly. Users extending songs via multiple API calls or iterative generation may incur unexpected multipliers. No context caching or grounding features are available, limiting use to standalone music generation rather than retrieval-augmented composition.
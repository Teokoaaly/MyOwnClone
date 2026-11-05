---
id: 2026-10-28-xai-imagine-api-pricing
type: atom
certainty: solid
sources: [sources/2026-10-28-xai-api-pricing.md]
links: ["[[2026-1028-anthropic-api-pricing.md]]", "[[2026-1023-priceai-grok-x-subscription-cuatro-escalones]]"]
---

## Claim
The xAI Imagine API charges per image from $0.002 to $0.08 depending on model (grok-imagine-image-2.0 vs grok-imagine-image) and resolution, with video generation ranging from $0.01/sec (480p) to $0.25/sec (1080p); the grok-imagine-image-quality model adds $0.01-$0.07 per image for quality enhancement, and the grok-imagine-video-1.5-lite offers a discounted video rate at $0.01/img / $0.02/sec.

## Why It Matters
Image and video generation are priced per-image or per-second, making cost scale directly with media duration and resolution. The wide resolution range (1K-2K) and quality tiers mean a single high-res video can cost significantly more than a low-res static image. Compared to Anthropic's per-token vision pricing, xIA's per-image model is better suited for batch media production but harder to estimate for open-ended creative workflows.

[[2026-1028-anthropic-api-pricing.md]]
[[2026-1023-priceai-grok-x-subscription-cuatro-escalones]]
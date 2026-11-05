---
id: 2026-11-01-gemini-image-models
type: atom
certainty: solid
sources: [sources/2026-10-28-gemini-api-pricing.md]
links: [[2-atoms/2026-11-01-gemini-pricing-features]]
---

## Claim
Gemini image generation models (3.1 Flash Image, 3.1 Flash Lite Image, 3 Pro Image, 2.5 Flash Image, 2.5 Flash Preview TTS family) are native image generation models optimized for speed, flexibility, and contextual understanding.

## Pricing — Gemini 3.1 Flash Image (Nano Banana 2)
- Input price: Not available; $0.50 (text/image)
- Output price: Not available; $3.00 (text and thinking); $60.00 (images)
  — Equivalent to $0.045 per 1K image*; $0.067 per 2K image*; $0.101 per 4K image*
  — 1K (1024x1024px) consumes 1120 tokens; 2K (2048x2048px) consumes 1680 tokens; 4K (4096x4096px) consumes 3780 tokens
- Grounding with Google Web and Image Search*: Not available; 5,000 free search requests/mo, then $14 per 1,000 requests for text and image-based grounding
- Used to improve products: Yes

## Pricing — Gemini 3.1 Flash Lite Image (Nano Banana 2 Lite)
- Input price: Not available; $0.25 (text/image/video)
- Output price: Not available; $1.50 (text and thinking); $30.00 (images)
  — Equivalent to $0.0336 per 1K resolution image*
  — 1K (1024x1024px) consumes 1120 tokens; equivalent to $0.0336 per image
- Used to improve products: Yes

## Pricing — Gemini 3 Pro Image (Nano Banana Pro)
- Input price: Not available; $2.00 (text/image), equivalent to $0.0011 per image*
- Output price: Not available; $12.00 (text and thinking); $120.00 (images)
  — Equivalent to $0.134 per 1K/2K image*; $0.24 per 4K image*
  — 1K (1024x1024px) and 2K (2048x2048px) consume 1120 tokens; 4K (4096x4096px) consumes 2000 tokens
- Used to improve products: Not available

## Pricing — Gemini 2.5 Flash Image (Nano Banana)
- Input price: Not available; $0.30 (text/image)
- Output price: Not available; $0.039 per image*
- Image output priced at $30 per 1M tokens (Standard); 1290 tokens per 1K image at Standard

## Why It Matters
Image models price per-output-image rather than per-token, with token consumption varying by resolution. The "Nano Banana" branding (2.5, 3.1) indicates generation quality tiers. 3 Pro Image is the highest quality but most expensive, while 2.5 Flash Image is the most cost-effective for production. Output token consumption (1120 for 1K, 1680 for 2K, 3780 for 4K in 3.1 Flash Image; 1120 for 1K/2K, 2000 for 4K in 3 Pro Image) is the key variable for cost modeling.

## [FRICTION]
> The per-image pricing model creates cost surprise for high-resolution generation: 4K images consume 3.4x more tokens than 1K in 3.1 Flash Image (3780 vs 1120), translating to $0.101 vs $0.045 per image — a 124% cost increase for quadrupling linear resolution. The "equivalent to $0.0336 per 1K image" metric for 3.1 Flash Lite Image masks the 2K/4K price jumps ($0.0504 and $0.113 respectively). Users budgeting for product imagery must explicitly model resolution tiers, as defaulting to the per-1K metric significantly understates 4K generation costs.
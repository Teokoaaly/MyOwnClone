---
id: 2026-11-01-gemini-embedding-2
type: atom
certainty: solid
sources: [sources/2026-10-28-gemini-api-pricing.md]
links: [[2-atoms/2026-11-01-gemini-pricing-features]]
---

## Claim
Gemini Embedding 2 is the first multimodal embedding model from Google, mapping text, images, video, audio, and PDFs into a unified embedding space. It supports retrieval, similarity search, and clustering across modalities.

## Pricing
- Text input price: Free of charge (Free Tier); Paid Tier: $0.20 per 1M tokens
- Image input price: Free of charge (Free Tier); Paid Tier: $0.45 per 1M tokens ($0.00012 per image)
- Audio input price: Free of charge (Free Tier); Paid Tier: $6.50 per 1M tokens ($0.00016 per second)
- Video input price: Free of charge (Free Tier); Paid Tier: $12.00 per 1M tokens ($0.00079 per frame)
- Used to improve products: Yes (contributor tier for input); No for output

## Why It Matters
Embedding 2's multimodal capability enables cross-modal retrieval: searching images with text queries, finding relevant audio clips, or clustering PDF documents by content. The unified embedding space means embeddings from different modalities can be compared directly in the same vector space. The per-image and per-second pricing makes it cost-effective for batch image embedding and audio feature extraction.

## [FRICTION]
> The audio input pricing of $0.00016/second means that just 10 minutes of audio = 600 seconds × $0.00016 = $0.096, while 10 minutes at 25 tokens/sec = 15,000 tokens × ($6.50/1M) = $0.0975 — the two pricing models converge near the 10-minute mark. This convergence point is unintuitive: users converting between seconds and tokens may miscalculate costs by 2x for short audio clips or 0.5x for very long clips.
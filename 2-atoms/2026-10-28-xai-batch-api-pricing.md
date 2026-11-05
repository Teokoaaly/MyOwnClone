---
id: 2026-10-28-xai-batch-api-pricing
type: atom
certainty: solid
sources: [sources/2026-10-28-xai-api-pricing.md]
links: ["[[2026-1101-openai-batch-processing-pricing.md]]", "[[2026-1023-priceai-grok-x-subscription-cuatro-escalones]]"]
---

## Claim
The xAI Batch API offers a flat 20% discount on all token types (input, output, cached, reasoning) for grok-4.7, grok-4.6, grok-4.5, grok-4.3, and the grok-4.20-0309 reasoning/non-reasoning variants, with most batches completing within 24 hours; batch requests don't count toward rate limits, and image/video generation in batch is billed at standard rates without discount.

## Why It Matters
A 20% discount on long-running workloads makes the Batch API attractive for bulk processing, but the 24-hour latency and lack of image/video discount limit its use cases. Since batch requests exempt from rate limits, users can scale volume beyond per-minute caps, though the delay makes it unsuitable for real-time applications. Compared to OpenAI's batch pricing (which varies by model and can reach 50% discount), xAI's fixed 20% across all listed models is simpler but less aggressive.

[[2026-1101-openai-batch-processing-pricing.md]]
[[2026-1023-priceai-grok-x-subscription-cuatro-escalones]]
---
id: 2026-1028-xai-priority-processing
type: atom
certainty: solid
sources: [sources/2026-10-28-xai-models.md]
links: ["[[2026-1028-xai-grok47-flagship]]", "[[2026-1028-xai-batch-discount]]"]
---

## Claim
Priority Processing gives text requests higher scheduling priority for lower latency, billed at a 2x premium over standard rates. It is available for Chat Completions and Responses endpoints only, not for image generation, video generation, or Batch API requests. A request is only billed at the priority rate when the response confirms `"service_tier": "priority"`; otherwise standard rates apply.

## Why It Matters
When sub-second latency is required, Priority Processing can reduce wait times at the cost of doubling token prices. Prompt caching discounts are applied before the 2x multiplier, so cached requests still benefit from prior savings. This is the only way to accelerate Grok 4.7 and grok-4.6 beyond standard scheduling, making it critical for time-sensitive applications, though the 2x premium makes it expensive for high-throughput workloads.

## [FRICTION]
> [[2026-1028-xai-batch-discount]] reduces cost for asynchronous workloads, while [[2026-1028-xai-priority-processing]] increases cost for synchronous latency. Both address different timing needs: batch for throughput, priority for latency. Marcado para juicio humano, no auto-resuelto.
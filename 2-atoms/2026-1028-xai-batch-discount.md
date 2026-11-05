---
id: 2026-1028-xai-batch-discount
type: atom
certainty: solid
sources: [sources/2026-10-28-xai-models.md]
links: ["[[2026-1028-xai-grok47-flagship]]", "[[2026-1028-xai-model-aliases]]"]
---

## Claim
The Batch API offers a 20% discount on standard rates for Grok 4.7 and related models (grok-4.6, grok-4.5, grok-4.3, grok-4.20-0309-reasoning, grok-4.20-0309-non-reasoning), enabling cost-effective processing of large-volume requests queued and processed asynchronously, typically within 24 hours.

## Why It Matters
At a flat 20% discount across all token types (input, output, cached, and reasoning), the Batch API can substantially reduce costs for workloads like bulk summarization, code generation, or batch classification. Requests don't count toward rate limits, and most complete within 24 hours. However, batch requests are not suitable for real-time use cases — latency is typically 24 hours or more. This discount applies only to text and language models; image and video generation in the Batch API are billed at standard rates.

## [FRICTION]
> [[2026-1028-xai-model-aliases]] auto-migrates users to the latest stable model version, which could change batch pricing and discount eligibility over time. Without pinning a specific `<modelname>-<date>` alias, batch cost projections may drift. Marcado para juicio humano, no auto-resuelto.
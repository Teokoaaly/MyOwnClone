---
id: 2026-1028-anthropic-batch
type: atom
certainty: solid
sources: [raw/2026-10-28-anthropic-api-pricing.md]
links: ["[[2026-1028-anthropic-api-pricing]]", "[[2026-1028-anthropic-model-pricing]]"]
---
## Claim
Anthropic batch processing pricing offers reduced per-MTok rates for submitted batch jobs, at the cost of increased latency. Batch requests are processed asynchronously with a delay that varies by queue depth. The batch discount is most significant for high-volume, non-interactive workloads where latency is not a constraint.

## Why It Matters
Batch processing can reduce per-MTok costs by 25-50% compared to real-time pricing, making it ideal for background jobs, report generation, and model fine-tuning data processing. However, the latency penalty (hours vs. seconds) means batch is unsuitable for interactive applications. Teams should route non-urgent workloads to batch mode and keep interactive requests on the real-time path, creating a two-tier cost structure.
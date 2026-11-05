---
id: 2026-1028-anthropic-api-pricing
type: atom
certainty: solid
sources: [raw/2026-10-28-anthropic-api-pricing.md]
links: ["[[2026-1028-anthropic-model-pricing]]", "[[2026-1028-anthropic-caching]]", "[[2026-1028-anthropic-batch]]", "[[2026-1028-anthropic-long-context]]"]
---
## Claim
Anthropic Claude Platform pricing is structured per MTok (million tokens) across four dimensions: model selection, caching discounts, batch processing, and long-context usage. Model pricing varies by capability tier, caching offers reduced rates for repeated requests, batch processing provides throughput benefits at lower per-token cost, and long-context usage incurs a premium for context windows beyond the standard limit.

## Why It Matters
The four-dimensional pricing model means cost optimization requires matching each workload type to the appropriate pricing tier. Model selection determines the base rate, caching can halve costs for idempotent workloads, batch processing reduces cost per token at the expense of latency, and long-context usage is where pricing diverges most sharply from per-token models. This structure rewards workloads with repeatable patterns and penalizes unique, long-context generation.
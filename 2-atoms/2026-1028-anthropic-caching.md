---
id: 2026-1028-anthropic-caching
type: atom
certainty: solid
sources: [raw/2026-10-28-anthropic-api-pricing.md]
links: ["[[2026-1028-anthropic-api-pricing]]", "[[2026-1028-anthropic-model-pricing]]"]
---
## Claim
Anthropic offers caching discounts for repeated requests, with reduced per-MTok rates for requests that match prior inputs. Caching is most effective for workloads with high request repetition, such as RAG systems, chat interfaces with persistent context, and code completion. The cache hit rate directly determines the effective per-token cost reduction.

## Why It Matters
Caching can reduce effective per-MTok costs by 50% or more for repetitive workloads. For multi-tenant platforms, caching is a key margin protection mechanism — the platform absorbs the cache cost once and serves many tenants from the same cached context. Teams should design prompt architectures with caching in mind, grouping similar queries and preserving context across user sessions.
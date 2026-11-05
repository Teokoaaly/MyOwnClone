---
id: 2026-10-29-vectorize
type: atom
certainty: solid
sources: ["0-raw/2026-10-29-cloudflare-workers-pricing.md"]
links: ["[[2026-10-29-workers-ai]]", "[[2026-10-29-stream-sql-transforms]]"]
---

## Claim

Vectorize vector search costs $0.01 per million dimensions queried after 30M dimensions per month are free.

## Why It Matters

Vectorize adds vector search to the Workers platform. The 30M/month free tier covers moderate vector search workloads, and at $0.01/M queried dimensions it is very affordable for semantic search, RAG, and similarity applications. Beyond the free tier, cost scales with search volume and dimensionality.

## [FRICTION]

> [[2026-10-29-workers-ai]] charges $0.011/K neurons for model inference, while [[2026-10-29-vectorize]] charges $0.01/M dimensions queried for vector search. Both are AI-related Workers services with different pricing models: neurons measure model size/capacity while dimensions measure query volume. A RAG pipeline using both would pay neuron costs for the LLM plus vector search costs for embedding retrieval, with the vector search typically being the lower-cost component.
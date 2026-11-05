---
id: 2026-10-28-xai-files-collections-pricing
type: atom
certainty: solid
sources: [sources/2026-10-28-xai-api-pricing.md]
links: ["[[2026-1101-openai-regional-residency-pricing.md]]", "[[2026-1023-priceai-grok-x-subscription-cuatro-escalones]]"]
---

## Claim
xAI charges $0.025/GiB/day for file storage and $0.10/GiB/day for collection storage, with downloads costing $0.20/GiB downloaded for both files and collections; storage is continuous (billed daily) while downloads are one-time per GiB, and collections (RAG-backed) cost 4x the storage rate of individual files.

## Why It Matters
The 4x storage cost differential between collections and files reflects the RAG overhead of maintaining indexed document collections. For long-term knowledge bases, storage costs can accumulate significantly ($0.025/day = ~$9.13/year per GiB for files, ~$36.50/year per GiB for collections). Download costs of $0.20/GiB mean moving large datasets out of xAI is inexpensive compared to compute costs, but frequent access to large collections can make the storage+download combo non-trivial at scale. Compared to OpenAI's storage pricing (which uses different mechanisms for files and vectors), xIA's per-GiB daily model is straightforward but requires careful capacity planning.

[[2026-1101-openai-regional-residency-pricing.md]]
[[2026-1023-priceai-grok-x-subscription-cuatro-escalones]]
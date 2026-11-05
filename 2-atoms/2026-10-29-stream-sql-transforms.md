---
id: 2026-10-29-stream-sql-transforms
type: atom
certainty: solid
sources: ["0-raw/2026-10-29-cloudflare-workers-pricing.md"]
links: ["[[2026-10-29-data-egress]]", "[[2026-10-29-workers-ai]]"]
---

## Claim

Stream SQL transforms cost $0.04 per GB after 50 GB per month are free.

## Why It Matters

Stream SQL transforms process data streaming pipelines. The 50 GB/month free tier covers moderate ETL workloads, and at $0.04/GB the cost is competitive against alternative streaming processors. Billing is shared across sinks (JSON, Parquet, Iceberg) within the 50 GB pool, making it efficient for multi-destination data pipelines.

## [FRICTION]

> [[2026-10-29-data-egress]] costs $0.05/GB for data egress after 1,000 GB/month free, while [[2026-10-29-stream-sql-transforms]] costs $0.04/GB after 50 GB/month free. Transforms are 20% cheaper per GB but have a much lower free tier (50 GB vs 1,000 GB). A pipeline that processes 60 GB monthly pays $2.40 for transforms (first 50 free, $0.04 × 10) plus $0.50 for egress (first 1,000 free, $0.05 × 60 beyond tier), making transforms the higher-cost component for this volume.
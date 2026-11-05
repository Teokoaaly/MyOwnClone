---
id: 2026-10-29-data-egress
type: atom
certainty: solid
sources: ["0-raw/2026-10-29-cloudflare-workers-pricing.md"]
links: ["[[2026-10-29-stream-sql-transforms]]", "[[2026-10-29-r2-storage]]"]
---

## Claim

Data Egress costs $0.05 per GB after the first 1,000 GB per month are free.

## Why It Matters

Data Egress charges for leaving the Cloudflare network. The 1,000 GB/month free tier is generous and covers most personal and professional workloads. Beyond that, $0.05/GB is competitive against traditional cloud egress rates (which often charge $0.10+/GB), making Cloudflare's network particularly cost-effective for outbound data transfer.

## [FRICTION]

> [[2026-10-29-stream-sql-transforms]] costs $0.04/GB after 50 GB/month free, while [[2026-10-29-data-egress]] costs $0.05/GB after 1,000 GB/month free. For workloads under 50 GB/month, transforms ($0.04/GB) are cheaper than egress ($0.05/GB since no free tier applies until 1,000 GB). For workloads over 1,000 GB/month, egress drops to effectively $0.05/GB while transforms still charge $0.04/GB only after the first 50 GB, making egress the lower-cost component for massive data volumes.
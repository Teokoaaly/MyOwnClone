---
id: 2026-10-29-workers-compute-requests
type: atom
certainty: solid
sources: ["0-raw/2026-10-29-cloudflare-workers-pricing.md"]
links: ["[[2026-10-29-workers-compute-cpu]]", "[[2026-10-29-r2-storage]]"]
---

## Claim

Workers compute costs $0.30 per million requests after the first 100,000 requests per day are free.

## Why It Matters

This is the base compute charge for Workers. Personal projects under 100k daily requests pay $0 for requests, making Workers essentially free for low-traffic use cases. Beyond that threshold, the cost scales linearly at $0.30/M, which is competitive against traditional cloud compute but can add up for high-traffic applications.

## [FRICTION]

> [[2026-10-29-r2-storage]] stores data at $0.015/GB-month after 10 GB-month free, while Workers compute charges $0.30/M requests after 100k/day free. For a workload that serves 1M requests daily with 10 GB of storage, the compute cost alone ($90/month) exceeds the R2 storage cost ($0.15/month), making compute the dominant cost factor rather than storage.
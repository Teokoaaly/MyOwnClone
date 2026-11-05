---
id: 2026-10-29-kv-storage
type: atom
certainty: solid
sources: ["0-raw/2026-10-29-cloudflare-workers-pricing.md"]
links: ["[[2026-10-29-workers-compute-cpu]]", "[[2026-10-29-d1-database]]"]
---

## Claim

KV Storage Standard Operations cost $0.40 per million operations after 10,000 operations per day are included.

## Why It Matters

KV Storage provides ultra-fast key-value access for Workers. The 10K/day included tier covers moderate workloads, and at $0.40/M operations it is competitive for read-heavy patterns. Queries are free (100K/day), but data operations (write/delete/list) incur the per-M charge, shaping the cost model for applications that rely heavily on KV for caching, state, or config.

## [FRICTION]

> [[2026-10-29-d1-database]] charges $0.50/GB-month for stored data plus $0.50/M read requests and $5.00/M write/delete/list requests, while [[2026-10-29-kv-storage]] charges $0.40/M operations with free queries. For a workload storing 10 GB and performing 1M reads and 1M writes monthly, D1 costs $5.00 (storage) + $0.50 (reads) + $5.00 (writes) = $10.50, while KV costs $0.40 × 2 = $0.80 for operations alone — excluding any storage fee that KV may also carry.
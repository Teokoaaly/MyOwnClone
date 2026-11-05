---
id: 2026-10-29-workers-compute-cpu
type: atom
certainty: solid
sources: ["0-raw/2026-10-29-cloudflare-workers-pricing.md"]
links: ["[[2026-10-29-workers-compute-requests]]", "[[2026-10-29-kv-storage]]"]
---

## Claim

Workers compute costs $0.02 per million CPU ms after the first 10 ms per request are free.

## Why It Matters

This CPU time charge applies per request invocation. The 10 ms free tier per request means short-lived handlers often incur no CPU charge. For compute-intensive Workers, the $0.02/M rate is very low — equivalent to ~$0.00002 per ms per million invocations — but can still be significant at massive scale compared to the "free" 10 ms allocation.

## [FRICTION]

> [[2026-10-29-workers-compute-requests]] charges $0.30/M requests regardless of complexity, while [[2026-10-29-workers-compute-cpu]] adds $0.02/M CPU ms on top. A request that uses 100 ms of CPU time instead of 10 ms free would incur both $0.30 for the request plus $0.008 for the extra 90 ms of CPU, making the total cost per request higher than the per-request rate alone suggests.
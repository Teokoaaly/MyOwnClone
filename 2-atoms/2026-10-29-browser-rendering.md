---
id: 2026-10-29-browser-rendering
type: atom
certainty: solid
sources: ["0-raw/2026-10-29-cloudflare-workers-pricing.md"]
links: ["[[2026-10-29-workers-compute-requests]]", "[[2026-10-29-workers-ai]]"]
---

## Claim

Browser Rendering costs $0.09 per hour after 10 minutes per day are free, with 3 concurrent browsers included in the free tier.

## Why It Matter

Browser Rendering provides automated headless browsers at the edge. The 10 min/day free tier covers light testing or automation use cases. At $0.09/hr (or $0.0015/min), it is priced for intermittent use rather than continuous rendering. The 3-browser concurrent limit means multiple isolated sessions require separate paid instances.

## [FRICTION]

> [[2026-10-29-workers-compute-requests]] charges $0.30/M requests for Workers compute, while [[2026-10-29-browser-rendering]] charges $0.09/hr for browser sessions. A workload that runs 100 browser hours monthly ($9.00) and handles 1M requests ($0.30) sees browser costs dominate, but the two services serve completely different use cases — one is for headless rendering, the other for serverless compute.
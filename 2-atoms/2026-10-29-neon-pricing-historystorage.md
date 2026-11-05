---
id: 2026-10-29-neon-pricing-historystorage
type: atom
certainty: solid
sources: [sources/2026-10-29-neon-pricing.md]
links: ["[[2026-10-29-neon-pricing-scaleplan]]", "[[2026-10-29-neon-pricing-functions]]"]
---

## Claim
History storage (instant restore) is billed at $0.20 per GB-month based on the amount of WAL retained within the history window, separate from regular database storage at $0.35/GB-month; the default history window is 1 day on paid plans and can be configured to reduce costs if deep recovery or long Time Travel is not required.

## Why It Matters
For applications that need instant restore to previous database states or Time Travel queries, history storage can become a significant cost component, and shortening the history window is an effective cost optimization when deep recovery is not needed.

## [FRICTION]
> [[2026-10-29-neon-pricing-scaleplan]] includes HIPAA and private network features but does not address whether the default history window changes on the Scale plan versus Launch. If Scale enables a longer default history window (e.g., 7 days vs. 1 day), the $0.20/GB-month history storage cost could be substantially higher for Scale plan databases with large workloads.
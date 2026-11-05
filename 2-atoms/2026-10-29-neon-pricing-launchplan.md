---
id: 2026-10-29-neon-pricing-launchplan
type: atom
certainty: solid
sources: [sources/2026-10-29-neon-pricing.md]
links: ["[[2026-10-29-neon-pricing-cudef]]", "[[2026-10-29-neon-pricing-scaleplan]]"]
---

## Claim
The Launch plan has a typical monthly spend of $15 based on intermittent load with 1 GB of storage, offering $0.106 per CU-hr, $0.35 per GB-month, and compute sizes up to 16 CU (64 GB RAM) with 3-day metrics/logs retention in the UI.

## Why It Matters
This plan bridges the gap between the Free plan's 100 CU-hours/project limit and the Scale plan's higher compute needs, making it suitable for small production applications and databases that need to be always-on for features like real-time sync.

## [FRICTION]
> [[2026-10-29-neon-pricing-cudef]] defines a CU as approximately 4 GB RAM with associated CPU, but the Launch plan's typical $15/mo estimate is based on "Intermittent load, 1 GB" which may assume a minimum 0.25 CU size. If the actual minimum compute size on Launch differs from 0.25 CU, the cost estimation based on CU-hour rates could be off by a factor of up to 4x for always-on databases.
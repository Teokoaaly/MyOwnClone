---
id: 2026-10-29-neon-pricing-cudef
type: atom
certainty: solid
sources: [sources/2026-10-29-neon-pricing.md]
links: ["[[2026-10-29-neon-pricing-freeplan]]", "[[2026-10-29-neon-pricing-launchplan]]"]
---

## Claim
A CU (Compute Unit) is Neon's way of representing Postgres database compute size, where each CU allocates approximately 4 GB of RAM along with associated CPU, and databases autoscale between a minimum and maximum CU based on load.

## Why It Matters
Understanding CUs is essential for cost estimation because CU-hour pricing ($0.106 on Launch, $0.222 on Scale) multiplies the average CU size by the number of hours compute runs, making compute the most variable part of a Neon bill.

## [FRICTION]
> [[2026-10-29-neon-pricing-freeplan]] states the Free plan gives 100 CU-hours per project monthly, but does not clarify whether the Free plan's default compute size is 0.25 CU (as mentioned in the CU-hour explanation section) or a different minimum. These two descriptions of the Free plan's compute baseline could represent different assumptions about minimum database size.
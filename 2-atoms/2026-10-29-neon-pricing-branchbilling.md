---
id: 2026-10-29-neon-pricing-branchbilling
type: atom
certainty: solid
sources: [sources/2026-10-29-neon-pricing.md]
links: ["[[2026-10-29-neon-pricing-scaleplan]]", "[[2026-10-29-neon-pricing-functions]]"]
---

## Claim
Extra branches beyond the plan allowance are billed at $1.50 per extra branch-month (prorated hourly at ~$0.002 per hour), and each project includes 10 branches on Launch and 25 branches on Scale; exceeding these limits incurs charges prorated by hour of existence.

## Why It Matters
Teams running many temporary branches for feature work or experiments can incur unexpected costs if branches are not cleaned up, making branch expiration and automation critical for cost control on paid plans.

## [FRICTION]
> [[2026-10-29-neon-pricing-scaleplan]] includes 25 branches per project at no additional cost, but the myownclone stack (referenced in [[2026-1022-neon-postgres-serverless]]) may create branches more aggressively than a typical development workflow. If myownclone's branch creation pattern exceeds 25 per project, the $1.50/branch-month charge could apply unexpectedly, though the atom does not quantify myownclone's actual branch creation rate.
---
id: 2026-10-29-neon-pricing-maulimit
type: atom
certainty: solid
sources: [sources/2026-10-29-neon-pricing.md]
links: ["[[2026-10-29-neon-pricing-freeplan]]", "[[2026-10-29-neon-pricing-launchplan]]"]
---

## Claim
The Free plan includes Managed Better Auth at no additional cost for up to 60,000 MAU per project, while paid plans include it through 1 million MAU per project before extra charges apply; MAU limits apply separately per project, so multiple Free plan projects can each have up to 60,000 MAU.

## Why It Matters
Applications needing authentication must monitor MAU counts carefully, as exceeding the Free plan's 60,000 MAU per project limit requires either upgrading to a paid plan or managing MAU distribution across multiple projects.

## [FRICTION]
> [[2026-10-29-neon-pricing-launchplan]] does not specify whether the 1M MAU inclusion on paid plans is per project or aggregated across projects in a database. If 1M MAU is aggregated across all projects in a single database, a single project on Scale could exceed the limit and face charges sooner than expected; if per-project, the limit is more forgiving for multi-project setups.
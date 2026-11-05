---
id: 2026-10-29-neon-pricing-objectstorage
type: atom
certainty: solid
sources: [sources/2026-10-29-neon-pricing.md]
links: ["[[2026-10-29-neon-pricing-functions]]", "[[2026-10-29-neon-pricing-branchbilling]]"]
---

## Claim
Object Storage is billed at $0.023 per GB-month of stored volume with no per-operation charge, and Egress counts toward public network transfer allowance; the Free plan includes 5 GB of Object Storage per project, and Object Storage costs are separate from CU-hours which measure only Postgres database compute.

## Why It Matters
Applications storing files, backups, or user-generated content in Neon Object Storage should account for $0.023/GB-month in their budgets, and the 5 GB per-project Free allowance can significantly reduce costs for small applications.

## [FRICTION]
> [[2026-10-29-neon-pricing-functions]] includes Functions billing but does not connect Object Storage costs to the Function invocation pattern. Functions that write large files to Object Storage could create storage costs that are not reflected in the Function invocation rates, creating a cost tracking gap between the two billing subsystems.
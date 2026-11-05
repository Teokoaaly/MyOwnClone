---
id: 2026-10-29-neon-pricing-freeplan
type: atom
certainty: solid
sources: [sources/2026-10-29-neon-pricing.md]
links: ["[[2026-1022-neon-postgres-serverless]]", "[[2026-10-29-neon-pricing-cudef]]"]
---

## Claim
The Free plan gives each project 100 CU-hours of database compute per month with automatic scale-to-zero when idle, and compute only runs when a database is actively processing queries.

## Why It Matters
This allows developers to have many small or intermittent databases (for development, demos, previews, or experiments) without being forced into a paid plan, since CU-hours are only consumed during active use and compute scales down to zero when idle.

## [FRICTION]
> [[2026-1022-neon-postgres-serverless]] describes Neon as the managed database for myownclone, but that atom does not address how the 100 CU-hour Free plan allowance scales across multiple projects or interacts with branch compute costs. The friction arises because the source capture shows per-project allowances while the myownclone stack may run multiple projects concurrently.
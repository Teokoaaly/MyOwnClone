---
id: 2026-10-29-neon-pricing-functions
type: atom
certainty: solid
sources: [sources/2026-10-29-neon-pricing.md]
links: ["[[2026-10-29-neon-pricing-scaleplan]]", "[[2026-10-29-neon-pricing-objectstorage]]"]
---

## Claim
Functions are billed for active compute, waiting compute, and invocations at the rates in the plan table, with the Free plan including 10 active capacity-hours, 400 waiting capacity-hours, and 1 million invocations per project per month; active capacity-hours are consumed when a function is running, waiting capacity-hours when idle but warmed, and invocations charge $0.60 per 1M.

## Why It Matters
For applications using Neon Functions as a backend, the cost depends on how often functions are invoked and how long they run per invocation, making it important to disable scale-to-zero only when needed and monitor invocation patterns.

## [FRICTION]
> [[2026-10-29-neon-pricing-scaleplan]] mentions Functions as an included capability but does not specify whether the 1M free invocations/month per project apply on the Scale plan or whether invocation charging begins immediately after the quota is exceeded. The source capture shows Free plan limits but leaves Scale plan invocation policy ambiguous.
---
id: 2026-1029-langfuse-billable-units
type: atom
certainty: solid
sources: [0-raw/2026-10-29-langfuse-pricing.md]
links: ["[[2026-1029-langfuse-graduated-pricing]]", "[[2026-1029-langfuse-hobby-tier]]"]
---

## Claim
In Langfuse, a billable unit is any tracing data point sent to the platform, including complete traces (application interactions), individual observations (spans, events, and generations), and evaluation scores, with the included quota varying by plan (Hobby: 50k, Core/Pro/Enterprise: 100k units/month).

## Why It Matters
Understanding what constitutes a billable unit is essential for cost estimation and optimization, since the included quota and overage rates directly determine the monthly bill. A project's unit consumption depends on trace granularity, number of generations, and evaluation frequency, making it critical to instrument consciously and monitor usage against plan limits to avoid unexpected overage charges.

## [FRICTION]
The Hobby tier includes 50k units/month while Core/Pro/Enterprise all include 100k units/month, yet Hobby costs $0 and the paid plans start at $29/month. The 2x increase in included units from Hobby to Core does not proportionally increase the value gap — Hobby's 50k may be sufficient for light POC use, but the jump to 100k at $29/month represents a marginal utility increase for a cost that scales with project growth, creating a cost-benefit discontinuity for projects transitioning from experimentation to production.
> [[2026-1029-langfuse-hobby-tier]] includes 50k units/month for free, while Core includes 100k units/month at $29/month. Both cannot be simultaneously optimal for projects growing beyond POC scale. Marcado para juicio humano, no auto-resuelto.
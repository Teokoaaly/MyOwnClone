---
id: 2026-1028-newapi-consumption-mechanism
type: atom
certainty: solid
sources: [0-raw/2026-10-28-newapi-ratio-settings.md]
links: ["[[2026-1028-newapi-quota-formulas]]", "[[2026-1028-newapi-models-without-ratios]]"]
---
## Claim
NewAPI uses a dual billing mechanism of pre-consumption (estimated token count before call) and post-consumption (actual token count after call), with automatic difference adjustment to the user's quota balance.

## Why It Matters
Pre-consumption deducts estimated quota before the API call executes, preventing overruns during the call. Post-consumption recalculates based on actual usage after completion. If actual differs from estimated, the system adjusts the balance automatically. This two-phase approach provides both safety (pre-deduction) and accuracy (true-up after).

## [FRICTION]
> No direct friction with existing atoms. The prior atom [[2026-1023-new-api-precios-por-ratio-y-expresion]] discusses cache-adjusted pricing (`cc12h` = 2.5× for 12h writes) as a post-computation modifier, which is compatible with and distinct from the pre/post-consumption mechanism. One governs base quota calculation; the other adjusts the result for cache write scenarios.
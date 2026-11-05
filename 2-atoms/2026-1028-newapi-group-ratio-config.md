---
id: 2026-1028-newapi-group-ratio-config
type: atom
certainty: solid
sources: [0-raw/2026-10-28-newapi-ratio-settings.md]
links: ["[[2026-1028-newapi-ratio-system]]", "[[2026-1028-newapi-quota-formulas]]"]
---
## Claim
Group ratios in NewAPI differentiate billing multipliers per user group: internal-test at 0.5, standard at 1.0, enterprise-client at 0.8, and trial at 2.0, with group ratio applied multiplicatively on top of the model ratio.

## Why It Matters
Group ratios enable cost allocation, budget control, and enterprise customer billing configuration. A standard user has group ratio 1.0 (no multiplier), an internal-test user pays half the base rate (0.5), an enterprise-client pays 80% (0.8), and a trial user pays double (2.0). This allows a single model configuration to produce different effective rates per segment.

## [FRICTION]
> The prior atom [[2026-1023-new-api-precios-por-ratio-y-expresion]] establishes that group serves as the allocation lever for pricing, stating "el grupo es la palanca de asignación". The three-tier system formalizes this as Model Ratio × Group Ratio within the quota formula, confirming group as a multiplicative factor. No contradiction: the earlier atom describes the operational reality, and this atom documents the formal configuration schema.
---
id: 2026-1028-newapi-ratio-system
type: atom
certainty: solid
sources: [0-raw/2026-10-28-newapi-ratio-settings.md]
links: ["[[2026-1028-newapi-model-ratio-defaults]]", "[[2026-1028-newapi-completion-ratio-defaults]]"]
---
## Claim
NewAPI's billing uses a three-tier ratio system where quota consumption is calculated as Model Ratio × Completion Ratio × Group Ratio, establishing a compound multiplier for all user quota consumption.

## Why It Matters
The three-tier structure separates concerns: model ratios reflect inherent cost differences between AI models, completion ratios balance input vs output token costing, and group ratios enable differentiated billing per user segment. Without this structure, all billing would collapse into a single multiplier losing both model differentiation and group-level control.

## [FRICTION]
> The existing atom [[2026-1023-new-api-precios-por-ratio-y-expresion]] describes ratio pricing coexisting with expression-based pricing (cc/cc1h/cc12h notations). Both mechanisms operate in the NewAPI ecosystem but serve different purposes: the three-tier ratio system calculates quota consumption, while expression-based pricing handles cached write adjustments. No direct contradiction, but operators must distinguish which mechanism applies per billing context.
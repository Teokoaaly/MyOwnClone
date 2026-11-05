---
id: 2026-1028-newapi-quota-formulas
type: atom
certainty: solid
sources: [0-raw/2026-10-28-newapi-ratio-settings.md]
links: ["[[2026-1028-newapi-completion-ratio-defaults]]", "[[2026-1028-newapi-consumption-mechanism]]"]
---
## Claim
NewAPI provides two quota calculation formulas: (1) pay-as-you-go models use (input_tokens + output_tokens × completion_ratio) × model_ratio × group_ratio, and (2) per-call billing models use model_fixed_price × group_ratio × 500,000 quota points per dollar.

## Why It Matters
The pay-as-you-go formula converts token consumption into quota points through the three-tier multiplier, while per-call billing converts a fixed dollar price into quota points using the group ratio and the system's base conversion (1 USD = 500,000 quota points). Understanding which formula applies is essential for accurate quota tracking and cost prediction.

## [FRICTION]
> The prior atom [[2026-1023-new-api-precios-por-ratio-y-expresion]] notes that ratio pricing bills 12-hour writes at twice the cache write ratio, and that GPT models with cache write ratio convert to expressions with `cc12h`. The quota formulas in this atom operate on raw token counts before cache adjustments are applied. Cache notation (`cc12h`, `cc1h`, etc.) modifies the final quota after the three-tier formula computes base consumption. These are sequential stages, not alternative formulas.
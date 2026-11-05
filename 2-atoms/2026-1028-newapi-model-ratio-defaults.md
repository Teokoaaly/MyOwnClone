---
id: 2026-1028-newapi-model-ratio-defaults
type: atom
certainty: solid
sources: [0-raw/2026-10-28-newapi-ratio-settings.md]
links: ["[[2026-1028-newapi-ratio-system]]", "[[2026-1028-newapi-group-ratio-config]]"]
---
## Claim
NewAPI pre-sets default model ratios relative to a base billing unit: gpt-4o at 1.25, gpt-3.5-turbo at 0.25, gpt-4o-mini at 0.075, and o1 at 7.5, reflecting the cost differential of each model class.

## Why It Matters
Model ratios allow the system to charge proportionally more for more expensive models. A ratio of 1.25 means gpt-4o costs 25% more than the base unit, while 0.075 for gpt-4o-mini means it costs roughly 1/13th. Without model ratios, all models would bill at the same rate obscuring the true cost per capability tier.

## [FRICTION]
> The prior atom [[2026-1023-new-api-precios-por-ratio-y-expresion]] cites ratio pricing that bills 12-hour cache writes at twice the cache write ratio, with Claude 1-hour writes using 6/3.75. The three-tier ratio system (model × completion × group) and the expression-based pricing mechanism (cc/cc1h/cc12h) operate in parallel: the ratio system determines base quota consumption, while expression notation applies on top for cache-specific adjustments. Operators should not conflate the base ratio multiplier with cache-specific pricing rules.
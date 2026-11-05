---
id: 2026-1028-newapi-models-without-ratios
type: atom
certainty: solid
sources: [0-raw/2026-10-28-newapi-ratio-settings.md]
links: ["[[2026-1028-newapi-consumption-mechanism]]", "[[2026-1028-newapi-quota-examples]]"]
---
## Claim
For models without configured ratio settings, NewAPI applies a default model ratio of 37.5, prompts "Ratio or price not configured" in billing mode, and displays unconfigured models in the management interface for operator action.

## Why It Matters
Unconfigured models create billing ambiguity. The default ratio of 37.5 ensures some quota consumption is calculated even without explicit settings, but the explicit error prompt prevents silent misbilling. Operators must configure ratios for production models to avoid the default applying unexpectedly and producing inaccurate cost reports.

## [FRICTION]
> No friction detected. The prior atom [[2026-1023-new-api-precios-por-ratio-y-expresion]] does not address the "models without ratio settings" behavior, so there is no conflict. The three-tier ratio system requires explicit configuration; the default of 37.5 serves as a safety net for edge cases only.
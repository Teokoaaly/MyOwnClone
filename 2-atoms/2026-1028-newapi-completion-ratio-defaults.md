---
id: 2026-1028-newapi-completion-ratio-defaults
type: atom
certainty: solid
sources: [0-raw/2026-10-28-newapi-ratio-settings.md]
links: ["[[2026-1028-newapi-ratio-system]]", "[[2026-1028-newapi-quota-formulas]]"]
---
## Claim
NewAPI pre-sets default completion ratios that balance output token billing relative to input: gpt-4o at 4x, gpt-3.5-turbo at 2x, gpt-image-1 at 8x, and gpt-4o-mini at 4x, meaning output tokens are billed at a multiple of input token cost.

## Why It Matters
Output tokens consistently cost more than input tokens across most models. The completion ratio explicitly accounts for this disparity so quota consumption reflects real cost structure. A completion ratio of 4 means each output token costs 4× the base quota of an input token, preventing underbilling on models where generation is substantially more expensive than comprehension.

## [FRICTION]
> The prior atom [[2026-1023-new-api-precios-por-ratio-y-expresion]] documents expression-based pricing with `cc12h` applying a 2.5× multiplier on 12-hour cache writes at $25/M token for gpt-6-astra. The completion ratio (4× for gpt-4o) governs per-token billing in the three-tier formula, while `cc12h` is a cache-write adjustment that applies after the base quota is computed. These are sequential, not overlapping, rules: completion ratio sets the baseline, cache notation modifies the result.
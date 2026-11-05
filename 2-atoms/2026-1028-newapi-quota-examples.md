---
id: 2026-1028-newapi-quota-examples
type: atom
certainty: solid
sources: [0-raw/2026-10-28-newapi-ratio-settings.md]
links: ["[[2026-1028-newapi-quota-formulas]]", "[[2026-1028-newapi-models-without-ratios]]"]
---
## Claim
The NewAPI quota calculation examples demonstrate three scenarios: (1) GPT-4 standard user conversation consumes 30,000 quota points (1,000 input + 500 output × 2 completion ratio) × 15 model ratio × 1.0 group ratio, (2) GPT-3.5 internal-test group conversation consumes 416.25 quota points ((2,000 + 1,000 × 1.33) × 0.25 model ratio × 0.5 group ratio), and (3) per-call billing (e.g., Midjourney) at $0.02 fixed price × 1.0 group ratio × 500,000 = 10,000 quota points.

## Why It Matters
Concrete examples resolve ambiguity in the abstract formulas. The first example shows a standard GPT-4 conversation costing $0.06 USD (30,000 ÷ 500,000). The second shows internal-test GPT-3.5 at $0.00083 USD. The third shows per-call model billing. These walkthroughs help operators verify their own calculations and understand how the three-tier ratio system compounds in practice.

## [FRICTION]
> No friction detected. The prior atom [[2026-1023-new-api-precios-por-ratio-y-expresion]] discusses ratio pricing and expression-based caching separately; the quota examples here focus on the three-tier formula (model × completion × group) for live API calls. The two mechanisms serve different use cases (live calls vs. cached writes) and do not contradict.
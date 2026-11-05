---
id: 2026-1028-xai-us-endpoint
type: atom
certainty: solid
sources: [sources/2026-10-28-xai-models.md]
links: ["[[2026-1028-xai-grok47-flagship]]", "[[2026-1028-xai-priority-processing]]"]
---

## Claim
The xAI US Regional Endpoint (`https://us.api.x.ai/v1`) adds a 1.1x premium to all token rates for inference in the United States. Only grok-4.7 and grok-4.6 are available on this endpoint. The 1.1x multiplier applies to input, output, and cached input tokens, including long-context rates, with prompt caching discounts applied before the multiplier.

## Why It Matters
Users requiring US-based inference for data sovereignty or latency reasons must accept a 10% cost premium. The endpoint currently only supports grok-4.7 and grok-4.6, so users of older models must use the global endpoint. The 1.1x multiplier is applied on top of any other discounts (batch, prompt caching), meaning the effective cost increase may be less than 11% if other discounts are in effect. This is the only regional variant available; xAI has not announced plans for additional regions.

## [FRICTION]
> [[2026-1028-xai-priority-processing]] offers a 2x premium for lower latency, while [[2026-1028-xai-us-endpoint]] adds only 1.1x for regional inference. Priority is about speed; US endpoint is about geography. Both are orthogonal concerns that can compound: a priority request on the US endpoint incurs both multipliers. Marcado para juicio humano, no auto-resuelto.
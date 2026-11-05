--- 
id: 2026-1028-cto-new-openai-proxy-models-and-quotas
type: atom
certainty: tentative
sources: [sources/2026-10-28-cto-new-openai-proxy.md]
links: ["[[2026-1028-cto-new-openai-proxy-go-reverse-proxy]]", "[[2026-1028-cto-new-openai-proxy-account-pool]]"]
---

## Claim

Model mapping: `gpt-5.4` → `gpt_5_4` (3× quota, multimodal), `glm-5.1` → `glm_5_1` (2× quota, text-only), with aliases `gpt-4o`, `o1`, `claude-sonnet-4.6` all routing to `gpt_5_4`. Each free account receives ~300 requests/day quota, and the proxy marks accounts exhausted when response text contains limit/quota/exceeded keywords, triggering a 6-hour cooldown.

## Why It Matters

With a 7-account pool, GPT-5.4 delivers ≈700 daily requests (×3 multiplier) while GLM-5.1 delivers ≈1050 (×2 multiplier). The `/v1/models` endpoint returns the full list. Quota enforcement is keyword-based, not precise numeric — the proxy does not currently query `/billing` for exact remaining counts.

## [FRICTION]

> [[2026-1028-cto-new-openai-proxy-account-pool]] (escrita hace hoy) describe la selección LRU y el marcado exhausted/dead, pero no detalla el umbral cuantitativo de "~300/requests/día" por cuenta, que proviene de la free tier de cto.new y no está documentado oficialmente en el repo. La discrepancia entre el estimado y el consumo real puede hacer que accounts marquen exhausted prematuramente en cargas de trabajo variables.
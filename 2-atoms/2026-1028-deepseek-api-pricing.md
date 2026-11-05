---
id: 2026-1028-deepseek-api-pricing
type: atom
certainty: solid
sources: [sources/2026-10-28-deepseek-api-pricing.md, 0-raw/2026-10-28-deepseek-api-pricing.md]
links: ["[[2026-1028-anthropic-api-pricing]]", "[[2026-1026-new-api-deepseek-v41-flash-y-busqueda-por-agentes]]", "[[2026-1023-new-api-precios-por-ratio-y-expresion]]", "[[2026-1023-new-api-tokenkit-conteo-de-tokens-calibrado]]"]
---
## Claim

DeepSeek API pricing uses a tiered model: off-peak (all hours outside 01:00-04:00 and 06:00-10:00 UTC, Mon-Fri, excluding Chinese public holidays) and peak (those windows, Mon-Fri). Rates differ by model (deepseek-flash vs deepseek-v4-pro), by token type (input cache hit, input cache miss, output), and by concurrency limit (2500 for flash, 500 for v4-pro). An Anthropic-format endpoint is also available at https://api.deepseek.com/anthropic. Search and Fetch APIs are billed separately at $0.75 per 1,000 successful requests.

## Why It Matters

The 4x price gap between cache hit and cache miss ($0.003 vs $0.15 per 1M input tokens for flash) makes caching a decisive cost factor. Peak hours double all rates, which matters for time-sensitive workloads. The concurrency limit disparity (2500 vs 500) affects multi-tenant routing decisions. The availability of an Anthropic-format endpoint lowers integration friction for teams already invested in that surface, but the thinking-mode modifiers (`@thinking`, `@effort`, and model suffixes `-none`/`-low`/`-max`) mean the effective price per token varies with the chosen reasoning level — a comparable Western provider would need equivalent effort multipliers for price parity. Search/Fetch at $0.75/1K adds a predictable per-request cost for agentic workflows that use tool calls, and billing starts 2026-11-01 Beijing time when using Harness, Claude Code, or Codex.

## [FRICTION]

- **Peak-hour definition**: 01:00-04:00 and 06:00-10:00 UTC, Mon-Fri, excluding Chinese public holidays. Weekend and holiday off-peak rates are half, but the window calculation requires a calendar-aware gate, which the gateway currently does not enforce — risk of unexpected 2x charges.
- **Cache hit vs miss**: 50x price differential means a cache miss in production can balloon bills. No built-in cache-invalidation guidance in the docs; the vault should link [[2026-1023-new-api-precios-por-ratio-y-expresion]] for ratio-pricing patterns that mitigate this.
- **Concurrency limits**: 2500 (flash) vs 500 (v4-pro) — multi-model gateways must route accordingly or hit 429 isolation errors. No per-model quota dashboard in the docs.
- **Thinking-mode pricing**: `@thinking` and `@effort` modifiers change the effective token cost, but the pricing table only shows base rates. The gateway must map modifier combinations to the correct price point; otherwise a `@thinking` flash request could be billed at v4-pro peak rates unintentionally.
- **Anthropic-format endpoint**: Available but undocumented whether it mirrors the OpenAI-format pricing exactly. Teams migrating from Anthropic should validate line-item costs before switching endpoints.
- **Search/Fetch billing start**: 00:00 Beijing time on November 1, 2026. Calls before that date are free through Harness/Codex/Codex but will retrospectively incur $0.75/1K charges — a date-window gotcha for invoicing.
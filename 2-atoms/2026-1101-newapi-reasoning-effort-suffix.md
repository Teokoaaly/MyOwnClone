---
id: 2026-1101-newapi-reasoning-effort-suffix
type: atom
certainty: solid
sources: [sources/2026-10-28-newapi-features-introduction.md]
links: ["[[2026-1028-newapi-deployment-methods]]", "[[2026-1028-newapi-api-token]]"]
---
## Claim

New API supports setting reasoning effort via model name suffix: OpenAI o-series models use `-high`, `-medium`, `-low` suffixes (e.g., `o3-mini-high`), while Claude thinking models use `-thinking` suffix (e.g., `claude-3-7-sonnet-20250219-thinking`). The suffix directly maps to reasoning effort levels that control model thinking depth and cost.

## Why It Matters

Developers can fine-tune reasoning depth per use case without changing channel configuration. High effort increases cost but improves answer quality for complex queries; low effort reduces cost for simple tasks. The suffix pattern is appended directly to the model name in the API call, making it a lightweight, composable configuration mechanism.

## [FRICTION]

> The suffix mechanism is documented per-provider (OpenAI o-series vs Claude), but no cross-provider comparison exists — operators managing multiple channels may not realize the suffix is not universal, risking unexpected reasoning behavior when switching models.

> No guidance on how suffix choices interact with token pricing or quota calculations, meaning high-effort suffixes may incur disproportionate costs if not monitored against rate-limiting settings.

> The `-thinking` suffix for Claude models has no equivalent in the OpenAI suite, creating a mental model mismatch for teams transitioning between providers; documentation does not clarify whether `-high` maps to any Claude-equivalent effort level.

---
[[2026-1101-newapi-model-rate-limiting]]
[[2026-1101-newapi-cache-billing]]
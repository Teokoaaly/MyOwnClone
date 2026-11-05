---
id: 2026-1028-xai-knowledge-cutoff
type: atom
certainty: solid
sources: [sources/2026-10-28-xai-models.md]
links: ["[[2026-1028-xai-grok47-flagship]]", "[[2026-1028-xai-model-selector]]"]
---

## Claim
Grok 4.7 has a knowledge cut-off of May 2026 and has no knowledge of current events or data beyond its training data. To incorporate realtime data, users must enable server-side search tools (Web Search / X Search). Without search tools enabled, the model will silently lack up-to-date information.

## Why It Matters
Applications that require current events, real-time data, or post-May 2026 information must enable xAI's search tools (Web Search or X Search) to supplement the model's training knowledge. The knowledge cut-off means the model cannot answer questions about events after May 2026 without external search. This affects use cases like news analysis, product launch monitoring, or any domain where data is fresher than the training cut-off. Enabling search tools adds cost (Web Search $5/1k calls, X Search $5/1k posts/$10/1k profiles) but is the only way to access realtime information.

## [FRICTION]
> [[2026-1028-xai-model-selector]] recommends model choices per modality, and this note adds that realtime capability depends on search tool enablement, not model selection alone. A user could select the right model but still lack realtime data without search tools. Marcado para juicio humano, no auto-resuelto.
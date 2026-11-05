---
id: 2026-1028-xai-chat-features
type: atom
certainty: solid
sources: [sources/2026-10-28-xai-models.md]
links: ["[[2026-1028-xai-grok47-flagship]]", "[[2026-1028-xai-knowledge-cutoff]]"]
---

## Claim
xAI chat models have no role order limitation (system, user, or assistant roles can be mixed in any sequence), and logprobs/top_logprobs are not supported by grok-4.20 and newer models — these fields will be silently ignored if set. This makes the chat API more flexible for prompt formatting but requires care when relying on probability outputs.

## Why It Matters
The absence of a role order constraint simplifies prompt design: you can mix system, user, and assistant messages in any order without the model rejecting or misinterpreting the conversation. However, developers who depend on logprobs for features like autocomplete, guided generation, or confidence scoring will find these fields silently dropped on grok-4.20+ models. This is relevant when migrating from older grok versions (where logprobs may have been supported) to the latest models, and when designing fallback logic for probability-based features.

## [FRICTION]
> [[2026-1028-xai-knowledge-cutoff]] focuses on knowledge cut-off and search tools, while [[2026-1028-xai-chat-features]] focuses on chat API constraints. Both affect how developers build on xAI, but one is about data recency and the other about API contract details. Marcado para juicio humano, no auto-resuelto.
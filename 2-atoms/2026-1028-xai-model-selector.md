---
id: 2026-1028-xai-model-selector
type: atom
certainty: solid
sources: [sources/2026-10-28-xai-models.md]
links: ["[[2026-1028-xai-grok47-flagship]]", "[[2026-1028-xai-voice-api]]"]
---

## Claim
Use Grok 4.7 for all text/code use cases; Grok Imagine Image 2.0 for images; Grok Imagine Video 1.5 for videos; and Grok Voice API for real-time or batch audio. The model choice guide maps each modality to its dedicated xAI model.

## Why It Matters
The model selection guide states: for code and everything else, use Grok 4.7; for images, use Grok Imagine Image 2.0; for videos, use Grok Imagine Video 1.5; for voice, use Grok Voice API. Choosing the wrong model for the modality results in either missing capabilities (e.g., using Grok 4.7 for image generation when dedicated Imagine APIs exist) or unnecessary cost (e.g., using the Text API for image prompts when Imagine API is 10x cheaper per image). This mapping ensures users pick the right trade-off of capability, latency, and price per modality.

## [FRICTION]
> [[2026-1028-xai-voice-api]] asserts voice is a lower-cost entry point, while [[2026-1028-xai-model-selector]] positions text/code as the default Grok 4.7 use case. Different modalities make both statements valid within their domains. Marcado para juicio humano, no auto-resuelto.
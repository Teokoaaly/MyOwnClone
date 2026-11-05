---
id: 2026-1028-xai-voice-api
type: atom
certainty: solid
sources: [sources/2026-10-28-xai-models.md]
links: ["[[2026-1028-xai-grok47-flagship]]", "[[2026-1028-xai-imagine-api]]"]
---

## Claim
xAI's Voice API provides real-time conversations with speech-to-text ($0.10/hr batch, $0.20/hr streaming), text-to-speech ($15.00/M chars), and speech-to-speech ($0.08/min or $4.80/hr) using grok-voice-2.0 and grok-voice-3.0 models.

## Why It Matters
At $0.08/min for speech-to-speech and $15.00 per million characters for TTS, the Voice API is priced for conversational agents and long-form audio generation. STS (Speech-to-Speech) with grok-voice-3.0 is the current production model, while grok-voice-2.0 is deprecated but still functional. The batch STT at $0.10/hr and streaming STT at $0.20/hr make it suitable for prolonged transcription workloads.

## [FRICTION]
> [[2026-1028-xai-imagine-api]] assumes image/video generation is the primary cost driver, whereas this note asserts voice is the lower-cost entry point for real-time interaction. Both can be true depending on use case. Marcado para juicio humano, no auto-resuelto.
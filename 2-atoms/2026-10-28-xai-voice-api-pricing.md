---
id: 2026-10-28-xai-voice-api-pricing
type: atom
certainty: solid
sources: [sources/2026-10-28-xai-api-pricing.md]
links: ["[[2026-1028-openai-api-pricing.md]]", "[[2026-1023-priceai-grok-x-subscription-cuatro-escalones]]"]
---

## Claim
The xAI Voice API pricing ranges from $0.10/hr (STT REST) / $0.20/hr (STT Streaming) to $15.00/M characters (TTS), with Speech-to-Speech at $0.08/min ($4.80/hr) and $0.004 per text input; the grok-voice-3.0 model is the current standard, while grok-voice-2.0 is deprecated but still listed at the same rate, and batch STT rates are half the streaming rate.

## Why It Matters
Voice API costs accumulate per hour of audio or per million characters of text, making streaming vs REST and batch processing significantly different in price. The 2x difference between streaming and REST STT, and the per-character TTS pricing, mean that long-form content is cheaper via batch TTS while real-time conversation is priced per minute of audio. Compared to OpenAI's audio pricing structure, xAI charges slightly less for TTS ($15 vs $30 per M chars) but more for streaming STT ($0.20 vs $0.06 per hr).

[[2026-1028-openai-api-pricing.md]]
[[2026-1023-priceai-grok-x-subscription-cuatro-escalones]]
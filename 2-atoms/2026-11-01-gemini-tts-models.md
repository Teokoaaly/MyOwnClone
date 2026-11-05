---
id: 2026-11-01-gemini-tts-models
type: atom
certainty: solid
sources: [sources/2026-10-28-gemini-api-pricing.md]
links: [[2-atoms/2026-11-01-gemini-pricing-features]]
---

## Claim
Gemini TTS models (3.8 Flash TTS, 3.8 Flash-Lite TTS, 3.1 Flash TTS Preview, 3 Flash Preview, 2.5 Flash Preview TTS, 2.5 Pro Preview TTS) are text-to-speech models with studio-grade fidelity, expressive acting, and long-form stability.

## Pricing — Gemini 3.8 Flash TTS
- Input price: Free of charge; $0.50 (text) through December 31, 2026; $1.00 (text) starting January 1, 2027
- Output price: Free of charge; $9.00 (audio) through December 31, 2026; $18.00 (audio) starting January 1, 2027
  — Equivalent to $0.00225 per 10s audio* through December 31, 2026; $0.0045 per 10s audio* starting January 1, 2027
- Used to improve products: Yes; output: No
- Audio tokens correspond to 25 tokens per second of audio

## Pricing — Gemini 3.8 Flash-Lite TTS
- Input price: Free of charge; $0.50 (text) through December 31, 2026; $1.00 (text) starting January 1, 2027
- Output price: Free of charge; $6.00 (audio) through December 31, 2026; $12.00 (audio) starting January 1, 2027
  — Equivalent to $0.0015 per 10s audio* through December 31, 2026; $0.003 per 10s audio* starting January 1, 2027
- Used to improve products: Yes; output: No

## Pricing — Gemini 3.1 Flash TTS Preview
- Input price: Free of charge; $1.00 (text)
- Output price: Free of charge; $20.00 (audio)
- Used to improve products: Yes; output: No

## Pricing — Gemini 3 Flash Preview TTS
- Input price: Not available; $0.50 (text / image / video); $1.00 (audio)
- Output price (including thinking tokens): Not available; $3.00
- Context caching: Free of charge; $0.05 (text/image/video); $0.10 (audio); $1.00/1M tokens/hour (storage)

## Pricing — Gemini 2.5 Flash Preview TTS
- Input price: Free of charge; $0.25 (text)
- Output price: Free of charge; $5.00 (audio)
- Used to improve products: Yes; output: No

## Pricing — Gemini 2.5 Pro Preview TTS
- Input price: Not available; $1.00 (text); $0.0006 (image)*
- Output price: Not available; $20.00 (audio)
- Used to improve products: Not available

## Why It Matters
TTS pricing is uniformly based on output audio token consumption (25 tokens/sec of audio). The 3.8 Flash TTS offers the best price-performance for studio-grade output, while Flash-Lite TTS is optimized for high-throughput conversational speech at lower cost. The "per 10s audio" equivalence metric helps estimate costs without counting raw tokens. All TTS models share the "used to improve products: Yes" flag, meaning audio outputs may contribute to model training.

## [FRICTION]
> The audio token conversion (25 tokens/sec) creates a hidden cost multiplication: a 5-minute voice response = 7,500 audio tokens at the output rate. Users counting output tokens without converting to audio minutes will underestimate costs by ~25x. The 3.8 Flash TTS at $0.00225/10s is ~2.25¢/minute, while Flash-Lite at $0.0015/10s is ~1.5¢/minute — a 50% cost difference for what may be qualitatively similar output, creating a pricing tier decision boundary for conversational agents.
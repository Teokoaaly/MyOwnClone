---
id: 2026-11-01-gemini-live-api-models
type: atom
certainty: solid
sources: [sources/2026-10-28-gemini-api-pricing.md]
links: [[2-atoms/2026-11-01-gemini-pricing-features]]
---

## Claim
Gemini 3.8 Live, 3.8 Live Extended Thinking, and 3.1 Flash Live Preview are low-latency, audio-to-audio models optimized for real-time voice agents and live dialogue, including background reasoning support with Extended Thinking.

## Pricing — Gemini 3.8 Live / Live Extended Thinking
- Input price: Free of charge; $0.75 (text); $3.00 or $0.005/min (audio); $1.00 or $0.002/min (image/video) per 1M tokens in USD
- Output price (including thinking tokens): Free of charge; $4.50 (text); $12.00 or $0.018/min (audio) per 1M tokens in USD
- Grounding with Google Search*: Supported; 5,000 free search requests per month (shared across all Gemini 3+ models), then $14 per 1,000 requests
- Used to improve products: Yes; output: No

## Pricing — Gemini 3.1 Flash Live Preview
- Input price: Free of charge; $0.75 (text); $3.00 or $0.005/min (audio); $1.00 or $0.002/min (image/video) per 1M tokens in USD
- Output price (including thinking tokens): Free of charge; $4.50 (text); $12.00 or $0.018/min (audio) per 1M tokens in USD
- Grounding with Google Search*: Supported; 5,000 free search requests per month (shared), then $14 per 1,000 requests
- Used to improve products: Yes; output: No

## Why It Matters
Live API models enable real-time voice agent architectures with bidirectional streaming. The Extended Thinking variant adds background reasoning support, allowing the model to perform internal reasoning during a live session. Pricing is based on input modality: text is cheapest, audio is moderate, image/video is most expensive. The "per minute" audio pricing model (at ~25 tokens/sec) means sustained conversations have a clear cost floor.

## [FRICTION]
> The shared 5,000 free grounding search requests per month across all Gemini 3+ models creates a pooling friction: a Live API deployment handling real-time voice queries with grounding competes with Flash/Argon grounding requests for the same monthly bucket. Additionally, the "per-minute" audio pricing model creates cost unpredictability for long conversations — a 1-hour call at $0.005/min = $0.30 in audio input alone, plus text token costs, can exceed expectations if not explicitly modeled per-minute rather than per-token.
---
id: 2026-11-01-gemini-robotics
type: atom
certainty: tentative
sources: [sources/2026-10-28-gemini-api-pricing.md]
links: [[2-atoms/2026-11-01-gemini-pricing-features]]
---

## Claim
Gemini Robotics ER 2 Preview and ER 2 Streaming Preview are vision-language model endpoints enabling robots to understand their environments precisely, supporting agentic orchestration of robots, video progress understanding, multi-robot collaboration, and advanced spatial reasoning.

## Pricing — Gemini Robotics ER 2 Preview
- Input price: Free of charge; $1.00 (text/image/video/audio) through December 31, 2026; $2.00 starting January 1, 2027
- Output price (including thinking tokens): Free of charge; $5.00 through December 31, 2026; $10.00 starting January 1, 2027
- Context caching: $0.10 through December 31, 2026; $0.20 starting January 1, 2027; $0.50/1M tokens/hour (storage) through December 31, 2026; $1.00 starting January 1, 2027
- Grounding with Google Search: Not available; 5,000 free search requests per month (shared), then $14 per 1,000 requests
- Used to improve products: Yes; output: No

## Pricing — Gemini Robotics ER 2 Streaming Preview
- Input price: Free of charge; $1.00 (text/image/video/audio) through December 31, 2026; $2.00 starting January 1, 2027
- Output price: Free of charge; $5.00 through December 31, 2026; $10.00 starting January 1, 2027
- Grounding with Google Search: Not available; 5,000 free search requests per month (shared), then $14 per 1,000 requests
- Used to improve products: Yes; output: No

## Why It Matters
Robotics ER 2 brings Gemini's multimodal reasoning to physical robots. The streaming preview enables real-time text streaming via the Live API, accepting text, image, video, and audio input with bidirectional streaming and function calling. This is the first Gemini model family explicitly priced for robotics applications, with per-modality input pricing that mirrors the Live API structure.

## [FRICTION]
> The shared 5,000 free grounding search requests per month creates the same pooling friction as Live API: robotics deployments querying visual environments compete with Flash/Argon grounding requests for the same bucket. Additionally, the context caching charge ($0.10/1M tokens/hour storage) applies on top of the per-token input cost, making long-horizon robotics video sessions expensive when caching is needed for replay or multi-step reasoning.
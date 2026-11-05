---
id: 2026-11-01-gemini-pricing-features
type: atom
certainty: solid
sources: [sources/2026-10-28-gemini-api-pricing.md]
links: [[2-atoms/2026-11-01-gemini-4-argon-reasoning]], [[2-atoms/2026-11-01-gemini-3-8-flash]], [[2-atoms/2026-11-01-gemini-3-5-flash-lite]], [[2-atoms/2026-11-01-gemini-2-5-flash]]
---

## Claim
The Gemini API pricing schema includes a standardized set of pricing features across all models: free tier, paid tier with Standard/Batch/Flex/Priority/Contributor modes, context caching, Google Search grounding, Google Maps grounding, and tool usage pricing. Understanding which features each model supports is critical for cost modeling.

## Pricing Feature Matrix

| Feature | Gemini 4 Argon | Gemini 3.8 Flash | Gemini 3.6 Flash | Gemini 3.5 Flash-Lite | Gemini 2.5 Flash |
|---|---|---|---|---|---|
| Free Tier Input | Limited/Not Avail | Yes (free) | Yes (free) | Yes (free) | Yes (free) |
| Free Tier Output | Limited/Not Avail | Yes (free) | Yes (free) | Yes (free) | Yes (free) |
| Batch (50% off) | Yes | Yes | Yes | No | Yes |
| Context Caching | Implicit only, $0.10/1M | $0.075/1M + storage | $0.075/1M + storage | Not available | $0.03/1M + storage |
| Google Search Grounding | 5K free/mo, then $14/1K | 5K free/mo, then $14/1K | 5K free/mo, then $14/1K | Not available | 500 RPD free, then $35/1K |
| Google Maps Grounding | 5K free/mo, then $14/1K | 5K free/mo, then $14/1K | 5K free/mo, then $14/1K | Not available | 500 RPD free, then $25/1K |
| Audio Pricing | Model-dependent | $0.0053/min (input) | $0.0053/min (input) | Same as text/image/video | $1.00/1M (input) |
| Image Pricing | Model-dependent | $0.75/1M (input) | $0.375/1M (input) | $0.10/1M (input) | $0.30/1M (input) |
| Contributor Tier (improve products) | Yes (output: No) | Yes | Yes | Yes | Yes |
| Rate Limits (RPD) | Varies by feature | Varies by feature | Varies by feature | Varies by feature | 500 free RPD shared with Flash-Lite |

## Why It Matters
The pricing feature matrix reveals explicit upgrade paths: Flash-Lite → Flash enables grounding; Flash-Lite → Flash enables context caching; the 500 RPD free grounding limit shared with Flash-Lite creates a hard upgrade threshold. Batch pricing (50% cost reduction) is available across most models, making high-volume workloads more economical. Context caching pricing is model-agnostic in structure (per 1M tokens per hour storage) but varies in cost per 1M tokens.

## [FRICTION]
> The most significant friction is the **model-tier grounding gate**: Flash-Lite has zero grounding support, Flash has 500 RPD free, and Flash/Pro have 1,500 RPD free. This means any RAG or retrieval-augmented application must explicitly upgrade from Flash-Lite to access grounding, increasing minimum costs. The shared 500 RPD limit between Flash and Flash-Lite creates a coordination friction in mixed-model organizations — grounding usage by one model directly reduces the other's free capacity. Additionally, context caching is universally charged per 1M tokens/hour of storage, with no free tier, creating a hidden cost for long-context workloads that is often underestimated during prototyping.
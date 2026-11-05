---
id: 2026-10-28-xai-tools-pricing
type: atom
certainty: solid
sources: [sources/2026-10-28-xai-api-pricing.md]
links: ["[[2026-1028-openai-api-pricing.md]]", "[[2026-1023-priceai-grok-x-subscription-cuatro-escalones]]"]
---

## Claim
xAI charges $5 per 1k calls for web_search, x_search, code_execution, attachment_search, and collections_search tools, $10 per 1k profiles for x_search, and token-based pricing (matching the model's input/cached/output rates) for view_image and view_x_video; remote MCP tools are token-based only with no separate invocation fee.

## Why It Matters
Tool invocation costs scale with query complexity since the agent autonomously decides tool calls. At $5/1k calls, individual tool requests are cheap but multiply quickly in multi-turn agent workflows. The token-based pricing for image/video understanding means analyzing search results visually costs the model's standard token rate on top of the search fee. Compared to OpenAI's function calling model pricing, xAI bundles tool costs separately from token usage, which can be more transparent for simple operations but harder to predict when tools and tokens interact.

[[2026-1028-openai-api-pricing.md]]
[[2026-1023-priceai-grok-x-subscription-cuatro-escalones]]
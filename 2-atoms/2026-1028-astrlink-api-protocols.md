---
id: 2026-1028-astrlink-api-protocols
type: atom
certainty: tentative
sources: [sources/2026-10-28-astrlink-github.md]
links: ["[[2026-1028-astrlink-on-device-privacy]]", "[[2026-1028-astrlink-model-routing]]"]
---

## Claim

AstrLink exposes multiple API protocols —OpenAI Responses (/v1/responses), OpenAI Chat Completions (/v1/chat/completions), Anthropic Messages (/v1/messages), and Gemini (/v1beta/models/{model}:generateContent)— with protocol conversion configured according to upstream capabilities.

## Why It Matters

Agents using different API client libraries can all route through a single AstrLink gateway. The gateway handles protocol conversion so the agent doesn't need to know whether the upstream provider uses Chat Completions or Messages format. This unifies the agent's model configuration across multiple providers with different wire formats.

## [FRICTION]

> [[2026-1027-gptgrok2api-285-estrellas-y-24-commits-con-12-tags-y-3-mes-sin-movimiento]] documenta un repositorio con 285 estrellas, 145 forks y topics `ai-gateway`, `grok`, `grok-api`, `oauth`, `openai-api` pero sin actividad de commits desde julio de 2026 y sin releases recientes. Este átomo presiona la creencia de que la conversión de protocolos en AstrLink cubre todos los casos de uso: el proyecto GPTGrok2API es un proyecto secundario ("second version, er kai") de chatgpt2api con licencia partida (LICENSE y GROK2API_LICENSE) y su último commit fue hace tres meses de la captura. AstrLink's protocol conversion opera a nivel de gateway y asume que el proveedor upstream admite alguna variante del modelo solicitado; proyectos con esquemas de licencia fragmentados y historiales de commits discontinuos pueden tener capacidades de protocolo desconocidas o incompatibles. Ambas afirmaciones pueden ser ciertas —AstrLink cubre los protocolos documentados de los proveedores principales, mientras que repositorios secundarios pueden tener protocolos no documentados o personalizados— pero la creencia de que todas las APIs son igualmente convertibles ignora la realidad de esquemas de liga distinta y contratos de proveedor variables. Marcado para juicio humano.
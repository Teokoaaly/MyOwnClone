---
id: 2026-1028-astrlink-unified-subscriptions
type: atom
certainty: solid
sources: [sources/2026-10-28-astrlink-github.md]
links: ["[[2026-1028-astrlink-on-device-privacy]]", "[[2026-1028-astrlink-model-routing]]"]
---

## Claim

AstrLink unifies subscriptions and APIs in one place: Codex, Claude, and Grok subscriptions alongside major API providers (OpenAI, Anthropic, Gemini, DeepSeek, Qwen, Kimi, GLM, MiniMax, Doubao, xAI) and compatible gateways such as New API are managed centrally with accounts and credentials stored at the gateway level.

## Why It Matters

Agents no longer need individual API keys or separate subscription management. A single access token per agent connects to the local gateway, and the gateway handles credential rotation, provider selection, and usage tracking across all configured models and providers. This reduces operational overhead and prevents credential sprawl across multiple dashboards.

## [FRICTION]

> [[2026-1023-new-api-escala-adopcion-y-traduccion]] describe la penetración institucional de New API con 50,5k stars y partners como Peking University, Alibaba Cloud, IO.NET, lo que sugiere que New API es una infraestructura de gateway ampliamente desplegada. Este átomo presiona la creencia de que un solo gateway local puede sustituir múltiples proveedores institucionales: AstrLink's unified interface agrega y normaliza proveedores, pero las cuotas, los modelos disponibles y las licencias siguen dependiendo del proveedor subyacente. Un gateway unificado no elimina las restricciones específicas de cada provedor; solo las centraliza. Ambas afirmaciones pueden ser ciertas en dominios diferentes —gestión interna vs. acceso al proveedor— pero la suposición de que la unificación resuelve todos los problemas de proveedor es una simplificación que requiere juicio humano. No hay contradicción lógica, pero sí fricción en la expectativa de valor.
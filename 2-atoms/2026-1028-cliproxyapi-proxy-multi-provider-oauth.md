---
id: 2026-1028-cliproxyapi-proxy-multi-provider-oauth
type: atom
certainty: solid
sources: [sources/2026-10-28-cliproxyapi-github.md]
links: ["[[2026-1023-new-api-una-sola-api-multiproto]]", "[[2026-1024-veridrop-cobertura-de-protocolos-por-relay]]"]
---

## Claim

CLIProxyAPI provides a single CLI-compatible API surface that routes requests to over 10 distinct LLM providers (OpenAI GPT-6, Anthropic Claude, Google Gemini, xAI Grok, Kimi, Meta Muse, Antigravity, Devin) through individual OAuth login flows, whereas most gateway relays support only 1–3 protocols natively.

## Why It Matters

The vault's gateway comparisons (notably [[2026-1024-veridrop-cobertura-de-protocolos-por-relay]]) show that 36 % of relays support only one protocol, 38 % support exactly two, and only 15 % offer full multi-protocol coverage. CLIProxyAPI collapses this fragmentation: a single binary and config file can speak OpenAI-compatible, Anthropic Messages, Gemini, and Grok APIs, each with its own OAuth-registered account. This matters for product teams building coding assistants or multi-model workflows who want to avoid maintaining separate proxies per provider, and it shifts the integration cost from "one proxy per provider" to "one proxy with N OAuth credentials."

## [FRICTION]

> [[2026-1023-new-api-una-sola-api-multiproto]] tabula una API unificada cuatros protocolos, pero su superficie es del software, no del estándar de despliegue: la mayoría de relays del mercado exponen un único dialecto (ver [[2026-1024-veridrop-cobertura-de-protocolos-por-relay]]). La afirmación de CLIProxyAPI de soportar 10+ providers a través de una sola API no es un estándar de la industria; es una implementación propietaria que asume responsabilidad de conversión en el cliente del proxy, no en el upstream.

> Ambas no pueden ser completamente correctas. Una ofrece una ruta `/v1` unificada que habla múltiples protocolos; la otra documenta que el mercado se reparte en relays de un solo protocolo. El conflicto radica en si el costo de la capa de conversión se paga al deployer (CLIProxyAPI) o si se espera que cada relay hable nativo (el modelo de mercado actual). Marcado para juicio humano, no auto-resuelto.
--- 
id: 2026-1028-cto-new-openai-proxy-go-reverse-proxy
type: atom
certainty: tentative
sources: [sources/2026-10-28-cto-new-openai-proxy.md]
links: ["[[2026-1028-cto-new-openai-proxy-account-pool]]", "[[2026-1028-cto-new-openai-proxy-turnstile-friction]]"]
---

## Claim

A Go reverse proxy exposes cto.new free chat models (GPT-5.4, GLM-5.1) as standard OpenAI `/v1/chat/completions` and Anthropic `/v1/messages` compatible APIs, enabling users to access these models without direct cto.new accounts.

## Why It Matters

Lowering the access barrier to cto.new's free tier models expands the available model pool for developers who need OpenAI/Anthropic-compatible endpoints. The proxy handles account rotation, JWT refresh, and quota management so the caller only needs to provide a bearer key.

## [FRICTION]

> [[2026-1028-cto-new-openai-proxy-no-tool-use]] (escrita hace hoy) afirma que el proxy no soporta function calling / tool use. Esto presiona el diseño porque muchos flujos de trabajo de opencode/cline dependen de `tools` injection, y alternar proveedores añade complejidad operativa. Ambas pueden ser ciertas en partes: el proxy funciona para chat completions sin herramientas, pero cualquier pipeline que espere respuestas estructuradas `tool_calls` debe usar proveedores nativos.

> [[2026-10-28-cto-new-home.md]] (escrita hace unas líneas) describe las features nativas de cto.new, que incluyen capacidades de agent con su propio sandbox. El proxy deliberadamente no reimplementa ese protocolo en la capa HTTP, lo que rompe la compatibilidad con flujos que esperan tool uso end-to-end.

Ambas no pueden ser completamente correctas. Marcado para juicio humano, no auto-resuelto.
---
id: 2026-1028-cliproxyapi-mgmt-api-provider-orchestration
type: atom
certainty: solid
sources: [sources/2026-10-28-cliproxyapi-github.md]
links: ["[[2026-1023-new-api-gateway-unificado-de-modelos]]", "[[2026-1024-veridrop-cobertura-de-protocolos-por-relay]]"]
---

## Claim

CLIProxyAPI includes a Management API (exposed via `MANAGEMENT_API.md` and referenced from `AGENTS.md`) that supports OAuth credential registration, API provider configuration, model aliasing, plugin management, and CPA settings — all SQLite-backed with request history, latency, TTFT, token, and cost breakdowns per model, provider, account, key, and channel.

## Why It Matters

Gateway operators need more than a binary that routes requests: they need observability, credential rotation, per-account quota tracking, and the ability to sync model prices from OpenRouter or other price sources without redeploying. The Management API turns CLIProxyAPI from a dumb pipe into a controllable platform, and the SQLite-backed request history enables live monitoring, failure diagnosis, and cost attribution — features that standalone proxy binaries typically lack or require external tools (CPA-Manager-Plus, Oh-My-CPA) to provide.

## [FRICTION]

> [[2026-1024-veridrop-cobertura-de-protocolos-por-relay]] documenta que solo 15 de 50 relays del mercado ofrecen multi-protocolo completo, y el vault sabe que la mayoría de deployments son de un solo dialecto. El atom de Management API asume que el operador necesita y usará todas estas funciones (OAuth registration, model aliasing, price sync), pero en deployments mínimos o individuales el sobrecimiento de la API completa puede ser innecesario. No está claro si la API completa se despliega siempre o si existe un perfil "lite" que expone solo el enrutamiento básico sin gestión SQLite. Ambas afirmaciones no pueden ser completamente correctas sin conocer el perfil de deploy del operador. Marcado para juicio humano, no auto-resuelto.
---
id: 2026-1023-ai-security-tools-agente-como-categoria-dominante
type: atom
certainty: solid
sources: [sources/2026-10-22-awesome-ai-security-tools.md]
links: ["[[2026-1022-ia-y-auth-totalmente-servidor]]", "[[2026-1022-pipeline-chat-actual-myownclone]]", "[[2026-1023-ai-security-tools-runtime-61-entradas-aislamiento-no-deteccion]]"]
---

## Claim
La categoría **AI Agent & Coding-Agent Security** es la mayor del listado con **101 entradas** y el README la describe explícitamente como "a fast-moving 2026 category", subdividida por rol en tres: **Scanners & Auditors (26)**, **Frameworks, Rule Standards & Benchmarks (14)** y **Runtime Protection & Enforcement (61)**. Su alcance declarado es "securing the AI agents themselves — auditing coding agents (Claude Code, Codex, OpenClaw), scanning skills / plugins / MCP manifests, and governance for agentic development".

## Why It Matters
Que la categoría más poblada esté orientada a *agentes de código* y no a *agentes conversacionales* dice algo sobre el estado del campo: el objeto que se está intentando asegurar es el asistente que escribe y ejecuta código con permisos, no el chatbot que responde a un visitante. Eso deja al producto del vault ([[2026-1022-pipeline-chat-actual-myownclone]], [[2026-1022-ia-y-auth-totalmente-servidor]]) fuera del centro de gravedad de las herramientas: su superficie no es un workspace con skills y MCP, sino un endpoint de chat server-side. Lo que sí es transferible del catálogo es la subsección de runtime (61 entradas, ver [[2026-1023-ai-security-tools-runtime-61-entradas-aislamiento-no-deteccion]]), que es donde vive el patrón de aislar al agente y controlar su salida.

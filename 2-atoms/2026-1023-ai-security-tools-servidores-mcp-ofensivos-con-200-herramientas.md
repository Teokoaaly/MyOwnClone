---
id: 2026-1023-ai-security-tools-servidores-mcp-ofensivos-con-200-herramientas
type: atom
certainty: solid
sources: [sources/2026-10-22-awesome-ai-security-tools.md]
links: ["[[2026-1023-ai-security-tools-mcp-como-superficie-de-ataque]]", "[[2026-1023-ai-security-tools-honeypots-llm-y-decepcion-6-entradas]]", "[[2026-1022-dns-superficie-publica-myownclone]]"]
---

## Claim
La categoría **"Pentest & Red-Team Agents"** (29 entradas) documenta un salto de capacidad concreto: **servidores MCP que exponen arsenales de herramientas ofensivas a agentes de IA**. `HexStrike-AI` — "MCP server exposing 150+ security tools (nmap, gobuster, nuclei, …) to AI agents"; `pentest-ai` — "Offensive-security MCP server with 200+ wrapped tools, specialist agents, and OWASP-oriented probes"; `pentest-ai-agents` — colección de subagentes ofensivos para Claude Code; `MCP Security Hub` — colección de servidores MCP dockerizados que exponen Nmap, Nuclei, SQLMap, Ghidra, Hashcat; `Burp Suite MCP Server` de PortSwigger — la extensión oficial de Burp exponiendo Burp a clientes de IA vía MCP. A eso se suman agentes autónomos con capacidad de streaming de resultados: `Strix` (68.259 ★, Apache-2.0), `PentAGI` (27.471 ★, sandboxing Docker), `Shannon` (48.816 ★, con variante Lite AGPL-3.0 y Pro comercial), `PentestGPT` (15.926 ★).

## Why It Matters
La cifra que importa no es el número de entradas sino el de **herramientas por servidor**: 150 y 200+ herramientas ofensivas invocables por un agente. Eso convierte al agente en un **orquestador de herramientas ofensivas** con la capacidad de encadenarlas, lo que antes requería un operador humano por paso. Es el mismo patrón que se ve en la categoría de reversa: `ida-pro-mcp` (12.722 ★), `GhidraMCP` (11.156 ★), `ghidra-mcp` y `ReVa` bridged a MCP, más `REA` (176.042 ★, CLI y toolkit MCP para análisis asistido de binarios).

La consecuencia de seguridad es directa y es la que el listado repite en cada ficha: estos proyectos exigen "authorized testing only", "use only in isolated, authorized environments", "on a dedicated isolated host", y varios tienen stacks pesados con acceso al socket de Docker o `seccomp=unconfined`. El vector para el vault es la versión defensiva: un producto con IA expuesto públicamente es un objetivo que un agente de este perfil puede atacar con arsenal, y por eso la superficie DNS/HTTP y la de invocación de herramientas ([[2026-1022-dns-superficie-publica-myownclone]], [[2026-1023-ai-security-tools-mcp-como-superficie-de-ataque]]) son la prioridad — y también el mejor señuelo defensivo, como muestra `Beelzebub` ([[2026-1023-ai-security-tools-honeypots-llm-y-decepcion-6-entradas]]).

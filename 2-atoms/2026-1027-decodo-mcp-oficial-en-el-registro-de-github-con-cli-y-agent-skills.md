---
id: 2026-1027-decodo-mcp-oficial-en-el-registro-de-github-con-cli-y-agent-skills
type: atom
certainty: solid
sources: [sources/2026-10-26-decodo-smartproxy-home.md]
links: ["[[2026-1026-brightdata-mcp-un-solo-comando-por-cliente-de-agente]]", "[[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]", "[[2026-1026-github-search-suno-piapi-skills-un-bundle-de-skills-para-agentes-con-hermes]]", "[[2026-1026-decodo-integraciones-de-navegador-y-agentes-como-gratis-con-cada-plan]]"]
---

## Claim
Decodo publica **cuatro superficies de integración para agentes** en la home, bajo el epígrafe "Plug the web into your agent stack" y la frase *"An official MCP server, CLI, agent skills, and SDKs, so you connect with config instead of custom code."*:

- **MCP Server** — *"Add it with one line of config and your agent can scrape, map, crawl, and search on its own. **Officially listed in GitHub's MCP Registry**."*
- **CLI** — *"Run any endpoint from your terminal or a shell script. Good for quick tests, CI jobs, and coding agents with shell access."*
- **Agent Skills** — *"Drop a skill file into your coding assistant so it calls the API correctly, with the right endpoint, parameters, and output format, **instead of guessing from docs**."*
- **SDKs and integrations** — *"Use the Python or TypeScript SDK in code, or connect through **n8n, LangChain, or OpenClaw** with no wrapper code."*

La sección "AI integrations" añade: *"Native MCP server support plus **LangChain and LlamaIndex** integrations – an agent calls Decodo directly as a tool, no custom wrapper code needed."*

## Why It Matters
Decodo es el **cuarto proveedor del corpus que publica servidor MCP para agentes**, y el primero que lo hace **con el respaldo de un registro público** —GitHub's MCP Registry— en lugar de un repositorio propio ([2Captcha](https://github.com/2captcha), [Bright Data](https://github.com/brightdata)). El efecto es de **descubribilidad**: un MCP listado en el registro oficial de GitHub es **encontrable por un agente que busca herramientas**, mientras que un repositorio con README lo es solo por un humano que ya sabe que existe. La diferencia práctica para el vault: **la superficie de integración de un proveedor pasa de ser una URL que hay que conocer a ser un elemento de catálogo**.

Lo segundo es que Decodo es el **primer proveedor del corpus que publica "agent skills" como producto** —el mismo patrón que el vault ya registró para el bundle de skills de GitHub Search, Suno y PiAPI con Hermes ([[2026-1026-github-search-suno-piapi-skills-un-bundle-de-skills-para-agentes-con-hermes]]). Y la frase que lo justifica es una **diagnosis del fallo más común de los agentes**: *"so it calls the API correctly, with the right endpoint, parameters, and output format, **instead of guessing from docs**". Es decir, el proveedor está vendiendo **el ahorro del error de invocación**, que es un coste invisible: un agente que adivina el endpoint consume cuota fallando y, con la unidad de cobro por mil de requests ([[2026-1027-decodo-la-unidad-no-es-estable-requests-paginas-y-crawls]]), **los fallos también se facturan**.

Lo tercero, y es el patrón de fondo: la **superficie comercial del acceso web para agentes ya está completa en Decodo** —MCP + CLI + skills + SDKs + n8n + LangChain + LlamaIndex + OpenClaw — y todo eso **sin coste adicional declarado**: la página de precios declara las mismas features en **todos** los planes, incluido el gratuito ([[2026-1026-decodo-integraciones-de-navegador-y-agentes-como-gratis-con-cada-plan]]). Frente a Bright Data, donde el MCP documenta comandos concretos por cliente y el token viaja en la URL en Claude Code ([[2026-1026-brightdata-mcp-un-solo-comando-por-cliente-de-agente]]), y frente a 2Captcha, que llegó al MCP desde el captcha ([[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]), Decodo llega **desde el proxy** y **reutiliza su pool de 125M+**.

## Nota de verificación
Frases transcritas literalmente. La captura **no** publica: el nombre del paquete en el registro de MCP de GitHub, el catálogo de herramientas del servidor MCP, qué Skills concretos hay en `decodo.com/agent-skills`, si el MCP consume la misma cuota que la API por mil, ni si los SDKs Python/TypeScript son open source.

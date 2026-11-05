---
id: 2026-1026-brightdata-mcp-un-solo-comando-por-cliente-de-agente
type: atom
certainty: solid
sources: [sources/2026-10-25-brightdata-docs-intro.md]
links: ["[[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]", "[[2026-1023-ai-security-tools-mcp-como-superficie-de-ataque]]", "[[2026-1026-brightdata-una-sola-api-key-para-todos-los-productos]]"]
---

## Claim
La sección "Set up your AI tools" declara: *"Connect Bright Data to the tool you already use. Each command is the same one documented in its MCP integration guide."* Enumer **cuatro clientes** con su comando literal: **Claude Code** —`claude mcp add --transport sse brightdata "https://mcp.brightdata.com/sse?token=YOUR_API_KEY"`; **Cursor** —`npx -y @brightdata/mcp` con `"env": {"API_TOKEN": "<your API token>"}`; **Codex CLI** —`codex mcp add brightdata --env API_TOKEN=YOUR_API_KEY -- npx -y @brightdata/mcp`; y **Bright Data CLI** —`npx -p @brightdata/cli brightdata --version`. El producto MCP se titula **"Bright Data MCP — Live web access for agents"**.

## Why It Matters
Es el **segundo actor del corpus que publica servidor MCP para agentes**, y el vault ya tiene el primero: 2Captcha con **cuatro** servidores MCP (Web, Browser, Web Search, Web Scraper) y repositorio propio ([[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]). La diferencia de negocio es sustantiva: mientras 2Captcha llega al MCP **desde el captcha**, Bright Data llega al MCP **desde el proxy y el dataset**, es decir, desde la capa que el vault ya costea en $/GB. El resultado es que **el acceso web para agentes es ya un producto de catálogo con dos proveedores y dos modelos de precio** (créditos sin conversión publicada frente a $/GB), lo que hace la tabla de coste por insumo aún más incompleta.
El detalle de seguridad que el vault no puede dejar pasar: en Claude Code **el token viaja en la URL** (`?token=YOUR_API_KEY`), mientras que en Cursor y Codex **viaja como variable de entorno**. Eso significa que **el mismo producto MCP expone el token en dos superficies distintas según el cliente**: una URL —que queda en el historial del shell y en los logs del cliente MCP— y un entorno —que queda en el archivo de configuración del cliente. Es exactamente la superficie que el vault registró como vector: el objetivo deja de ser el prompt y pasa a ser **la definición y el transporte de la herramienta** ([[2026-1023-ai-security-tools-mcp-como-superficie-de-ataque]]).

## Nota de verificación
Comandos transcritos literalmente. La captura **no publica**: el catálogo de herramientas que expone el MCP, cuántos créditos consume cada llamada, si el endpoint SSE acepta el token por header además de por query, ni si existe scoped token por producto.


## Nota de extensión 2026-10-27
Decodo publica **su propio servidor MCP y lo lista en el registro oficial de MCP de GitHub** ("Officially listed in GitHub's MCP Registry"), lo que abre una diferencia de **distribribución** frente al patrón de Bright Data que este átomo documenta: aquí el MCP es **una entrada de catálogo de un registro público** (descubrible por un agente que busca herramientas), no un repositorio propio que hay que conocer de antemano.

La otra diferencia es que **Decodo llega al MCP desde el proxy y reutiliza su pool de 125M+**, con las cuatro superficies de integración en el mismo bloque: **MCP Server + CLI + Agent Skills + SDKs** (Python y TypeScript), más **n8n, LangChain, LlamaIndex y OpenClaw**. El vault puede registrar que la **superficie de agente ya está completa en Decodo** y que **ninguna de las cuatro se cotiza por separado**: la página de precios declara las mismas features en todos los planes, incluido el gratuito. Ver [[2026-1027-decodo-mcp-oficial-en-el-registro-de-github-con-cli-y-agent-skills]] y [[2026-1026-decodo-integraciones-de-navegador-y-agentes-como-gratis-con-cada-plan]].

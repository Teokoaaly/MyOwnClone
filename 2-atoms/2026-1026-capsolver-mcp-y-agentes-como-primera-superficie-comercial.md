---
id: 2026-1026-capsolver-mcp-y-agentes-como-primera-superficie-comercial
type: atom
certainty: solid
sources: [sources/2026-10-25-capsolver-home.md]
links: ["[[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]", "[[2026-1023-ai-security-tools-mcp-como-superficie-de-ataque]]", "[[2026-1026-decodo-integraciones-de-navegador-y-agentes-como-gratis-con-cada-plan]]"]
---

## Claim
La home de CapSolver ordena su oferta comercial en **tres bloques numerados**, y el primero es **"01 AGENTS — AI agent automation"**, marcado como **NEW**, con la descripción "Give AI agents the ability to solve CAPTCHAs through framework tools, browser actions, or the Model Context Protocol" y cinco destinos: **MCP**, **Browser Use**, **LangChain**, **OpenAI SDK** y **Playwright**. Los otros dos bloques son "02 BROWSER — Browser automation" (Selenium, Puppeteer, n8n, Extension, Playwright) y "03 API & CAPTCHA services" (REST API + SDKs + los tipos de captcha).

## Why It Matters
La **primera** superficie comercial que CapSolver enumera no es el captcha: es la integración con agentes. Es exactamente el giro que el vault ya registró en 2Captcha — Browser API, Scraper API, Web Unlocker y cuatro servidores MCP ([[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]])— pero aquí el orden es distinto y más explícito: **el captcha es el producto y el agente es el canal de venta**, mientras que allí el scraping era el producto y el captcha el gancho.
La diferencia útil para el vault es de **superficie de integración**: MCP, LangChain, OpenAI SDK y Playwright son **frameworks de agente**, no solo navegadores. Es decir, el proveedor de captchas entra en la cadena de un agente por un lado que no es el scraping (LangChain, OpenAI Agents SDK). Eso refuerza la lectura del vault de que el MCP se está convirtiendo en **superficie de ataque**: un proveedor comercial de elusión anti-bot expone ahora herramientas para que el agente resuelva el captcha él mismo ([[2026-1023-ai-security-tools-mcp-como-superficie-de-ataque]]), igual que Decodo reparte integraciones de navegador y agentes como gratis con cada plan ([[2026-1026-decodo-integraciones-de-navegador-y-agentes-como-gratis-con-cada-plan]]).
El punto de fricción para el vault: **si resolver el captcha es una llamada más en el tool loop de un agente, su coste ($0.001) deja de ser una partida de presupuesto y pasa a ser un parámetro más del prompt** — lo que destruye la tabla de coste por insumo de la §7 del thread.

## [FRICTION]
> La §7 del thread [[economia-de-la-verificacion-y-reventa-de-cuentas]] sostiene que el captcha es "la partida más barata y la más fácil de cotizar" y que su coste marginal se mide en $0.0005 — $0.00299 por captcha ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]).
> Este átomo presiona esa lectura en un punto de arquitectura: si el captcha se resuelve **desde dentro del agente** (MCP, Browser Use, LangChain, OpenAI SDK), entonces **no hay una línea de coste por captcha** sino un tool call cuyo precio unitario ($0.001) es irrelevante frente al coste del turno del agente que lo invoca. Es decir: o el captcha es una partida de coste medible porque alguien la mide por separado, o es un **consumo interno no contabilizado** del propio modelo. Marcado para juicio humano, no auto-resuelto: la captura **no** publica el precio de las integraciones de agente, ni si el MCP es de pago o incluido, ni el coste por token del turno del agente que llama al solver.

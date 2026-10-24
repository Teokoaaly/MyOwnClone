---
id: 2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes
type: atom
certainty: solid
sources: [sources/2026-10-23-2captcha-solver.md]
links: ["[[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]]", "[[2026-1023-ai-security-tools-mcp-como-superficie-de-ataque]]", "[[2026-1023-midjourney-proxy-oferta-comercial-de-api-no-oficial]]"]
---
## Claim
La home de 2Captcha ya no vende solo captchas: publica una **línea de scraping y datos** — Browser API (navegador automatizado con stealth y gestión de proxies), Scraper API (rotación de proxies, anti-bot bypass, renderizado JS), Browser fingerprints (perfiles reales de navegador) y **Web Unlocker** ("automatically handles blocks, captchas, and proxy rotation, **so you pay only for successful data extraction**") — más **cuatro servidores MCP** para agentes: Web MCP, Browser MCP, Web Search MCP y Web Scraper MCP, con repositorio `github.com/2captcha/2captcha-mcp`.

## Why It Matters
Es un **giro de categoría de producto**: de "resolver captchas" a "infraestructura de acceso a web para agentes de IA". Y lo hace con el mismo argumento económico que ya usa el vault para el relay: cobrar por el **resultado útil** (extracción exitosa) y no por el recurso ([[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]]).
La pieza MCP es la directamente relevante: cuatro servidores MCP publicados para conectar agentes a búsqueda, scraping y automatización de navegador es exactamente la superficie que el vault registró como **nuevo vector de ataque** ([[2026-1023-ai-security-tools-mcp-como-superficie-de-ataque]]). Que un proveedor comercial de elusión anti-bot sea a la vez proveedor de herramientas MCP para agentes confirma que la convergencia "agente = navegador que evade controles" ya tiene un proveedor de facto, y que el vault está del lado del cliente de esa oferta, no del lado del proveedor.
También es el mismo patrón de negocio que el proxy de imagen: **core abierto en GitHub + valor en la operación comercial** ([[2026-1023-midjourney-proxy-oferta-comercial-de-api-no-oficial]]).
Nota: la captura **no** publica precios de Browser API, Scraper API, fingerprints, Web Unlocker ni de los MCP; solo la tabla de captchas.

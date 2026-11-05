---
id: 2026-1027-2captcha-mcp-seis-modos-con-precios-por-llamada
type: atom
certainty: solid
sources: [sources/2026-10-26-2captcha-pricing-mcp.md]
links: ["[[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]", "[[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]]", "[[2026-1023-ai-security-tools-mcp-como-superficie-de-ataque]]"]
---
## Claim
La página de precios del MCP de 2Captcha (`2captcha.com/pricing/mcp`) publica una tabla de **seis modos** —**API Tier, Fast, Impersonated, SERP, Render y Camoufox**— con cuatro columnas: "**Credits per call**", "**Price per 1,000 calls**", "**Price per call**" y una acción "**Buy**" que enlaza a `2captcha.com/pay`. Los precios por llamada van de **$0.0001** (API Tier) a **$0.0048** (Camoufox), y los créditos por llamada de **1** a **48**.

## Why It Matters
Es la **primera vez que el vault puede cotizar la línea de agentes de 2Captcha**, que hasta ahora era solo una lista de nombres ([[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]). Y lo que aparece es una **unidad nueva para el corpus**: el MCP se cobra **por llamada**, no por mil, no por GB y no por captcha resuelto. El vault tenía hasta ahora cuatro unidades de elusión (captcha por 1000, requests por 1000, $/GB y $/proxy por mes), y esta es la quinta.

El dato que más importa para el vault no es el precio sino **qué se está vendiendo**: el modo "**Camoufox**" —el navegador con fingerprint antisimulación— aparece en la misma tabla que "**SERP**" y "**API Tier**", es decir, la navegación con evasión avanzada se vende como **un modo más de una tabla de precios**, no como un producto aparte. Es exactamente la superficie que el vault marcó como vector de ataque ([[2026-1023-ai-security-tools-mcp-como-superficie-de-ataque]]): ahora esa superficie tiene **tarifa publicada**, lo que la convierte en infraestructura costeable y, por tanto, en dependencia.

La tercera consecuencia es de coherencia comercial: la tabla del MCP **no publica ninguna cláusula de éxito**. El contrato deliberadamente barato del proveedor —"The server load does not affect the price" y "Pay only for solved captchas" ([[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]])— era una afirmación de la línea de captchas; aquí, en la línea de agentes, la página solo dice cuántas llamadas cuestan y cuántos créditos gasta cada una, sin decir si una llamada fallida se factura.

Nota: la captura **no** publica qué incluye una "call" (¿una petición, un render completo, un reintento?), el precio del paquete de créditos, ni SLA. La tabla es una transcripción literal; toda comparación de precio con otras unidades es derivación del vault.

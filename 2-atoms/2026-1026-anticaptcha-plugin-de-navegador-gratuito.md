---
id: 2026-1026-anticaptcha-plugin-de-navegador-gratuito
type: atom
certainty: solid
sources: [sources/2026-10-25-anti-captcha-pricing.md]
links: ["[[2026-1024-2captcha-integrado-en-4500-software-con-api-key]]", "[[2026-1024-2captcha-flujo-api-en-cinco-pasos-con-captcha-id]]", "[[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]"]
---

## Claim
AntiCaptcha incluye un **plugin de navegador gratuito** para **Chrome, Firefox y Safari** ("Free captcha solving tool for your favorite browser", con Chrome y Firefox vía `antcpt.com/eng/download/...` y Safari en la App Store), que funciona con "**No user interaction required**" — "Captchas are recognized automatically, in the background" — y se integra con "**iMacros, Puppeteer and Selenium**".

## Why It Matters
Es una **superficie de entrada que el corpus no tenía**: hasta ahora el captcha se compraba por API key en un producto de terceros ([[2026-1024-2captcha-integrado-en-4500-software-con-api-key]]) o por flujo asíncrono con `captcha ID` y polling ([[2026-1024-2captcha-flujo-api-en-cinco-pasos-con-captcha-id]]). Un plugin que **detecta el captcha solo, en segundo plano, sin interacción del usuario** es un modelo distinto: el coste de integración es cero y el coste de operación es una extensión instalada.
Para el vault esto importa por dos razones. La primera, operativa: con el plugin, el scraping manual-asistido y el scraping automatizado comparten **la misma pieza de resolución**, lo que elimina la discontinuidad "captcha resuelto a mano en el navegador" que hoy rompe cualquier pipeline. La segunda, de mercado: la Mention "Integrates smoothly with iMacros, Puppeteer and Selenium" coloca al plugin **en el mismo canal de integración que los frameworks de automatización** que ya usa el vault, lo que hace que el solver sea invocable desde un agente sin escribir código de API.
Y es la pieza que más se parece a lo que 2Captcha hizo con sus MCP: una capa que hace la elusión **invisible** al cliente final ([[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]). Pero mientras 2Captcha lo hizo como giro hacia *scraping para agentes*, AntiCaptcha lo hace como *comodity de elusión*, y esa diferencia de empaque es la que el thread debe registrar.
Nota: la captura **no** publica el precio del plugin, su política de uso, ni si el plugin tiene su propio consumo de saldo más allá de los captchas resueltos.

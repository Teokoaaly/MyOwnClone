---
id: 2026-1026-patchright-scrappey-clearcote-chromium-parcheado-como-servicio-de-un-endpoint
type: atom
certainty: tentative
sources: [sources/2026-10-25-patchright-playwright.md]
links: ["[[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]", "[[2026-1026-brightdata-browser-api-navegadores-remotos-para-automatizar]]"]
---

## Claim
El bloque de Scrappey es el único que **describe una alternativa comercial a construir la capa de navegador**, y la separa explícitamente de Patchright. El texto: *"Getting the browser past detection is one problem. Keeping proxies rotating, fingerprints current and sessions alive across a few million requests is a different one. **Scrappey takes the second problem**: one endpoint, solved pages back."* Sus cinco capacidades: **Clearcote** —"our own patched Chromium, maintained in-house, not a stock build"—; *"Several engines behind one endpoint — blocked on one stack, routed to another"*; *"Click, type, wait and scroll over the API — a real session, not a fetch proxy"*; proxies residenciales y de datacenter incluidos o bring your own; y **"Per request, no monthly minimum"**. El ejemplo es un `curl -X POST "https://publisher.scrappey.com/api/v1?key=YOUR_KEY"` con `{"cmd": "request.get", "url": "..."}`.

## Why It Matters
Es la versión **comercial y gestionada** de la misma idea que Patchright implementa como parche abierto: en ambos casos hay un Chromium **parcheado y mantenido en casa** —Clearcote aquí, el driver parcheado del driver de Patchright allí. La diferencia es de modelo: Scrappey **no vende el parche, vende el resultado**, con una estructura de pago por request sin mínimo mensual, mientras que Patchright vende el parche con un modelo de licencia Apache 2.0 y un coste de mantenimiento propio.
Lo que aporta al vault es una **tercera vía** en el modelo de coste de la elusión, que hasta ahora estaba solo en dos: comprar captcha por unidad ([[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]) o construir el navegador ([[2026-1026-brightdata-browser-api-navegadores-remotos-para-automatizar]]). Aquí aparece **pagar por página resuelta**, es decir, por unidad de resultado — el mismo patrón de "se paga por el éxito" que el Web Unlocker de Bright Data, pero con la promesa adicional de que la sesión es real (click, type, wait, scroll) y no una petición.
Y hay un elemento de resiliencia que el vault no tenía registrado en ninguna parte: **"several engines behind one endpoint — blocked on one stack, routed to another"**. Es una redundancia de stack anti-bot declarada como producto: si un motor te bloquea, el endpoint te enruta a otro. Eso convierte la detección en **un problema de portfolio de motores**, no de un motor concreto, y es un diseño que el vault no había visto en ninguna otra captura.

## Nota de verificación
Todo el bloque está transcrito literalmente del README, incluidos el endpoint y el ejemplo de `curl`. La captura **no** publica **ningún precio** de Scrappey, ni el número de motores, ni qué motores son, ni qué es exactamente Clearcote más allá de "patched Chromium". El código de descuento "PATCHRIGHT" es el único dato comercial. Todo lo que esta fuente dice de Scrappey es **claim del patrocinador**, no medición del vault, y no se ha observado ninguna llamada a la API.

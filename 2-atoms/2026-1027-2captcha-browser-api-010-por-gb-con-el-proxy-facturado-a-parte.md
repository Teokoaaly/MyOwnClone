---
id: 2026-1027-2captcha-browser-api-010-por-gb-con-el-proxy-facturado-a-parte
type: atom
certainty: solid
sources: [sources/2026-10-26-2captcha-pricing-browser-api.md]
links: ["[[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]", "[[2026-1026-brightdata-un-credito-por-request-y-cinco-por-mb-en-browser-api]]", "[[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]"]
---
## Claim
La página de precios del Browser API de 2Captcha publica **una sola fila**: "**Browser API | 1 GB Traffic | $0.1 / GB | 0% off | Top up**", y un texto explícito: *"Browser API costs **$0.10/GB**. **Proxy traffic is billed separately. With your own proxies, you pay only for browser traffic.**"* No hay planes, ni tramos, ni descuento por volumen: **0% off** y acción "**Top up**" (recarga de saldo), no "Buy" como en el Scraper API.

## Why It Matters
El dato de mayor peso del vault aquí es que **el proxy queda fuera del precio**: el Browser API es **navegador sin IP**, y el IP es una línea de factura separada. Eso significa que el coste total de la navegación con evasión es **$0,10/GB de tráfico de navegador + el coste del proxy que el cliente elija** — y el cliente puede traer proxies propios. El vault gana por primera vez una **componibilidad explícita de la cadena de elusión**: navegador y red son dos elementos que se pueden sustituir por separado, con precios de dos proveedores distintos ([[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]: $0.50/GB datacenter a $5/GB premium residencial).

Comparado con el corpus, **$0,10/GB es el extremo más bajo de la banda**: 5 veces más barato que el datacenter de DataImpulse ($0.50/GB) y 40 veces más barato que el PAYG de Bright Data a $4/GB ([[2026-1024-brightdata-payg-a-4-por-gb-sin-compromiso]]). Pero hay que leerlo con la misma cautela con la que el vault leyó el "5 créditos por MB" de Bright Data ([[2026-1026-brightdata-un-credito-por-request-y-cinco-por-mb-en-browser-api]]): **$0,10/GB no incluye el proxy**, mientras que buena parte de los $/GB del corpus **sí** incluye la IP. La comparación honesta es $0,10/GB **más** un proxy, contra un $/GB **con** proxy incluido: solo el cliente que ya tiene proxies baratos (o los usa de otra fuente) obtiene de verdad ese 5–40×.

La segunda lectura es de **estrategia de proveedor**: con "0% off", sin planes y solo recarga, el Browser API se ofrece como **una capacidad de coste marginal casi negligible** cuyo propósito no es el margen sino **atracción**: es la puerta de entrada por la que el cliente entra, y el ingreso está en el proxy y en el resto de la cartera (Scraper API, MCP, captchas). Es un producto **de gancho con precio de consumo** — el mismo patrón que el "0% off" del corpus de proxies en general, aplicado aquí a la capa de navegador.

## Nota de verificación
Precios y texto transcritos literalmente. La captura **no** publica: qué es un "GB" (¿tráfico de red total?), número de navegadores concurrentes, si el tráfico de proxy propio se factura aparte de forma verificable, SLA, ni el precio de los proxies de 2Captcha. El "0% off" se transcribe literal, sin inferir qué descuento sería posible.

---
id: 2026-1026-2captcha-browser-api-pricing-0-10gb
type: atom
certainty: solid
sources: [sources/2026-10-26-2captcha-pricing-browser-api.md]
links: ["[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]"]
---

## Claim
La página de precios del Browser API de 2Captcha publica una sola fila: **Browser API | 1 GB Traffic | $0.1 / GB | 0% off | Top up**, con un texto explícito: *"Browser API costs **$0.10/GB**. Proxy traffic is billed separately. With your own proxies, you pay only for browser traffic."* No hay planes, ni tramos, ni descuento por volumen: **0% off** y acción **"Top up"** (recarga de saldo), no **"Buy"** como en el Scraper API.

## Why It Matters
Este es el punto de entrada más bajo al ecosistema de 2Captcha: **$0,10/GB es el extremo más barato de la banda** — 5× más barato que el datacenter de DataImpulse ($0.50/GB) y 40× más barato que el PAYG de Bright Data a $4/GB. Sin embargo, hay una salvedad crítica: **$0,10/GB no incluye el proxy**, mientras que buena parte de los $/GB del corpus sí incluyen la IP. El coste total de la navegación con evasión es **$0,10/GB de tráfico de navegador + el coste del proxy que el cliente elija** — y el cliente puede traer proxies propios. El vault gana por primera vez una **componibilidad explícita de la cadena de elusión**: navegador y red son dos elementos que se pueden sustituir por separado, con precios de dos proveedores distintos.

## [FRICTION]
> [[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]] describe precios de proxy con IP incluida a $0.50/GB (datacenter) hasta $5/GB (premium residencial). Este átomo presiona esa creencia: el Browser API de 2Captcha separa navegador y red, de modo que el cliente que ya tiene proxies baratos obtiene realmente ese 5–40× de ahorro, mientras que quien paga proxy separado ve el costo total suma. Ambas no pueden ser completamente correctas a la vez: o el precio del Browser API es solo el costo del tráfico, o incluye algún nivel de servicio de red. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
Precios y texto transcritos literalmente. La captura no publica: qué es un "GB" (¿tráfico de red total?), número de navegadores concurrentes, si el tráfico de proxy propio se factura aparte de forma verificable, SLA, ni el precio de los proxies de 2Captcha. El "0% off" se transcribe literal, sin inferir qué descuento sería posible.
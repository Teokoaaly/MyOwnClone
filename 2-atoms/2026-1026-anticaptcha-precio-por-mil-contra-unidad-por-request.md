---
id: 2026-1026-anticaptcha-precio-por-mil-contra-unidad-por-request
type: atom
certainty: tentative
sources: [sources/2026-10-25-anti-captcha-pricing.md]
links: ["[[2026-1024-iproyal-web-unblocker-ia-a-1-dolar-por-1000-solicitudes]]", "[[2026-1024-brightdata-web-unlocker-resuelve-captcha-y-no-requiere-kyc]]", "[[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]]"]
---

## Claim
AntiCaptcha **no publica la unidad de cobro** en ningún sitio de la página capturada: la tabla da "Price per 1000" por tipo, pero **no hay ninguna frase del tipo "pay only for solved captchas"** ni equivalente, ni declaración de qué se factura cuando el captcha se resuelve mal, ni qué ocurre con la pestaña "Subscription" ([[2026-1026-anticaptcha-pestana-subscription-sin-cifras]]). El único dato de continuidad es el "**Busy: 1000 / Idle: 1200**" de la columna "Workers" ([[2026-1026-anticaptcha-capacidad-libre-uniforme-de-1000-por-minuto]]).

## Why It Matters
Es un **hueco de contrato, no una cifra**, y es el más relevante del corpus para el criterio del thread: 2Captcha publica explícitamente "**Pay only for solved captchas**" y "The server load does not affect the price", que es lo que permite al vault leer la partida como "coste marginal por resultado" ([[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]]). AntiCaptcha no dice nada equivalente.
La consecuencia comparativa es la que el thread ya affrontó en el caso de IPRoyal: el Web Unblocker de IPRoyal cobra **$1.00/1000 requests**, la unidad de entrada, mientras que el de 2Captcha cobra por extracción exitosa ([[2026-1024-iproyal-web-unblocker-ia-a-1-dolar-por-1000-solicitudes]]); y el Web Unlocker de Bright Data **reabsorbe la resolución de captcha dentro del producto** ([[2026-1024-brightdata-web-unlocker-resuelve-captcha-y-no-requiere-kyc]]). Con AntiCaptcha hay **tres unidades distintas** en el corpus de elusión —captchas resueltos, requests intentadas y "por 1000 de un tipo" sin contractualizar— y por tanto **ninguna de las tres filas de la tabla de coste por insumo es directamente comparable con las otras dos sin leer la letra pequeña del checkout**.
Eso obliga al vault a una regla que ya se insinúa en el thread: **la unidad de cobro hay que leerla proveedor por proveedor**, y un "price per 1000" sin cláusula de cobro **no es un precio, es una cotización**.
Nota: la captura **no** publica los términos de facturación, la política de reintento ni si hay reembolso por resolución fallida.

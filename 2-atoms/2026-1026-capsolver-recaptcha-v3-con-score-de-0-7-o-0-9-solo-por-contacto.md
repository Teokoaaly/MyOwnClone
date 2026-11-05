---
id: 2026-1026-capsolver-recaptcha-v3-con-score-de-0-7-o-0-9-solo-por-contacto
type: atom
certainty: solid
sources: [sources/2026-10-25-capsolver-home.md]
links: ["[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]", "[[2026-1024-gptgrok2api-registro-protocolo-sin-navegador-y-captcha-solver-integrado]]"]
---

## Claim
La fila de reCAPTCHA v3 de CapSolver lleva un texto que no es un precio: **"Please contact us if you can't get a higher score of 0.7 or 0.9"**. El precio publicado del tipo es **$1.0 / 1k** con velocidad **< 3S**, pero el **score** que produce el token se trata como una variable que se negocia por contacto, no como una garantía del producto de catálogo.

## Why It Matters
Es la primera vez que el vault ve **la calidad del token declarada como parte no catalogada del precio**. En 2Captcha el score aparecía solo en el blog ("How to Solve reCAPTCHA v3 and Get a Human Like (>0.7–0.9)") y el precio de catálogo cubría reCAPTCHA v3 a $1.45 — $2.99 sin mención de score ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]). Aquí el proveedor **degrada explícitamente el producto**: la cifra por 1000 compra "un reCAPTCHA v3", pero "un reCAPTCHA v3 con score ≥ 0.9" es un **contacto comercial aparte**.
Para el vault esto importa porque el score de reCAPTCHA v3 no es decorativo: es la variable que decide si el destino acepta la respuesta. Es decir, **el precio unitario de $0.001 por captcha no es el coste de un captcha aceptado**, porque la aceptación se cotiza aparte y fuera de la tabla. Es la primera grieta seria del modelo "el captcha es commodity cotizable" del thread.

## [FRICTION]
> [[2026-1024-gptgrok2api-registro-protocolo-sin-navegador-y-captcha-solver-integrado]] afirma que el captcha es "la partida que 2Captcha vende como commodity" y de ahí saca que hay tres vías —comprar por unidad, internalizar el navegador o evitar el destino—, con el coste medido en $ por captcha resuelto.
> Este átomo presiona esa clasificación en un punto: **un token de reCAPTCHA v3 no cotiza por unidad si su score se negocia por contacto**, de modo que la "commodity" se rompe justo en el tipo que la automatización de altas necesita —el que se usa para parecer humano. O el score es una variable del proveedor y entonces la commodity es solo el precio del token sin score, o el score es una propiedad del tipo y entonces **el precio de catálogo es incompleto**. Marcado para juicio humano, no auto-resuelto: la captura no publica el score medio, ni si el contacto tiene coste, ni qué significa "higher score".

Nota: la captura **no** publica precio, SLA ni condiciones del servicio "a medida" que ese contacto abriría; solo el mensaje en la propia fila.

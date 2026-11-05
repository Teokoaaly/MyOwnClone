---
id: 2026-1026-capsolver-nueve-tipos-con-precio-y-latencia
type: atom
certainty: solid
sources: [sources/2026-10-25-capsolver-home.md]
links: ["[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1026-anticaptcha-trece-tipos-con-precio-por-1000]]", "[[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]]"]
---

## Claim
La tabla de precios de la home de CapSolver publica **nueve tipos** con "Price per 1000" y una columna "Speed": reCAPTCHA v2 **$0.8 / 1k** (< 5S), reCAPTCHA v3 **$1.0 / 1k** (< 3S), reCAPTCHA v2 Enterprise **$1.0 / 1k** (< 3S), reCAPTCHA v3 Enterprise **$3.0 / 1k** (< 3S), AWS WAF **$2.0 / 1k** (< 3S), Geetest v3 / v4 **$1.2 / 1k** (< 5S), ImageToText **$0.4 / 1k** (< 1S), Cloudflare Turnstile **$1.2 / 1k** (< 3S) y Cloudflare Challenge **$1.2 / 1k** (< 10S). El rango de precio va de **$0.4 a $3.0 por 1000** y el de latencia de **< 1S a < 10S**.

## Why It Matters
Es el **tercer catálogo de solver con precios públicos del vault**, y el primero con **precio unitario cerrado por tipo** (una sola cifra por fila, sin rangos), al contrario que el de 2Captcha ($1 — $2.99, $1.45 — $50) ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]) y el de AntiCaptcha (precios con asteriscos y nota de volumen) ([[2026-1026-anticaptcha-trece-tipos-con-precio-por-1000]]).
El suelo del corpus baja a **$0.4 por 1000** (ImageToText) y el techo baja a **$3.0** (reCAPTCHA v3 Enterprise), de modo que la dispersión de este proveedor es de **7,5×**, intermedia entre las de 2Captcha (100×) y AntiCaptcha (10×).
La latencia, en cambio, **no vuelve a ser una propiedad del tipo**: el tipo más barato es el más rápido (< 1S) y el más caro no es el más lento —el lento es Cloudflare Challenge (< 10S) a precio medio ($1.2). Eso vuelve inservible el criterio "precio alto = captcha difícil = más lento" que el vault extrajo del catálogo de 2Captcha ([[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]]).

## [FRICTION]
> La §8.6 del thread [[economia-de-la-verificacion-y-reventa-de-cuentas]] afirma que "un captcha estándar no es un cuello de botella de tiempo" porque en 2Captcha los tipos estándar resuelven en **1–2 segundos**, y de ahí saca que "solo los dos tipos caros son además los lentos".
> Este átomo presiona esa afirmación en dos puntos: (1) la banda "< 5S" de CapSolver para reCAPTCHA v2 y Geetest muestra que **1–2 s no es un estándar del sector**, sino la cifra de un proveedor; (2) el caso de **Cloudflare Challenge a < 10S con precio medio ($1.2)** desarma la correlación precio-lentitud dentro de un mismo catálogo: un captcha de 10 s se puede comprar al mismo precio que uno de 3 s. Marcado para juicio humano, no auto-resuelto: la captura no publica percentiles ni si los "< 10S" son media o techo.

Nota: la captura **no** publica el tipo de cambio, el IVA, los cargos por API ni el desglose de los paquetes; los precios son "price per 1000" de la tabla de la home.

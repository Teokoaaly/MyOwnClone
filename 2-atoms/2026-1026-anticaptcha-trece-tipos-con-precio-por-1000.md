---
id: 2026-1026-anticaptcha-trece-tipos-con-precio-por-1000
type: atom
certainty: solid
sources: [sources/2026-10-25-anti-captcha-pricing.md]
links: ["[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1024-2captcha-arkose-funcaptcha-50-dolares-por-1000]]", "[[2026-1024-2captcha-hcaptcha-y-geetest-ausentes-del-catalogo-publicado]]"]
---

## Claim
La tabla "Supported captcha types and prices" de anti-captcha.com publica **trece tipos** con "Price per 1000": Images **$0.5 - $0.7\***, reCAPTCHA v2 **$0.95 - $2\***, reCAPTCHA v3 **$1 - $2\*\***, reCAPTCHA Enterprise v2/v3 **$5**, GeeTest **$1.8**, Arkose Labs **$3**, Turnstile **$2**, Custom Tasks **$2**, Object Coordinates **$2**, Prosopo **$2**, Friendly Captcha **$2**, Amazon WAF **$2**, Altcha **$2**. La home resume el suelo como "Starting from 0.5USD per 1000 images, depending on your daily spending volume" y "prices starting from $0.5 per 1000 captchas".

## Why It Matters
Es el **segundo catálogo de solver con precios públicos** del vault, y a diferencia del de 2Captcha ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]) el suyo está **cerrado**: trece filas, sin "Show more", y con un suelo de $0.5 y un techo de $5 — una dispersión de **10×** frente a la de 2Captcha ($0.5 a $50, 100×) ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]).
La diferencia de cobertura también es real: AntiCaptcha publica **GeeTest a $1.8** como producto de catálogo, tipo que en la captura de 2Captcha no aparecía en ninguna parte ([[2026-1024-2captcha-hcaptcha-y-geetest-ausentes-del-catalogo-publicado]]), y añade tipos que 2Captcha no lista: Custom Tasks, Object Coordinates, Prosopo, Friendly Captcha y reCAPTCHA Enterprise v2/v3 como fila propia.
Y es la primera vez que un catálogo del vault incluye **tipos de respuesta no textual** (Object Coordinates: las coordenadas del objeto en la imagen), que no son un token opaco sino un dato que hay que consumir en lógica de automation.
Nota: la captura **no** publica el tipo de cambio, el IVA, los cargos por API ni el contenido de la pestaña "Subscription"; los precios son "price per 1000" sueltos en la home.

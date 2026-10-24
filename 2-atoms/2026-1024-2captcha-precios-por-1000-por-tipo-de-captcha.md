---
id: 2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha
type: atom
certainty: solid
sources: [sources/2026-10-23-2captcha-solver.md]
links: ["[[2026-1024-2captcha-arkose-funcaptcha-50-dolares-por-1000]]", "[[2026-1024-2captcha-altcha-299-y-17-segundos-el-mas-lento]]", "[[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]"]
---
## Claim
La tabla "Order captchas: types and prices" da **precio por 1000** para ocho tipos visibles: reCAPTCHA v2 **$1 — $2.99**, Image Captcha **$0.5 — $1**, Cloudflare Turnstile **$1.45**, reCAPTCHA v3 **$1.45 — $2.99**, reCAPTCHA Enterprise **$1 — $2.99**, Arkose Labs captcha (FunCaptcha) **$1.45 — $50**, Amazon captcha **$1.45**, ALTCHA **$2.99**. El precio de referencia del catálogo va de **$0.5 a $2.99 por 1000**, con dos outliers muy por encima: FunCaptcha hasta **$50** y ALTCHA a **$2.99**.

## Why It Matters
Es el **precio de referencia del mercado de elusión anti-bot** con cifras públicas, algo que el vault no tenía: el coste de resolver un captcha está en el orden de **milésimas de dólar por captcha**, varios órdenes de magnitud por debajo del coste de una verificación SMS ([[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]). Eso significa que el captcha **no es** la barrera cara de la automatización: es una partida de céntimos por mil.
Pero la dispersión interna es enorme y no es uniforme: un captcha de reCAPTCHA v2 cuesta entre $1 y $2.99 por mil, mientras un FunCaptcha puede llegar a $50 por mil ([[2026-1024-2captcha-arkose-funcaptcha-50-dolares-por-1000]]) y un ALTCHA son $2.99 fijos ([[2026-1024-2captcha-altcha-299-y-17-segundos-el-mas-lento]]). Elegir mal el tipo de captcha que hay que resolver multiplica el coste por 33.
## [FRICTION]
> [[2026-1023-midjourney-proxy-edicion-plus-ampliada]] describe la edición plus de un proxy de imagen como la capa que vive **por encima** del core público, y coloca explícitamente entre sus funciones premium la "verificación automática de popups" y la resolución de caída de token. Es decir, ahí la resolución de captchas es una **función que el proveedor del servicio construye y cobra** dentro de su propio tier premium.
> Este átomo presiona esa creencia en un punto: esa misma capacidad existe como **insumo commoditizado de terceros**, con precio de lista público — $0.5 a $2.99 por mil en los tipos estándar ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]) — y con SLA declarado (99.9% uptime). Externalizar la verificación de popups a un proveedor con API key ([[2026-1024-2captcha-integrado-en-4500-software-con-api-key]]) es más barato que mantenerla como función premium propia, salvo que el volumen o la latencia lo justifiquen.
> Ambas no pueden ser completamente correctas a la vez: o la resolución de captchas es un **core técnico** que un proveedor debe construir para diferenciarse de sus competidores, o es una **commodity** con precio de mercado. Marcado para juicio humano, no auto-resuelto: la fuente no publica los precios de la edición plus, así que no hay comparación de coste posible.

Nota: la captura **no** publica el tipo de cambio, el IVA, los cargos por API ni los planes de suscripción; los precios son "price per 1000" sueltos en la home.

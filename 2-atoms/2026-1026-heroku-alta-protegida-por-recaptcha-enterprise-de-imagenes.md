---
id: 2026-1026-heroku-alta-protegida-por-recaptcha-enterprise-de-imagenes
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-signup.md]
links: ["[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1024-2captcha-arkose-funcaptcha-50-dolares-por-1000]]", "[[2026-1024-2captcha-hcaptcha-y-geetest-ausentes-del-catalogo-publicado]]"]
---

## Claim
El alta de Heroku está protegida por **reCAPTCHA Enterprise**, no por reCAPTCHA v2 ni por un simple checkbox. El pie lo declara literalmente —"This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply."— y el enunciado del desafío es **"Select all images with crosswalks"** sobre una **rejilla de 3×3 imágenes**, con botón **"Verify"**. Las nueve URLs de imagen apuntan a **`www.recaptcha.net/recaptcha/enterprise/payload?p=…`**, es decir **el endpoint `enterprise`**, no el de `v2` ni el de `v3`. La captura también reproduce el texto de error del componente: **"Recaptcha requires verification."**

## Why It Matters
Esto convierte a Heroku en **el primer destino real de alta documentado en el vault que usa el tipo Enterprise**, y por tanto en el caso donde la aritmética de la thread se puede confrontar con la realidad del catálogo: 2Captcha cotiza **reCAPTCHA Enterprise a $1 – $2,99 por 1000** y **Arkose/FunCaptcha a $1,45 – $50 por 1000** ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]], [[2026-1024-2captcha-arkose-funcaptcha-50-dolares-por-1000]]), mientras que el vault ya registró que **hCaptcha y Geetest no constan en el catálogo publicado** ([[2026-1024-2captcha-hcaptcha-y-geetest-ausentes-del-catalogo-publicado]]). Heroku, con 65 millones de apps declaradas, es un destino **masivo** — de los que justifican un precio de captcha y una latencia de resolución en la decisión.
Y hay un detalle que solo se ve en la URL: el payload se sirve desde **`recaptcha.net`**, no desde `google.com`, y la ruta literal es `recaptcha/enterprise/payload`. El vault no puede deducir de ahí una política antifraude concreta, pero sí registrar que **la integración es Enterprise, lo que en la práctica significa que la señal de riesgo se evalúa server-side y el desafío se adapta** — y eso es exactamente lo que separa un captcha "de catálogo" de uno caro.

## [FRICTION]
> [[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]] afirma que el catálogo publica **precio por 1000 para ocho tipos** y que "reCAPTCHA Enterprise" figura con **$1 — $2,99**, agrupado con los tipos estándar; y [[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]] le asigna **2 segundos** de resolución.
> Este átomo presiona esa creencia en un punto concreto: **el reCAPTCHA Enterprise que aparece en una página real de alta no es el mismo objeto que la línea "reCAPTCHA Enterprise" del catálogo**. En la captura de Heroku el desafío es un **grid de 3×3 imágenes con la instrucción "select all images with crosswalks"** —es decir, una resolución de tipo *image puzzle*—, mientras que el catálogo de 2Captcha tiene una **línea separada y más barata, "Image Captcha", a $0,5 – $1 por 1000**. El vault no puede saber con este material si el payload `enterprise` que sirve Heroku se factura como "Enterprise" ($1 – $2,99) o como "Image Captcha" ($0,5 – $1), ni si el precio por 1000 cubre un token o una rejilla resuelta.
> Ambas no pueden ser simultáneamente la base de una comparación de coste: o "reCAPTCHA Enterprise" del catálogo es un tipo concreto (token) que **no** es lo que Heroku exige, o el catálogo no distingue el modo de desafío y su precio no es aplicable a un alta real. Marcado para juicio humano, no auto-resuelto: la fuente 2Captcha no publica la taxonomía de lo que cubre la línea Enterprise.

---
id: 2026-1026-capsolver-geetest-v3-v4-y-aws-waf-tipos-que-el-catalogo-de-2captcha-no-publica
type: atom
certainty: solid
sources: [sources/2026-10-25-capsolver-home.md]
links: ["[[2026-1024-2captcha-hcaptcha-y-geetest-ausentes-del-catalogo-publicado]]", "[[2026-1026-anticaptcha-trece-tipos-con-precio-por-1000]]", "[[2026-1026-capsolver-nueve-tipos-con-precio-y-latencia]]"]
---

## Claim
El catálogo de CapSolver publica **Geetest v3 / v4 a $1.2 / 1k** (< 5S) y **AWS WAF a $2.0 / 1k** (< 3S). Geetest **no aparecía en ninguna parte** de la página de 2Captcha capturada el 2026-10-23 —ni en la lista de "Supported captchas" ni en la tabla de precios— y AWS WAF tampoco: allí la fila equivalente era "Amazon captcha" a $1.45.

## Why It Matters
La fricción 13 del thread [[economia-de-la-verificacion-y-reventa-de-cuentas]] afirma que **Geetest no se puede cotizar** con el catálogo publicado de 2Captcha ([[2026-1024-2captcha-hcaptcha-y-geetest-ausentes-del-catalogo-publicado]]). Con esta captura, la afirmación se **corrige en su alcance**: Geetest **sí es cotizable**, en otro proveedor, a **$1.2 por 1000** — con un precio un 17 % por debajo del "Amazon captcha" de 2Captcha y una latencia (< 5S) dentro de la banda estándar de ese proveedor. Lo que **no** está cotizado en ningún catálogo del vault sigue siendo **hCaptcha**: no aparece en 2Captcha, ni en AntiCaptcha ([[2026-1026-anticaptcha-trece-tipos-con-precio-por-1000]]), ni en CapSolver.
La lección operativa es la que importa para cualquier cliente del sector: **la no cotizabilidad de un tipo es una propiedad del catálogo, no del tipo**. Geetest cuesta menos en CapSolver que en la única fila comparable de 2Captcha, y aun así era "no cotizable" con esa fuente.

## [FRICTION]
> [[2026-1024-2captcha-hcaptcha-y-geetest-ausentes-del-catalogo-publicado]] sostiene que "**hCaptcha y Geetest no están en el escaparate**" y que, por tanto, "no se pueden comprar como producto de catálogo publicado", dejando abierta la hipótesis de que estén tras el "Show more".
> Este átomo presiona esa afirmación en un punto concreto: **Geetest es un producto de catálogo publicado de otro proveedor del mismo mercado a $1.2/1000**, con lo que la hipótesis de "solo estaba tras el Show more" queda como explicación incompleta de por qué el vault no pudo cotizarlo. La redacción correcta sería "no cotizable **con la captura de 2Captcha**", y el tipo que **sigue** sin cotizar en todo el corpus es **hCaptcha**. Marcado para juicio humano, no auto-resuelto: la captura no permite afirmar que 2Captcha no soporte Geetest; solo que no lo publica en la página capturada.

Nota: la captura **no** publica la variante de AWS WAF que se resuelve (con o sin challenge), ni el detalle de qué es "AWS WAF" frente a "Amazon captcha" de 2Captcha.

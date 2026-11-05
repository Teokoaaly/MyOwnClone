---
id: 2026-1026-anticaptcha-altcha-a-2-dolares-y-5-segundos
type: atom
certainty: solid
sources: [sources/2026-10-25-anti-captcha-pricing.md]
links: ["[[2026-1024-2captcha-altcha-299-y-17-segundos-el-mas-lento]]", "[[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]]", "[[2026-1026-anticaptcha-arkose-labs-a-3-dolares-por-1000]]"]
---

## Claim
AntiCaptcha publica **Altcha a $2 por 1000** con velocidad de resolución de **5 s**, tarea `AltchaTaskProxyless`. Es el mismo tipo que 2Captcha publica como el más caro y el más lento de su catálogo.

## Why It Matters
Duplica el punto de fricción de Arkose en el otro extremo del catálogo de 2Captcha: el átomo de 2Captcha llama a ALTCHA "el techo de coste **sin rango**: frente a reCAPTCHA v2 ($1 — $2.99, 2 sec) es más lento en 8,5 veces" y lo señala como "el punto donde el mercado anti-bot se está endureciendo" ([[2026-1024-2captcha-altcha-299-y-17-segundos-el-mas-lento]]). AntiCaptcha lo vende a **$2 y 5 s**, es decir, por debajo del precio de reCAPTCHA v2 de 2Captcha y con una latencia **3,4 veces menor** que los 17 sec del otro proveedor.
Juntos, Arkose a $3/5 s y ALTCHA a $2/5 s en AntiCaptcha **desarman el argumento de hardening**: si el captcha de deslizador es el último bastón del WAF, entonces el precio y la latencia de resolverlo **son proveedor-dependientes**, y el vault no puede inferir dificultad de un precio de catálogo.

## [FRICTION]
> [[2026-1024-2captcha-altcha-299-y-17-segundos-el-mas-lento]] afirma que ALTCHA es "el único tipo con **precio único cerrado de $2.99 por 1000** y el de **velocidad más lenta de la tabla: 17 sec**", y lo usa como indicador de que "la industria del WAF se está moviendo hacia resistencias que el scraping directo no salva".
> Este átomo presiona eso en el punto de la latencia: **17 sec no es una propiedad del captcha de deslizador**, es la latencia de un proveedor. Con $2 y 5 s, el mismo tipo entra en el rango de latencia que 2Captcha reserva a sus tipos estándar ([[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]]). La "generación posterior de resistencias" sigue siendo un hecho plausible, pero **su coste y su latencia de resolución son variables de proveedor**, no un techo del mercado: el vault no puede citar "$2.99 y 17 segundos" como el precio de atravesar un ALTCHA.
> Ambas no pueden ser completamente correctas a la vez: o el captcha de deslizador impone una latencia estructural de ~17 s, o el pool de trabajadores especializados de 2Captcha para ALTCHA es lo que la produce. Marcado para juicio humano, no auto-resuelto: la captura de 2Captcha no explica el mecanismo de sus 17 sec ni su 203 captchas libres por minuto.

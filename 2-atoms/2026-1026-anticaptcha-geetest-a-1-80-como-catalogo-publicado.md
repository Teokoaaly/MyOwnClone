---
id: 2026-1026-anticaptcha-geetest-a-1-80-como-catalogo-publicado
type: atom
certainty: solid
sources: [sources/2026-10-25-anti-captcha-pricing.md]
links: ["[[2026-1024-2captcha-hcaptcha-y-geetest-ausentes-del-catalogo-publicado]]", "[[2026-1026-anticaptcha-trece-tipos-con-precio-por-1000]]", "[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]"]
---

## Claim
AntiCaptcha publica **GeeTest a $1.8 por 1000**, con 5 s de resolución y tarea `GeeTestTaskProxyless`. Es un tipo de catálogo **con precio cerrado**, no un rango.

## Why It Matters
Es la corrección directa de una limitación que el vault había registrado como **falta de dato**: el átomo de 2Captcha decía que "hCaptcha y Geetest **no aparecen en ninguna parte** de la página" y concluía que "**no se pueden comprar como producto de catálogo publicado**" ([[2026-1024-2captcha-hcaptcha-y-geetest-ausentes-del-catalogo-publicado]]). AntiCaptcha publica Geetest a $1.8, de modo que **la ausencia era del catálogo capturado, no del mercado**: el tipo se compra con precio de lista en otro proveedor.
El vault ya tenía el precio de catálogo de los tipos estándar de 2Captcha como referencia ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]); lo que faltaba era el precio de este tipo concreto. Eso no contradice la observación original —la captura de 2Captcha efectivamente no lo mostraba— pero **cambia la conclusión operativa**: el vault ya puede cotizar Geetest ($1.8/1000) y, por tanto, dejar de tratarlo como línea no cotizable. Para el thread, la fila "captcha" de la tabla de coste por insumo puede incluir un tipo que antes era un hueco.
Y aporta el dato de cobertura que faltaba: **GeeTest es el único tipo del corpus que no es de Google, Cloudflare, Microsoft, Amazon, Arkose ni un captcha de imagen** — es un captcha de proveedor chino que 2Captcha no listaba y AntiCaptcha sí.
Nota: la captura **no** publica qué variantes de GeeTest cubre, ni el desglose por subtipo (slide, puzzle, click), ni si el precio de $1.8 es agregado.

## [FRICTION]
> [[2026-1024-2captcha-hcaptcha-y-geetest-ausentes-del-catalogo-publicado]] afirma que "hCaptcha y Geetest no están en el escaparate" y que, por tanto, "si un destino de scraping usa hCaptcha, el coste y la latencia de esa resolución no se pueden cotizar con esta fuente", cerrando con la cautela de que "la captura **no** permite afirmar que hCaptcha o Geetest no se soporten; solo que no constan en la página capturada".
> Este átomo presiona el uso operativo de esa afirmación, no su literales: la caution del átomo viejo ("no constan en la página capturada") es correcta, pero la **conclusión que el vault extrapuso** —tratar Geetest como no cotizable— queda desmentida por el catálogo de AntiCaptcha. El límite correcto no es "no se puede cotizar", sino "**no se puede cotizar con la captura de 2Captcha**". Y hCaptcha sigue sin cotizar: **ninguno de los dos proveedores del corpus publica hCaptcha**, lo cual sí es un hueco de mercado del vault.
> Ambas no pueden ser completamente correctas a la vez: o la captura de 2Captcha era parcial (el "Show more" sin expandir lo explicaría) y el átomo viejo debía acotar su conclusión al catálogo visible, o hCaptcha y Geetest son tipos de catálogo residual y no se pueden comprar en ninguno de los dos proveedores. Marcado para juicio humano, no auto-resuelto: **la captura de AntiCaptcha tampoco publica hCaptcha**, así que la ausencia de hCaptcha en el corpus es una observación de dos capturas y no un inventario.

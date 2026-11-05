---
id: 2026-1027-2captcha-keycaptcha-37-segundos-como-nuevo-techo-de-latencia
type: atom
certainty: solid
sources: [sources/2026-10-26-2captcha-pricing-captcha.md]
links: ["[[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]]", "[[2026-1024-2captcha-altcha-299-y-17-segundos-el-mas-lento]]", "[[2026-1027-2captcha-catalogo-completo-de-48-filas-de-captcha]]"]
---
## Claim
Con las 48 filas del catálogo visibles, el **techo de latencia de 2Captcha sube de 17 a 37 segundos**: **KeyCAPTCHA** es el tipo más lento, con **37 sec** de "Solving speed", precio **$2.99 por 1000** y **3,452** de capacidad libre por minuto. Le siguen **Cutcaptcha** y **Prosopo Procaptcha** a **24 sec** ($1.45, 4.500 y 4.563 libres/min), **Lemin captcha** a **20 sec** ($1.45, 4.562), **Arkose Labs captcha (FunCaptcha)** a **18 sec** ($1.45 — $50, 578), **Yidun - NeCaptcha** a **17 sec** ($2.99, 203), **TSPD captcha** a **16 sec** ($2.99, 203), **ALTCHA** a **15 sec** ($2.99, 203) y **Akamai** a **15 sec** ($0, 203). Son **7 de los 48 tipos** los que superan los 15 segundos y **9 los que los igualan o superan**, con una mediana de 18 segundos en esa banda lenta.

## Why It Matters
El vault tenía un "presupuesto de latencia" de dos bandas: 1–2 segundos para lo estándar y 16–17 segundos para dos outliers ([[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]]). Con el catálogo completo, **la banda lenta no tiene techo fijo**: hay tipos a 15, 16, 17, 18, 20, 24 y 37 segundos, y los tres más lentos —KeyCAPTCHA, Cutcaptcha y Prosopo— **no son los caros**: KeyCAPTCHA cuesta $2.99 (el peldaño alto pero no el techo) y los otros dos **$1.45**, el peldaño más habitual del catálogo.

Eso rompe de forma más fuerte que antes la inferencia "precio alto = captcha difícil = más lento" que el thread sostiene en la §8.6: **el tipo más lento cuesta $2.99 —el peldaño alto, pero no el techo de $50— y los dos siguientes $1.45, el peldaño más habitual**, mientras que los tipos más rápidos (1 sec) incluyen tanto el peldaño más barato ($0.5 — $1, Image y Normal Captcha) como el alto ($1.45, reCAPTCHA v3). Y abre la lectura correcta: **la latencia mide la familia del reto, no su precio**. Los captchas de puzzle interactivo y los de puzzle posicional (KeyCAPTCHA, Cutcaptcha, Prosopo, Lemin) son los que se resuelven con intervención humana o con modelo caro de visión; los detectores antibot con precio $0 resuelven en 8–15 s ([[2026-1027-2captcha-akamai-kasada-y-perimeterx-publicados-a-cero-por-1000]]).

Para un pipeline esto es un dato de **concurrencia**: con 3,452 libres/min y 37 s por token, el techo teórico de KeyCAPTCHA es ~5.598 tokens/hora (~134.348/día), frente a los ~19.488/día de ALTCHA con 203/min y 15 s. La latencia y la capacidad **multiplican**, no se suman: por eso el tipo "caro" no es necesariamente el que limita el volumen.

## [FRICTION]
> [[2026-1024-2captcha-altcha-299-y-17-segundos-el-mas-lento]] afirma que ALTCHA es "el de **velocidad más lenta de la tabla: 17 sec**" y que su combinación "precio cerrado + slowest + menor capacidad libre" señala "el punto donde el mercado anti-bot se está endureciendo".
> Este átomo presiona esa afirmación en tres puntos verificables: (1) en la captura del 2026-10-26 **ALTCHA figura a 15 sec, no a 17**, de modo que ni siquiera su cifra de latencia quedó congelada; (2) **ALTCHA no es el más lento**: KeyCAPTCHA está a **37 sec**, más del doble; (3) la tesis de "endurecimiento" **no se sostiene con el catálogo completo**, porque los tipos más lentos y caros en tiempo (KeyCAPTCHA a 37 s, $2.99) no son los más caros en dinero, y el más caro del catálogo (FunCaptcha, hasta $50) está a **18 sec**, en la banda media-alta. Ambas no pueden ser completamente correctas: o el endurecimiento se manifestaba en los tipos de slider —y ALTCHA es un slider, pero ya no es el más lento— o el endurecimiento no es la lectura correcta de la columna de latencia. Marcado para juicio humano, no auto-resuelto: la captura no explica qué mide "Solving speed" ni si es media, mediana o valor típico.

Nota: la captura **no** publica percentiles de latencia, ni tasa de éxito por tipo, ni qué ocurre al saturarse la capacidad libre.

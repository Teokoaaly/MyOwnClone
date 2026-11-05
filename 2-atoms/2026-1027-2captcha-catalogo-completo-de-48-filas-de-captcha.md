---
id: 2026-1027-2captcha-catalogo-completo-de-48-filas-de-captcha
type: atom
certainty: solid
sources: [sources/2026-10-26-2captcha-pricing-captcha.md]
links: ["[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1024-2captcha-capacidad-libre-por-minuto-como-proxy-de-cola]]", "[[2026-1024-2captcha-hcaptcha-y-geetest-ausentes-del-catalogo-publicado]]"]
---
## Claim
La tabla de precios de `2captcha.com/pricing` capturada el 2026-10-26 tiene **48 filas** —cada una con cuatro datos: tipo, "Price per 1000", "Solving speed" y "Free capacity, per minute"— frente a las **ocho filas visibles** tras el botón "Show more" de la captura del 2026-10-23 ([[2026-1024-2captcha-hcaptcha-y-geetest-ausentes-del-catalogo-publicado]]). El reparto de los 48 precios por 1000 es: **$2.99 en 14 tipos**, **$1.45 en 13**, **$0.5 — $1 en 7**, **$1 — $2.99 en 4**, **$1.2 en 3**, **$0 en 3**, **$0.5 en 2**, **$1 en 1** y **$1.45 — $50 en 1** (Arkose Labs captcha / FunCaptcha). Los tipos incluyen variantes que antes no aparecían: **reCAPTCHA v2 Callback**, **reCAPTCHA v2 Invisible**, **GeeTest captcha**, **DataDome captcha**, **Imperva**, **Prosopo Procaptcha**, **TikTok Captcha**, **Tencent (TenDI)**, **KeyCAPTCHA**, **TSPD captcha**, **Basilisk captcha**, **Alibaba captcha**, **Binance captcha**, **Yidun - NeCaptcha**, **Capy Puzzle captcha**, **atbCAPTCHA**, **Lemin captcha**, **MTCaptcha**, **CaptchaFox**, **Cutcaptcha**, **Friendly captcha**, **Temu captcha**, **VK captcha**, **Hunt captcha**, **Bounding Box**, **CyberSiARA captcha** y los captchas textuales genéricos (Normal Captcha, Russian Captcha, Chinese Captcha, Number Captcha, Math Captcha, Text Captcha, Click captcha, Slider Captcha, Rotate captcha, Image Captcha, Audio captcha).

## Why It Matters
La primera consecuencia es **de método y cierra una laguna del vault**: el "Show more" sin expandir era la razón por la que el átomo de precios de 2024 describía un catálogo de "ocho tipos visibles" y el de hCaptcha/Geetest afirmaba que "el catálogo real es al menos más grande que ocho filas". Con esta captura, **el catálogo publicado queda enumerable por primera vez**: 48 filas, y por tanto la pregunta "¿qué tipos compra un cliente de 2Captcha?" tiene respuesta enumerada, no una cota.

La segunda es **de estructura de precios**: el catálogo no es un continuo de precios sino una **escalera discreta de nueve valores** ($0, $0.5, $1, $1.2, $1.45, $2.99 y los dos rangos $0.5—$1 y $1—$2.99, más el techo de $50), y **22 de los 48 tipos tienen precio cerrado de $1.45 o menos** (34 si se cuenta el precio de entrada de los tipos con rango). Es decir, la dispersión que el vault venía midiendo ("de $0.5 a $2.99, con FunCaptcha hasta $50") era el efecto de una escalera de precios con tres o cuatro PELDAÑOS muy poblados, no un reparto continuo. Para un modelador de coste esto importa: **elegir tipo de captcha no es elegir un precio, es elegir un peldaño**, y el peldaño habitual es $1.45.

La tercera es de **superficie de cobertura**: los 48 tipos incluyen detectores antibot que no son "captchas" en el sentido del puzzle (Akamai, Kasada, PerimeterX, Imperva, DataDome), lo que confirma que el objeto que 2Captcha vende es **"el paso por un control anti-bot"** y no "un captcha". Ver [[2026-1027-2captcha-akamai-kasada-y-perimeterx-publicados-a-cero-por-1000]].

## [FRICTION]
> [[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]] afirma que "el precio de referencia del catálogo va de **$0.5 a $2.99 por 1000**" y usa ese rango como la medida de la dispersión del mercado de elusión anti-bot.
> Este átomo presiona esa cifra en dos puntos verificables: (1) el suelo del catálogo **no es $0.5**: con tres tipos a **$0** (Akamai, Kasada, PerimeterX) el rango publicado es **$0 — $50**; (2) el techo de $50 sigue siendo único y el suelo es ahora cero, de modo que el factor de dispersión **pasa de 100× a indefinido**. Ambas no pueden ser la misma afirmación: o el rango del vault era el del catálogo visible de ocho filas, o es el del catálogo real de 48.
> Marcado para juicio humano, no auto-resuelto: el átomo viejo ya advertía que el "Show more" hacía la captura parcial, y esta captura confirma que la cifra de $0.5 era una cota de la ventana visible, no del catálogo.

Nota: la captura **no** publica si el catálogo de 48 filas es completo ni si hay más detrás de una paginación; el recuento de 48 es una medición sobre el fichero de `sources/`, no una declaración del proveedor.

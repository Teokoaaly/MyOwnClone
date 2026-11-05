---
id: 2026-1027-2captcha-click-slider-y-perimeterx-con-64-libres-por-minuto
type: atom
certainty: solid
sources: [sources/2026-10-26-2captcha-pricing-captcha.md]
links: ["[[2026-1024-2captcha-capacidad-libre-por-minuto-como-proxy-de-cola]]", "[[2026-1027-2captcha-catalogo-completo-de-48-filas-de-captcha]]", "[[2026-1024-2captcha-altcha-299-y-17-segundos-el-mas-lento]]"]
---
## Claim
Con las 48 filas visibles, la columna "Free capacity, per minute" de 2Captcha **baja de 203 a 64**: **Click captcha** ($1.2, 11 sec), **Slider Captcha** ($1.2, 9 sec) y **PerimeterX** ($0, 9 sec) publican **64 captchas libres por minuto**. Los 203/min que hasta ahora eran el mínimo del catálogo corresponden a **ALTCHA, Akamai, Kasada, Audio captcha, CaptchaFox, Temu, Yidun - NeCaptcha, Hunt captcha, TSPD captcha, Basilisk captcha, Alibaba captcha y Binance captcha** (doce tipos). El siguiente peldaño hacia arriba es **Capy Puzzle captcha con 263**, y después **Rotate captcha con 567** y **Arkose Labs con 578**.

## Why It Matters
El suelo de capacidad es el dato que dimensiona un pipeline, y **ha bajado un 68 %** respecto a lo que el vault tenía registrado. Con 64/min y 11 segundos de resolución, el techo de Click captcha es de **~349 tokens/hora** y el de Slider y PerimeterX de **~427/hora** — el orden de **8.000–10.000 al día**, muy por debajo de los 19.488/día que el vault calculaba para ALTCHA con 203/min y 15 s. Es decir: **el tipo que el vault creía "el más lento y el de menor capacidad" no era ninguno de los dos**: hay tipos que resuelven en 9–11 segundos (más rápido que ALTCHA) y solo pueden entregar 64 por minuto.

La consecuencia estructural es que **capacidad y latencia no se ordenan juntas**, y por tanto el dimensionado necesita las dos columnas multiplicadas y no sumadas: Image Captcha (1 sec, 12.000/min ≈ 17,3 millones/día) y KeyCAPTCHA (37 sec, 3.452/min ≈ 134.348/día) están a un orden de magnitud del límite de capacidad, mientras Click y Slider lo están a un orden de magnitud del límite de concurrencia. Y hay una lectura incómoda en la combinación de Slider Captcha y ALTCHA: **el vault trata ALTCHA como "el captcha de deslizador", pero el catálogo publica Slider Captcha como un tipo aparte con su propio precio ($1.2 frente a $2.99) y su propia capacidad (64 frente a 203)**. Es decir, **"ser un slider" no define un precio**: hay dos sliders con precios que difieren ×2,5 y capacidades que difieren ×3,2.

## [FRICTION]
> [[2026-1024-2captcha-capacidad-libre-por-minuto-como-proxy-de-cola]] afirma que la columna va "de **203 a 12.000** de capacidad por minuto" y que "**ALTCHA baja a 203 por minuto** — unos 59 veces menos que Image Captcha", y de ahí saca que el pool de trabajadores por tipo está ordenado de forma distinta al precio.
> Este átomo presiona esa afirmación en tres puntos verificables: (1) el **suelo real es 64**, no 203, y el intervalo de dispersión de la columna pasa de **59× a 187×** (12.000 ÷ 64); (2) los tipos con **64/min no son los caros**, sino **$1.2 y $0** — mientras que los tipos a **$2.99** como ALTCHA, Yidun o TSPD comparten las 203/min, de modo que "el tipo de captcha que además es el más caro por mil es el que además tiene menos capacidad" **ya no se sostiene** en el catálogo completo; (3) la dispersión de capacidad **no ordena por precio** en ninguna dirección monótona: hay tipos a **$0** con 203/min y a **$0** con 64/min en el mismo catálogo. Ambas no pueden ser completamente correctas: o la capacidad libre es un proxy del pool de trabajadores por tipo con ordenación propia (y entonces el mínimo de ese pool es 64, no 203, y no está correlacionado con el precio), o la columna mide otra cosa. Marcado para juicio humano, no auto-resuelto: la fuente no define "Free capacity" ni publica qué ocurre al saturarse.

Nota: la captura **no** define la unidad ni el periodo de "Free capacity, per minute", ni publica tasa de éxito por tipo, ni el comportamiento al saturar la cola.

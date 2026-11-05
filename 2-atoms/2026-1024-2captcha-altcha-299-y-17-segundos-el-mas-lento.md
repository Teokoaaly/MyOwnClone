---
id: 2026-1024-2captcha-altcha-299-y-17-segundos-el-mas-lento
type: atom
certainty: solid
sources: [sources/2026-10-23-2captcha-solver.md]
links: ["[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]]", "[[2026-1024-2captcha-capacidad-libre-por-minuto-como-proxy-de-cola]]"]
---
## Claim
**ALTCHA** es el único tipo con **precio único cerrado de $2.99 por 1000** y el de **velocidad más lenta de la tabla: 17 sec**. La captura añade el dato cualitativo que lo explica: "A key feature of this captcha is that it is designed as a slider, making it difficult for bots to bypass" — es un captcha de deslizador. Su "free capacity, per minute" es de **203**, la más baja del catálogo.

## Why It Matters
ALTCHA define el techo de coste **sin rango**: frente a reCAPTCHA v2 ($1 — $2.99, 2 sec) es más lento en 8,5 veces y no tiene banda de precio. Para un pipeline de scraping, 17 segundos por captcha es un límite de concurrencia, no un detalle: define cuántos workers hacen falta y, por tanto, cuál es la factura de capacidad.
La combinación **precio cerrado + slowest + menor capacidad libre** lo señala como el punto donde el mercado anti-bot se está endureciendo: los captchas de deslizador (slider) son la generación posterior a reCAPTCHA y aquí son los que cuestan más por unidad de tiempo. Es la señal temprana de que laIndustria del WAF se está moviendo hacia resistencias que el scraping directo no salva.
Nota: la captura **no** publica cuánto cuesta resolver un ALTCHA en horas punta ni si el precio $2.99 cubre Sites con slider más complejos.


## Nota de extensión 2026-10-26
Este átomo sostiene que ALTCHA define "el techo de coste **sin rango**", que es "más lento en 8,5 veces" que reCAPTCHA v2, y que su combinación "precio cerrado + slowest + menor capacidad libre" "lo señala como el punto donde el mercado anti-bot se está endureciendo". La captura de AntiCaptcha **desarma la parte de latencia**: AntiCaptcha publica **Altcha a $2 por 1000 y 5 s**, tarea `AltchaTaskProxyless` ([[2026-1026-anticaptcha-altcha-a-2-dolares-y-5-segundos]]). Es decir, el mismo captcha de deslizador —que el átomo identifica como la "generación posterior a reCAPTCHA"— resuelve **3,4 veces más rápido** que en 2Captcha y **más barato que el reCAPTCHA v2** de ese catálogo. La tesis de hardening **no queda refutada** —que un tipo de captcha exista en dos catálogos a $2 y $2.99 no dice nada sobre la dificultad del captcha en sí—, pero sí queda **acotada**: ni el $2.99 ni los 17 segundos son propiedades de ALTCHA, sino de un proveedor, y por tanto no pueden citarse como "el precio de atravesar un ALTCHA". La lectura correcta es que **el precio y la latencia de un tipo de captcha son variables de proveedor**, y que el vault tiene ahora dos proveedores con cifras para el mismo tipo, lo que basta para no leer el catálogo de uno como si fuera el mercado.


## Nota de extensión 2026-10-27
La captura del 2026-10-26 **cambia las dos cifras de este átomo**: ALTCHA sigue en **$2.99 por 1000**, pero su "Solving speed" pasa de **17 sec a 15 sec**, y su capacidad libre por minuto sigue en **203**. Ver [[2026-1027-2captcha-cuatro-velocidades-cambiaron-en-tres-dias]].

Más importante: **ALTCHA ya no es el tipo más lento**. Con la tabla de 48 filas, el techo de latencia es **KeyCAPTCHA a 37 sec**, seguido de Cutcaptcha y Prosopo a 24 sec y Lemin a 20 sec. Ver [[2026-1027-2captcha-keycaptcha-37-segundos-como-nuevo-techo-de-latencia]]. Y la tesis que este átomo sostiene —que "la combinación **precio cerrado + slowest + menor capacidad libre** señala el nicho donde el mercado anti-bot se está endureciendo"— **queda desmentida por el catálogo completo en dos de sus tres términos**: (1) ALTCHA no es el más lento; (2) la menor capacidad libre del catálogo (64/min) corresponde a **Click captcha y Slider Captcha a $1.2** y a **PerimeterX a $0**, es decir, a tipos **más baratos** que ALTCHA, no más caros.

Lo que sí queda en pie, y es un dato nuevo, es que **el propio catálogo de 2Captcha separa dos cosas que este átomo confundía**: publica **"Slider Captcha" como tipo independiente**, con precio **$1.2** y capacidad **64/min**, frente a ALTCHA con precio **$2.99** y **203/min**. Es decir, **"ser un slider" no define un precio ni una capacidad**: hay dos sliders en el mismo catálogo con precios que difieren ×2,5 y capacidades que difieren ×3,2. El corrector es que **el coste del captcha lo fija la familia técnica concreta del reto (slider propio de un proveedor frente a slider genérico), no el hecho de arrastrar un elemento**. La conclusión final del átomo —"la industria del WAF se está moviendo hacia resistencias que el scraping directo no salva"— **no se contradice**, pero deja de estar apoyada en la cifra de ALTCHA: el endurecimiento visible en la captura es **de latencia y de precio a la vez en tipos de reto mecánicos** (KeyCAPTCHA 37 sec a $2.99, Lemin 20 sec a $1.45), no en ALTCHA.

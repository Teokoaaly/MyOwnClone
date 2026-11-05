---
id: 2026-1027-2captcha-akamai-kasada-y-perimeterx-publicados-a-cero-por-1000
type: atom
certainty: solid
sources: [sources/2026-10-26-2captcha-pricing-captcha.md]
links: ["[[2026-1027-2captcha-catalogo-completo-de-48-filas-de-captcha]]", "[[2026-1026-patchright-declara-pasar-catorce-detectores-publicados]]", "[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]"]
---
## Claim
Tres de las 48 filas del catálogo de 2Captcha tienen **precio "$0" por 1000**: **Akamai** (15 sec, 203 libres por minuto), **Kasada** (8 sec, 203 libres por minuto) y **PerimeterX** (9 sec, **64** libres por minuto). Son los **únicos tres tipos de precio $0** del catálogo. Los tres son detectores antibot que no son puzzles de imagen: Akamai y Kasada aparecen además como detectores listados en la documentación de Patchright, que declara poderlos pasar sin solver.

## Why It Matters
Es la primera vez que el corpus del vault ve **precio cero** en una partida que hasta ahora era "la más barata y la más fácil de cotizar". Hasta aquí la conclusión estructural del thread era que el captcha es una partida de milésimas de dólar, siempre positivo y siempre seleccionable por tipo ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]). Un precio de **$0** para tres de los controles antibot más reputados del sector cambia el eje: **la variable que decide el coste no es qué control hay, sino qué tipo de control hay**.

Y conecta directamente con una tensión que el vault ya tenía anotada: [[2026-1026-patchright-declara-pasar-catorce-detectores-publicados]] documenta que Patchright declara pasar Akamai, Kasada y PerimeterX **sin mencionar ningún solver**, es decir, por debajo de la capa del captcha. Si eso es cierto, el **$0** de 2Captcha es coherente: **el proveedor no cobra por lo que no tiene que resolver**, o bien la fila a $0 es un marcador de "tipo no vendible" y no un precio. La captura no permite distinguir entre las dos lecturas, y esa ambigüedad es el dato.

Un apunte operativo: **PerimeterX a $0 tiene la capacidad libre más baja del catálogo (64 por minuto)**, por debajo de los 203 del suelo de doce tipos, y **Akamai y Kasada a $0 resuelven en 15 y 8 segundos** — dentro de la banda lenta del catálogo (ALTCHA, a $2.99, está en 15 s), muy por encima de los 1–2 s de los captchas de texto. Es decir: **el precio cero se paga en latencia y en cola**. Un pipeline que intente atravesar Akamai con este proveedor tendría un techo de 203/min con 15 s por token; uno que intente atravesar PerimeterX, 64/min con 9 s.

## [FRICTION]
> [[2026-1026-patchright-declara-pasar-catorce-detectores-publicados]] (escrita el 2026-10-26) declara que Patchright pasa "Cloudflare, Kasada, Akamai, Datadome, Fingerprint.com y Shape/F5" **sin mencionar ningún solver** y con la única condición de "with the right setup".
> Este átomo presiona esa afirmación en un punto concreto: **2Captcha sí ofrece solver para dos de esos mismos detectores, y lo ofrece a $0 por 1000**. Las dos cosas no pueden ser completamente ciertas a la vez: o Patchright los pasa de verdad sin coste de resolución, o el bypass "gratuito" no cubre el caso de uso de 2Captcha (que es ejecución **server-side** desde una IP de servidor, no un navegador con perfil parcheado). La captura no permite decidirlo —no dice para qué caso resuelve 2Captcha cada detector— pero sí deja escrito que **"resolver gratis" y "no necesitar resolver" son dos estrategias distintas con la misma etiqueta de precio cero**.
> Marcado para juicio humano, no auto-resuelto.

Nota: la captura **no** publica si la fila "$0" significa precio real, "sin coste por no estar disponible", o un marcador de tipo forthcoming; ni publica volumen, SLA ni condiciones específicas para estos tres tipos.

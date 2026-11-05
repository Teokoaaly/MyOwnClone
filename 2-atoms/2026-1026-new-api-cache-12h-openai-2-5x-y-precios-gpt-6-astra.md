---
id: 2026-1026-new-api-cache-12h-openai-2-5x-y-precios-gpt-6-astra
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-precios-por-ratio-y-expresion]]", "[[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]]", "[[2026-1023-new-api-tokenkit-conteo-de-tokens-calibrado]]"]
---

## Claim
En **v1.0.0-rc.47** el OpenAI **12-hour prompt cache** pasa a tener precio propio: **2,5 veces el precio de entrada**, cuando antes se cobraba **a la tarifa de 30 minutos**. El changelog da además la cifra concreta de un modelo: **gpt-6-astra** cobra las escrituras de 12 h a **$25 por millón de tokens** y a **$50 por millón por encima de 272K tokens**.

## Why It Matters
Convierte la caché en una **tercera unidad de precio** dentro de la misma llamada, y no un detalle: el vault ya tiene el problema abierto de que el mismo producto se mide en requests, prompts, credits o dólares ([[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]]), y aquí el multiplicador 2,5× es **sobre la entrada**, no sobre el precio oficial del token.
Para el modelo de coste del vault ([[2026-1022-myclone-tier-plans-usage-api]]) esto importa: un prompt cacheado de largo recorrido no es gratis, es **2,5× la entrada**, y por encima de 272K tokens el escalón se dobla a **$50/M**. Un relay que no cobre la caché de 12 h regala margen; uno que la cobre mal (a la tarifa de 30 min) regala service.
El mecanismo ya estaba descrito en el motor de precios del gateway ([[2026-1023-new-api-precios-por-ratio-y-expresion]]), y el conteo de tokens es lo que decide qué se factura ([[2026-1023-new-api-tokenkit-conteo-de-tokens-calibrado]]): aquí aparece por primera vez **el número de lista**, no solo el multiplicador.

## [FRICTION]
> [[2026-1023-new-api-precios-por-ratio-y-expresion]] afirma, citando el historial de commits del repo, que *"Ratio pricing bills 12-hour writes at twice the cache write ratio, the same way Claude 1-hour writes use 6/3.75"*, y que los modelos GPT con cache write ratio **se convierten a expresiones con `cc12h`**.
> Este átomo presiona esa creencia en un punto numérico: la release rc.47 dice que el 12 h de OpenAI se cobra **a 2,5× el precio de entrada**, mientras el motor de ratio lo describía como **2× el cache write ratio**. Con el dato de la propia fuente — Claude 1 h usa **6/3.75 = 1,6× la entrada** — un "2× el cache write ratio" daría **3,2× la entrada**, no 2,5×. Las dos afirmaciones **no pueden ser simultáneamente la regla vigente**: o la de ratio era la regla anterior y rc.47 la sustituye, o ambas conviven en motores distintos (ratio vs expresión) y entonces el precio del mismo caché depende de qué motor aplica el canal.
> Marcado para juicio humano, no auto-resuelto: el changelog **no declara** a qué motor pertenece la regla de rc.47, y no dice qué modelo usa el cache write ratio con el 2,5×. Para el vault esto no es un detalle: **el caché es la partida donde "el multiplicador publicado" y "el multiplicador aplicado" pueden divergir**, y por tanto donde una comparación de 0,05x entre canales puede ser falsa ([[2026-1023-new-api-precios-por-ratio-y-expresion]]).



## Nota de extensión 2026-10-27
La página de detección de VeriDrop da **la capacidad declarada de gpt-6-astra** y su coste de medición: **máximo de entrada 922k**, con sondas **32k → 461k → 875.9k** en modo extremo (**"官方标准输入价估算约 $27.06,不含输出和中转站加价"**) y **32k → 100k → 200k** en modo profundidad (**"约 $3.32"**). La cifra de $25/M de este átomo, aplicada a 875.9k, daría **~$21.90**: hay **~24 % de diferencia** con la estimación publicada, y la captura no publica la fórmula de la estimación. Véanse [[2026-1027-veridrop-la-sonda-de-contexto-largo-y-la-maxima-por-modelo]] y [[2026-1027-veridrop-el-coste-de-la-sonda-larga-paga-el-usuario]].

---
id: 2026-1024-veridrop-metodo-de-la-puntuacion-mediana-publica
type: atom
certainty: solid
sources: [sources/2026-10-23-veridrop-relays.md]
links: ["[[2026-1024-veridrop-directorio-de-relays-distinto-del-ranking]]", "[[2026-1023-priceai-patrocinadores-y-canales-de-reventa-con-multiplicador]]", "[[2026-1024-veridrop-insignia-pro-de-9-de-50-y-no-es-ranking-de-actividad]]"]
---

## Claim
El bloque de recomendación patrocinada de la página (etiquetado **"推荐 / 赞助"**, para **酷站AI**, `api.koozhan.com`) publica una métrica con **cuatro piezas literales**: **"公开检测综合中位分 99/100"**, **"421 份有效样本"** ("muestras válidas"), **"最近检测 2026-10-23"** y la lista de "近期已通过检测模型", cuyo texto capturado es *"Opus 5Opus 5 5Sonnet 5 5Fable 5 1GPT 6.astraGPT 6.sol等 21 个"* (es decir, Opus 5, Sonnet 5, Fable 5, GPT 6.astra, GPT 6.sol **y 21 modelos en total**, con el texto de la captura duplicando los tokens). Debajo hay una salvedad explícita: **"推荐展示不参与检测分计算；分数来自公开报告聚合，并会随新检测变化"** — el bloque recomendado no participa en el cálculo de la puntuación, la puntuación proviene de **agregación de informes públicos** y varía con nuevas detecciones.

## Why It Matters
Es el **método de medición de la calidad de un relay**, que PriceAI no publica en absoluto: no es un porcentaje de disponibilidad sino una **mediana de un scoring compuesto**, y su unidad no es el test sino la **"muestra válida"** (421). El vault ya tiene el precedente de que un porcentaje de disponibilidad sin denominador es incomparables ([[2026-1023-priceai-transit-disponibilidad-7d-con-denominadores-heterogeneos]]); aquí el denominador sí se publica ("421 份有效样本"), pero **no se publica qué es una muestra válida ni cómo se agrega** —solo que viene de informes públicos agregados, es decir, **fuera del control directo de VeriDrop**. Es una cadena de custodia más débil que la de un test propio, declarada por el propio sitio.
La salvedad es la pieza más útil para el vault: el propio VeriDrop admite que **la recomendación pagada no computa en la puntuación** — una separación explícita entre bloque comercial y métrica que es más fuerte que la de PriceAI, donde los patrocinadores aparecen dentro de la propia tabla ([[2026-1023-priceai-patrocinadores-y-canales-de-reventa-con-multiplicador]]).
Para MyOwnClone, si algún día se necesita evidencia objetiva de un relay, la salida es la URL de historial individual (`/leaderboard/<dominio>`), no la tarjeta de recomendación: la tarjeta mezcla un dato de scoring (99/100), un dato de volumen (421 muestras), un timestamp y un catálogo de modelos, y el propio sitio declara que su valor cambia con cada detección.

## Nota de verificación
Las cuatro piezas ("99/100", "421 份有效样本", "最近检测 2026-10-23", "等 21 个") y la salvedad están transcritas literalmente. La captura **no** define "样本 válido", ni el algoritmo de la mediana compuesta, ni qué son los "公开报告" agregados.

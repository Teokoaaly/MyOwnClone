---
id: 2026-1023-priceai-catalogo-ocho-canales-y-fecha-de-tipo-de-cambio
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-official-api.md]
links: ["[[2026-1023-priceai-chatgpt-plus-y-pro-precios-y-ventanas]]", "[[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]]", "[[2026-1023-priceai-descargo-de-responsabilidad-sin-sla]]"]
---

## Claim
PriceAI mantiene una **biblioteca de precios oficiales de API** con dos vistas: la tabla de "标准模型全部报价" (modelos estándar: input, output y cache token para texto; unidades oficiales de imagen o vídeo para generación) y la vista "Coding Plan" (suscripciones oficiales y Coding Plans con su cuota). La cabecera de la captura declara: **"数据库同步：2026-10-15"**, **"当前显示：8个渠道/订阅计划"** y **"汇率日期：2026-06-07"**. Es decir, la página sincroniza el catálogo el 2026-10-15, muestra 8 canales o planes de suscripción, y su tipo de cambio es del 2026-06-07.

## Why It Matters
El vault ya distingue lo observado de lo inferido: átomos como [[2026-1022-myclone-viaje-embeddings-voyage]] o [[2026-1022-pgvector-embeddings-openai-inferidos]] salen de endpoints reales o de bundles, no de catálogos de terceros. PriceAI es un **agregador**: útil como tabla de referencia rápida (8 canales, nombres de modelo, ventanas de cuota) pero con dos marcas de fiabilidad: los nombres de modelo (GPT-5.5, DeepSeek V4, Claude Fable 5) y las fechas "最近更新" son **declaraciones del agregador**, y el tipo de cambio de la tabla está congelado en junio 2026, cuatro meses antes de la sincronización del catálogo.
Consecuencia práctica: cualquier cifra de precio en yuanes o dólares de esta fuente debe tratarse como **precio de referencia de agregador**, no como precio oficial confirmado, y recalcularse con un tipo de cambio actual antes de modelar margen (ver [[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]] para el problema de unidades). El propio PriceAI se posiciona como quien "no vende API ni promete disponibilidad" ([[2026-1023-priceai-descargo-de-responsabilidad-sin-sla]]).

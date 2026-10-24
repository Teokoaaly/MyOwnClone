---
id: 2026-1024-veridrop-directorio-de-relays-distinto-del-ranking
type: atom
certainty: solid
sources: [sources/2026-10-23-veridrop-relays.md]
links: ["[[2026-1023-priceai-transit-cobertura-parcial-y-criterio-de-ranking]]", "[[2026-1023-priceai-modulo-api-transit-tres-ejes-de-comparacion]]", "[[2026-1023-new-api-gateway-unificado-de-modelos]]"]
---

## Claim
La página `veridrop.org/relays` se define a sí misma, en su propio bloque explicativo final, como un **directorio** y **no** como un ranking: *"中转站导航 按「最近活跃」或「检测热度」排列 Veridrop 检测过的全部中转站… 它 不替代 红黑榜（算法中立排名）——红黑榜回答「谁最好」，这里回答「市场上都有谁、谁最近在动」"*. Es decir, dos superficies distintas del mismo sitio: el **directorio** (quién existe y quién se mueve) y la **红黑榜** (quién es mejor, con ranking algorítmicamente neutral). La captura añade tres reglas explícitas: el orden depende **enteramente de parámetros de URL** ("排序逻辑完全由 URL 参数决定，公开透明"), **no acepta ningún peso comercial** ("不接受任何商业加权") y los espacios pagados van **etiquetados aparte** con la marca "赞助" ("赞助位单独标注「赞助」角标"). La superficie también ofrece filtros por protocolo (`/relays/claude`, `/relays/openai`, `/relays/gemini`) y un grupo de pares de operadores con QR de WeChat ("扫码加入中转站同行交流群").

## Why It Matters
Para MyOwnClone, que consume un proveedor LLM vía `OPENAI_API_BASE` y contempla auto-hospedar un relay, esto separa dos preguntas que el vault venía mezclando: **existencia/actividad** (directorio) frente a **calidad relativa** (ranking). Un directorio con orden por parámetros de URL es reproducible y auditable —se puede re-ordenar con la misma URL— mientras que un ranking algorítmico no lo es.
También fija el precedente de transparencia que el vault exige a los agregadores: el bloque pagador existe pero está **marcado y separado**, y la neutralidad se declara de forma textual y comprobable. Esto contrasta con la mezcla sponsor/tabla observada en PriceAI ([[2026-1023-priceai-transit-patrocinadores-y-ranking-en-la-misma-pagina]]), y encaja con el patrón de "separación de capa de datos y capa comercial" que el vault ya documentó como lo defendible en PriceAI ([[2026-1023-priceai-limite-de-verificacion-y-responsabilidad]]).
La existencia de un canal de pares de operadores (grupo WeChat) es además una señal de que el sector de relays **se coordina entre operadores**, no solo entre compradores: relevante para quien quiera operar un relay propio y para quien quiera saber de dónde vienen los relays que consume ([[2026-1023-new-api-gateway-unificado-de-modelos]]).

## Nota de verificación
Las tres reglas del pie (orden por URL, sin peso comercial, marca 赞助) y la contraposición directorio/红黑榜 están transcritas literalmente del bloque "这个频道怎么用?". La captura **no** publica: la fórmula exacta de los parámetros de URL, el criterio de inclusión en el directorio, ni la identidad del autor del sitio.

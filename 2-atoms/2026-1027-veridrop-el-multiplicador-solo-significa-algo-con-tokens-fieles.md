---
id: 2026-1027-veridrop-el-multiplicador-solo-significa-algo-con-tokens-fieles
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1023-priceai-transit-formula-del-multiplicador-compuesto]]", "[[2026-1027-veridrop-tres-formas-de-dilucion-o-concubamiento]]", "[[2026-1027-veridrop-cinco-indicadores-duros-para-elegir-relay]]"]
---

## Claim
La FAQ formula la regla de comparabilidad de precio como una **precondición de tres pasos**: **"倍率只有在 token 数真实时才有意义。同样标 0.5 倍,如果输入 token 被多算了三成,实际花的并不少"**, y por tanto antes de comparar hay que confirmar **① si el número de tokens es creíble** (los detectores **token usage** y **token billing** de VeriDrop), **② si lo que se entrega es el modelo anunciado**, y **③ cómo se factura la lectura y la escritura de caché**. Solo si las tres pasan, se comparan los multiplicadores. La FAQ añade el motivo estructural de la competencia: los relays existen porque **"部分中转站把多家厂商的批发额度打包零售,价格比官方低 30-70%"** y porque **"一些中转站把 Claude / GPT / Gemini 全统一成 OpenAI 兼容接口"**.

## Why It Matters
Esta es la **corrección más directa al thread del agregador de precios**, porque convierte la tabla de multiplicadores de PriceAI ([[2026-1023-priceai-transit-formula-del-multiplicador-compuesto]]) en una **tabla con precondición**: el número **no es comparable** hasta que el contador de tokens está verificado, y el vault tiene ahora la **herramienta concreta** para verificarlo (los detectores de uso y de facturación de VeriDrop) — algo que antes solo se tenía como intuición.
El ejemplo numérico de la FAQ merece quedarse: **"标 0.5 倍" con un 30 % de tokens de entrada inflados no sale más barato**. Es la forma más económica de explicar por qué **el precio y la calidad no son ejes separables en este mercado**: un multiplicador bajo puede ser exactamente el síntoma de un contador inflado, no de un buen negocio. Y de ahí sale la consecuencia de la regla de la §3 del mismo material: **comparar precio antes que pureza es comparar dos cosas que se pueden falsear en la misma dirección**.
El tercer punto de la precondición —**cómo se factura la caché**— enlaza directamente con el modelo de coste del gateway de referencia, donde la caché de 12 h de OpenAI se cobra a 2,5× la entrada y Gemini 2.5 Pro consume un presupuesto de pensamiento de 32768 tokens: **la caché y el razonamiento son partidas de coste que cambian lo que significa "el mismo multiplicador"**.

## Nota de verificación
Las tres precondiciones, el ejemplo del 0,5× y el rango de 30-70 % son literales de la FAQ. La captura **no** publica los umbrales numéricos de los detectores de token usage ni de token billing, ni la distribución real de multiplicadores por relay.

## [FRICTION]
> [[2026-1023-priceai-transit-formula-del-multiplicador-compuesto]] (escrita el 2026-10-23) establece la fórmula `综合倍率 = 充值系数 × 模型倍率` como **la** unidad de comparación de precios de relays, y [[2026-1023-priceai-modulo-api-transit-tres-ejes-de-comparacion]] la usa como uno de los tres ejes (multiplicador, estabilidad, información declarada) del módulo de tránsito. Esta nota presiona esa creencia con la condición que PriceAI no exige: la FAQ de VeriDrop afirma que **"倍率只有在 token 数真实时才有意义"** y da el contraejemplo de un 0,5× con un 30 % de tokens de entrada inflados. El multiplicador, tal como PriceAI lo publica, es un **número sin audited sobre su propio denominador**: si el `usage` que el relay factura está inflado, el multiplicador路口 describe un precio que no se puede pagar. Ambas no pueden ser completamente correctas: o la tabla de multiplicadores de PriceAI se lee como precio efectivo (y entonces necesita una columna de fidelidad de tokens que no publica), o se lee como la configuración del grupo (y entonces no es comparable entre operadores sin verificar el contador). Marcado para juicio humano, no auto-resuelto.

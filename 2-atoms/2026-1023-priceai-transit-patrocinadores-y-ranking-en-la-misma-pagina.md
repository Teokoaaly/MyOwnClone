---
id: 2026-1023-priceai-transit-patrocinadores-y-ranking-en-la-misma-pagina
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-api-transit.md]
links: ["[[2026-1023-priceai-patrocinadores-y-canales-de-reventa-con-multiplicador]]", "[[2026-1023-priceai-limite-de-verificacion-y-responsabilidad]]", "[[2026-1023-priceai-transit-dispersion-de-multiplicadores]]"]
---

## Claim
La página **API 中转** tiene su propio bloque de patrocinadores (etiquetado 赞助) **con los mismos nombres que aparecen en la tabla de ranking**: **Dragon API** (patrocinador con "统一 API 快速调用 OpenAI、Claude、Gemini 等热门模型" y también rank 2 del ranking), **合聚API** (patrocinador con "GPT Pro Max 满血版，0.2× 计费倍率" y también rank 20, con rango ChatGPT **0.10-7.00x**) y **灵绘AI** (patrocinador con "注册即送1$" y también rank 13 con Gemini **0.75-0.90x**). Los otros dos patrocinadores son **OneHop AI** (soporta OpenAI, Anthropic, Google, DeepSeek, Minimax, Moonshot, GLM, "注册即送 1$") y **Dragon API**. La página declara además: **"不售卖 API，不替商家担保"** (no vende API, no responde por los comerciantes) y **"没有完成审核发布的数据不会出现在榜单里"** (los datos no completados, revisados y publicados no aparecen en el ranking).

## Why It Matters
Confirma en la página de tránsito lo que el vault solo había inferido desde la home: **patrocinador y tabla comparten el mismo conjunto de nombres**, es decir, los relays patrocinados no están fuera del ranking — compiten dentro de él, con la ventaja de visibilidad que implica el bloque de pago pagador ([[2026-1023-priceai-patrocinadores-y-canales-de-reventa-con-multiplicador]]).
El caso de 合聚API es el más elocuente: su copy patrocinado vende **"0.2× 计费倍率"** mientras que en la tabla su rango de ChatGPT llega hasta **7.00x** — el multiplicador del texto comercial y el de la tabla no son el mismo número, o el rango cubre varios 号池/modelos distintos.
La cláusula de revisión es un dato de fiabilidad favorable y verificable: la tabla **excluye lo no auditado**, lo que acota el problema de las cifras obsoletas ya detectado en el catálogo oficial ([[2026-1023-priceai-limite-de-verificacion-y-responsabilidad]]).

## [FRICTION]
> [[2026-1023-priceai-limite-de-verificacion-y-responsabilidad]] afirma que la home **sí** declara una frontera entre la capa de datos y la capa comercial —*"PriceAI 提供信息，不替任何渠道背书"*, "PriceAI 不参与交易", separación por bloque y etiqueta 赞助/推广— y deja el conflicto con el átomo de patrocinadores abierto a juicio humano.
> Este átomo **no cierra** ese conflicto pero aporta el dato que faltaba: en la página de tránsito los patrocinadores y las filas del ranking son **el mismo conjunto de nombres** (Dragon API, 合聚API, 灵绘AI). La frontera es de bloque y de etiqueta, no de contenido: los canales pagadores están dentro de la tabla que se presenta como ranking independiente.
> Ambas no pueden ser completamente correctas: o la etiqueta 赞助 y la tabla son separables y la neutralidad se mantiene, o el contenido compartido invalida la separación. Marcado para juicio humano, no auto-resuelto: este átomo observa coexistencia de nombres, no prueba de sesgo en el orden.

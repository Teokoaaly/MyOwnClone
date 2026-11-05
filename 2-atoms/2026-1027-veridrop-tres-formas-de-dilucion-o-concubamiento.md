---
id: 2026-1027-veridrop-tres-formas-de-dilucion-o-concubamiento
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-la-prueba-de-pureza-en-tres-pasos]]", "[[2026-1027-veridrop-el-usage-de-la-respuesta-delata-el-trasvase-de-protocolo]]", "[[2026-1023-priceai-faq-antifraude-y-prueba-pequena]]"]
---

## Claim
La FAQ define la **dilución** ("掺水") como el caso en que el relay entrega **menos de lo anunciado**, y la descompone en **tres formas exactas**: **① 换模型** — cambiar Opus o GPT flagship por un modelo más barato o de otro fabricante; **② 多算 token** — el `usage` reporta entrada y salida **por encima del valor real**; **③ 砍能力** — **truncar el contexto largo**, o eliminar thinking, tool calling o multimodal. Y añade la razón por la que una prueba naive no sirve: **"掺水的站照样能正常回复,所以发一句话测试看不出来,要用针对性的检测"**.

## Why It Matters
Es la **taxonomía del fraude del relay**, y es distinta de la del "modelo falso" que el vault tenía: aquí las tres vías son **modelo, contador y capacidad**, y **cada una se ataca con una prueba distinta**. El vault ya tenía el eje "modelo" ([[2026-1027-veridrop-el-usage-de-la-respuesta-delata-el-trasvase-de-protocolo]]), pero no el eje **billing**: **el token inflado es la forma de dilución que solo se detecta mirando la varianza del contador**, y por eso la métrica del CV de `completion_tokens` funciona como prueba simultánea de fidelidad y de estabilidad.
La observación de método —"una frase de prueba no lo detecta"— invalida el patrón de prueba barata que el vault venía asumiendo: **cualquier smoke test de una sola llamada es estructuralmente incapaz de detectar dilución**, porque un relay diluido responde bien. Esto conecta directamente con el protocolo antifraude que el vault ya tenía para otros canales ([[2026-1023-priceai-faq-antifraude-y-prueba-pequena]]): la prueba pequeña de compra no es un control de calidad, es solo un control de que el canal entrega algo.
Y hay un cuarto eje que la taxonomía hace visible por omisión: **el precio**. Un relay que diluye el token factura sobre un número inflado, así que **el multiplicador bajo y la token inflada se refuerzan**. Comparar multiplicadores entre relays sin haber verificado el contador es comparar dos cosas que se pueden falsear en la misma dirección.

## Nota de verificación
Las tres formas son literales de la FAQ. La captura **no** publica los umbrales numéricos que separan "token inflado" de "token real", ni las cifras de prevalencia de cada forma de dilución.

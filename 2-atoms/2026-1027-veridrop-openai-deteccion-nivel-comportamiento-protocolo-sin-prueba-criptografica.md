---
id: 2026-1027-veridrop-openai-deteccion-nivel-comportamiento-protocolo-sin-prueba-criptografica
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-openai-detection.md, sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1024-veridrop-home-12292-relays-y-cuatro-modelos-con-doble-nivel-de-evidencia]]", "[[2026-1027-veridrop-thinking-signature-500-a-2000-caracteres-con-peso-25]]", "[[2026-1023-priceai-transit-guia-previa-y-verificacion-de-modelo-pendiente]]"]
---

## Claim
La página de detección OpenAI de VeriDrop declara su propio límite en un recuadro literal: **"行为/协议级验证: 本检测无法可靠区分高配模型真品与低配模型伪装"** — es decir, la detección OpenAI **no puede distinguir de forma fiable un modelo de gama alta auténtico de uno de gama baja disfrazado**; lo que comprueba es que la interfaz del relay **cumpla la especificación del protocolo OpenAI Chat Completions**, que las **capacidades estén completas** y que la **forma del campo `usage` sea la oficial**. La FAQ lo formula por el otro lado: **"OpenAI 协议没有像 thinking signature 这样的加密级指标"** y, por tanto, la recomendación explícita del propio sitio es **detectar un modelo Claude en el mismo relay para obtener una conclusión firme** ("想要确定结论，推荐用 Claude 模型检测同一家中转站"). El contraste está en el mismo conjunto de datos: el `thinking signature` de Claude es una **firma criptográfica de servidor que el relay no puede falsificar** y pesa **25 %** del score.

## Why It Matters
Es la **declaración de un techo epistémico hecha por el propio competidor**, y es la pieza que le falta a cualquier tabla de precios de relays: cuando el producto agrega precios y disponibilidad pero no verifica el modelo ([[2026-1023-priceai-transit-guia-previa-y-verificacion-de-modelo-pendiente]]), **una fila "OpenAI" no significa "GPT"**, significa "habla el dialecto". La home de VeriDrop ya distinguía dos niveles de evidencia —Claude con firma criptográfica, OpenAI y Gemini con campos de protocolo ([[2026-1024-veridrop-home-12292-relays-y-cuatro-modelos-con-doble-nivel-de-evidencia]])— pero **sin quantifying cuánto vale esa diferencia**; aquí está el número y la honestidad: 25 % de peso para una prueba concluyente, y ninguna para OpenAI.
La consecuencia de producto para el vault es una **regla de catálogo, no un matiz**: si un agregador publica una columna "OpenAI" junto a una columna "Claude", **no puede mezclarlas en la misma escala de confianza** salvo que declare el nivel de evidencia de cada una. Y hay una palanca barata: **la verificación concluyente de un relay dado se puede hacer con un modelo Claude sobre el mismo relay** — es decir, la prueba criptográfica es portable a cualquier relay que también hable Claude, aunque su venta principal sea OpenAI.

## Nota de verificación
Las dos frases son transcripción literal de las fuentes (la del recuadro, del chino; la de la FAQ, del chino). La captura **no** publica qué se entiende por "alto/bajo rango" ni qué umbral de desviación de comportamiento dispara la sospecha.

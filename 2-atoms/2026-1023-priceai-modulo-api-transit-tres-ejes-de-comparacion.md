---
id: 2026-1023-priceai-modulo-api-transit-tres-ejes-de-comparacion
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-home.md, sources/2026-10-22-priceai-api-transit.md]
links: ["[[2026-1023-priceai-cuatro-modulos-y-home-solo-desvia]]", "[[2026-1023-priceai-patrocinadores-y-canales-de-reventa-con-multiplicador]]", "[[2026-1023-priceai-descargo-de-responsabilidad-sin-sla]]", "[[2026-1023-priceai-transit-formula-del-multiplicador-compuesto]]", "[[2026-1023-priceai-transit-precio-y-estabilidad-desacoplados]]"]
---

## Claim
El módulo **中转 API** (estaciones de reventa) se define por **tres ejes de comparación**, no por el precio: *"面向 GPT、Claude、Gemini、Grok 等模型的第三方中转站，重点看倍率、稳定性和披露信息"* — el **倍率** (multiplicador de facturación), la **estabilidad** y la **información declarada** (披露信息). La "información declarada" es un eje de confianza: el sitio no certifica al canal, publica lo que el canal declara sobre sí mismo.

## Why It Matters
Es la definición operativa de **fiabilidad de un relay**, y fija qué significa "transparencia" en este mercado: publicar los propios datos, no verificarlos. El multiplicador es la unidad de precio del sector y lo que separa una oferta de 0,05× de otra de 0,2× ([[2026-1023-priceai-patrocinadores-y-canales-de-reventa-con-multiplicador]]); la estabilidad es la dimensión que no aparece en ninguna tabla de precios y que el descargo del sitio declara no garantizada ([[2026-1023-priceai-descargo-de-responsabilidad-sin-sla]]).
Para el vault esto importa porque el producto consume inferencia **por token** y no tiene ninguna capa de reseller ([[2026-1022-costes-por-categoria-tenant]]): si el multiplicador más bajo del mercado es 0,05×, la pregunta que este módulo deja abierta —y que PriceAI no puede responder— es qué parte de esa TaqSIM de precio corresponde a **estabilidad no declarada**. El eje de "披露信息" es exactamente el hueco que el vault tiene que cubrir por su cuenta, porque su coste de inferencia no puede depender de un canal sin SLA.
El hecho de que el comparador oficial sea el multiplicador y no el precio efectivo implica además que **cualquier cifra de coste derivada de una suscripción oficial ([[2026-1023-priceai-suscripcion-no-es-api-token]]) tiene que multiplicarse por el倍率 antes de compararse** con una oferta de relay.

## Extensión (captura de la página de tránsito, 2026-10-23)
La tabla real del módulo 中转 API confirma los tres ejes y los cuantifica: el precio se publica como **综合倍率 = 充值系数 × 模型倍率** ([[2026-1023-priceai-transit-formula-del-multiplicador-compuesto]]), la estabilidad como **近 7 日可用率** sobre muestra de monitorización pública (no SLA), y la información declarada como el campo **来源渠道** (Sub2API / New API) más la cobertura por modelo. La comprobación empírica es que **el eje de precio no predice el de estabilidad**: el relay más barato de la tabla no es el más disponible ([[2026-1023-priceai-transit-precio-y-estabilidad-desacoplados]]).

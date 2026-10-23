---
id: 2026-1023-priceai-transit-formula-del-multiplicador-compuesto
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-api-transit.md]
links: ["[[2026-1023-priceai-modulo-api-transit-tres-ejes-de-comparacion]]", "[[2026-1023-priceai-transit-dispersion-de-multiplicadores]]", "[[2026-1023-priceai-suscripcion-no-es-api-token]]"]
---

## Claim
La página **API 中转站价格榜** define la unidad de precio del sector con una fórmula explícita: **"综合倍率 = 充值系数 × 模型倍率，越低越便宜"** — el *multiplicador compuesto* es el producto del **coeficiente de recarga** (充值系数, lo que pagas por el saldo que compras) por el **multiplicador de modelo** (模型倍率, el recargo por usar ese modelo). El ranking que publica es el **"API 中转站综合推荐前 30 名"**, y la cabecera declara **"最近更新：2026-10-23"** con **"样本 15721"**.

## Why It Matters
Es la primera vez que el vault puede descomponer la unidad de precio del relay: no es un "precio" sino el producto de dos factores que se pueden manipular por separado — un canal puede parecer barato por un coeficiente de recarga bajo yMultiplier de modelo alto, o al revés. Para cualquier comparación de coste del vault, **el número tabulado no es comparable con otro número tabulado sin saber qué parte del descuento es recarga y qué parte es modelo**.
Refuerza la lectura del átomo de los tres ejes ([[2026-1023-priceai-modulo-api-transit-tres-ejes-de-comparacion]]): el precio es un eje, pero es un precio compuesto y relativo al precio oficial, no un $/M tokens — por lo que la tabla no puede alimentar un modelo de coste por token tal como está ([[2026-1023-priceai-suscripcion-no-es-api-token]]).
El "越低越便宜" es también la regla de ordenación: mejor (menor) multiplicador compuesto, lo que hace que el ranking esté dominado por un solo número, con la estabilidad como criterio secundario ([[2026-1023-priceai-transit-cobertura-parcial-y-criterio-de-ranking]]).

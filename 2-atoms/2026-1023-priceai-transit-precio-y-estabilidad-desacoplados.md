---
id: 2026-1023-priceai-transit-precio-y-estabilidad-desacoplados
type: atom
certainty: tentative
sources: [sources/2026-10-22-priceai-api-transit.md]
links: ["[[2026-1023-priceai-transit-dispersion-de-multiplicadores]]", "[[2026-1023-priceai-transit-disponibilidad-7d-con-denominadores-heterogeneos]]", "[[2026-1023-priceai-modulo-api-transit-tres-ejes-de-comparacion]]"]
---

## Claim
En la tabla de 30 relays, **el multiplicador más bajo no coincide con la disponibilidad más alta**, y la correlación no es evidente. Casos del extremo barato: 悠米AI中转 con **0.04-0.10x** en ChatGPT pero **85.1%** de disponibilidad (样本 62) y **sin Claude ni Gemini registrados**; 皓悦 APISub2API con **0.01-0.20x** pero **80.2%** (样本 600). Casos caros y estables: HubCore con **99.8%** (样本 1320) y un techo de **2.00x** en ChatGPT; Top-API con **99.2%** (样本 796) y hasta **2.10x** en Claude. En el extremo, 贝贝 tiene el mínimo de disponibilidad (**73.9%**) con un rango de Claude de **0.05-1.60x**.

## Why It Matters
Es la confirmación empírica de los **tres ejes separados** que PriceAI declara en su módulo de reventa — precio, estabilidad e información declarada ([[2026-1023-priceai-modulo-api-transit-tres-ejes-de-comparacion]]): el precio no predice la estabilidad, y por tanto **el multiplicador no puede usarse como proxy de calidad**.
Para el vault esto es la lección operativa de esta fuente: si el producto necesita inferencia estable, la decisión de canal no se puede tomar por el número más bajo de la tabla, porque ese número coincide con los relays menos monitorizados y con peor disponibilidad observada.
Lectura marcada *tentative* y no *solid* porque la correlación no se ha calculado sobre las 30 filas y las muestras son desiguales; lo que sí es sólido es la existencia de los cuatro casos concretos citados, cada uno verificable en la tabla.

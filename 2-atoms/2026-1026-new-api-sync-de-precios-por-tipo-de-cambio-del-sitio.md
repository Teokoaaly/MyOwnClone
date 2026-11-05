---
id: 2026-1026-new-api-sync-de-precios-por-tipo-de-cambio-del-sitio
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-precios-por-ratio-y-expresion]]", "[[2026-1023-priceai-catalogo-ocho-canales-y-fecha-de-tipo-de-cambio]]", "[[2026-1023-priceai-transit-formula-del-multiplicador-compuesto]]"]
---

## Claim
**v1.0.0-rc.47** añade a la **sincronización de precios upstream** la posibilidad de **ajustar el precio por el tipo de cambio del sitio**: se puede **mantener el precio de origen**, o **multiplicarlo o dividirlo por el tipo de cambio**. Además, los **modelos que ya tienen el mismo precio** pueden seleccionarse también para ajustarse en bloque.

## Why It Matters
Esto convierte al gateway en su propio **agregador de precios con conversión de moneda**: el precio de origen del upstream se reexpresa en la moneda del sitio con una regla declarable (identidad, ×, ÷). Es la misma operación que hace un agregador de precios externo, pero **dentro del software de reventa** — y por tanto applied a cada modelo del catálogo, no a una tabla.
La conexión con el vault es directa y es una crítica: el agregador externo del vault **publica su tipo de cambio con fecha propia** (PriceAI congela el cambio en el 2026-06-07 mientras sincroniza el catálogo el 2026-10-15) ([[2026-1023-priceai-catalogo-ocho-canales-y-fecha-de-tipo-de-cambio]]). Es decir, la tabla de referencia que el vault usa tiene **más de cuatro meses de desfase cambiario**, mientras que el software del relay puede reexpresar sus precios cada vez que el operador cambia el tipo.
Consecuencia para el modelo de coste: el multiplicador que el vault tabula ([[2026-1023-priceai-transit-formula-del-multiplicador-compuesto]]) es un número **relativo** (综合倍率 = 充值系数 × 模型倍率) y **no dice en qué moneda ni con qué fecha de cambio**; esta feature es la prueba técnica de que esa pregunta tiene respuesta operativa dentro del stack — y de que **el multiplicador solo es comparable con la misma regla de cambio**.

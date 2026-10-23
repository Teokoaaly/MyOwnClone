---
id: 2026-1023-priceai-cuatro-modulos-y-home-solo-desvia
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-home.md]
links: ["[[2026-1023-priceai-home-como-radar-y-no-como-vendedor]]", "[[2026-1023-priceai-token-plan-como-categoria-producto]]", "[[2026-1023-priceai-catalogo-ocho-canales-y-fecha-de-tipo-de-cambio]]", "[[2026-1023-priceai-sin-cuotas-gratis-tabuladas]]"]
---

## Claim
PriceAI está estructurado como **cuatro módulos** con ejes de comparación distintos, y la home solo hace de índice: **卡网订阅** (canales de terceros: membresías, cuentas, correos, 卡密, CDK, Kiro — eje: precio con stock y forma de entrega), **官方订阅** (precio oficial, precio regional, precio por elegibilidad y umbral de pago), **官方 API** (API oficial de modelos chinos: DeepSeek, 千问, Kimi, GLM — eje: cuota gratuita, Token Plan y límites) y **中转 API** (estaciones de reventa para GPT, Claude, Gemini, Grok — eje: **倍率** (multiplicador), estabilidad e información declarada). Los usuarios veterans pueden entrar directamente al módulo conocido: *"新手按购买问题走，老用户可以直接进入熟悉的模块."*

## Why It Matters
La taxonomía de cuatro módulos es la Contribution más reutilizable del sitio para el vault, porque separa **cuatro tipos de commodity distintos** que se comparan con métricas distintas: suscripción de producto (cuota en ventana de tiempo), API oficial (precio por token), reventa de API (multiplicador) y reventa de cuentas (stock y entrega). El vault ya knows que suscripción y API son cosas distintas ([[2026-1023-priceai-suscripcion-no-es-api-token]]) y que "Coding Plan"/"Token Plan" son categorías de producto, no de proveedor ([[2026-1023-priceai-token-plan-como-categoria-producto]]); esta home confirma que un agregador ordena el mercado exactamente con esas cuatro categorías.
El eje de **倍率** para el módulo de reventa es la unidad de precio que el vault no tenía documentada: el coste de un relay no se expresa en $/M tokens sino en un multiplicador sobre el precio oficial, y esa es la razón por la que las páginas de canal pueden discrepar del precio de lista ([[2026-1023-priceai-catalogo-ocho-canales-y-fecha-de-tipo-de-cambio]]).
También revela una asimetría: el módulo de API oficial promete **cuota gratuita** en su propia descripción, aunque la tabla que la captura sí documentó no tabula ninguna ([[2026-1023-priceai-sin-cuotas-gratis-tabuladas]]).

## [FRICTION]
> [[2026-1023-priceai-sin-cuotas-gratis-tabuladas]] afirma que la captura de la página de API oficial **no tabula ninguna cuota gratuita** — Free y Go aparecen nombrados pero sin precio ni ventana, y el precio de entrada más bajo de los 8 canales es de pago (¥39/mes y $10/mes).
> Este átomo presiona esa creencia porque la **descripción oficial del módulo**, en la home, afirma lo contrario: la API oficial "包含免费额度、Token Plan 和限制" (incluye cuota gratuita, Token Plan y límites), y además la home enrutает al desarrollador a mirar precisamente los "免费额度" de DeepSeek, 千问, Kimi y GLM.
> Ambas no pueden ser completamente correctas: o el módulo de la home y la tabla de la página de API no son la misma superficie (una descripción de marketing frente a una tabla que solo lista planes de pago), o la cuota gratuita existe y la tabla que la captura documentó la omitió. Marcado para juicio humano, no auto-resuelto.

---
id: 2026-1023-priceai-transit-dispersion-de-multiplicadores
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-api-transit.md]
links: ["[[2026-1023-priceai-transit-formula-del-multiplicador-compuesto]]", "[[2026-1023-priceai-transit-precio-y-estabilidad-desacoplados]]", "[[2026-1023-priceai-patrocinadores-y-canales-de-reventa-con-multiplicador]]"]
---

## Claim
El rango de multiplicadores compuestos que PriceAI tabula en los 30 primeros relays es de **casi dos órdenes de magnitud**:

- **Extremo barato (ChatGPT)**: 悠米AI中转 (New API) con **0.04-0.10x**, y 皓悦 APISub2API (rank 1) con **0.01-0.20x**; en Claude, 贝贝 y 無忧 Ai con **0.05-1.60x** y **0.05-1.50x** respectivamente.
- **Extremo caro**: 合聚API (rank 20) con **0.10-7.00x** en ChatGPT, 悟空api con **0.08-3.75x**, codex666ai con **0.05-1.25x** y Top-API con **0.07-0.49x** pero Claude hasta **2.10x**.
- **Gemini**: de **0.10-0.35x** (RelayCore) a **0.70-3.75x** (悟空api), con 灵绘 AI como extremo alto **0.75-0.90x**.

La cabecera de la página resume: **"Claude 最低 0.045x，Gemini 最低 0.10x"**.

## Why It Matters
Da al vault la **cifra de suelo y techo del sector**: un canal puede vender acceso a Claude a la **quinta parte** del precio oficial y otro a **2-3×** el oficial, con el mismo nombre de modelo detrás. Es una prueba de que el multiplicador no es un campo de marketing sino una variable de negocio con dispersión real ([[2026-1023-priceai-transit-formula-del-multiplicador-compuesto]]).
Refuerza la advertencia ya existente sobre los relay como reventa, no como infraestructura con SLA ([[2026-1023-priceai-patrocinadores-y-canales-de-reventa-con-multiplicador]]): el rango 0.04x–7.00x es exactamente el tipo de dispersión que hace imposible inferir calidad a partir del precio.
Nota de verificación: el mínimo de Claude que **la cabecera** declara (0.045x) **no aparece en ninguna de las 30 filas visibles** — el mínimo tabulado en Claude es 0.05x. El 0.045x puede venir de un grupo fuera del top 30 (la página dice que el ranking solo usa grupos con monitorización directa); el de Gemini (0.10x) sí coincide con la tabla.
## Nota de extensión 2026-10-26 — el multiplicador ya tiene denominador
Fuente: `sources/2026-10-25-heroku-pricing.md`. Este átomo establecía que el multiplicador de los relays tiene una dispersión de casi dos órdenes de magnitud (Claude de **0,05× a 2,10×**, ChatGPT de **0,04× a 7,00×**) pero que **"el precio oficial" era una magnitud no verificada**: la tabla de PriceAI no publica precios por token. La captura de Heroku Managed Inference **publica por primera vez en el vault un precio de lista por 1M de tokens con entrada y salida separadas** para la misma familia de modelos: **claude-4-5-sonnet $3,30 / $16,50**, **claude-opus-4-8 $5,50 / $27,50**, **claude-3-haiku $0,25 / $1,25**, y en open-weights **glm-4-7-flash $0,07 / $0,40**, **gpt-oss-120b $0,15 / $0,60**, **minimax-m2 $0,30 / $1,20**, **nova-lite $0,06 / $0,24**. Con ese denominador, el extremo barato del ranking **ya no es una magnitud abstracta**: 0,05× de Sonnet 4.5 son **$0,165 por millón de tokens de entrada**, y 0,05× de un open-weight como glm-4-7-flash serían **$0,0035** — dos órdenes de magnitud por debajo con el mismo multiplicador. La consecuencia para la lectura del vault es que **"el oficial" es ambiguo y por tanto el multiplicador no es comparable entre filas**: el multiplicador de un canal solo significa algo si se sabe contra qué precio de lista se multiplica, y el rango de precios de lista verificados para un mismo "modelo de frontera" va de **$0,06 a $5,50 por 1M de tokens de entrada (×92)**. Ver [[2026-1026-heroku-inference-claude-opus-4-8-a-5-50-y-27-50-por-millon]] y [[2026-1026-heroku-inference-modelos-abiertos-0-07-a-0-62-por-millon-de-entrada]].

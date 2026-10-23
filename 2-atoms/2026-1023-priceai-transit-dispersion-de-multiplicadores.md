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

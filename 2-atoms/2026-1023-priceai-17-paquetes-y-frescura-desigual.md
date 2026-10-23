---
id: 2026-1023-priceai-17-paquetes-y-frescura-desigual
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-official-prices.md]
links: ["[[2026-1023-priceai-catalogo-ocho-canales-y-fecha-de-tipo-de-cambio]]", "[[2026-1023-priceai-grok-sin-descuento-regional]]", "[[2026-1023-priceai-chatgpt-go-egipto-56-menos]]"]
---

## Claim
La cabecera de la página declara: **"价格更新：3天前 汇率更新：2026-10-22 当前显示：17个标准套餐 来源：Supabase + 官网公开快照"**. Los 17 paquetes se reparten en ChatGPT (5: Go, Plus, Pro 100刀档, Pro 200刀档, Pro 500刀档), Claude (4: Pro, Max 5x, Max 20x, Pro Annual), Gemini (4: AI Plus, AI Pro, AI Ultra 5x, AI Ultra 20x) y Grok (4: Plus, Premium, Super, Ultra). La columna 地区样本 va de **48 a 235** regiones (235 en ChatGPT Go, 48 en Grok Plus) y la columna 价格更新 marca **3天前 en 14 filas y 9天前 en las 3 filas de 官网直购 de Grok** (Plus, Super, Ultra).

## Why It Matters
La frescura no es uniforme dentro de la misma tabla: cuando la página dice "3天前" en la cabecera, tres filas de Grok son de hace 9 días ([[2026-1023-priceai-grok-sin-descuento-regional]]). Es un matiz pequeño frente al de la página de API, cuyo tipo de cambio estaba congelado en el 2026-06-07 ([[2026-1023-priceai-catalogo-ocho-canales-y-fecha-de-tipo-de-cambio]]): aquí el tipo de cambio sí se declara actualizado al 2026-10-22, lo que hace comparables los yuanes de esta tabla con los de la otra, siempre que se acepte que la fuente es un agregador.
La columna 地区样本 es la que da la calidad de cada mínimo: un "mínimo" sobre 235 regiones (ChatGPT Go, [[2026-1023-priceai-chatgpt-go-egipto-56-menos]]) es una afirmación mucho más robusta que uno sobre 48 (Grok Plus). Y que la fuente sea **Supabase + 官网公开快照** significa que hay una base de datos detrás, no un scrapeo puntual: es reutilizable como serie histórica si se vuelve a capturar.

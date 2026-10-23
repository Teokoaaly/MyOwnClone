---
id: 2026-1023-priceai-transit-cobertura-parcial-y-criterio-de-ranking
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-api-transit.md]
links: ["[[2026-1023-priceai-transit-formula-del-multiplicador-compuesto]]", "[[2026-1023-priceai-transit-disponibilidad-7d-con-denominadores-heterogeneos]]", "[[2026-1023-priceai-transit-canal-tipo-sub2api-vs-new-api]]"]
---

## Claim
El ranking de PriceAI **no cubre todos los canales**: la columna de Gemini muestra **"未收录"** (sin收录 / no collected) en 6 de las 30 filas (無忧 Ai, 鑫旺Neko API, NC API, 猫肥NekoAPI, Sub Callai One, 卡拉 Khala) y la de Claude en 3 (AL-API, 悠米AI中转, 星链AI). El criterio de ordenación está declarado: **"排名只用有直连监测的分组"** — solo entran los grupos **con monitorización directa (直连)**; el cálculo usa "按模型族价格篮子综合价格、缓存与稳定性" (precio por cesta de modelos de la familia, caché y estabilidad) y los filtros permitidos son **modelo, canal y 号池 (pool de cuentas)**.

## Why It Matters
La cobertura parcial **no es un dato faltante sino una selección**: la ausencia de un canal en la tabla significa "sin monitorización directa", no "no existe". Cualquier lectura de esta tabla como "estado del mercado" es inválida — es un ranking de lo que PriceAI puede observar.
El 号池 (pool de cuentas) aparece explícitamente como dimensión de filtrado, lo que confirma que la oferta de un relay no es una capacidad propia sino una **bolsa de cuentas compartidas** reutilizadas — el mismo modelo de negocio de reventa de identidades que el vault ya caracterizó en otro sitio ([[2026-1023-lzt-categoria-llm-accounts-para-reventa]]).
El criterio "precio + caché + estabilidad" también es relevante: la caché de tokens aparece como criterio de ranking, lo que indica que el ahorro por prompt cache es una palanca de coste real en este mercado y no un detalle de la API oficial.

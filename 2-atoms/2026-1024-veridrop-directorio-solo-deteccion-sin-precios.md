---
id: 2026-1024-veridrop-directorio-solo-deteccion-sin-precios
type: atom
certainty: solid
sources: [sources/2026-10-23-veridrop-relays.md]
links: ["[[2026-1023-priceai-transit-formula-del-multiplicador-compuesto]]", "[[2026-1023-priceai-modulo-api-transit-tres-ejes-de-comparacion]]", "[[2026-1024-veridrop-directorio-de-relays-distinto-del-ranking]]"]
---

## Claim
La página `veridrop.org/relays` **no publica ningún precio**: en la captura no aparece ni una sola vez 倍率 (multiplicador), 价格 (precio), 元 (yuan) ni `$`. El modelo de datos del directorio es puramente de **medición**: por cada relays, el dominio, las etiquetas de protocolo (Claude / Gemini / OpenAI), la hora del último test ("最近检测"), el recuento acumulado de tests ("累计 N 次"), el recuento en la ventana actual ("窗口内 N 次") y el reparto de veredictos ("N 通过 · N 边缘 · N 失败"). Es decir, **la misma página que el vault ya tenía como fuente de precio en PriceAI está aquí sin la variable de precio**, y esa ausencia es total, no parcial.

## Why It Matters
El vault necesita **las dos mitades** para decidir si consumir un relay vía `OPENAI_API_BASE`: el multiplicador (lo que cuesta) y la estabilidad medida (si funciona). PriceAI publica el primero con una fórmula explícita —"综合倍率 = 充值系数 × 模型倍率" ([[2026-1023-priceai-transit-formula-del-multiplicador-compuesto]])— y VeriDrop publica el segundo con recuento de tests y veredictos. Ninguna de las dos fuentes cubre los tres ejes que PriceAI declara —multiplicador, estabilidad e información declarada— por sí sola ([[2026-1023-priceai-modulo-api-transit-tres-ejes-de-comparacion]]): PriceAI no da historial de test por relay y VeriDrop no da precio.
Para MyOwnClone la consecuencia práctica es que **la tabla de coste/riesgo del relay que se monte tendrá que ser compuesta**: precio de una fuente y fiabilidad de otra, con fechas de captura distintas. Y un dato estructural relevante: como el directorio de VeriDrop **no tiene columna de precio**, su ordenación no puede estar sesgada por el precio — lo que hace que el orden "por actividad" sea el único que ofrece.

## Nota de verificación
La ausencia de precios es un resultado de búsqueda literal sobre la captura (cero ocurrencias de 倍率/价格/元/$), no una omisión de lectura. La captura **no** publica: el precio de ningún relay, ni la relación entre su texto de recomendación y el resto de datos del sitio.

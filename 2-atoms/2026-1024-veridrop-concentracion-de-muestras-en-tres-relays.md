---
id: 2026-1024-veridrop-concentracion-de-muestras-en-tres-relays
type: atom
certainty: solid
sources: [sources/2026-10-23-veridrop-relays.md]
links: ["[[2026-1023-priceai-transit-cobertura-parcial-y-criterio-de-ranking]]", "[[2026-1023-priceai-transit-disponibilidad-7d-con-denominadores-heterogeneos]]", "[[2026-1024-veridrop-directorio-de-relays-distinto-del-ranking]]"]
---

## Claim
El directorio de VeriDrop lista **50 relays** y su recuento acumulado de tests está extremadamente concentrado. La suma de "累计 N 次" de las 50 entradas es **36.555 tests**, de los cuales `la-api.vxvxvx.top` aporta **19.772 (54,1 %)** y los tres primeros (`la-api.vxvxvx.top` 19.772, `wawazz.xyz` 5.241, `kuaiapi.net` 4.285) suman **29.298 (80,1 %)**. En el otro extremo: **22 de las 50 entradas tienen ≤ 6 tests acumulados** y la mediana de la lista es **9 tests**; solo **5 entradas superan los 1.000 tests** (la-api 19.772, wawazz 5.241, kuaiapi 4.285, api.xiaoxuapi.com 2.705, api.a6api.com 1.316). En la cola hay entradas con **1 test** (`666six.top`, `codex.zone.id`, `sub.lk1950.xyz`).

## Why It Matters
Es la misma lesson que PriceAI ya dio sobre denominadores heterogéneos ([[2026-1023-priceai-transit-disponibilidad-7d-con-denominadores-heterogeneos]]), pero agravada por un orden de magnitud: una tabla con 50 filas donde una sola fila acumula más de la mitad de la evidencia total no es una muestra de 50, es **una muestra de 3 y uncola de ruido**. Un relay con 1 test y 1 veredicto "通过" no aporta ninguna señal de disponibilidad: solo prueba que alguien lo miró una vez.
Para MyOwnClone esto significa que el directorio **no puede usarse como lista blanca de proveedores de `OPENAI_API_BASE`**. El filtro honesto es por recuento acumulado (p. ej. ≥ 1.000 tests deja 5 candidatos), y aun así el criterio de inclusión del sitio es "todo lo que ha testeado", no "lo que ha testeado suficiente veces" — que es precisamente la diferencia entre una cobertura parcial y una cobertura útil.

## [FRICTION]
> [[2026-1023-priceai-transit-cobertura-parcial-y-criterio-de-ranking]] afirma que el criterio de ordenación de PriceAI es explícito —*"排名只用有直连监测的分组"*, solo entran los grupos **con monitorización directa**— y concluye que la cobertura parcial "es un dato faltante pero una selección: la ausencia de un canal en la tabla significa 'sin monitorización directa', no 'no existe'".
> Este átomo presiona esa creencia en un punto concreto: la regla de PriceAI (monitorización directa como condición de entrada) **no es la regla de todo el sector**. El directorio de VeriDrop incluye relays con **un solo test** y aun así presenta la lista como "todos los 中转站 que ha testeado", sin ningún umbral mínimo de evidencia declarado. La inferencia "ausente en la tabla de PriceAI ⇒ sin monitorización directa" es correcta para PriceAI pero **no transferible**: un canal puede no estar en la tabla de PriceAI y tener (o no tener) monitorización en otro sitio, y el vault no ha medido esa cobertura cruzada.
> Ambas no pueden ser simultáneamente la regla general del sector: o "solo entra lo que tiene monitorización directa" describe un estándar del sector y PriceAI lo cumple mientras VeriDrop no, o es una decisión local de PriceAI y no un estándar. Marcado para juicio humano, no auto-resuelto: son dos sitios distintos y el vault no ha medido la intersección de ambas listas.

## Nota de verificación
Recuentos y porcentajes calculados sobre los valores literales "累计 N 次" de las 50 entradas de la captura. La captura **no** publica: el criterio de inclusión en el directorio, el intervalo exacto de la "ventana", ni el significado de "边缘".

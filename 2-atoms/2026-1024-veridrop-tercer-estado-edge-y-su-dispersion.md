---
id: 2026-1024-veridrop-tercer-estado-edge-y-su-dispersion
type: atom
certainty: solid
sources: [sources/2026-10-23-veridrop-relays.md]
links: ["[[2026-1023-priceai-transit-precio-y-estabilidad-desacoplados]]", "[[2026-1023-priceai-transit-disponibilidad-7d-con-denominadores-heterogeneos]]", "[[2026-1024-veridrop-concentracion-de-muestras-en-tres-relays]]"]
---

## Claim
El veredicto de VeriDrop tiene **tres estados, no dos**: cada fila reporta "N 通过 · N 边缘 · N 失败", donde **边缘** ("edge", al límite) es un estado intermedio distinto de aprobado y de fallido. La dispersión de ese estado es enorme y **no se deduce de la tasa de fallos**: `modelflare.dev` tiene **0 fallos** pero **66边缘 sobre 249 tests (26,5 %)** y `api.vilao.ai` **5 fallos y 19 边缘 sobre 73 (26,0 % de edge)**, frente a `api.a6api.com` con **26 fallos y 217 边缘 sobre 1.316 (16,5 % de edge)** y `la-api.vxvxvx.top` con solo **75 边缘 sobre 19.772 (0,4 %)**. En el agregado de las 50 filas hay **35.738 通过 · 627 边缘 · 190 失败** sobre 36.555 tests: **0,52 % de fallos y 1,72 % de edge**. En contraste, entre los relays con ≥ 50 tests, el rango de fallo va de **0 %** (`shushutoken.com` 708/2/0 en 710, `cc.yzzt.top` 273/7/0 en 280, `modelflare.dev` 183/66/0 en 249, `91token.com` 79/4/0 en 83) a **9,5 %** (`api.relayrouter.ai`, 2 fallos sobre 21) y **4,95 %** (`cc-vibe.com`, 19 sobre 384).

## Why It Matters
El estado "边缘" cambia la lectura de un filtro de calidad construido sobre "pasa o no pasa". `modelflare.dev` es, por fallos, un relay perfecto (0 de 249) y por edge uno de los peores de la lista (26,5 %): un cuarto de sus respuestas estaba **al límite de no funcionar**, lo que es compatible con degradación, throttling intermitente o respuestas recortadas. Un ranking por tasa de fallo —la métrica que PriceAI usa en su columna "近 7 日可用率" ([[2026-1023-priceai-transit-disponibilidad-7d-con-denominadores-heterogeneos]])— es ciego a esa señal.
Y encaja con lo que el vault ya sabe del sector: **el precio no predice la estabilidad** y las muestras desiguales hacen incomparables dos cifras de disponibilidad ([[2026-1023-priceai-transit-precio-y-estabilidad-desacoplados]]). Aquí el eje es otro —volumen de respuestas marginales— y la dispersión confirma que "estable" no es una etiqueta binaria que un relay pueda llevar sin ambigüedad.

## [FRICTION]
> [[2026-1023-priceai-transit-disponibilidad-7d-con-denominadores-heterogeneos]] afirma que la columna de PriceAI "可用率为近 7 日公开监测样本" es un **porcentaje** de disponibilidad que el vault no puede comparar entre filas sin mirar el denominador, y critica que la columna mezcle dos denominadores distintos ("样本 N" y "24h 请求 N万").
> Este átomo presiona esa creencia en un punto concreto: VeriDrop no mezcla denominadores —escribe siempre los **tres recuentos crudos** (通过/边缘/失败) más "累计 N 次" y "窗口内 N 次"—, pero con ello introduce una **tercera dimensión que PriceAI no expone**: el edge. Dos filas con idéntico porcentaje de fallos pueden tener perfiles radicalmente distintos (0 % fallos / 26 % edge frente a 0 % fallos / 0,3 % edge), así que la granularidad no resuelve la comparabilidad: la resuelve la **semántica del veredicto**, que en PriceAI no está publicada.
> Ambas no pueden ser la misma medida: o "可用率" de PriceAI ya descuenta o ignora un estado equivalente a "边缘" —y entonces el vault está comparando plazos distintos sin saberlo— o son métricas de cosas distintas y sus números no son comparables entre sitios aunque ambos se llamen "estabilidad". Marcado para juicio humano, no auto-resuelto: la captura de PriceAI no define la semántica de sus estados.

## Nota de verificación
Recuentos y porcentajes calculados sobre los valores literales "N 通过 · N 边缘 · N 失败" de las 50 filas. La captura **no** define qué significa exactamente "边缘", ni la longitud de la "ventana".

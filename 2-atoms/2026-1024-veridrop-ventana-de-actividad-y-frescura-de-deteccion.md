---
id: 2026-1024-veridrop-ventana-de-actividad-y-frescura-de-deteccion
type: atom
certainty: solid
sources: [sources/2026-10-23-veridrop-relays.md]
links: ["[[2026-1024-veridrop-concentracion-de-muestras-en-tres-relays]]", "[[2026-1023-priceai-transit-disponibilidad-7d-con-denominadores-heterogeneos]]", "[[2026-1024-veridrop-directorio-de-relays-distinto-del-ranking]]"]
---

## Claim
Cada fila de VeriDrop publica **dos denominadores distintos**: el histórico ("累计 N 次") y el de la **ventana activa** ("窗口内 N 次"). Sumando las 50 entradas, el histórico es de **36.555 tests** y la ventana suma **4.146**, es decir, **~11,3 %** del histórico es actividad reciente concentrada en la ventana. El reparto es altísimo: `la-api.vxvxvx.top` acumula **3.077 tests en ventana sobre 19.772 históricos (15,6 %)** y `shushutoken.com` **435 sobre 710 (61,3 %)**, el más activo del momento, mientras que `wawazz.xyz` —segundo por histórico con 5.241 tests— solo tiene **15 en ventana (0,3 %)** y `kuaiapi.net` **88 sobre 4.285 (2,1 %)**. La frescura declarada va de **"最近检测 5 分钟前"** (`8stoken.com`) y "6 分钟前" (`shushutoken.com`) a **"最近检测 8 小时前"** (`91token.com`, `direct.saviour.cc.cd`), y **41 de las 50 entradas** con su último test hace **3 horas o más**.

## Why It Matters
Es la misma trampa de denominadores que PriceAI ya tenía documentada —comparar dos cifras de disponibilidad exige mirar el denominador ([[2026-1023-priceai-transit-disponibilidad-7d-con-denominadores-heterogeneos]])— pero aquí con un efecto operativo añadido: **un relay con mucho histórico puede estar dead**, no solo poco probado. `wawazz.xyz` es 2º por histórico (5.241 tests, 54 fallos acumulados) y sin embargo su actividad reciente es casi cero; su histórico no dice nada de hoy. La señal accionable para MyOwnClone no es "tiene muchos tests" sino "**tiene muchos tests en la ventana**" — que es exactamente la variable que ordena el directorio por "最近活跃".
Y la consecuencia de la frescura es un plazo de caducidad corto: con la mediana de la lista en tests de hace **5-6 horas** y el intervalo de ventana **no publicado** en la captura, cualquier puntuación de proveedor derivada de esta página **envejece en horas**, no en semanas. Si el vault construye una tabla de proveedores de `OPENAI_API_BASE` desde esta fuente, esa tabla necesita un timestamp por fila y un criterio de re-verificación, no un refresh global.

## Nota de verificación
Sumas calculadas sobre los valores literales "累计 N 次" y "窗口内 N 次" de las 50 entradas. La captura **no** publica: la duración de la "ventana", el intervalo de muestreo, ni el criterio de qué entradas son "recientes".

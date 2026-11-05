---
id: 2026-1026-new-api-plaza-de-modelos-con-estado-horario-y-precio-de-cache
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-priceai-catalogo-ocho-canales-y-fecha-de-tipo-de-cambio]]", "[[2026-1023-new-api-precios-por-ratio-y-expresion]]", "[[2026-1026-new-api-consulta-de-saldo-upstream-y-prioridad-arrastrable]]"]
---

## Claim
**v1.0.0-rc.44** define la **"model square"** (plaza de modelos) como el catálogo visible del gateway: **muestra las últimas 24 muestras horarias de estado dentro de 7 días, sin huecos** (PR #7757); las **tarjetas de modelo de expresión muestran el precio de lectura de caché** (PR #7757); la conversión de precios **acepta metadatos de modelo que declaran los endpoints como array** (PR #7724); y **root puede gestionar precios con la plaza de modelos desactivada** (PR #7761). En **rc.45**, los **modelos de precios nuevos aparecen arriba** (PR #7782) y los **precios se ordenan por entrada, salida y precio por petición** (PR #7813).

## Why It Matters
La **model square** es la pieza del gateway que **más se parece a un agregador de precios**: un catálogo con precio, orden y **estado de disponibilidad**. El vault tiene el agregador como producto en estudio ([[2026-1023-priceai-catalogo-ocho-canales-y-fecha-de-tipo-de-cambio]]) y este release muestra **cómo lo implementa el propio gateway de referencia**: no un tabla estática, sino **una carta de precios con reloj de disponibilidad detrás**.
Las **24 muestras horarias de 7 días** son el dato más valioso: un agregador que publica "0,05x" sin **historial de disponibilidad** miente en la práctica, porque el precio de un canal que estuvo caído media hora no es ese precio. El vault tiene ya la lección del **canal tipo Sub2API vs New API** ([[2026-1023-priceai-transit-canal-tipo-sub2api-vs-new-api]]): el tipo de canal determina la fiabilidad, y **un historial horario es la forma barata de hacerla visible**.
El detalle de "**root puede gestionar precios con la plaza desactivada**" es una señal de producto: la plaza es una **capa de presentación encima del motor de precios**, no su fuente de verdad. Es la arquitectura correcta para un producto que quiere vender "la carta" sin quedar atado a ella.
Y que las tarjetas muestren el **precio de lectura de caché** es coherente con la dirección de esta versión: la caché pasa de ser un detalle de implementación a ser **una partida visible en la carta de precios** ([[2026-1023-new-api-precios-por-ratio-y-expresion]]).

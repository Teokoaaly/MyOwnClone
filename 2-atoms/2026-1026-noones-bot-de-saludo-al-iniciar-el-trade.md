---
id: 2026-1026-noones-bot-de-saludo-al-iniciar-el-trade
type: atom
certainty: solid
sources: [sources/2026-10-25-noones-developer-api.md]
links: ["[[2026-1026-noones-api-dos-formatos-directo-y-delegado]]", "[[2026-1026-noones-bot-de-compra-de-gift-cards-con-procesador-externo]]", "[[2026-1024-noones-limite-diario-suma-de-todas-las-operaciones-en-24h]]", "[[2026-1026-noones-dev-noones-sin-precios-ni-limites-ni-documentacion-publica]]", "[[2026-1022-myclone-widget-comunicacion-websocket]]"]
---

## Claim
La página publica un caso de uso que no es de trading sino de **latencia de respuesta**: *"Make trading even smoother with a greeting bot. Once a trade starts, the bot will greet your trade partner and let them know you'll be there shortly."* Su caso de uso es `https://dev.noones.com/case-studies/greeting_app/`. Es decir, la automatización no mueve el dinero: **cubre el hueco de tiempo entre que se inicia el trade y que el operador humano aparece**, y la página lo lista junto a "decrease trade times" entre los beneficios de la API.

## Why It Matters
En un mercado P2P con contrapartes anónimas, la primera variable que se resuelve por software es **el tiempo de respuesta humano**: el saludo automático es el mínimo producto que un bot puede hacer sin riesgo y que **no toca fondos**. Es la prueba de que la API existe para los tiempos, no solo para el volumen — y por eso su valor no es un multiplicador de capacidad sino una **fricción de confianza resuelta por software**. Para el vault es un buen caso de estudio de arquitectura: un producto que no necesita ser regulado para automatizarse. Nota de rigor: la captura **no cuantifica** ese "decrease trade times" — no hay segundos ni SLA publicados, así que la mejora de tiempos es un claim sin medir ([[2026-1026-noones-dev-noones-sin-precios-ni-limites-ni-documentacion-publica]]). La diferencia con el widget del producto propio es que allí la comunicación en tiempo real es **infraestructura de primer orden**, no una función decorativa ([[2026-1022-myclone-widget-comunicacion-websocket]]).

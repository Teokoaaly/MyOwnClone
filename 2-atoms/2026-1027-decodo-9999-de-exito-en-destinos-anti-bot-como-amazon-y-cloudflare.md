---
id: 2026-1027-decodo-9999-de-exito-en-destinos-anti-bot-como-amazon-y-cloudflare
type: atom
certainty: tentative
sources: [sources/2026-10-26-decodo-smartproxy-home.md, sources/2026-10-26-decodo-web-data-api-pricing.md]
links: ["[[2026-1026-decodo-metricas-de-proxyway-2024-como-fuente-de-las-cifras-de-exito-y-uptime]]", "[[2026-1024-brightdata-web-unlocker-resuelve-captcha-y-no-requiere-kyc]]", "[[2026-1026-decodo-fraud-score-32-72-contra-45-57-del-pool-global]]", "[[2026-1027-decodo-web-data-api-ocho-planes-mensuales-con-limite-de-crawls-y-paginas]]"]
---

## Claim
La home de Decodo publica una promesa de éxito **específica por clase de destino**: *"**99.99% success** on the hard, anti-bot-protected targets such as **Amazon and Cloudflare-protected sites** – that trip up most AI-native scraping tools."* La página de precios de la Web Data API repite, en la lista de features **incluidas en todos los planes**, un **"99.99% success rate"** genérico. El hero de la home añade además **"<0.2s response time"** y **"99.99% uptime"**.

Los tres números conviven en la misma marca con las cifras de la página de proxies, que son distintas y **atribuidas a un tercero con metodología declarada**: "<0.5s avg. response time", "99.92% success rate" y "99.99% uptime", medidos por Proxyway 2024 contra `ipinfo.io/ip`.

## Why It Matters
El vault ya tiene el marco para juzgar esto: [[2026-1026-decodo-metricas-de-proxyway-2024-como-fuente-de-las-cifras-de-exito-y-uptime]] estableció que el **99,92 % de éxito no es una promesa contractual sino una medición de tercero con fecha, y además mide conectividad, no supervivencia ante un sitio que bloquea** — porque el objetivo de la prueba era `ipinfo.io/ip`, un endpoint que casi nadie bloquea. Es exactamente el criterio que decide un scraping real.

Y aquí aparece **la cifra opuesta**: **99,99 % de éxitospecifically contra Amazon y sitios protegidos por Cloudflare**. Es decir, el proveedor **sustituye deliberadamente el 99,92 % (con método y sin metodología de bloqueo) por un 99,99 % (sin método y específicamente contra objetivos que bloquean)**. El 99,99 % es **más alto y menos auditable**: no dice cuántas peticiones, contra qué URLs, en qué ventana, ni qué cuenta como éxito. Y la cifra de latencia pasa en la dirección contraria: **<0,2 s en el hero frente a <0,5 s en la página de precios** — el doble.

El detalle del corpus que el vault ya tiene sobre el pool de Decodo ([[2026-1026-decodo-fraud-score-32-72-contra-45-57-del-pool-global]]) es relevante como contexto: un **fraud score de 32,72 frente a una media global de 45,57** describe un pool relativamente limpio, y ese es el activo que hace plausible un 99,99 % contra sitios con anti-bot. Pero plausible no es lo mismo que medido.

Para el modelo de coste, la consecuencia práctica es que **el vault no puede usar ninguna de las tres cifras como parámetro de reintentos**. Con 99,92 % medido, un lote de 100.000 peticiones son 80 fallos y el coste del reintento es acotable. Con 99,99 % sin método, **el número de fallos es desconocido**, y si el scraper factura por mil de requests ([[2026-1027-decodo-la-unidad-no-es-estable-requests-paginas-y-crawls]]), cada reintento es cuota consumida: **el coste del fallo es el mismo que el del éxito**.

## [FRICTION]
> [[2026-1026-decodo-metricas-de-proxyway-2024-como-fuente-de-las-cifras-de-exito-y-uptime]] afirma que "el 99,92 % mide conectividad, no supervivencia ante un sitio que bloquea — y el criterio que decide un alta real es el segundo", y trata las cifras propias de Decodo como **cifras de marketing de página** sin metodología adjunta, aunque la metodología exista en el FAQ para los residenciales.
> Este átomo presiona esa lectura en el punto más fuerte: la home **sí** publica una cifra de éxito **específicamente contra objetivos anti-bot** —Amazon y Cloudflare— y es **más alta** (99,99 %) que la cifra medida (99,92 %). Es decir, **el marketing ya no es "una cifra más alta sin contexto"**: es una cifra **más alta y además temáticamente relevante**, la que el vault más necesitaría para cotizar reintentos, pero **sin ninguna de las garantías que el átomo viejo exige** (nº de peticiones, objetivo, modo de sesión, fecha). Y en sentido inverso, la latencia se **duplica** entre hero y página de precios (<0,2 s frente a <0,5 s).
> Ambas no pueden ser completamente correctas: o la cifra de la home es marketing sin medición —en cuyo caso el vault debe seguir usando 99,92 % porque es la única con método—, o existe una medición de éxito contra Amazon/Cloudflare que el proveedor no publica, en cuyo caso **el proveedor retiene deliberadamente el dato que mejor sostiene su producto**. Marcado para juicio humano, no auto-resuelto: la captura no publica método, tamaño de muestra ni ventana para ninguna de las dos cifras.

## Nota de verificación
Frases transcritas literalmente. `certainty: tentative` porque las tres cifras son **claims de página**, no mediciones con método visible: la home no dice qué_urls, cuántas peticiones ni en qué fecha se midió el 99,99 %. La captura **no** publica: el método del 99,99 %, si la cifra incluye reintentos internos, ni el significado exacto de "success" ( ¿página servida o datos extraídos? ).

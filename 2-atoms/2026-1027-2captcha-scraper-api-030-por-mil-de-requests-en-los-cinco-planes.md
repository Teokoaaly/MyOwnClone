---
id: 2026-1027-2captcha-scraper-api-030-por-mil-de-requests-en-los-cinco-planes
type: atom
certainty: solid
sources: [sources/2026-10-26-2captcha-pricing-scraper-api.md]
links: ["[[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]", "[[2026-1024-iproyal-web-unblocker-ia-a-1-dolar-por-1000-solicitudes]]", "[[2026-1026-anticaptcha-descuento-automatico-por-volumen-diario]]"]
---
## Claim
La página de precios del Scraper API de 2Captcha publica **cinco planes** —**Scraper-1K (1.000 requests, $0.3), Scraper-10K (10.000, $3), Scraper-100K (100.000, $30), Scraper-1M (1.000.000, $300) y Scraper-10M (10.000.000, $3.000)**— y en **los cinco** la columna "Price per 1,000 requests" es idéntica: **$0.3**. La acción es "Buy" a `2captcha.com/pay`. El precio unitario es, por tanto, **invariante al volumen**: un plan de 10 millones de requests cuesta exactamente 10.000 veces el de 1.000.

## Why It Matters
Es la primera línea del corpus donde el proveedor **declara el precio de la extracción por request** y lo hace **sin escalera**: el único mecanismo de mejora es el pre-pago de un volumen mayor, no un mejor precio unitario. La consecuencia aritmética es que **el coste unitario de scraping con 2Captcha es $0,0003 por request en todo el rango**, de modo que un modelo de coste del vault no necesita tramos: basta con multiplicar requests × $0,0003.

El dato comparativo más relevante: ese **$0,30 por 1.000 requests** es **3,3 veces más barato que el "from $1.00/1000 requests"** del Web Unblocker de IPRoyal ([[2026-1024-iproyal-web-unblocker-ia-a-1-dolar-por-1000-solicitudes]]) para una capacidad conceptual equivalente (obtener datos sin bloquearse), y **más barato que el suelo de $0.5 por 1000** del propio catálogo de captchas de 2Captcha ([[2026-1027-2captcha-catalogo-completo-de-48-filas-de-captcha]]). Es decir: **para el mismo proveedor, la capa de extracción es más barata que la de resolución de captchas**.

La lectura estructural: los cinco planes son **cinco tamaños de precarga del mismo producto**, no cinco productos. El vault debe registrar esto como "precio único por request con cinco denominaciones de venta", lo que lo distingue tanto de las escaleras de volumen de IPRoyal y DataImpulse como de los rangos con descuento automático de AntiCaptcha ([[2026-1026-anticaptcha-descuento-automatico-por-volumen-diario]]).

## [FRICTION]
> [[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]] describe el giro de 2Captcha hacia el scraping con el argumento económico de que "cobrar por el **resultado útil** (extracción exitosa) y no por el recurso", y cita su Web Unblocker como "you pay only for successful data extraction".
> Este átomo presiona ese argumento en un punto verificable: **la otra línea de scraping del mismo proveedor se cobra por request, no por extracción exitosa**. El Scraper API está publicado a **$0,3 por 1.000 requests** —unidad de entrada— sin ninguna cláusula de éxito visible en la página. Si "pagar por el resultado" fuera una propiedad del producto, ambos productos del mismo proveedor no podrían usar unidades tan distintas sin contradicción.
> Ambas no pueden ser completamente correctas: o "pay only for successful data extraction" describe una garantía comercial negociada caso por caso (y entonces no es una propiedad del catálogo), o el Scraper API no la aplica. Marcado para juicio humano, no auto-resuelto: la captura **no** publica si las peticiones fallidas o bloqueadas se facturan, y el Web Unblocker no tiene página de precios propia en esta captura.

## Nota de verificación
Precios transcritos literalmente de la tabla. La captura **no** publica: qué es una "request" (petición HTTP, URL, intento), si se factura lo fallido, el número de IPs, SLA, ni el precio del proxy subyacente.


## Nota de extensión 2026-10-27
La Web Data API de Decodo da **un segundo precio de catálogo por 1.000 requests** en el corpus, y **es la mitad**: el titular es **"From $0.15/1K"** —"Access web data, starting at $0.15/1K requests"— frente a los **$0,30 por 1.000 requests** del Scraper API de 2Captcha, cuyo precio unitario además es **invariante al volumen** en los cinco planes.

El contraste de estructura es lo que importa para el thread: 2Captcha cotiza **un único precio unitario en cinco tamaños de precarga** (nunca mejora por volumen), mientras que Decodo publica **una escalera de ocho planes** en la que el precio efectivo por mil **cae de forma monótona**: **$0,5000/1K páginas** en el plan de $19, **$0,3000** en el de $99, **$0,2075** en el de $249, **$0,1848** en el de $499, **$0,1611** en el de $999 y **$0,1514** en el de $1499. Es decir, **el titular de $0,15/1K solo es alcanzable en el plan más caro**, y su equivalente por crawls es $0,5169/1K.

El dato que el vault debe registrar para el agregador: **el precio por 1.000 requests del sector está entre $0,15 y $0,30**, y **el mismo número en dos proveedores significa dos cosas distintas** — en 2Captcha es el precio único del producto; en Decodo es el mejor caso de una escalera de suscripción con cuota. Ver [[2026-1027-decodo-el-titular-de-015-por-mil-solo-se-alcanza-en-el-plan-de-1499]] y [[2026-1027-decodo-la-unidad-no-es-estable-requests-paginas-y-crawls]].

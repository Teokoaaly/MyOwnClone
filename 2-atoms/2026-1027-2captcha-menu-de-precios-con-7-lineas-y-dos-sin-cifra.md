---
id: 2026-1027-2captcha-menu-de-precios-con-7-lineas-y-dos-sin-cifra
type: atom
certainty: solid
sources: [sources/2026-10-26-2captcha-pricing-mcp.md, sources/2026-10-26-2captcha-pricing-scraper-api.md, sources/2026-10-26-2captcha-pricing-browser-api.md, sources/2026-10-26-2captcha-pricing-data-annotation.md, sources/2026-10-26-2captcha-pricing-enterprise-support.md]
links: ["[[2026-1027-2captcha-scraper-api-030-por-mil-de-requests-en-los-cinco-planes]]", "[[2026-1027-2captcha-data-annotation-sin-precio-publico-solo-contacto]]", "[[2026-1027-2captcha-enterprise-support-sin-precio-publico-ni-cifras]]", "[[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]"]
---
## Claim
La sección de precios de 2Captcha (`2captcha.com/pricing`) es un **menú de siete líneas de producto**, idéntico en las cinco páginas capturadas: **Captcha** (`/pricing`), **Proxy** (`/pricing/proxy`), **Browser API** (`/pricing/browser-api`), **Scraper API** (`/pricing/scraper-api`), **MCP** (`/pricing/mcp`), **Data annotation** (`/pricing/data-annotation`) y **Enterprise support** (`/pricing/enterprise-support`). Las **cinco primeras** remiten a páginas de producto con catálogo o tabla (Captcha, Proxy, Browser API, Scraper API, MCP); las **dos últimas** (Data annotation y Enterprise support) no publican ninguna cifra y sustituyen el precio por un formulario de contacto.

## Why It Matters
El menú **es** la carta de precios de la compañía, y por eso el vault puede leerla como una tabla de dos columnas: **qué capacidad es producto cotizable y qué capacidad es servicio vendible a puerta cerrada**. Las siete líneas no son siete productos equivalentes: el captcha es **infraestructura medible** (precio por 1000, catálogo de 48 filas en [[2026-1027-2captcha-catalogo-completo-de-48-filas-de-captcha]]), el proxy es **red por GB**, dos líneas son **automatización de acceso** (Browser API por GB de tráfico y Scraper API por 1000 requests) y dos son **servicios** (anotación de datos y soporte enterprise) sin cifra. Esto confirma y precisa el giro registrado en [[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]: la compañía ya no vende "captchas" sino **una cartera de acceso a web** en la que el captcha es solo la primera pestaña.

La consecuencia para el modelo de coste del vault es una **regla de lectura del catálogo**: cuando una página de precios no tiene cifras, no es un fallo de captura ni una ambigüedad comercial — en esta carta es una **decisión deliberada del proveedor** sobre dónde termina el producto y empieza la negociación. Y da un indicador temprano y reutilizable: **la presencia de un formulario "Contact sales" en la pestaña es la señal, no la ausencia de dato**, porque el resto de pestañas funciona igual salvo en el precio.

El dato estructural más fino es que las dos pestañas opacas **comparten literalmente el mismo formulario** (mismos campos, mismo desplegable de temas con "Enterprise / VIP request", misma casilla de Terms of Service y Privacy Policy, mismo botón "Send"): no son dos procesos de venta distintos, es uno solo. Ver [[2026-1027-2captcha-data-annotation-sin-precio-publico-solo-contacto]] y [[2026-1027-2captcha-enterprise-support-sin-precio-publico-ni-cifras]].

Nota de verificación: la captura **no** publica una pestaña "Web Unlocker" ni "Fingerprints" — aunque el átomo del giro de 2026-10-24 las mencionara como parte de la oferta—, de modo que el menú capturado son **siete líneas visibles**, y no hay evidencia de que la carta completa tenga más.

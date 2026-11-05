---
id: 2026-1101-brightdata-el-hub-de-precios-no-publica-ninguna-cifra
type: atom
certainty: solid
sources: [sources/2026-10-31-brightdata-pricing.md, sources/2026-11-01-brightdata-pricing.md, sources/2026-11-02-brightdata-pricing.md]
links: ["[[2026-1031-brightdata-pricing]]", "[[2026-1024-brightdata-precios-por-ip-dos-tablas-sin-etiquetar]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
La página `brightdata.com/pricing` es un **catálogo de ocho fichas de producto sin ninguna cifra**: "Proxy Networks", "Web Scraper API", "Scraper Studio", "Scraping Browser", "SERP API", "Web Unlocker", "Datasets" y "Bright Insights", cada una con un único enlace "See Pricing" que lleva a una subpágina de precio propia (`/pricing/proxy-network`, `/pricing/web-scraper`, `/pricing/web-scraper/studio`, `/pricing/scraping-browser`, `/pricing/serp`, `/pricing/web-unlocker`, `/pricing/datasets`, `/pricing/insights`). Tres capturas consecutivas del mismo URL (2026-10-31, 2026-11-01, 2026-11-02) repiten la misma estructura de ocho fichas y **no publica ni un solo precio, plan, umbral, mínimo ni unidad de cobro**. El único dato numérico del hub es "400M+ monthly Residential IPs".

## Why It Matters
Para el vault esto explica por qué la captura de precios de Bright Data sale siempre vacía de cifras: **`/pricing` no es una página de precios, es un índice de ocho páginas de precios**. Es el mismo patrón de navegación —landing con tiles y "See Pricing"— que ya tienen otros proveedores del corpus, y significa que el dato de coste solo existe un clic más adentro: en `/pricing/proxy-network` ([[2026-1024-brightdata-precios-por-ip-dos-tablas-sin-etiquetar]]), que es de donde salen el PAYG de $4/GB, la escalera 141→798 GB y el compromiso de $499. Consecuencia operativa para el agregador de precios: **una sola captura del hub no da ningún dato cotizable**, y el número de subpáginas a visitar (ocho) es exactamente el coste de construcción de la tabla de coste por insumo.
Y para el eje abierto del vault —coste por asiento vs coste por infraestructura— el hub es la prueba de que **el precio de este proveedor no se puede reducir a un único número por producto**: el modelo vive en ocho subpáginas con unidades distintas (GB, créditos, peticiones, suscripción), tal y como el átomo de la página de precios ya anticipaba ([[2026-1031-brightdata-pricing]]).

## [FRICTION]
> [[2026-1031-brightdata-pricing]] afirma que "Bright Data's pricing is proxy/infrastructure-tier based, where cost scales by the type of residential, datacenter, or ISP proxy and volume of traffic".
> Este átomo presiona esa afirmación en su origen: **la fuente citada por aquel átomo (`sources/2026-10-31-brightdata-pricing.md`) no contiene ninguna de esas cosas**. Es la ficha de ocho tiles sin cifras; no nombra "residential, datacenter, ISP" como niveles de precio, no menciona volumen, y no publica ningún escalón. Los números de tiers y volumen vienen de otra página distinta (`brightdata.com/pricing/proxy-network`, capturada el 2026-10-24), no de `/pricing`. Ambas no pueden ser completamente correctas: o la página citada sostiene la afirmación y la captura está incompleta, o la afirmación se extrapoló desde una página que no es la que dice. Marcado para juicio humano, no auto-resuelto: la captura de `/pricing` no está en blanco por error — tres capturas en tres días dan el mismo hub sin cifras.
> Nota adicional de verificación: el bloque `[FRICTION]` del átomo viejo enlaza a `2026-1025-refinery-brightdata-proxy-pricing.md`, y ese nombre de archivo no existe hoy en `2-atoms/`; el enlace queda apuntando a una nota ausente.

## Nota de verificación
Cifras y rutas transcritas literalmente. La captura **no** publica: los precios de ninguna de las ocho subpáginas, ni qué parte de la oferta es autoservicio y qué parte es "contact sales", ni si las ocho fichas comparten un mismo sistema de unidades.

## Actualización 2026-11-04
La **cuarta captura** del slug (`sources/2026-11-04-brightdata-pricing.md`, 371 líneas, 743 palabras) **corrobora este átomo sin añadir ni una cifra**: repite las mismas ocho fichas, los mismos ocho enlaces "See Pricing" con href y los mismos dos únicos números de la página ("400M+ monthly Residential IPs" y "Trusted by 50,000+ customers worldwide"). Es byte a byte idéntica a la del 2026-11-01 — detalle en [[2026-1104-brightdata-cuarta-captura-del-slug-identica-byte-a-byte-a-la-del-11-01]].
Lo que sí añade esta captura es la **medida del coste de la repetición**: de las ocho subpáginas de precio que este hub publica, **el vault solo ha capturado una** (`/pricing/proxy-network`, el 2026-10-24); las otras siete nunca se han visitado, y la lista de lectura apunta al hub en vez de a ellas — detalle en [[2026-1104-brightdata-siete-de-las-ocho-subpaginas-de-precio-nunca-se-han-capturado]].

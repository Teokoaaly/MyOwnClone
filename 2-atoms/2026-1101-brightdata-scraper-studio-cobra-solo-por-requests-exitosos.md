---
id: 2026-1101-brightdata-scraper-studio-cobra-solo-por-requests-exitosos
type: atom
certainty: solid
sources: [sources/2026-11-01-brightdata-pricing.md, sources/2026-11-02-brightdata-pricing.md, sources/2026-10-31-brightdata-pricing.md]
links: ["[[2026-1026-brightdata-un-credito-por-request-y-cinco-por-mb-en-browser-api]]", "[[2026-1026-brightdata-pool-unico-de-creditos-cinco-productos]]", "[[2026-1026-brightdata-capa-de-servicio-encima-de-la-api]]"]
---

## Claim
La ficha de **Scraper Studio** en la página de precios declara tres cosas que no aparecen en ninguna otra ficha del catálogo: **"Only pay for successful requets"** [sic, errata en el original], **"Free tier pricing available"** y **"Launch AI-powered scrapers for any website in minutes"**. Es decir, el producto se posiciona explícitamente como **cobro por request exitoso**, no por request lanzado ni por registro extraído.

## Why It Matters
Es la primera vez que el vault ve al proveedor **vender el resultado y no el intento**, y eso tiene una consecuencia directa sobre el modelo de coste de la thread de agregador de precios: si Bright Data solo factura lo que extrae con éxito, el coste marginal de un scraper no depende de la tasa de bloqueo del sitio sino del número de **registros válidos**, lo que convierte al scraper en un producto con coste variable de calidad, no solo de volumen. Para MyOwnClone, que ya tiene su pipeline de ingesta asíncrono con jobs y reindexado de embeddings ([[2026-1022-myclone-scraping-ingestion-pipeline]]), esa es exactamente la frontera entre "construir" y "comprar": el proveedor está cobrando por el resultado de una tarea que el vault ya construye ([[2026-1026-brightdata-capa-de-servicio-encima-de-la-api]]).
El matiz que hay que guardar es que "free tier pricing available" aquí **no coincide con el free tier de 5.000 créditos** que el vault ya tiene atomizado como pool único de cinco productos ([[2026-1026-brightdata-pool-unico-de-creditos-cinco-productos]]): la landing de precios dice "free tier" sin cifras ni unidades, mientras la documentación dice 5.000 créditos al mes y un crédito por carga de página ([[2026-1026-brightdata-un-credito-por-request-y-cinco-por-mb-en-browser-api]]). Si el "free tier" de la landing fuera el mismo pool, la unidad de facturación sería la **carga de página**, no el "successful request" que anuncia la misma ficha.

## [FRICTION]
> [[2026-1026-brightdata-un-credito-por-request-y-cinco-por-mb-en-browser-api]] afirma que **Scraper Studio consume 1 crédito por carga de página** —*"One credit per page load, not per record"*— y que Web Unlocker, SERP API y Web Scraper API consumen 1 crédito por request o record.
> Este átomo presiona esa tabla desde la página de precios oficial: la ficha de Scraper Studio dice literalmente **"Only pay for successful requets"**, que describe una unidad distinta de la que la documentación atribuye al mismo producto (carga de página). Si una carga de página que falla se factura igual, entonces "solo se paga por lo que tiene éxito" es publicidad; si no se factura, entonces la documentación de "one credit per page load" está incompleta o cuenta también las fallidas. Ambas no pueden ser completamente correctas: o la unidad de la landing es marketing, o la tabla de la documentación usa "page load" de forma laxa. Marcado para juicio humano, no auto-resuelto: la captura **no** publica la tabla de precios de Scraper Studio ni el significado de "successful request" frente a "page load".

## Nota de verificación
Texto transcrito literalmente, errata incluida ("requets"). La captura **no** publica: el precio de Scraper Studio, qué es una "página" para el proveedor, si un record fallido cuenta, ni el contenido del "free tier" que la landing anuncia.

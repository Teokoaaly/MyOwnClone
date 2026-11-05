---
id: 2026-1026-brightdata-capa-de-servicio-encima-de-la-api
type: atom
certainty: solid
sources: [sources/2026-10-25-brightdata-docs-intro.md]
links: ["[[2026-1026-brightdata-marketplace-de-datasets-con-250-dominios]]", "[[2026-1022-myclone-scraping-ingestion-pipeline]]", "[[2026-1024-brightdata-web-unlocker-resuelve-captcha-y-no-requiere-kyc]]"]
---

## Claim
La familia "Data extraction" de la documentación ofrece, junto a los productos API, dos offerings de **servicio**: **"Scraper Studio — Build and host custom scrapers"** y **"Managed services — Done-for-you data collection"** (esta última enlazada a `brightdata.com/pricing/managed-services`, fuera del árbol de documentación). El titular de la home resume la oferta comercial como **"Scrape any site, buy ready-made datasets"**, es decir, tres Roads: **scrapear en casa, comprar el dato hecho y contratar la recogida**.

## Why It Matters
El vault tiene medida la ingesta como una **construcción propia**: pipeline asíncrono con jobs, `auto-onboard`, `bulk-onboard`, estado y auditoría, y un subsistema de voz con reindexado de embeddings ([[2026-1022-myclone-scraping-ingestion-pipeline]]). Scraper Studio es la **externalización parcial** de esa capa (el cliente define el scraper, el proveedor lo hospeda); Managed services es la **externalización total** (el proveedor recoge y entrega). La diferencia entre ambos es exactamente la que decide el build-vs-buy del vault: **Scraper Studio conserva la lógica de extracción en el cliente y solo delega la ejecución**; Managed services la elimina.
El dato que hay que retener es que el proveedor con el coste de red más alto del sector (PAYG a $4/GB, compromiso mínimo de $499) también vende **la gestión de la tarea**, y que su página de precios de managed services **no está en la captura**. Es decir: la capa de servicio es el punto donde el proveedor puede mover el coste de "tráfico" a "proyecto", y el vault **no puede cotizarlo**. Conviene además no confundirlo con Web Unlocker, que es un producto API distinto —desbloquear y devolver contenido ([[2026-1024-brightdata-web-unlocker-resuelve-captcha-y-no-requiere-kyc]])— y no una recogida completa.

## Nota de verificación
Nombres y descripciones transcritos literalmente. La captura **no publica**: el precio de Scraper Studio ni de Managed services, qué parte del trabajo se factura como tráfico y qué parte como servicio, ni los plazos de entrega.

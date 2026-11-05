---
id: 2026-1026-brightdata-marketplace-de-datasets-con-250-dominios
type: atom
certainty: solid
sources: [sources/2026-10-25-brightdata-docs-intro.md]
links: ["[[2026-1024-iproyal-casos-de-uso-precios-y-viajes]]", "[[2026-1022-myclone-scraping-ingestion-pipeline]]", "[[2026-1026-brightdata-endpoint-unico-datasets-v3-con-dataset-id]]"]
---

## Claim
La documentación incluye un producto de **datos ya hechos**: **"Dataset Marketplace — Ready-made datasets, 250+ domains"**, dentro de la familia "Data extraction", y el titular de la home ofrece **"Scrape any site, buy ready-made datasets"**. En la familia "AI training data" aparecen **"Media Data API — Video, audio and captions at scale"** y **"Web Archive — Cached web page snapshots"**, bajo el encabezado *"Media and archived pages for model training."* En "Web search", **"Business Search — Find people and companies by criteria"**, bajo *"Search records and the live web by API."* La captura **no publica** el precio ni el formato de ningún dataset, ni la unidad de cobro de Media Data API o Web Archive.

## Why It Matters
Es la alternativa que el vault no tenía registrada al lado del scraping: **comprar el dato ya extraído en vez de construir el pipeline que lo extrae**. El marketplace declara **250+ dominios**, lo que para un agregador de precios significa que la capa de acceso podría ser **una compra de catálogo por vertical** en lugar de un contrato de proxy más una orquestación de scraping ([[2026-1024-iproyal-casos-de-uso-precios-y-viajes]]).
El vault ya tiene documentado el coste y la complejidad de construir la ingesta: pipeline asíncrono con jobs, `auto-onboard`, `bulk-onboard`, estado y auditoría por job ([[2026-1022-myclone-scraping-ingestion-pipeline]]). Un catálogo de "ready-made datasets" es exactamente la alternativa de compra para esa capa, y **su unidad de precio —que la captura no publica— es la variable que decide el build-vs-buy**. La captura deja claro, eso sí, que la misma plataforma cubre los tres ejes: **comprar dato hecho**, **scrapear uno mismo** con el mismo `dataset_id` y `format=json` ([[2026-1026-brightdata-endpoint-unico-datasets-v3-con-dataset-id]]), y **comprar histórico** (Web Archive, "cached web page snapshots").
El tercer eje del catálogo tiene nombre propio y es un vector que no estaba cartografiado en el vault: **Business Search, "find people and companies by criteria"**, un buscador de **personas y empresas** por API — la misma plataforma que da la IP y el desbloqueo da también el **listado de a quién verificar**. Ese producto tiene su propio átomo ([[2026-1026-brightdata-business-search-personas-y-empresas-por-criterio]]), y aquí solo se deja constancia de que convive, en la misma página y bajo el mismo proveedor, con la venta de datos ya extraídos.

## Nota de verificación
Cifras y nombres transcritos literalmente. La captura **no publica**: el precio por dataset, el formato (CSV/JSON/parquet), la frecuencia de actualización, ni qué hay dentro de los "250+ dominios".

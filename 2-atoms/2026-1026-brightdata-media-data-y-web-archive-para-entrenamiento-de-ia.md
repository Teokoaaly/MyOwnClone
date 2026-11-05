---
id: 2026-1026-brightdata-media-data-y-web-archive-para-entrenamiento-de-ia
type: atom
certainty: solid
sources: [sources/2026-10-25-brightdata-docs-intro.md]
links: ["[[2026-1022-myclone-knowledge-library-fuentes]]", "[[2026-1024-dataimpulse-uso-de-ips-en-agentes-y-visibilidad-en-ia]]", "[[2026-1022-myclone-scraping-ingestion-pipeline]]"]
---

## Claim
Bajo el encabezado "AI training data" —*"Media and archived pages for model training"*— la documentación ofrece dos productos: **"Media Data API — Video, audio and captions at scale"** y **"Web Archive — Cached web page snapshots"**. El primero entrega **vídeo, audio y subtítulos**; el segundo, **instantáneas de páginas web en caché**. La captura **no publica** precio, unidad de cobro, ni ventana de retención de las instantáneas.

## Why It Matters
El vault tiene medida la capa de ingesta como **construcción propia con siete tipos de fuente**, límites de tamaño por archivo (**10 MB** de audio, **200 MB** por vídeo, tope total **500 MB**) y un subsistema aparte de voz con reindexado de embeddings ([[2026-1022-myclone-knowledge-library-fuentes]]). Y tiene medida su alternativa: DataImpulse declara el uso de sus IPs para "build large, clean training and RAG datasets" con una lista nominal de fuentes —Amazon, eBay, Walmart, Shopify, Allegro; Google, Bing, DuckDuckGo… ([[2026-1024-dataimpulse-uso-de-ips-en-agentes-y-visibilidad-en-ia]]).
La novedad de esta captura es que **el corpus ya está en catálogo con nombre y unidad**: "vídeo, audio y subtítulos a escala" es exactamente el perfil de la Knowledge Library del vault —**incluidos los subtítulos, que el pipeline propio tiene como capa de processing y no como tipo de fuente**—, y "cached web page snapshots" es la alternativa comprada a la instantánea histórica que un agregador de precios necesitaría para reconstruir la trayectoria de un precio y no solo su valor actual ([[2026-1022-myclone-scraping-ingestion-pipeline]]).
La consecuencia para el modelo de coste del vault es la misma que en el resto de la thread: **la capa de ingesta es hoy una construcción y mañana es una línea de catálogo**, y el thread de build-vs-buy del producto necesita ese número. Lo que la captura no da es precisamente el número: **ni el precio de Media Data API ni la ventana de retención del archivo**.

## Nota de verificación
Nombres y descripciones transcritos literalmente. La captura **no publica**: unidad de cobro, precio, si el archivo incluye metadatos o solo el medio, ni el período de cobertura del Web Archive.

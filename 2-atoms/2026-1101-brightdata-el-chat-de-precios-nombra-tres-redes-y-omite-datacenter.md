---
id: 2026-1101-brightdata-el-chat-de-precios-nombra-tres-redes-y-omite-datacenter
type: atom
certainty: solid
sources: [sources/2026-11-01-brightdata-pricing.md, sources/2026-11-02-brightdata-pricing.md, sources/2026-10-31-brightdata-pricing.md]
links: ["[[2026-1024-brightdata-cuatro-tipos-de-red-y-solo-tres-pestanas-de-precio]]", "[[2026-1026-brightdata-cinco-tipos-de-red-en-docs-contra-cuatro-en-faq]]", "[[2026-1024-brightdata-precios-por-ip-dos-tablas-sin-etiquetar]]"]
---

## Claim
El widget de chat de la página de precios ("Sophie", *"Ask Sophie about any service you need from Bright Data"*) incluye respuestas predefinidas que describen las redes de IP con una **tercera taxonomía**. A la pregunta *"I want to scrape LinkedIn profiles by URL"* la respuesta es **"Target your traffic by geolocation with residential, ISP, or mobile proxies"** — exactamente **tres redes: residential, ISP y mobile**, y **datacenter no aparece**. Las otras tres respuestas predefinidas cubren *"How do I collect Google Maps business data?"* → *"Get structured data like names, addresses, and phone numbers from Google Maps listings"*, *"I want to extract product data from ecommerce sites"* → *"Scrape product listings, prices, and reviews from Amazon, Shopify, and more"*, e *"I need proxies"* → *"Quickly setup proxy solution that match your specific needs today."*

## Why It Matters
El vault ya tiene registradas **dos** taxonomías de redes en el mismo dominio y ahora aparece una **tercera, en la página que el proveedor usa para vender**: docs = "cinco network types" (tres redes + dos herramientas), FAQ de precios = "cuatro redes" (Datacenter, ISP, Residential, Mobile), y el chat de venta = **tres redes** (Residential, ISP, Mobile), con **Datacenter —la más barata— omitida del mensaje de venta** ([[2026-1024-brightdata-cuatro-tipos-de-red-y-solo-tres-pestanas-de-precio]], [[2026-1026-brightdata-cinco-tipos-de-red-en-docs-contra-cuatro-en-faq]]).
La diferencia no es cosmética, porque **cada taxonomía deja una partida distinta sin cotizar**: el FAQ deja el móvil sin pestaña de precio, los docs ocultan el móvil detrás de dos herramientas de software, y el chat oculta el datacenter. Para la tabla de coste por insumo del vault ([[2026-1024-brightdata-precios-por-ip-dos-tablas-sin-etiquetar]]) esto significa que **la red que más se vende es la que menos se explica en cada página** —y que el número "de tipos de red" del proveedor no es una propiedad del producto sino una propiedad de la página.
El contenido de las otras tres respuestas tiene además valor propio para el vault: el proveedor **promete tres casos de extracción ya resueltos** —perfiles de LinkedIn por URL, fichas de Google Maps (nombre, dirección, teléfono) y fichas de producto en Amazon/Shopee (listings, precios, reseñas)— que son exactamente las tres fuentes que el agregador de precios y el pipeline de ingesta de MyOwnClone ([[2026-1022-myclone-scraping-ingestion-pipeline]]) tendrían que construir.

## [FRICTION]
> [[2026-1024-brightdata-cuatro-tipos-de-red-y-solo-tres-pestanas-de-precio]] afirma que el proveedor declara **cuatro redes de IP** (Datacenter, ISP, Residential, Mobile) y [[2026-1026-brightdata-cinco-tipos-de-red-en-docs-contra-cuatro-en-faq]] afirma que la documentación declara **cinco "network types"** de los que solo tres son redes.
> Este átomo añade una tercera declaración incompatible: la página de precios, en su propio widget de venta, nombra **tres redes** —Residential, ISP y Mobile— y en esa lista **Datacenter no está**. Las tres no pueden ser simultáneamente la taxonomía oficial: o son cuatro (y el chat omite una), o son tres (y el FAQ y los docs cuentan más cosas que redes). Marcado para juicio humano, no auto-resuelto: el chat es material de marketing, no una declaración de producto, y la captura no publica el precio del datacenter ni el del móvil en ninguna de las tres páginas.

## Nota de verificación
Textos transcritos literalmente. La captura **no** publica: qué redes cubre la suscripción de cada respuesta, si el chat es un bot real o un guion, ni el precio de ninguna de las tres redes nombradas.

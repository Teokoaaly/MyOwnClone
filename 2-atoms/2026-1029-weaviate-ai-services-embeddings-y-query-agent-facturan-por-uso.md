---
id: 2026-1029-weaviate-ai-services-embeddings-y-query-agent-facturan-por-uso
type: atom
certainty: solid
sources: [sources/2026-10-29-weaviate-cloud-pricing.md]
links: ["[[2026-1026-heroku-embeddings-0-10-y-0-12-por-millon-de-tokens-de-entrada]]", "[[2026-1022-myclone-viaje-embeddings-voyage]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---
## Claim
Weaviate Cloud incluye **servicios de IA propios que se facturan por uso, incluidos en todos los planes**: el **Embedding Service** con tres modelos y precio por millón de tokens — **SNOWFLAKE ARCTIC-EMBED-M-V1.5 a $0.025**, **SNOWFLAKE ARCTIC-EMBED-M-V2.0 a $0.040** y **MODERNVBERT COL (etiqueta rafeada en la captura como "MODERNVBERT COLMODERNVBERT") a $0.065** — y el **Query Agent**, con **1.000 requests/mes de prueba gratuita**, un **plan mensual de $30 por organización que incluye 4.000 requests** y **requests adicionales ilimitados por uso**. Los límites de ratio del Query Agent suben por plan: **1.000 req/mes en Free, 30.000 req/mes en Flex, ilimitados en Premium** (Shared y Dedicated). Una salvedad de la tabla: **Embeddings figura como "Coming soon" en Premium Dedicated**, aunque la cabecera del bloque diga "included on every plan".

## Why It Matters
Es la **tercera fuente de embeddings con precio de lista** del vault, y la más barata por millón de tokens: **$0.025–$0.065 por 1M** frente a **$0.10–$0.12 de Cohere en Heroku** ([[2026-1026-heroku-embeddings-0-10-y-0-12-por-millon-de-tokens-de-entrada]]), y frente a un Voyage cuyo precio el vault **no ha verificado** ([[2026-1022-myclone-viaje-embeddings-voyage]]). La comparación tiene un matiz que la tabla de Heroku no tiene: **aquí el embedding se factura por tokens consumidos y el Query Agent por requests, no por tenant ni por documento**, así que el coste escala con el uso del cliente, no con el número de clientes — que es exactamente la frontera entre `categoryIngestion` (facturable al tenant) y `categoryPlatformOps` (pagada por la plataforma) del corte de costes del vault ([[2026-1022-costes-por-categoria-tenant]]). La observación estructural es que **Weaviate no solo almacena vectores: vende la inferencia que los produce**, lo que abre la tentación de mover ahí el embedding que hoy está partido entre Voyage y `text-embedding-3` — pero atarlo al vector store ata también el modelo, y por tanto ata el coste de la indexación al proveedor de base de datos.

## Nota de verificación
La fuente **no** publica qué modelo de embeddings es el que usa por defecto el vectorizador de Weaviate, ni los precios del Embedding Service en self-hosted (donde el servicio no existe: es una de las tres funciones que solo aporta el envoltorio gestionado). El bloque de la tabla marca Embeddings como **"Coming soon" solo en Premium Dedicated**; en Free es un contingent de **2.000 req/día** y en Flex y Premium Shared es **usage-based**.

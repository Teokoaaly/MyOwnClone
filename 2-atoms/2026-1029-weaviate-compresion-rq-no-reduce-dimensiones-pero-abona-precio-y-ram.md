---
id: 2026-1029-weaviate-compresion-rq-no-reduce-dimensiones-pero-abona-precio-y-ram
type: atom
certainty: solid
sources: [sources/2026-10-29-weaviate-cloud-pricing.md]
links: ["[[2026-1029-weaviate-cobra-por-dimensiones-vectoriales-no-por-objetos]]", "[[2026-1029-weaviate-autoalojado-competiria-por-ram-con-postgres-y-redis-en-el-vps]]", "[[2026-1029-qdrant-billing-model]]"]
---
## Claim
La compresión de vectores en Weaviate **no reduce el número de dimensiones facturadas**, pero sí abarata el precio por dimensión y reduce la memoria y CPU de búsqueda. La FAQ lo dice literal: *"Compression does not change the number of vector dimensions stored, but it reduces the memory and compute required for search. More aggressive compression yields greater efficiency, reflected in discounted list prices for vector dimensions."* La calculadora de precios expone **dos perfiles de optimización**: **"Cost Optimized"** —*"Lower memory footprint and storage cost. Suitable for small or non-latency-sensitive workloads"*, con índice **HFresh** y compresión **Auto** — y **"Performance Optimized"** —*"In-memory retrieval balancing speed and search quality. Suitable for most workloads"*, con índice **HNSW** y compresión **RQ-8**. La tabla de planes marca **"Vector compression" como ✓ en los cuatro niveles, incluidos Free y Flex**, mientras que **"Flexible index types" es × solo en Free**.

## Why It Matters
Es la palanca de coste más fina que ofrece el motor, y es exactamente la que compite por la RAM del VPS: **la compresión es lo que hace que un motor vectorial quepa en un presupuesto de memoria pequeño**, y lo hace sin tocar la factura dimensional — el mismo corpus con RQ-8 que con HNSW se factura por las mismas dimensiones, solo que más barato por dimensión y con menos RAM. Para el stack autoalojado, esto significa que **la diferencia entre "Weaviate no cabe en el VPS" y "Weaviate sí cabe" puede ser una decisión de compresión, no de RAM del servidor** ([[2026-1029-weaviate-autoalojado-competiria-por-ram-con-postgres-y-redis-en-el-vps]]).

La asimetría de la tabla de planes es lo que hay que retener: **Free y Flex ya traigan compresión ✓**, así que la diferencia real entre planes no está en la compresión sino en el **índice flexible** (× solo en Free) y en el **perfil de optimización por defecto** — que en la calculadora puede ser Cost Optimized o Performance Optimized según el caso. Y para el competidor de categoría, la comparación es instructiva: **Qdrant factura por vCPU/memoria/storage realmente consumidos** ([[2026-1029-qdrant-billing-model]]), es decir, **la compresión que en Weaviate es un descuento explícito de precio, en Qdrant es automáticamente un ahorro de CPU y RAM** — mismo mecanismo económico, modelo de cobro distinto.

## Nota de verificación
La fuente **no publica las tarifas por dimensión concretas de cada nivel de compresión** (RQ-1, RQ-4, RQ-8) ni el descuento porcentual asociado a cada uno: solo afirma que la compresión más agresiva produce precios más bajos. La correspondencia entre "Cost Optimized" y HFresh y "Performance Optimized" y HNSW/RQ-8 está **en la calculadora de la propia página**; el fragmento de precios no marca explícitamente que HFresh ⇄ RQ-8. Los mínimos de RAM para un perfil concreto **no están publicados**.

---
id: 2026-1029-weaviate-cobra-por-dimensiones-vectoriales-no-por-objetos
type: atom
certainty: solid
sources: [sources/2026-10-29-weaviate-cloud-pricing.md]
links: ["[[2026-1029-weaviate-cloud-flex-minimo-45-dolares-al-mes]]", "[[2026-10-29-vectorize]]", "[[2026-1022-myclone-viaje-embeddings-voyage]]", "[[2026-1029-qdrant-billing-model]]"]
---
## Claim
Weaviate Cloud **no factura por objetos ni por consultas: factura por el número total de dimensiones vectoriales almacenadas**, más almacenamiento y backup por separado. La FAQ lo dice literal: *"The total count of vector dimensions is a good indicator of the resources required — a simple number you can calculate, rather than abstract Read/Write units or CPU cycles."* Las tarifas de lista por 1M de dimensiones son **Flex desde $0.00465**, **Premium compartido desde $0.003875** y **Premium dedicado desde $0.002718**; el **almacenamiento va desde $0.12/GiB** (Flex) y el **backup desde $0.03036/GiB** (Flex). El precio de las dimensiones **varía por tipo de índice, método de compresión y región**; el de storage por cloud y región.

## Why It Matters
Cambia la unidad de medida con la que hay que estimar el coste del RAG: **no importa cuántos documentos indexa el tenant, importa el producto `nº de chunks × nº de dimensiones del modelo`**. Con un Voyage/OpenAI de 1.536 dimensiones, los **100.000 objetos del free tier** equivalen a **153,6 M de dimensiones**, que a tarifa Flex serían **≈ $0,71/mes** de dimensiones — es decir, **el cargo por dimensiones es de unos céntimos y el mínimo de $45/mes es lo que domina de verdad** ([[2026-1029-weaviate-cloud-flex-minimo-45-dolares-al-mes]]). La consecuencia arquitectónica es más dura: **cambiar de modelo de embeddings cambia la factura de Weaviate Cloud aunque no cambien los tenants ni el número de objetos**, lo que refuerza la lección ya extraída del competidor de que el proveedor de embeddings se decide antes de indexar ([[2026-1022-myclone-viaje-embeddings-voyage]]). Y da al vault un criterio de comparación con otros motores: **Cloudflare Vectorize cobra $0.01/M de dimensiones *consultadas*** ([[2026-10-29-vectorize]]), es decir por lectura, mientras Weaviate cobra por dimensiones *almacenadas*; y Qdrant factura por vCPU/memoria/storage realmente consumidos ([[2026-1029-qdrant-billing-model]]) — tres unidades distintas para el mismo producto.

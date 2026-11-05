---
id: 2026-1101-lambda-1-click-clusters-minimo-16-gpus-y-escala-hasta-2000
type: atom
certainty: solid
sources: [sources/2026-11-01-lambda-gpu-pricing.md, sources/2026-10-31-lambda-gpu-pricing.md]
links: ["[[2026-1101-lambda-dos-lineas-de-producto-instances-y-clusters]]", "[[2026-1101-lambda-cluster-h100-precio-por-gpu-hr-segun-tamano]]", "[[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]"]
---

## Claim
El producto 1-Click Clusters de Lambda **no tiene venta unitaria**: el mínimo es **16 GPUs** y la escala llega a **2.000+ GPUs** ("Production-ready clusters from 16 to 2,000+ NVIDIA B200 or H100 GPUs"), con "production-ready" como atributo explícito del producto. Los tres tamaños tarifados de la tabla son 16, 64 y 256+ GPUs.

## Why It Matters
Fija el **suelo de entrada** de la oferta de GPU de Lambda: 16 GPUs del mismo modelo, es decir, con el H100 a $6,16 son $98,56/hora, y con el B200 a $9,86 son $157,76/hora. No hay opción de comprar "una GPU en un cluster" ni de comprar una fracción: la granularidad mínima es un clúster. Para el vault esto cierra la vía de "alquilar GPU barata para el RAG de los tenants": ni el producto barato (1x) ni el producto clusterizado (16+) encajan en un modelo de coste por asiento pequeño, y la comparación útil sigue siendo contra la inferencia por API.

## Nota de extensión 2026-11-03
Texto verbatim de `sources/2026-11-01-lambda-gpu-pricing.md` y `sources/2026-10-31-lambda-gpu-pricing.md` (ambas capturas incluyen la frase "from 16 to 2,000+").

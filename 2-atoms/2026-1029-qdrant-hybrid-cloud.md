---
id: 2026-1029-qdrant-hybrid-cloud
type: atom
certainty: solid
sources: [0-raw/2026-10-29-qdrant-cloud-pricing.md]
links: ["[[2026-1029-qdrant-free-tier]]", "[[2026-1029-qdrant-private-cloud]]"]
---

## Claim

El Hybrid Cloud de Qdrant permite ejecutar clusters gestionados sobre la propia infraestructura del usuario, usando sus compute, network y storage, ofreciendo residencia de datos local y operaciones gestionadas desde la nube de Qdrant.

## Why It Matters

El Hybrid Cloud resuelve el conflicto entre residencia de datos regulada y la comodidad de un servicio gestionado. Es la opción elegida cuando los datos no pueden salir de la red del usuario pero aún se quiere aprovechar el plane de gestión de Qdrant para operatividad, actualizaciones y monitorización sin mover la carga de trabajo a la nube de Qdrant.

## [FRICTION]

> [[2026-1029-qdrant-private-cloud]] (escrita hace ~21 semanas) afirma que el Private Cloud ofrece "dedicated, isolated deployment for strict security or compliance needs" y "full isolation", mientras que el Hybrid Cloud también satisface necesidades de residencia de datos pero comparte el plano de gestión de Qdrant —la diferencia fundamental es que el Private Cloud aísla tanto el plano de control como de datos del usuario, mientras que el Hybrid Cloud usa la propia infraestructura del usuario pero aún depende del plano de control gestionado por Qdrant, lo que significa que la isolation de datos depende de la configuración del usuario y no es garantizada por el mismo modelo que el Private Cloud. Ambas satisfacen necesidades de compliance pero con modelos de riesgo y responsibility distintos. Marcado para juicio humano, no auto-resuelto.
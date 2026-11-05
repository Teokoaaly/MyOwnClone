---
id: 2026-1101-azure-architecture-center-cinco-tipos-de-artefacto
type: atom
certainty: solid
sources: [sources/2026-11-01-azure-architecture-center.md]
links: ["[[2026-1031-azure-architecture-center]]", "[[2026-1022-myclone-competidor-arquitectura]]", "[[2026-1023-hetzner-costes-por-categoria-vs-infraestructura-propia]]"]
---

## Claim
El Azure Architecture Center se declara como un catálogo de **cinco tipos de artefacto** —solution ideas, example workloads, reference architectures, technology decision guides y architecture guides— cuyo propósito declarado es alinear las cargas con el **Azure Well-Architected Framework** y el **Cloud Adoption Framework for Azure**.

## Why It Matters
El center no es un documento único sino una taxonomía de cinco líneas de producto con frameworks de referencia (WAF + CAF) como marco evaluador. Para MyOwnClone la consecuencia práctica es doble: (a) el material útil para un backend Flask + Next.js está disperso entre "reference architectures" y "technology decision guides", no en una sola página; (b) los dos frameworks que estructuran todo el catálogo (WAF para la carga, CAF para la adopción) son la lista de chequeo con la que se puede auditar la plataforma multi-tenant — sus cinco pilares son el criterio con el que juzgar el stack de Postgres + Redis + Weaviate que hoy no tiene ningún documento de arquitectura propio. Es además el contexto que da sentido al átomo previo [[2026-1031-azure-architecture-center]]: este center es marco, no proveedor de precios, así que la comparativa de coste del vault (que separa coste por infra de coste por asiento en [[2026-1023-hetzner-costes-por-categoria-vs-infraestructura-propia]] y [[2026-1022-myclone-competidor-arquitectura]]) tiene que apoyarse en otra parte.

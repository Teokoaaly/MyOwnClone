---
id: 2026-1029-render-compute-services-workers
type: atom
certainty: solid
sources: [sources/2026-10-29-render-pricing.md]
links: ["[[2026-1029-render-compute-per-second]]", "[[2026-1029-render-hobby-plan]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
El compute de Services & Workers se factura por instancia y mes: $7/mes por menos de 1 CPU (512 MB, tipo 0.5c-512mb), $25/mes por 1 CPU (2 GB, 1c-2g), $85/mes por 2 CPU (4 GB), $175/mes por 4 CPU (8 GB), $300/mes por 8 CPU (16 GB) y hasta $1.500/mes por 12 CPU (96 GB); el techo del producto es 12 CPU y 96 GB de RAM, y los discos SSD costan $0,25/GB/mes.

## Why It Matters
Esta es la tabla que decide si Render cabe en el presupuesto: la instancia pagada más barata son $7/mes de cómputo, y la primera que serviría de verdad el backend Flask de MyOwnClone (2 GB) cuesta $25/mes. Sumado al workspace, ningún plan de Render con cómputo real cabe en los ≤ 4 EUR/mes del vault; solo la instancia gratuita de 512 MB (Hobby) es gratis, y 512 MB no alcanza para Flask + Postgres + Redis + Weaviate en el mismo servicio. El dato operativo útil es que los servicios corren por segundo ([[2026-1029-render-compute-per-second]]): un servicio que solo despierta para responder peticiones tiene un coste marginal casi nulo, lo cual sí es coherente con un carga variable de clones — pero el suelo de $7/mes sigue sin caber en 4 EUR, al contrario que el CPX02 de 5,99 EUR de [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]].

## [FRICTION]
> No conflicting atom found. This is a price-table atom documenting the compute floor; no direct contradiction in the current vault. No [FRICTION] block added.

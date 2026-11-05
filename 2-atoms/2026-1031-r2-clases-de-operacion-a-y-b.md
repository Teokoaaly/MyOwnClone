---
id: 2026-1031-r2-clases-de-operacion-a-y-b
type: atom
certainty: solid
sources: [sources/2026-10-31-cloudflare-r2-storage.md]
links: ["[[2026-1031-cloudflare-r2-storage]]", "[[2026-10-29-r2-storage]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
Cloudflare R2 Standard Class A operations cuestan $4.50 por millón de peticiones (1 millón gratis) y las Standard Class B cuestan $0.36 por millón de peticiones (10 millones gratis); las operaciones se clasifican en A (escritura/listado) y B (lectura).

## Why It Matters
El storage no es el único vector de coste: R2 cobra por operación aunque los GB almacenados sean gratis hasta 10 GB-month (ver [[2026-1031-cloudflare-r2-storage]]). Esto separa R2 del modelo de [[2026-10-29-neon-pricing-objectstorage]], donde el object storage se factura "sin cargo por operación", y confirma el eje abierto del vault ([[2026-1022-costes-por-categoria-tenant]]): el coste de infraestructura puede escalar con el número de operaciones por tenant (uso del producto) y no solo con el número de asientos.

Para MyOwnClone, los free tiers cubren de sobra un MVP multi-tenant: si cada tenant genera 1.000 lecturas al día, 100 tenants consumirían 3 millones de operaciones B al mes, dentro de los 10 millones de cortesía; el techo de clase B se alcanza con unos 333 tenants de ese perfil. En clase A el margen es mucho mayor: un artefacto subido por tenant y día son 30 escrituras por tenant al mes, de modo que el free tier de 1 millón aguantaría a unos 33.000 tenants antes de entrar en el tramo de pago de $4.50 por millón. La lectura trata de decir que, en un producto cuyo coste dominante es el asiento, la operación que escala es la de lectura (releer el propio histórico del clone), y ahí el free tier de clase B es 10 veces más pequeño que el de clase A: es el número a vigilar cuando el producto crezca.

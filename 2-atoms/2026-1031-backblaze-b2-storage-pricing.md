---
id: 2026-1031-backblaze-b2-storage-pricing
type: atom
certainty: solid
sources: [sources/2026-10-31-backblaze-b2-storage-pricing.md, sources/2026-11-01-backblaze-b2-storage-pricing.md, sources/2026-11-02-backblaze-b2-storage-pricing.md, sources/2026-11-03-backblaze-b2-storage-pricing.md]
links: ["[[2026-1031-proton-business-vpn-essentials-6-99-minimo-2-usuarios]]", "[[costes-por-categoria-tenant]]"]
---

## Claim
Backblaze B2 Storage charges per-gigabyte per-month with no per-user seat multiplier, creating a pure capacity-cost model where cost scales with stored data volume rather than number of users.

## Why It Matters
Unlike the per-seat cost dominance model validated in `costes-por-categoria-tenant` (where user count is the dominant cost variable), Backblaze's per-gigabyte pricing makes storage cost proportional to data volume regardless of user count. This creates a fundamental cost-model divergence: for multi-tenant SaaS products, storage cost may scale with data per user rather than user count alone, meaning the `costes-por-categoria-tenant` framework needs to account for per-user storage growth as a secondary cost driver alongside the primary per-seat cost.

## [FRICTION]
> [[2026-1031-proton-business-workspace-standard-12-99]] includes 1 TB of storage per user at $12.99/user/mo, explicitly coupling storage cost to seat count. Backblaze's pure per-gigabyte model means these two approaches — per-user storage inclusion vs. per-gigabyte billing — represent opposing cost philosophies. For a product migrating from Backblaze to a per-user storage model, the cost impact depends on average storage per user, which requires measuring current Backblaze GB usage per active user before projecting the per-seat transition cost.

## Nota de extensión 2026-11-03
Fuente: `sources/2026-10-31-backblaze-b2-storage-pricing.md`, `sources/2026-11-01-backblaze-b2-storage-pricing.md`, `sources/2026-11-02-backblaze-b2-storage-pricing.md` (tres capturas consecutivas de `backblaze.com/cloud-storage/pricing`, contenido de precios idéntico salvo la versión del extractor). La afirmación de este átomo queda **anclada a cifras concretas**: B2 parte de **$6.95/TB/30-días**, facturado por byte-hora, con los **primeros 10 GB siempre gratis** (ver [[2026-1102-backblaze-b2-precio-6-95-por-tb-al-mes]] y [[2026-1102-backblaze-b2-sin-minimo-de-duracion-ni-de-tamano-de-archivo]]). El "pure capacity-cost model" que enuncia este átomo **debe matizarse**, no corregirse: el precio de almacenamiento no depende del asiento (eso se mantiene), pero la factura total de B2 incluye además **egreso a $0.01/GB por encima de 3× el almacenamiento medio** ([[2026-1102-backblaze-b2-egreso-gratis-hasta-3x-y-0-01-por-gb]]) y **transacciones de clase D a $0.004 por 10.000 llamadas** ([[2026-1102-backblaze-b2-transacciones-clase-a-b-c-gratis-y-clase-d-cobrada]]). La fricción con el modelo de R2 documentado en [[2026-1031-cloudflare-r2-storage]] queda así: **B2 es más barato por GB almacenado (~$0.0068 vs $0.015/GB/mes) pero no es gratis en egreso; R2 es más caro por GB almacenado y no cobra egreso**. Ninguna de las dos afirmaciones puede completarse sin esa asimetría, y el criterio de elección es la razón entre egreso mensual y almacenamiento medio, no el precio del GB.
## 2026-11-03 — re-verificación (cuarta captura)
La captura del 2026-11-03 de `backblaze.com/cloud-storage/pricing` (520 palabras, renderizado reducido) **confirma sin cambios** el precio unitario: B2 "Starts at **$6.95/TB/mo**" facturado por byte-hora a $6.95/TB/30-días, Overdrive a $15/TB/mo, egreso gratis hasta 3× y $0.01/GB después, clase D a $0.004/10.000 llamadas. La afirmación central de este átomo —**el precio de B2 no depende del número de asientos**— sigue sin ser contradicha por ninguna fuente del vault. El matiz ya anotado arriba (línea de egreso y línea de operaciones en la factura) se mantiene íntegro, y ahora se puede cuantificar con una cuarta confirmación: ver [[2026-1103-backblaze-b2-precios-estables-en-cuatro-capturas-consecutivas]].

**Advertencia metodológica**: esta captura pierde la línea "First 10GB storage is always free", presente en las dos anteriores. La omisión se atribuye al extractor, no a un cambio de condiciones, y queda marcada como fricción abierta en [[2026-1103-captura-reducida-omite-detalle-ya-documentado]].

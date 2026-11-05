---
id: 2026-1031-r2-egress-cero-contrasta-con-egress-de-workers
type: atom
certainty: solid
sources: [sources/2026-10-31-cloudflare-r2-storage.md, sources/2026-10-31-backblaze-b2-storage-pricing.md]
links: ["[[2026-1031-backblaze-b2-storage-pricing]]", "[[2026-10-29-data-egress]]", "[[2026-1031-cloudflare-r2-storage]]"]
---

## Claim
Cloudflare R2 no cobra salida de datos ("R2 doesn't charge for egress"), mientras que Backblaze B2 ofrece "free egress up to 3x storage" y después cobra $0.01/GB adicional; ambos son almacenamiento de objetos compatible con S3, pero solo R2 elimina el coste de egreso por completo.

## Why It Matters
El egreso es la variable que rompe los presupuestos de los que sirven media o artefactos desde object storage, y es donde el eje abierto del vault (coste por asiento vs coste por infraestructura) se decide: con R2, un tenant que descarga mucho no encarece la infraestructura del resto; con B2, el coste escala con el volumen extraído y hay que vigilarlo como una categoría facturable separada (ver [[2026-1031-backblaze-b2-storage-pricing]]). Para MyOwnClone, R2 encaja con el patrón "cada tenant descarga sus propios artefactos de clone": mover esos artefactos a R2 convierte una factura de egreso variable en coste de almacenamiento fijo ($0.015/GB-month, ver [[2026-1031-cloudflare-r2-storage]]), compatible con el presupuesto duro de ≤ €4/mes porque los primeros 10 GB-month son gratis.

## [FRICTION]
> [[2026-10-29-data-egress]] afirma que la salida de datos de Cloudflare cuesta $0.05 por GB tras 1.000 GB/mes gratis, mientras esta nota recoge que "R2 doesn't charge for egress". Ambas no pueden ser simultáneamente correctas salvo que sean productos distintos: R2 es object storage, y la cifra de $0.05/GB corresponde a otro producto de la plataforma (Workers / red). Marcado para juicio humano: no queda establecido en las capturas si la exención de egreso de R2 cubre también las lecturas servidas a través de Workers o CDN, o solo la API de R2.

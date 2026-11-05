---
id: 2026-1102-backblaze-b2-api-compatible-s3-sin-lock-in-de-proveedor
type: atom
certainty: solid
sources: [sources/2026-10-31-backblaze-b2-storage-pricing.md, sources/2026-11-01-backblaze-b2-storage-pricing.md, sources/2026-11-02-backblaze-b2-storage-pricing.md, sources/2026-11-03-backblaze-b2-storage-pricing.md]
links: ["[[2026-1102-backblaze-b2-transacciones-clase-a-b-c-gratis-y-clase-d-cobrada]]", "[[2026-1031-cloudflare-r2-storage]]"]
---

## Claim
Backblaze B2 se ofrece explícitamente como "**S3 compatible object storage**" ("High-performance, S3-compatible cloud storage, purpose built to provide simplicity, reliability, and affordability") y la página remite a una tabla propia de precios de llamadas API ("Free API calls" → `backblaze.com/cloud-storage/transaction-pricing`), que es **la misma página que usa para clasificar las transacciones en clases A, B, C y D**; no aparece en la página de precios un API propietario con tarifa distinta.

## Why It Matters
La compatibilidad S3 es lo que hace que este proveedor sea **sustituible** por el que documenta [[2026-1031-cloudflare-r2-storage]] sin reescribir el código: los snapshots de Postgres que se suben con `b2` / `aws s3` / `rclone` o cualquier SDK S3 se pueden mover cambiando endpoint y credenciales, no arquitectura. Eso reduce el coste de cambiar de proveedor cuando el número de tenants crezca y el almacenamiento pase de ser una línea marginal a ser una línea dominante del coste de plataforma. Y explica por qué la tabla de transacciones se publica aparte: la granularidad A/B/C/D es la de S3, heredada, no una taxonomía propietaria — lo que hace que el número de $0.004/10.000 de clase D sea comparable con el de otros proveedores S3-compatible en vez de ser un misterio de Backblaze.

## 2026-11-03 — re-verificación
La compatibilidad S3 se re-verifica **sin cambios** en el subtítulo y en el pie de la página: "Enterprise-grade, security & compliance-ready, **S3 compatible** object storage—at a fraction of the cost" y "High-performance, **S3-compatible** cloud storage, purpose built to provide simplicity, reliability, and affordability".

**Matiz nuevo de esta captura**: el pie de la calculadora remite a "View API call rate details here" — la misma página de detalle de transacciones que este átomo identifica como origen de la clasificación A/B/C/D — pero **el enlace ha desaparecido en el renderizado reducido** (queda como texto plano). El hecho de que ese pie sí esté presente en el 11-01 y el 11-02 confirma que el destino no cambió, solo el extractor (véase [[2026-1103-captura-reducida-omite-detalle-ya-documentado]]).

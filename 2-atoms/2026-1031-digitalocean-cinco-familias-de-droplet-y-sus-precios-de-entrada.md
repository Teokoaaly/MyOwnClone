---
id: 2026-1031-digitalocean-cinco-familias-de-droplet-y-sus-precios-de-entrada
type: atom
certainty: solid
sources: [sources/2026-10-31-digitalocean-droplets-pricing.md, sources/2026-11-03-digitalocean-droplets-pricing.md]
links: ["[[2026-1031-digitalocean-entrada-basic-512-mib-4-dolares-al-mes]]", "[[2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados]]", "[[2026-1024-buyvm-comparativa-precios-15-al-mes-contra-aws-do-linode-y-vultr]]"]
---

## Claim
DigitalOcean publica **cinco familias de Droplet** con precios de entrada y techos distintos: **Basic** desde **$4.00/mes** (512 MiB) hasta **$96.00** (16 GiB / 8 vCPU); **CPU-Optimized** (ratio 2:1 memoria/CPU, vCPU dedicadas 2.6 GHz+) desde **$42.00** (4 GiB) hasta **$1,008.00** (96 GiB / 48 vCPU); **General Purpose** (ratio equilibrado, CPU dedicada) desde **$63.00** (8 GiB / 2 vCPU) hasta **$1,260.00** (160 GiB / 40 vCPU); **Memory-Optimized** (8 GiB de RAM por vCPU, NVMe) desde **$84.00** (16 GiB) hasta **$1,344.00** (256 GiB / 32 vCPU); **Storage-Optimized** (NVMe de alto rendimiento) desde **$131.00** (16 GiB / 300 GiB de disco) hasta **$2,096.00** (256 GiB / 4,690 GiB de disco). Las variantes **Premium Intel** y **Premium AMD** (hasta 10 Gbps de salida y NVMe) aparecen como pestañas de CPU en las tablas, sin columna de precio propia.

## Why It Matters
La estructura de familias es la que convierte a DO en un catálogo de *tiering por ratio de memoria* y no en una escalera de precio: el primer salto útil (Basic → CPU-Optimized) multiplica por **10,5** el precio de entrada ($4 → $42) para pasar de CPU compartida a vCPU dedicadas, exactamente el patrón de salto que el vault ya había medido en Hetzner como ×6,70 hacia General Purpose ([[2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados]]). Para MyOwnClone la consecuencia es que **ninguna familia por encima de Basic es presupuestable**: el más barato de CPU-Optimized, General Purpose, Memory-Optimized y Storage-Optimized son $42, $63, $84 y $131 respectivamente, todos muy por encima del techo de ≤ €4/mes. La familia Basic, con su $4/$6/$12, es la única que entra en la conversación de presupuesto, y su techo de $96 (16 GiB) es el límite superior de lo que este proveedor es para el vault.

## 2026-11-03 — re-verificación
La captura del **2026-11-03** reproduce las **cinco familias con sus 31 filas idénticas** —Basic desde $4.00 hasta $96.00, CPU-Optimized desde $42.00 hasta $1,008.00, General Purpose desde $63.00 hasta $1,260.00, Memory-Optimized desde $84.00 hasta $1,344.00 y Storage-Optimized desde $131.00 hasta $2,096.00— sin ninguna variación. Ver [[2026-1103-digitalocean-precios-identicos-en-las-cuatro-capturas-del-31-oct-al-3-nov]].

Confirma además dos detalles de la nota de verificación de 2026-10-31: los encabezados de las tablas siguen mostrando las pestañas de CPU ("Regular | Premium Intel | Premium AMD" en Basic; "Regular | Premium Intel" en las cuatro familias dedicadas) y **la tabla sigue mostrando una sola columna de precio**, sin desglosar la variante premium. La captura del 11-03 **no publica** ninguna cifra de Premium Intel o Premium AMD, ni siquiera en las familias donde la descripción sí las menciona ("up to 10Gbps outbound network speeds and NVMe SSDs"). Sigue sin ser posible atribuir un precio concreto al premium.

## Nota de verificación
Precios transcritos literalmente de las tablas. Las pestañas **Premium Intel** y **Premium AMD** aparecen en el encabezado de la tabla Basic como opciones de CPU ("Regular | Premium Intel | Premium AMD") en el 2026-10-31, pero **la tabla muestra una sola columna de precio** ($/hr y $/mo) sin desglosar la variante premium: la captura **no permite atribuir un precio concreto** al premium, y no se afirma ninguno.

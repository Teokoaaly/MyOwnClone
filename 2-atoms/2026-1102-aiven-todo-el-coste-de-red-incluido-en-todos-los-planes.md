---
id: 2026-1102-aiven-todo-el-coste-de-red-incluido-en-todos-los-planes
type: atom
certainty: solid
sources: [sources/2026-11-02-aiven-postgresql-pricing.md, sources/2026-11-03-aiven-pricing.md]
links: ["[[2026-1102-aiven-escalera-de-precios-postgresql-de-0-a-270-dolares]]", "[[2026-10-29-data-egress]]", "[[2026-1031-cloudflare-r2-storage]]"]
---

## Claim
La fila "All networking cost included" de la tabla de planes de Aiven PostgreSQL está marcada en **los seis planes, del Free al Premium**. La página contrasta esto con los hyperscalers, que "typically meter networking, backups, data writes and reads, and high availability separately", y lista como partidas separadas de la nube: alta disponibilidad y replicación multi-AZ, backups automatizados y retención, **transferencia de datos y egreso entre servicios o regiones**, herramientas de monitorización, y el tiempo de ingeniería.

## Why It Matters
En el modelo de coste del vault el egreso es una partida abierta: [[2026-10-29-data-egress]] mide $0,05/GB tras 1.000 GB en Cloudflare y [[2026-1031-cloudflare-r2-storage]] lo trata como coste cero dentro de la red. Aiven convierte ese egreso en **coste contenido dentro de la tarifa del plan**, lo que hace la factura predecible frente a la combinación storage + egreso del stack autoalojado — un argumento a favor de Aiven para el producto multi-tenant, donde el egreso de datos de tenants es estructural y no accidental. Contrapeso: el aviso de [[2026-1101-aiven-runtime-pasa-a-facturacion-por-uso-con-egreso-de-red]] dice que el billing de Runtime migrará a consumo con egreso de red, así que la inclusividad hoy es una promesa con fecha de revisión.

## 2026-11-03 — re-verificación
La fila **"All networking cost included"** sigue marcada en los seis planes en la captura del 2026-11-03, sin variación. La versión reducida **elimina la lista desglosada de partidas de hyperscaler** (HA multi-AZ, backups y retención, transferencia de datos y egreso entre servicios o regiones, monitorización y tiempo de ingeniería) que estaba en la captura del 11-02: el contraste con los hyperscalers sigue en la FAQ, pero solo con la formulación genérica. La inclusividad de red no ha cambiado en cuatro capturas: [[2026-1103-aiven-precios-pitr-y-nubes-estables-en-cuatro-capturas-consecutivas]].

## Actualización 2026-11-04
Fuente: `sources/2026-11-04-aiven-pricing.md` (quinta captura, render completo). La fila **"All networking cost included"** sigue marcada en los seis planes y la FAQ de hyperscalers **vuelve a renderizarse con la lista desglosada** de partidas que el 11-03 había eliminado: "Cloud providers charge separately for: High availability and multi-AZ replication; Automated backups and storage retention; Data transfer and egress between services or regions; Monitoring and alerting tools; The engineering time to configure, maintain, and upgrade everything". La inclusividad de red queda confirmada por quinta captura; en esta versión el contraste con los hyperscalers es explícito y enumerado, no genérico.

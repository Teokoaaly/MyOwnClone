---
id: 2026-1101-digitalocean-backups-por-porcentaje-y-snapshots-006-por-gb
type: atom
certainty: solid
sources: [sources/2026-11-01-digitalocean-droplets-pricing.md, sources/2026-11-03-digitalocean-droplets-pricing.md]
links: ["[[2026-1031-digitalocean-entrada-basic-512-mib-4-dolares-al-mes]]", "[[2026-1024-buyvm-backups-al-10-del-precio-base-y-cinco-snapshots-gratis]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]"]
---

## Claim
La tabla "Additional product pricing" publica dos líneas de coste anexas al Droplet: **Backup**, elegible entre un modelo **por porcentaje del coste del Droplet —20 % (semanal) o 30 % (diario)—** y un modelo **por uso desde $0.01/GiB al mes**, con frecuencias de hasta cada 4 horas y retención de 3 días a 6 meses; y **Droplet Snapshots a $0.06/GB al mes**.

## Why It Matters
Es la partida que el thread de hosting barato ya identificó como **la que más se paga dos veces** —el backup no viene con el servidor en unos proveedores y se cobra como extra en otros— y aquí la cifra tiene dos efectos distintos según la arquitectura. Con el stack vivo ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) corriendo sobre un único VPS, un backup semanal al 20 % del precio del Droplet significa que **el 20 % del coste del servidor se paga dos veces**: una por la máquina y otra por poder deshacerla, y ese porcentaje es proporcional al tamaño del plan, no al volumen de datos que MyOwnClone almacena. El modelo por uso ($0.01/GiB/mes) rompe esa proporcionalidad y es la cifra que de verdad debe compararse con el almacenamiento de clones, donde el coste dominante no es el disco sino el número de versiones retenidas. Y el snapshot a $0.06/GB/mes es relevante porque es el precio de referencia para el backup de la base de datos: con una Postgres de producción de varios GB, un snapshot diario es ya una partida mensual del mismo orden que el VPS. La comparación con el tramo barato del vault es directa: BuyVM cobra los backups automáticos al 10 % del precio base y regala 5 snapshots ([[2026-1024-buyvm-backups-al-10-del-precio-base-y-cinco-snapshots-gratis]]), de modo que **el 20 % de DO es el doble del 10 % de BuyVM sobre un plan de entrada que ya es seis veces más caro**.

## 2026-11-03 — re-verificación
La captura del **2026-11-03** **no contiene** la tabla "Additional product pricing": el render reducido la sustituye por "…" junto con el bloque de v5 y la FAQ de droplets. Por tanto, el backup al 20 %/30 % y el snapshot a $0.06/GB **no se pueden re-verificar ni refutar** con esta captura, y este átomo sigue sosteniéndose por la del 2026-11-01 (que sí contiene la tabla, con la misma redacción). Al ser una partida de coste recurrente sobre el plan que sirve al stack, la consecuencia práctica es que **el vault no tiene todavía una re-verificación reciente de esta línea**: si una captura futura de esta URL vuelve a incluir la tabla, es el punto donde hay que mirar si los porcentajes o el precio por GB han cambiado. Ver [[2026-1103-digitalocean-captura-reducida-sin-tablas-de-backups-ni-precios-de-v5]].

## Actualización 2026-11-04
La captura del **2026-11-04** (render completo, 350 líneas) **vuelve a renderizar** la tabla "Additional product pricing" con **redacción idéntica** a la del 11-01 y el 11-02: "Percentage-based Backups, set at 20% (Weekly) or 30% (Daily) of Droplet cost. Usage-based plans start at $0.01/GiB per month and offer highly flexible frequencies (up to every 4 hours) and custom retention periods (3 days to 6 months)" y "Droplet Snapshots $0.06/GB per month". **El backup al 20 %/30 % y el snapshot a $0.06/GB quedan re-verificados** con datos frescos, tres días después del recorte del 11-03 que los había dejado sin confirmar. Ver [[2026-1104-digitalocean-captura-vuelve-a-render-completo-tras-el-render-reducido-del-3-nov]].

## Nota de verificación
Cifras y condiciones transcritas literalmente. La captura **no publica** el precio de los planes de backup por uso más allá del suelo de $0.01/GiB/mes, ni el coste por GB de las opciones de frecuencia distintas, ni los límites de retención por plan.

---
id: 2026-1031-digitalocean-entrada-basic-512-mib-4-dolares-al-mes
type: atom
certainty: solid
sources: [sources/2026-10-31-digitalocean-droplets-pricing.md, sources/2026-11-03-digitalocean-droplets-pricing.md]
links: ["[[2026-1031-digitalocean-droplets-pricing]]", "[[2026-1024-buyvm-comparativa-precios-15-al-mes-contra-aws-do-linode-y-vultr]]", "[[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]"]
---

## Claim
El Droplet más barato de DigitalOcean es el plan **Basic de 512 MiB**: **$4.00/mes** o **$0.00595/hora**, con **1 vCPU**, **10 GiB de SSD** y **500 GiB de transferencia de salida incluida** al mes (entrada siempre gratis). La tabla Basic publica siete filas, desde 512 MiB / $4.00 hasta 16 GiB / 8 vCPU / $96.00, con precios intermedios de $6.00 (1 GiB), $12.00 (2 GiB / 1 vCPU), $18.00 (2 GiB / 2 vCPU), $24.00 (4 GiB / 2 vCPU) y $48.00 (8 GiB / 4 vCPU).

## Why It Matters
Es el suelo de precio del proveedor y, por tanto, la cota inferior con la que hay que comparar todo el tramo barato que ya tiene medido el vault. El dato relevante para el stack vivo ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) es que **$4.00 no compra nada utilizable**: 512 MiB es la mitad del umbral de 2 GB que el thread de hosting barato identificó como el punto donde Postgres + Redis + app empiezan a caber, y el primer plan de 1 GiB cuesta **$6.00**. Es decir, el precio de entrada es publicidad: la aritmética real del stack empieza en $12.00 (2 GiB) y el plan con CPU dedicada y 4 GiB cuesta $24.00, seis veces la entrada. Comparado con el suelo de Hetzner ([[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]], €5.99 por 1 vCPU / 2 GB), el Basic de 2 GiB de DO es **el doble** en dólares, de modo que DigitalOcean no es el proveedor barato del vault: es la referencia cara contra la que se cotizan el resto.

## 2026-11-03 — re-verificación
La captura del **2026-11-03** conserva la tabla Basic **completa** (las 7 filas, con sus valores de memoria, vCPU, transferencia, SSD, $/hr y $/mo) **sin una sola variación** respecto a la del 2026-10-31: el plan de entrada sigue siendo 512 MiB / 1 vCPU / 500 GiB / 10 GiB SSD a **$0.00595/hora y $4.00/mes**. Ver [[2026-1103-digitalocean-precios-identicos-en-las-cuatro-capturas-del-31-oct-al-3-nov]].

Lo que esta captura **no** permite comprobar es el bloque "Additional product pricing" (backups y snapshots), que el render del 11-03 sustituye por "…": sigue sin poder construirse un TCO completo de DO a partir de ella. Ver [[2026-1103-digitalocean-captura-reducida-sin-tablas-de-backups-ni-precios-de-v5]].

## [FRICTION]
> [[2026-1024-buyvm-comparativa-precios-15-al-mes-contra-aws-do-linode-y-vultr]] registra la tabla comparativa de BuyVM, que atribuye a **DigitalOcean $40.00/mes con 2 cores, 60 GB de disco y 4 TB de ancho de banda** (y por eso usa a DO como uno de los dos competidores de $40 contra los que se atribuye un 62,5 % de ahorro).
> La página de precios de DigitalOcean del 2026-10-31 publica, para el plan Basic de **2 vCPU y 4 GiB**, un precio de **$24.00/mes** con **80 GiB de SSD** y **4,000 GiB de transferencia**. Las dos cifras no pueden ser simultáneamente el precio del mismo Droplet: o la tabla de BuyVM es una fotografía de un plan anterior o de otra configuración (60 GB de disco no corresponde a ninguna fila de la tabla actual), o el precio de DO ha bajado desde entonces.
> Ambas no pueden ser completamente correctas. Marcado para juicio humano, no auto-resuelto. Consecuencia operativa inmediata: **toda cifra de mercado atribuida a DO por terceros queda obsoleta hasta revalidarse contra la página del fabricante**, igual que ya se registró para los intermediarios que revenden capacidad de DO ([[2026-1026-bitlaunch-agrega-digitalocean-vultr-y-linode-en-un-panel-propio]]).

---
id: 2026-1102-digitalocean-la-transferencia-incluida-escala-con-el-plan-de-500-a-11-000-gib
type: atom
certainty: solid
sources: [sources/2026-11-02-digitalocean-droplets-pricing.md, sources/2026-11-03-digitalocean-droplets-pricing.md]
links: ["[[2026-1031-digitalocean-entrada-basic-512-mib-4-dolares-al-mes]]", "[[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]", "[[2026-1023-hetzner-comparativa-trafico-20tb-contra-hyperscalers]]"]
---

## Claim
Cada Droplet incluye **transferencia de salida gratuita** cuya cantidad **escala con el plan**: **500 GiB/mes** en el Basic de 512 MiB, 1,000 GiB en el de 1 GiB, 2,000 GiB en el de 2 GiB/1 vCPU, 3,000 GiB en el de 2 GiB/2 vCPU, 4,000 GiB en el de 4 GiB, 5,000 GiB en el de 8 GiB y 6,000 GiB en el de 16 GiB; las familias dedicadas arrancan en 4,000 GiB (CPU-Optimized) y suben hasta **11,000 GiB** (96 GiB / 48 vCPU). **El tráfico entrante es siempre gratis** ("Inbound bandwidth is always free").

## Why It Matters
Es la comparación directa que el vault necesitaba contra el dato de Hetzner —20 TB de salida incluidos por €5,99, luego €1,00/TB extra en la UE ([[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]])— y el resultado es que **el gigabyte incluido de DigitalOcean es entre 40 y 80 veces peor**: 500 GiB por $4.00 frente a 20 TB por €5,99. Traducido al producto: el stack de MyOwnClone sirve respuestas de clon con audio y vídeo, así que el egreso es la variable que dispara la factura antes que la CPU; con DO el techo de egreso **no es una restricción de capacidad** sino una factura que se dispara al superarlo, y la página **no publica en ningún punto el precio del exceso de transferencia**. Es decir, DO cotiza el byte incluido de forma generosa en apariencia (500 GiB "gratis") pero **no cierra el contrato de egreso**: el vault tiene aquí el mismo patrón que ya registró en el tramo barato, donde el egreso es la partida que más veces se cobra dos veces.

## 2026-11-03 — re-verificación
La captura del **2026-11-03** conserva las **cinco tablas completas**, y la columna "Transfer" es **idéntica fila a fila** a la de la captura del 2026-11-02: 500 GiB en el Basic de 512 MiB, 1,000 / 2,000 / 3,000 / 4,000 / 5,000 / 6,000 GiB en el resto de la familia Basic, 4,000 GiB de arranque en las cuatro familias dedicadas y 11,000 GiB en el techo de CPU-Optimized. Ver [[2026-1103-digitalocean-precios-identicos-en-las-cuatro-capturas-del-31-oct-al-3-nov]].

Lo que **no** re-verifica esta captura es la frase de la FAQ que la sostiene ("Each Droplet includes a generous amount of free outbound data transfer… Inbound bandwidth is always free"): el render del 11-03 sustituye toda la FAQ de droplets por "…". La afirmación sigue apoyada en las capturas del 11-01 y del 11-02.

## Nota de verificación
Cifras de la columna "Transfer" de las tablas y de la FAQ, verbatim. La captura **no publica** el precio por TB o GiB de transferencia excedente, ni el umbral exacto de corte, ni el tratamiento del tráfico entre droplets, y **no menciona ningún producto de "bandwidth pool"** ni pool de egreso agregado: la transferencia viene atada a cada Droplet individualmente, sin mecanismo de pool o de salida compartida publicada. La comparación de ratios es cálculo del átomo sobre cifras de dos fuentes distintas y en monedas distintas (dólares y euros), sin aplicar tipo de cambio ni IVA.

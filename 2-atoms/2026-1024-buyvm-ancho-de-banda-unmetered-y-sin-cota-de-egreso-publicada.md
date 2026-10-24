---
id: 2026-1024-buyvm-ancho-de-banda-unmetered-y-sin-cota-de-egreso-publicada
type: atom
certainty: solid
sources: [sources/2026-10-23-buyvm-kvm-slices.md]
links: ["[[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]", "[[2026-1024-extravm-modelo-de-red-puerto-1gbps-5gbps-y-tráfico-de-3-a-40-tb]]", "[[2026-1024-hostbrr-ancho-de-banda-2-5-tb-a-10-gbps]]"]
---
## Claim
BuyVM declara "**Unmetered** Bandwidth" en la ficha de los cuatro slices y "**Unlim.** 1000 Mbps" en la tabla de los seis planes de alto volumen. Es el único proveedor del eje barato documentado en el vault cuya página **no publica ninguna cifra de tráfico incluido ni recargo por exceso**: no hay umbral mensual, no hay TB incluidos, no hay sobrecoste por egreso. En su tabla comparativa de competidores, BuyVM aparece con "Bandwidth: Unmetered" frente a **4 TB** para DigitalOcean, Linode y Vultr, y la nota al pie 1 aclara que "Amazon AWS does not include bandwidth or disk space in their plans meaning the cost will be substantially higher".

## Why It Matters
Cierra una pregunta que el vault tenía abierta con cada proveedor barato: **¿cuál es el techo de egreso y qué pasa al superarlo?** En Hetzner el egreso son 20 TB incluidos y luego €1.00/TB en la UE ([[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]); en ExtraVM el egreso está topado desde el primer mes entre 3 y 40 TB ([[2026-1024-extravm-modelo-de-red-puerto-1gbps-5gbps-y-tráfico-de-3-a-40-tb]]); en HostBrr el plan de €2 da 2.5 TB a 10 Gbps ([[2026-1024-hostbrr-ancho-de-banda-2-5-tb-a-10-gbps]]); en BuyVM **no hay número**. Para MyOwnClone, cuyo producto mueve respuestas de clon con audio y vídeo y cuyo despliegue vivo es un nginx autoalojado, el egreso es una variable de coste que hoy el vault no puede cuantificar con BuyVM: la ausencia de techo publicado es利好 para el relay, pero **es ausencia de dato, no de coste** — la captura tampoco publica política de abuso ni qué ocurre en el borde del "unmetered".

## Nota de verificación
"Cifra de tráfico no publicada" es una observación sobre lo que la página dice, no una afirmación de que el egreso sea realmente ilimitado. La captura no publica SLA, ancho de banda agregado por nodo, ni política de uso justo.

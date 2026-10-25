---
id: 2026-1024-1984-hosting-vps-entry-9-66-1-cpu-1gb-y-25gb-nvme
type: atom
certainty: solid
sources: [sources/2026-10-24-1984-hosting-vps.md]
links: ["[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]]", "[[2026-1024-extravm-escalera-de-precios-14-planes-de-4-50-a-192]]", "[[2026-1024-1984-hosting-acepta-bitcoin-y-monero]]"]
---

## Claim
El VPS de entrada de **1984 Hosting** cuesta **$9.66/mes** y la página publica su ficha técnica completa: **1 CPU, 1 GB RAM, 25 GB NVMe SSD, 1 TB de transferencia y protección DDoS incluida**. La ubicación es Islandia ("reliable virtual private servers in Iceland powered by 100% renewable energy") sobre "enterprise-level hardware in highly secure Icelandic data centers". La captura **no publica una escalera de planes**: solo aparece el "Entry Plan".

## Why It Matters
Con $9,66/mes, 1984 queda **muy por encima del suelo del mercado barato que el vault viene midiendo** (≈$0,83/mes en las listas de $1 de LowEndBox, €2,00 en HostBrr, $2,99 en Evoxt) y también por encima del propio suelo de Hetzner a €5,99/mes ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]). Su valor no está en el precio sino en lo que la ficha incluye y en lo que la casa sostiene: NVMe, root, consola VNC, imágenes de privacidad, política de no logs y DDoS en el plan de $9,66 ([[2026-1024-1984-hosting-politica-de-sin-logs-e-imagenes-de-privacidad]]). Pero con **1 GB de RAM**, el plan de entrada queda por debajo del umbral de 2 GB que el vault identificó como el punto donde el stack Postgres + Redis + app empieza a caber ([[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]], [[2026-1024-extravm-escalera-de-precios-14-planes-de-4-50-a-192]]): es decir, **1984 no compite en el tramo barato, ni siquiera con su plan más barato**.

## Nota de verificación
La captura es la home del proveedor: **no publica SLA, ni crédito por caída, ni cifra de egreso por dirección, ni periodicidad distinta de "/mo"**, y no publica la ficha de ningún plan superior al de entrada. Es un precio de página de marketing, no un compromiso.

---
id: 2026-1024-hostkey-tres-tipos-vps-vds-y-vds-con-gpu
type: atom
certainty: solid
sources: [sources/2026-10-23-hostkey-bitcoin-vps.md]
links: ["[[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]", "[[2026-1024-hostbrr-vps-comparte-cpu-y-vds-dedicada-24-7]]", "[[2026-1024-hostkey-kyc-obligatorio-y-procesamiento-via-bitpay]]"]
---
## Claim
HOSTKEY define tres clases de servidor en la página de Bitcoin VPS: **VPS (Shared vCPU)**, que comparte recursos físicos con otros servidores virtuales de la misma máquina y puede ver su CPU/RAM/disco afectados por otros usuarios; **VDS (Dedicated vCPU)**, con CPU, RAM y disco completamente dedicados y rendimiento consistente; y **VDS with GPU**, donde "each VPS comes with a fully dedicated GPU — one physical GPU per virtual server, without sharing" pero **CPU y RAM siguen compartidas entre todas las VMs del host**.

## Why It Matters
Confirma que en el mercado europeo con pago en cripto la nomenclatura sigue igual de confusa que en el resto del sector: aquí "VPS" significa CPU compartida y "VDS" significa CPU dedicada —nomenclatura invertida respecto a lo que un lector español esperaría de "dedicated server"—, y la propia página usa "VPS" para el producto con GPU dedicada. El dato relevante para el vault no es el nombre sino el criterio: **la exclusividad de hardware no se propaga de la GPU a la CPU y la RAM**, es decir, un "VPS con GPU dedicada" para inferencia sigue teniendo la CPU compartida, exactamente el criterio compartido/dedicado que el vault ya usa para justificar el salto de escalón en Hetzner ([[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]) y en HostBrr ([[2026-1024-hostbrr-vps-comparte-cpu-y-vds-dedicada-24-7]]). Para MyOwnClone, si algún tenant pidiera GPU, la pregunta correcta no es "GPU dedicada" sino "CPU y RAM dedicadas a la vez".

---
id: 2026-1024-flokinet-nvme-u2-y-nodos-de-20-gbit-como-argumento
type: atom
certainty: solid
sources: [sources/2026-10-24-flokinet-vps-pricing.md]
links: ["[[2026-1024-hostbrr-flota-ryzen-epyc-xeon-y-nvme-gen4]]", "[[2026-1024-extravm-disco-proporcional-15-gb-nvme-por-gb-de-ram]]", "[[2026-1024-flokinet-escalera-de-precios-siete-planes]]", "[[2026-1024-flokinet-trafico-por-plan-y-direccion-no-publicada]]"]
---

## Claim
FlokiNET vende **solo almacenamiento SSD/NVMe de grado enterprise**, sin HDD: *"All VPSes provided are based on enterprise SSD only"* y *"We are doing our best to offer the latest in performance, by upgrading to NVMe PCIe 8x and U.2 NVMe as storage devices in all our locations"*. Los números que publica son **relacionales, no absolutos**: el NVMe y el SSD enterprise *"are superior to standard SSDs, and much higher than any HDD, with 5x more bandwidth, 1000x greater I/O performance and 300x faster response time"*. La red se apoya en **nodos de virtualización con conectividad 10/20 Gbit** y *"the routing is optimal wherever possible"*. El disco de cada plan va de **20 GB a 220 GB NVMe** (20, 50, 90, 120, 180, 200, 220), es decir **2,5–3,3 GB de NVMe por euro** en toda la escalera.

## Why It Matters
Aporta la contraparte del dato de ExtraVM, que aplica una regla de disco **proporcional a la RAM** (15 GB NVMe por cada GB de RAM, [[2026-1024-extravm-disco-proporcional-15-gb-nvme-por-gb-de-ram]]): en FlokiNET la proporción de disco es respecto al **precio**, no a la RAM, y el resultado es casi constante (2,5–3,3 GB/€) — el disco escala con la factura, no con la memoria. Los multiplicadores "5x / 1000x / 300x" frente a HDD son **comparaciones de marketing sin referencia medida**, y el vault ya tiene la contraejemplo documentada en [[2026-1024-hostbrr-flota-ryzen-epyc-xeon-y-nvme-gen4]], donde la especificación útil es el **modelo de CPU y el tipo de array** (AMD Ryzen/EPYC/Xeon, NVMe Gen4, DDR4 ECC), no un múltiplo contra un disco que ya nadie usa. La observación que este átomo deja: **el argumento de "NVMe" ya no discrimina entre proveedores** — todos lo dicen — y lo que sí compararía es el **uplink y el ratio disco/precio**, que aquí son 1 Gbit y 2,5–3,3 GB/€.

## Nota de verificación
Los multiplicadores 5x/1000x/300x están transcritos literalmente y **no tienen benchmark ni unidad declarada**: no se dice respecto a qué SSD "estándar" ni a qué HDD. La captura **no** publica modelo de CPU, GHz, tipo de array (RAID), ni si el NVMe es Gen4 o Gen5. El cálculo GB/€ es del átomo.

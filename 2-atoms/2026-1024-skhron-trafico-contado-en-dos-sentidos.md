---
id: 2026-1024-skhron-trafico-contado-en-dos-sentidos
type: atom
certainty: solid
sources: [sources/2026-10-23-skhron-bitcoin-vps.md]
links: ["[[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]", "[[2026-1024-skhron-precios-2-34-a-177-65]]", "[[2026-1023-hetzner-comparativa-trafico-20tb-contra-hyperscalers]]"]
---

## Claim
Skhron cuenta el tráfico **en los dos sentidos**: en cada plan se lee "Traffic incl. … **Sum of inbound and outbound traffic is accounted**". El volumen incluido va de **1 TiB** (XSIG-SE-0, ER-SE-0) a **64 TiB** (ER-SE-64), con valores intermedios de 2, 2,5, 4, 5, 8, 10, 16, 20, 32 TiB según plan; el uplink es de 1 Gbps compartido (línea XSIG, Intel) o 5 Gbps compartido (línea ER, AMD EPYC).

## Why It Matters
Es una diferencia de modelo de cobro frente a Hetzner, donde los 20 TB son de **salida** y el egreso adicional se factura a €1,00/TB ([[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]). Contar entrada y salida **duplica el consumo facturable por el mismo tráfico real**: un plan con 1 TiB incluidos es en la práctica ~0,5 TiB de egreso útil si el servidor también recibe peticiones. Para una arquitectura de clones que sirve respuestas por streaming y además ingiere documentos, el egreso es la partida que dispara facturas, así que el número de Skhron no es comparable con el de Hetzner sin normalizar. La captura **no publica** el precio del tráfico adicional ni el umbral de corte, a diferencia de Hetzner.

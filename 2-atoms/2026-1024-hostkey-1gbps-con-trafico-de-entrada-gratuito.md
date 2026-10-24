---
id: 2026-1024-hostkey-1gbps-con-trafico-de-entrada-gratuito
type: atom
certainty: solid
sources: [sources/2026-10-23-hostkey-bitcoin-vps.md]
links: ["[[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]", "[[2026-1024-hostbrr-ancho-de-banda-2-5-tb-a-10-gbps]]", "[[2026-1024-hostkey-precios-solo-dedicados-desde-23-y-vps-sin-tabla]]"]
---
## Claim
La pagina declara que todos los VPS de HOSTKEY se conectan por un puerto de **1 Gbps con trafico entrante gratuito**, mientras que la cantidad de trafico **saliente** la determina el plan elegido ("All HOSTKEY VPSs are connected to a high-speed network via a 1 Gbps port with free incoming traffic, while the amount of outgoing traffic is determined by the selected plan"). En la seccion de producto, el mismo dato aparece como "1GBps Internet access".

## Why It Matters
Es el mismo modelo de economia de egreso que ya separa a Hetzner (20 TB incluidos + EUR 1,00/TB extra, [[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]) de HostBrr (2,5 TB a 10 Gbps, [[2026-1024-hostbrr-ancho-de-banda-2-5-tb-a-10-gbps]]), pero aqui **la cifra de trafico incluido no se publica**: la pagina dice que depende del plan y no da el numero. Para un SaaS multi-tenant como MyOwnClone, el egreso es la variable que decide el coste marginal de las respuestas de los clones: la descarga de media o las llamadas a APIs externas se paga por salida, y "1 Gbps con entrada gratis" describe el puerto, no la factura. Lo que si queda fijado es una posicion: **HOSTKEY cobra el egreso como dimension de plan y no lo publica en la landing**, lo que deja el coste de trafico como incognito en el calculo de infraestructura.

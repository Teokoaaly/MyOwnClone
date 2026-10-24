---
id: 2026-1024-buyvm-block-storage-slabs-1-25-por-256gb-y-migrables-sin-downtime
type: atom
certainty: solid
sources: [sources/2026-10-23-buyvm-kvm-slices.md]
links: ["[[2026-1024-hostbrr-storageboxes-16-tb-directadmin-desde-2-50]]", "[[2026-1024-extravm-disco-proporcional-15-gb-nvme-por-gb-de-ram]]", "[[2026-1024-buyvm-backups-al-10-del-precio-base-y-cinco-snapshots-gratis]]"]
---
## Claim
BuyVM ofrece "**Block Storage Slabs**" como addon de almacenamiento adicional para su línea Dedicated KVM Slice: "**For $1.25 / month per 256GB additional storage**, customers can purchase a Block Storage Slab and **freely migrate it between services within the same facility without downtime or reboots**". La página lo describe como "Best in class performance with market leading pricing" y "a cost effective, high performance, addon available to our Dedicated KVM Slice product line".

## Why It Matters
Es la pieza que separa a BuyVM de la regla general del vault de **"disco proporcional a RAM"**: aquí el disco **no está atado a la RAM** del plan y se compra por bloques de 256 GB a un precio de lista explícito. A $1.25 por 256 GB, un bloque cuesta $5.00/GB-año, frente a la regla de ExtraVM de "15 GB de NVMe por cada GB de RAM" ([[2026-1024-extravm-disco-proporcional-15-gb-nvme-por-gb-de-ram]]) y frente a los storageboxes de HostBrr desde $2.50 ([[2026-1024-hostbrr-storageboxes-16-tb-directadmin-desde-2-50]]). La propiedad operativa relevante es la **migración sin downtime ni reboot entre servicios de la misma facility**: eso permite mover el volumen de datos entre slices al hacer un upgrade de RAM sin cortar servicio, que es exactamente el ciclo que necesita un despliegue vivo que crece ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) y que choca con el hecho de que BuyVM **no permite downgrade** (ver [[2026-1024-buyvm-solo-upgrades-nunca-downgrades]]).

## Nota de verificación
Precio y comportamiento de migración transcritos literalmente. La captura **no** publica: tipos de protocolo de block storage (iSCSI/NVMe over TCP), IOPS, Throughput, número máximo de slabs por instancia, ni si el slab sobrevive a la eliminación del servicio asociado.

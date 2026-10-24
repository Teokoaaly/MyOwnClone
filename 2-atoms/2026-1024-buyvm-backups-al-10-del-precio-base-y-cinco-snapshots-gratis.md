---
id: 2026-1024-buyvm-backups-al-10-del-precio-base-y-cinco-snapshots-gratis
type: atom
certainty: solid
sources: [sources/2026-10-23-buyvm-kvm-slices.md]
links: ["[[2026-1024-hostbrr-backups-como-addon-opcional-con-gfs]]", "[[2026-1024-evoxt-backup-semanal-offsite-gratuito]]", "[[2026-1024-extravm-sin-reembolso-en-pagos-cripto]]"]
---
## Claim
Las copias de seguridad automáticas de BuyVM son un **addon de pago** para todos los planes Dedicated KVM Slice, "Priced at just **10% of the base price of the instance** (or **$0.50/month on the 512MB & 1GB instances**)". "Backups are taken **every night** and **7 days** of backups are kept." Los **snapshots son gratis**: "the **5 free snapshots per location** included with every plan", utilizables como punto de rollback y también "a great way to **create a template** to quickly deploy new instances". Además, "Free Snapshots!" como característica de producto y "Daily backups are also available for a nominal monthly fee".

## Why It Matters
Es el modelo de **coste de continuidad** que el vault puede comparar proveedor a proveedor: HostBrr hace los backups un addon opcional con Google File Storage ([[2026-1024-hostbrr-backups-como-addon-opcional-con-gfs]]) y Evoxt ofrece backup semanal offsite gratuito ([[2026-1024-evoxt-backup-semanal-offsite-gratuito]]). BuyVM introduce una fórmula lineal —**el 10 % del precio base de la instancia**— que hace el coste de backup proporcional al tamaño del servidor y no a la cantidad de datos: en el slice de $15.00/mes serían $1.50/mes, y en los planes de alto volumen de $105.00/mes serían $10.50/mes. Para MyOwnClone, cuyo despliegue vivo es un nginx autoalojado ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) y cuyo producto necesita poder desplegar versiones de clones sin downtime, el dato operativo es el de los **5 snapshots incluidos**: permiten rollback y template de despliegue sin pagar. La contrapartida es la retención corta (**7 días**), que no cubre un incidente detectado tarde, y el hecho de que no hay copia offsite documentada.

## Nota de verificación
Cifras transcritas literalmente. La captura **no** publica si los backups automáticos son offsite, la ubicación del almacenamiento de backup, ni el coste de restaurar; tampoco publica SLA de recuperación.

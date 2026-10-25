---
id: 2026-1024-flokinet-upgrade-de-storage-exige-ajustar-particiones-a-mano
type: atom
certainty: solid
sources: [sources/2026-10-24-flokinet-vps-pricing.md]
links: ["[[2026-1024-buyvm-solo-upgrades-nunca-downgrades]]", "[[2026-1024-extravm-upgrade-con-prorrateo-pero-sin-downgrade]]", "[[2026-1024-flokinet-escalera-de-precios-siete-planes]]"]
---

## Claim
El **upgrade de recursos es trivial y el de disco no**: *"Upgrading is easy, and usually requires a simple reboot of the VPS, and the new resources will be available immediately after the reboot"*, pero *"when it comes to upgrading storage, partitions and filesystems on the VPS will not automatically adjust to the new storage size, so they will need to be adjusted manually. This is necessary since FlokiNET does not control or have access to your partitions or filesystems"*. El proveedor enlaza un how-to de su knowledge base (**"Resizing Partitions or Filesystem or LVMs after Upgrade"**, con GParted como referencia) y recomienda **copia de seguridad antes de cualquier upgrade**. La captura **no publica si se puede hacer downgrade**; describe solo el camino de subida.

## Why It Matters
Confirma el patrón de **asimetría del ciclo de vida** que el thread ya tenía documentado en BuyVM ("We only allow upgrading to a bigger plan", [[2026-1024-buyvm-solo-upgrades-nunca-downgrades]]) y ExtraVM ("we cannot downgrade your VPS plan", [[2026-1024-extravm-upgrade-con-prorrateo-pero-sin-downgrade]]): FlokiNET es el **tercer proveedor con upgrade permitido y downgrade no declarado**, y añade una capa que los otros dos no tinham — **el upgrade de disco no es automático**, es una operación de sistema de ficheros que hace el cliente con GParted. Para un despliegue Postgres en producción, eso significa que "subir de plan" no es una operación de un clic sino **una intervención sobre el volumen con riesgo de corrupción**, lo que convierte el backup en precondición, no en recomendación.

## Nota de verificación
La captura **no** publica: si el downgrade está permitido, si hay prorrateo, si el discos se migran de hardware, ni el contenido real del how-to enlazado (solo su título). El precio del upgrade **no** se publica: solo se sabe que la escalera de planes va de €7,99 a €73,90.

---
id: 2026-1024-evoxt-cloning-de-vms-sin-reconfigurar
type: atom
certainty: retired
sources: [sources/2026-10-23-evoxt-vps-pricing.md]
links: ["[[2026-1024-evoxt-sub-cuentas-por-rol-para-equipos]]", "[[2026-1024-evoxt-ip-management-floating-ip-y-reasignacion]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]"]
---

## [RETIRED 2026-10-24]
Superseded por el átomo canónico del mismo proveedor (misma afirmación, capturada de la home en `sources/2026-10-23-evoxt-vms.md`). Conservado por trazabilidad, no cuenta como átomo vigente.

## Claim
Evoxt declara la ** clonación de máquinas virtuales como función de plataforma**: *"Easily clone your virtual machines without having to resetup and reconfigure everytime"*. La clonación se ofrece junto con el resto del set de gestión del panel, como una de las siete funciones destacadas (Monitoring, IP Management, Firewall, Cloning, Sub Accounts, Backups, VNC).

## Why It Matters
Es la operación que necesita cualquier despliegue multi-instancia: el despliegue vivo de [[myownclone]] es un único nginx autoalojado ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]), y el modelo del producto es multi-tenant con un clon por tenant ([[2026-1022-multi-tenant-slug-unpublished]]). Con clonación en el panel, provisionar un tenant nuevo es una operación de un clic en lugar de un playbook de instalación por instancia — y encaja con la necesidad de **separar instancias** que el modelo de despliegue exige: sin clonar la base, cada tenant es una instalación manual y cada instalación manual es una deriva de configuración. La combinación de clonar + reasignar IP ([[2026-1024-evoxt-ip-management-floating-ip-y-reasignacion]]) es justamente el patrón de "staging que se convierte en producción cambiando la IP".

## Nota de verificación
Texto transcrito literalmente. La captura **no** publica: si la clonación es snapshot completo o de disco, si se puede clonar entre regiones, si la IP se replica en el clon, ni límites de número de clones.

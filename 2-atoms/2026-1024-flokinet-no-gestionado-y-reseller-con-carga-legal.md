---
id: 2026-1024-flokinet-no-gestionado-y-reseller-con-carga-legal
type: atom
certainty: solid
sources: [sources/2026-10-24-flokinet-vps-pricing.md]
links: ["[[2026-1024-extravm-vps-no-gestionado-con-soporte-propio-24-7]]", "[[2026-1024-hostbrr-vps-comparte-cpu-y-vds-dedicada-24-7]]", "[[2026-1024-flokinet-consola-ipmi-virtual-y-panel-novnc]]", "[[2026-1024-flokinet-migracion-desde-shared-con-cpanel-whm]]"]
---

## Claim
FlokiNET define su VPS como **servicio no gestionado** en tres sitios distintos: *"VPS is an unmanaged service provided by FlokiNET, which means that FlokiNET has no access to or responsibility for monitoring, securing, maintaining, developing or troubleshooting"* y *"FlokiNET provides VPS, Dedicated Servers and Shared Hosting un-managed"*. Pero la misma página enumera el **soporte que sí da, gratis y manual**: *"Full support for the basic functions of the VPS are included and we will act manually upon request. This includes, at no extra cost: SSH access, network access, Linux installation, partition/filesystem troubleshooting after upgrade, backup recovery"*. Y **autoriza la reventa** con la condición de que el reseller asuma el soporte y el cumplimiento legal: *"as a reseller you are responsible for providing customer support and ensuring that the server is well configured and secured as our VPS are not managed"* y *"responsible for any legal requirements that may apply to your business and that your clients comply with FlokiNET's Terms of Service and Acceptable Usage policy"*.

## Why It Matters
Es la **definición más precisa de "no gestionado" del vault**, porque separa dos cosas que los otros proveedores mezclan: la **no gestión del sistema operativo** (el cliente hace kernel, repos, firewall, apps — la lista es explícita: Python, Go, Ruby, PHP, MySQL, Oracle DB, MongoDB) de la **gestión del hypervisor**, que FlokiNET sí asume y ofrece sin coste en sus cinco funciones básicas. Eso lo sitúa en un punto intermedio que el thread no tenía: ExtraVM declara "VPS no gestionados" pero ofrece **soporte propio 24/7** ([[2026-1024-extravm-vps-no-gestionado-con-soporte-propio-24-7]]) y HostBrr vende una línea "Performance VDS" con CPU dedicada 24/7 ([[2026-1024-hostbrr-vps-comparte-cpu-y-vds-dedicada-24-7]]); FlokiNET **no tiene línea gestionada**, pero sí tiene una **franja de soporte base incluida** que cubre justo los cinco momentos en que un VPS autoalojado se rompe (red, instalación, particiones tras upgrade, recuperación de backup). Y la cláusula de reseller es la que hace de esto una **opción de negocio para el vault**: se puede revender hosting sobre un VPS no gestionado, con la condición explícita de que el reseller es quien responde al cliente final y del cumplimiento de la AUP.

## Nota de verificación
La captura **no** publica: horario del soporte, tiempo de respuesta, si el "soporte gratuito" es el mismo que el de un ticket de pago, ni si el reseller paga una tarifa por revender. La lista de cinco funciones básicas es "basic functions" según el proveedor.

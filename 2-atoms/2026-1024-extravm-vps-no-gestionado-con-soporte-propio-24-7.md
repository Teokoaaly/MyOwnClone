---
id: 2026-1024-extravm-vps-no-gestionado-con-soporte-propio-24-7
type: atom
certainty: solid
sources: [sources/2026-10-23-extravm-vps-pricing.md]
links: ["[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]", "[[2026-1024-extravm-os-instalables-y-iso-propia-por-enlace-https]]", "[[2026-1024-hostbrr-virtfusion-panel-rebuild-os-vnc-y-telemetria]]"]
---

## Claim
ExtraVM declara que **sus planes VPS son no gestionados**: "Our VPS plans are unmanaged, meaning you have full root access and control. However, our support team is available to help with and basic server questions. Full management may be offered to businesses at request, please contact us." El marketing añade **soporte técnico propio 24/7** ("In-house technical support available around the clock. No outsourced inexperienced techs") y un **panel de control propio** con reinstall de SO, consola, backups y gestión de red.

## Why It Matters
Define el reparto de trabajo que el vault tiene que asumir si autoaloja: con ExtraVM el **root, los backups, el firewall, los upgrades de SO y el monitorreo** son trabajo del cliente, igual que en el despliegue vivo con nginx ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]); lo único que el proveedor pone es un soporte de incidencias y, bajo petición, gestión completa para empresas — es decir, un precio "todo incluido" solo disponible **bajo negotiation**, sin tarifa publicada. Esa asimetría (root completo sin coste, operación completa sin coste, gestión completa a precio desconocido) es el patrón del mercado que el vault está midiendo: nadie publica el coste de la gestión, que es exactamente la partida que el autoalojado multiplica cuando aparecen varios tenants ([[2026-1022-costes-por-categoria-tenant]]). El panel propio con reinstall y backups es relevante porque evita el self-service de otros proveedores y porque el vault ya tiene experiencia con paneles de gestión (VirtFusion en HostBrr, [[2026-1024-hostbrr-virtfusion-panel-rebuild-os-vnc-y-telemetria]]).

## Nota de verificación
La captura no publica SLA de soporte, tiempos de respuesta, ni condiciones ni precio de la gestión completa bajo petición. El panel se documenta solo como demo en vídeo.

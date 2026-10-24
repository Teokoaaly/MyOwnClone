---
id: 2026-1024-hostbrr-os-debian-ubuntu-alma-windows-y-iso
type: atom
certainty: solid
sources: [sources/2026-10-23-hostbrr-vps-pricing.md]
links: ["[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]", "[[2026-1024-evoxt-os-windows-rdp-y-linux]]", "[[2026-1024-hostbrr-virtfusion-panel-rebuild-os-vnc-y-telemetria]]"]
---

## Claim
La página de precios de HostBrr declara el catálogo de sistemas operativos instalables con un clic ("We support a massive variety of constantly updated Operating Systems. Install your preferred OS with a single click"): **Debian, Ubuntu, AlmaLinux, Rocky Linux, Alpine, Fedora, FreeBSD y Windows**, más "**Also supporting: Arch Linux, SUSE, Oracle Linux, CloudLinux, and Custom ISO integration**". La FAQ (pregunta 02) reduce la lista oficial a cinco: "You can deploy **Debian, Ubuntu, AlmaLinux, Rocky Linux, or Windows**", y añade que "**Snapshots are supported**, so you can capture a known-good state before making big changes".

## Why It Matters
El despliegue vivo del vault corre `nginx/1.28.3 (Ubuntu)` ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]): Ubuntu está en la lista, así que el sistema operativo no es un coste de migración. La diferencia real con el competidor inmediato del vault es de alcance: Evoxt publica ocho logos (Windows RDP, Ubuntu, Debian, CentOS, AlmaLinux, Rocky, Fedora, SUSE) sin FreeBSD, sin Alpine y sin ISO ([[2026-1024-evoxt-os-windows-rdp-y-linux]]); HostBrr añade **FreeBSD y Alpine** y, sobre todo, **Custom ISO integration**, que es la vía para una imagen propia. Y el "Snapshots are supported" de la FAQ conecta directamente con la política de despliegue del producto: capturar un estado conocido-bueno antes de un cambio grande es la práctica que evita un incidente de configuración en producción, aquí ofrecida como función de plataforma y no como script.

## Nota de verificación
La página **no** publica versiones (Ubuntu 22.04 vs 24.04), ni kernels, ni coste de la licencia de Windows, ni si las imágenes son oficiales o propias. La lista del cuerpo de la página (13 sistemas) y la de la FAQ (5) **no coinciden**: la FAQ no menciona Alpine, Fedora ni FreeBSD. No se afirma que estén deprecados; la discrepancia está sin resolver.

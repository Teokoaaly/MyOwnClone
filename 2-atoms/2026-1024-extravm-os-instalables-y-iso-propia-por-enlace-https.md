---
id: 2026-1024-extravm-os-instalables-y-iso-propia-por-enlace-https
type: atom
certainty: solid
sources: [sources/2026-10-23-extravm-vps-pricing.md]
links: ["[[2026-1024-hostbrr-os-debian-ubuntu-alma-windows-y-iso]]", "[[2026-1024-extravm-8-datacenters-facilities-asn-y-test-ip]]", "[[2026-1024-evoxt-os-windows-rdp-y-linux]]"]
---

## Claim
ExtraVM publica una lista de **sistemas operativos instalables al instante**: Ubuntu, Debian, AlmaLinux, Rocky Linux, Fedora, Alpine Linux, FreeBSD, Windows y **Windows Server**. Además ofrece **ISO propia adjunta por enlace HTTPS directo**: "You can also attach your own custom ISO using HTTPS direct link to the ISO" (con la lista completa en su knowledgebase). La página de características añade **KVM Virtualization, Full Kernel Access, Linux / Windows / BSD e ISO Install Supported**, y todos los planes incluyen **full root access**.

## Why It Matters
El soporte de **Windows Server** y de **FreeBSD** diferencia a ExtraVM de la oferta Linux-only del resto del vault registrado: HostBrr publica Debian/Ubuntu/Alma/Windows + ISO ([[2026-1024-hostbrr-os-debian-ubuntu-alma-windows-y-iso]]) y Evoxt Windows RDP + Linux ([[2026-1024-evoxt-os-windows-rdp-y-linux]]), pero ExtraVM es el único que ofrece BSD explícitamente y **full kernel access**, que es lo que permite compilar kernel o tocar parámetros de sysctl — irrelevante para servir el stack Flask/Next.js del despliegue vivo ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) pero relevante como criterio de "VPS de propósito general frente a VPS de hosting". Para MyOwnClone la combinación útil es **Linux + ISO propia por HTTPS**, que permite una imagen reproducible del stack (con Postgres, Redis y dependencias fijadas) en lugar de un installur genérico que hay que re-configurar en cada reinstalación. El "custom ISO install" está además declarado como incluido en **todos** los planes, sin coste adicional.

## Nota de verificación
La captura no publica la lista completa de versiones de SO (remite a un knowledgebase externo), las licencias de Windows Server ni su coste, ni si Windows requiere licencia propia o está incluida en el precio.

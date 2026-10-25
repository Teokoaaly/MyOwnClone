---
id: 2026-1024-flokinet-sin-windows-ni-virtualizacion-anidada
type: atom
certainty: solid
sources: [sources/2026-10-24-flokinet-vps-pricing.md]
links: ["[[2026-1024-evoxt-os-windows-rdp-y-linux]]", "[[2026-1024-flokinet-ddos-1tbps-incluido-en-los-siete-planes]]", "[[2026-1024-flokinet-aup-prohibe-chia-netscan-y-origenes-de-ddos]]"]
---

## Claim
FlokiNET **no ofrece VPS con Windows**: *"At the moment, we do not offer Windows-based Virtual Private Servers"*, y remite a los **servidores dedicados** para quien necesite Windows, con la salvedad de que "FlokiNET does not provide Windows licenses, nor is responsible for any Windows licensing procedures". El catálogo de SO es **Linux/BSD**: Alma Linux, Alpine, CentOS, Debian, Fedora Server, Ubuntu Server, Ubuntu Desktop, FreeBSD, OpenBSD, OpenSUSE, RHEL, Rocky Linux y otros. La restricción explícita es la **virtualización anidada**: *"Nested Virtualization is not allowed"*, y la FAQ añade que por eso las aplicaciones de virtualización son de las pocas que no se pueden instalar, remitiendo a los dedicated para ese caso.

## Why It Matters
Es la restricción de SO más dura del vault junto con la de Skhron/ExtraVM: donde Evoxt publica "from Windows RDP all the way to Linux VPS" ([[2026-1024-evoxt-os-windows-rdp-y-linux]]), FlokiNET cierra la puerta de Windows en el VPS y la abre solo en el dedicado, sin licencia incluida. Para el stack vivo del vault —`nginx/1.28.3 (Ubuntu)` en [[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]— la restricción es **irrelevante**: Ubuntu Server está en la lista y no hay recertificación que hacer. Lo que sí tiene consecuencia operativa es la **virtualización anidada prohibida**: descarta a FlokiNET como host de un nodo que corra contenedores con virtualización anidada (KVM sobre KVM) o máquinas virtuales dentro del VPS, lo que separa este proveedor de los que sí la permiten. Es una decisión de arquitectura de producto, no una especificación: la misma empresa que la prohíbe en el VPS la vende en el dedicado, así que **la restricción es del producto, no de la plataforma**.

## Nota de verificación
La captura **no** publica: versiones de SO, si las imágenes son oficiales o propias, kernel, coste de la licencia Windows ni si la prohibición de virtualización anidada se aplica también a los dedicados (el texto dice "If you need to run virtual servers, please choose one of our Dedicated Server plans, they are all compatible with virtualization platforms" — lo que implica que la prohibición es del VPS).

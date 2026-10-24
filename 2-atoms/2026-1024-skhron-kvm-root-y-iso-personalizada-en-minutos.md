---
id: 2026-1024-skhron-kvm-root-y-iso-personalizada-en-minutos
type: atom
certainty: solid
sources: [sources/2026-10-23-skhron-bitcoin-vps.md]
links: ["[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]", "[[2026-1024-evoxt-despliegue-100-automatico-y-upgrade-con-un-boton]]", "[[2026-1024-extravm-despliegue-tras-confirmacion-en-15-30-minutos]]"]
---

## Claim
Todos los servidores de Skhron corren sobre **KVM** con "an isolated environment with full root access, powered with your own kernel, and any operating system installable from a custom ISO". El despliegue es automatizado: "Provisioning is automated and typically completes within a few minutes of you completing the build configuration in the control panel". Instalación de SO: plantillas listas de **Debian, Ubuntu Server, AlmaLinux, Rocky Linux y Alpine Linux**, o **cualquier otro SO mediante ISO personalizada desde una URL externa, de forma totalmente automatizada sin contactar a soporte**. Reverse DNS (PTR) es autoservicio en el panel **VirtFusion** para IPv4 e IPv6, sin ticket.

## Why It Matters
Es el vector de migración del vault: el despliegue vivo es un nginx autoalojado ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) y el stack operativo de MyOwnClone es Flask + Next.js, lo que exige control del SO, no una imagen prefabricada. "Custom ISO desde URL externa, automatizado" es exactamente lo que permite un proceso reproducible de build propio sin depender de los templates del proveedor. El coste del modelo es que el aprovisionamiento "en pocos minutos" **arranca tras completar la configuración**, es decir, la latencia la pone el usuario y no el panel; y el panel VirtFusion es el mismo que usa HostBrr ([[2026-1024-hostbrr-virtfusion-panel-rebuild-os-vnc-y-telemetria]]), señal de que es un stack de virtualización compartido por varios proveedores del tramo barato.

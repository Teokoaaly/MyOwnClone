---
id: 2026-1024-hostbrr-virtfusion-panel-rebuild-os-vnc-y-telemetria
type: atom
certainty: solid
sources: [sources/2026-10-23-hostbrr-vps-pricing.md]
links: ["[[2026-1024-evoxt-api-y-rescue-mode-para-gestion-de-vms]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]", "[[2026-1024-hostbrr-os-debian-ubuntu-alma-windows-y-iso]]"]
---

## Claim
El panel de gestión de los VPS de HostBrr es **VirtFusion**, y la página de precios declara sus capacidades: "Rebuild your OS, track live bandwidth usage, access the out-of-band VNC console, and manage SSH keys—all without ever needing to open a support ticket". Añade **"Live Telemetry"** —gráficas en tiempo real de uso de CPU, E/S de disco y throughput de red— y **"Rescue Mode & Out-of-Band"**: "Locked yourself out? Boot into a lightweight rescue environment or use the native VNC console to recover your system". La página incluye dos capturas de la interfaz (dashboard de VirtFusion y "VirtFusion — Backup Manager").

## Why It Matters
Convierte una tarea recurrente de operaciones en una función de plataforma. El vault tiene hoy un nginx autoalojado ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) sin instrumentación declarada ([[2026-1023-live-verify-sin-instrumentacion-sentry-posthog]]); el "Rescue Mode" es exactamente el mecanismo que evita el ticket de soporte cuando un tenant rompe la configuración, y el "manage SSH keys" sin soporte elimina la tarea de distribuir claves. Para un producto multi-tenant esto reduce el coste operativo recurrente, que es una de las partidas que el vault viene tratando como externalizable ([[2026-1023-hetzner-costes-por-categoria-vs-infraestructura-propia]]). El matiz del competidor inmediato es que Evoxt solo publica un "API y Rescue Mode" genérico sin detalle de VNC ni telemetría ([[2026-1024-evoxt-api-y-rescue-mode-para-gestion-de-vms]]).

## Nota de verificación
La captura **no** publica si el panel de VirtFusion tiene API, ni si la telemetría es exportable (Prometheus/Datadog), ni el precio del add-on de backups que se muestra en la captura del Backup Manager. Se transcribe el copy literal de la página.

---
id: 2026-1024-hostbrr-backups-como-addon-opcional-con-gfs
type: atom
certainty: solid
sources: [sources/2026-10-23-hostbrr-vps-pricing.md]
links: ["[[2026-1024-evoxt-backup-semanal-offsite-gratuito]]", "[[2026-1024-hostbrr-webhosting-1-25-litespeed-ssl-y-backups]]", "[[2026-1024-hostbrr-virtfusion-panel-rebuild-os-vnc-y-telemetria]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]"]
---

## Claim
Los backups de los VPS de HostBrr **no vienen incluidos**: la página los presenta como **"Optional Add-On"** — "Our backup add-on brings automated, block-level backups directly into your VirtFusion panel — no maintenance windows, no disruption to your running workloads". El add-on declara: **"Live Block-Level Backups"** (copian con la VM online mediante detección de consistencia), **"Full, Incremental & Differential"** (cadenas automáticas: baseline completo + incrementales o diferenciales), **"Flexible Retention Policies"** (retención por edad "keep everything from the last N days" o **planificación GFS** con puntos de restore diarios, semanales, mensuales y anuales simultáneos) y **"Self-Service Restore"** (restaurar una imagen de disco completa o extraer ficheros individuales sin tocar el servidor en marcha). El panel muestra un ejemplo: "server-001 · 30-day retention", full backup 21,4 GB hoy 03:00, incremental 1,2 GB ayer, incremental 0,8 GB hace 2 días, differential 4,1 GB hace 3 días. **El precio del add-on no se publica.**

## Why It Matters
Es la partida que separa el "cheap VPS" del coste total real: el plan de €2 no incluye backups, mientras que el hosting compartido de €1,25 **sí** incluye "Free Daily Backups" ([[2026-1024-hostbrr-webhosting-1-25-litespeed-ssl-y-backups]]) — el proveedor vende barato el servidor y cobra (o no) la continuidad por separado. Para MyOwnClone esto es una línea de coste hoy inexistente en el cálculo: el despliegue vivo es un nginx autoalojado ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) sin backup automático declarado, y el multiplicador de coste real del producto es "coste de servidor + coste de recuperación", no el primero solo. El contrapunto del vault es Evoxt, que sí publica **backup semanal offsite gratuito** ([[2026-1024-evoxt-backup-semanal-offsite-gratuito]]): mismo rango de precio, promesa de backup incluida, así que el add-on de HostBrr es una desventaja comparativa que solo se puede cuantificar con el precio ausente.

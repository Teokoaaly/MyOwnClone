---
id: 2026-1024-lowendbox-serverhost-leb-1gb-kvm-11-dolares-al-ano
type: atom
certainty: solid
sources: [sources/2026-10-23-lowendbox-1-usd-vps.md]
links: ["[[2026-1024-lowendbox-vps-anuales-de-10-a-11-dolares-no-mensuales]]", "[[2026-1024-lowendbox-lowend-score-cinco-estrellas-como-filtro]]", "[[2026-1024-lowendbox-ubicaciones-norteamerica-y-amsterdam]]", "[[2026-1024-lowendbox-cupon-1aleb-80-de-descuento]]"]
---

## Claim
**ServerHost LEB – 1GB KVM VPS**: 1x vCPU Core, **1GB RAM**, **15GB High Performance Storage**, **1000Mbps Port**, **Unmetered Bandwidth**, Full Root Access, 1 Dedicated IPv4 Address, **KVM/Virtualizor**, Linux O/S, disponible en múltiples ubicaciones, a **$11.00/year (80% off)** con **coupon code `1ALEB`**. La descripción del proveedor menciona almacenamiento **NVMe**, servicios de backup y "more than 10 years of experience in the hosting industry"; datacenters en **Los Angeles, Chicago, Dallas, Buffalo y Amsterdam**.

## Why It Matters
Es la oferta más completa de la lista en la variable que más pesa para un despliegue self-hosted: **ancho de banda sin medir (Unmetered Bandwidth)** frente a las otras tres, que topan en 1 TB/mes. Para un producto que sirve respuestas de clon con audio y vídeo, el egreso es la partida que dispara las facturas (ver [[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]] en el extremo caro) y aquí es el único plan del artículo sin esa variable. En contra: **1 GB de RAM** es menos que lo que necesita el stack Flask + Next.js + Postgres + Redis del despliegue vivo ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]), así que sirve como nodo auxiliary o worker, no como host del stack completo. Es también el único plan con **1 GB en lugar de 768 MB** y con IP dedicada incluida.

## Nota de verificación
Precio, coupon, specs y ubicaciones transcritos literalmente. La fuente **no** publica: SLA, número de cores compartidos, si el bandwidth sin medir tiene límite "fair use", ni condiciones del 80% off más allá del código.

## [NOTA 2026-10-24 — LowEndBox $2]
Fuente: `sources/2026-10-23-lowendbox-2-usd-vps.md`. ServerHost publica un **segundo plan LEB** en la lista hermana: **2 GB KVM VPS, 30 GB de almacenamiento, 1000Mbps Unmetered Port, $21.88/year (75% off), coupon `2LEBA`**, con la misma descripción de proveedor (NVMe, backup services, "over 10 years of experience") y los mismos datacenters (**Los Angeles, Chicago, Dallas, Buffalo y Amsterdam**). Pasa de 15 GB a 30 GB de disco y de 1 GB a 2 GB de RAM por $10,88 más al año. Ver [[2026-1024-lowendbox-2-usd-serverhost-2gb-21-88-cupon-2leba]].

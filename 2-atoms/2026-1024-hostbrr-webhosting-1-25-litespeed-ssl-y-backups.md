---
id: 2026-1024-hostbrr-webhosting-1-25-litespeed-ssl-y-backups
type: atom
certainty: solid
sources: [sources/2026-10-23-hostbrr-home.md, sources/2026-10-23-hostbrr-vps-pricing.md]
links: ["[[2026-1024-hostbrr-escalera-de-precios-vps-2-00-3-50-y-3-90]]", "[[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]"]
---

## Claim
El hosting compartido cPanel de HostBrr parte de **€1.25/mes** y se describe como "Powerful, easy-to-use shared hosting with cPanel, free SSL, and NVMe storage", con dos inclusiones declaradas: **Litespeed Web Server** y **Free Daily Backups**. En la home aparece además una oferta temporal de **50 % OFF** en cPanel webhosting con el código **NEWLAUNCH**, con enlace directo a la sección de precios. Es el producto más barato de todo el catálogo de la home.

## Why It Matters
Es la capa más barata del catálogo y la que el proveedor usa como embudo de entrada hacia su VPS (ver [[2026-1024-hostbrr-escalera-de-precios-vps-2-00-3-50-y-3-90]] y la trayectoria de upgrade que documenta [[2026-1024-hostbrr-trayectoria-shared-a-vps-con-root]]). Como referencia de arquitectura, el bundle "cPanel + SSL gratuito + backups diarios automáticos + NVMe" describe exactamente lo que el vault NO tiene hoy: el despliegue vivo de [[2026-1022-live-verify-deployment-migrada-a-vps-nginx]] es un nginx autoalojado ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) sin backups automáticos declarados. El precio de €1,25/mes es el suelo del coste de hosting de un producto SaaS con una sola línea de base.

## Nota de verificación
La captura no publica el descuento del 50 % en euros (ni su fecha de caducidad), los recursos del plan de entrada, ni las condiciones del "Free Daily Backups" (retención, Incremental o completo).

## [NOTA 2026-10-24 — página de precios]
Fuente: `sources/2026-10-23-hostbrr-vps-pricing.md`. La página de precios **vuelve a mostrar el mismo banner de oferta** —"Limited time offer: **50% OFF** cPanel Webhosting with code **NEWLAUNCH**"— pero dirigido a `hostbrr.com/cpanel.html#pricing`, es decir, la oferta es de **webhosting**, no de VPS, y se mantiene vigente en una página de VPS (captura del 2026-10-23). La observación operativa para el vault es la **asimetría de inclusiones dentro del mismo proveedor**: el webhosting de €1,25 trae "Free Daily Backups" incluidos mientras que los backups del VPS son un **"Optional Add-On" de pago** ([[2026-1024-hostbrr-backups-como-addon-opcional-con-gfs]]) — el backup gratuito no está en la familia cara, sino en la barata, lo que invierte el orden habitual de "más caro, más inclusiones".

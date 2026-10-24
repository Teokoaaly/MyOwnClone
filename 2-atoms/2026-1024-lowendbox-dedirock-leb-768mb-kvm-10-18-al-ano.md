---
id: 2026-1024-lowendbox-dedirock-leb-768mb-kvm-10-18-al-ano
type: atom
certainty: solid
sources: [sources/2026-10-23-lowendbox-1-usd-vps.md]
links: ["[[2026-1024-lowendbox-racknerd-leb-768mb-10-28-sin-stock]]", "[[2026-1024-lowendbox-cloudserver-leb-1gb-kvm-10-dolares-al-ano]]", "[[2026-1024-lowendbox-ubicaciones-norteamerica-y-amsterdam]]", "[[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]"]
---

## Claim
**DediRock LEB – 768MB KVM VPS**: 1x vCPU Core, **768MB RAM**, **10GB SSD Storage**, **1TB Monthly Bandwidth**, **1Gbps Public Network Port**, Full Root Admin Access, 1 Dedicated IPv4 Address, **KVM/SolusVM**, Linux O/S, disponible en múltiples ubicaciones, a **$10.18/year**. El artículo sitúa a DediRock en *"cutting-edge data centers in **Los Angeles and New York**"* y describe KVM con *"full root access"*, "advanced security features", **backups regulares** y soporte **24/7**.

## Why It Matters
Es la variante de 768 MB con la ficha de seguridad más concreta del artículo (backups regulares + soporte 24/7 declarados), lo que la hace el candidato más defendible para un nodo que corre un servicio de estado — por ejemplo, el relay o el backend de webhooks que hoy es una línea invisible en el corte por categoría ([[2026-1022-costes-por-categoria-tenant]]). Su techo es 768 MB de RAM y 1 TB/mes: insuficiente para el stack Flask + Next.js + Postgres + Redis ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]), pero suficiente para un relay tipo sub2api, que es exactamente el escenario que los patrocinadores chinos del vault describen ([[2026-1023-priceai-sponsors-vps-chinos-para-auto-hospedar-relay]]). El precio, $10.18/año, es 1,8 % más caro que el de CloudServer: la diferencia real entre ambos es RAM y disco, no precio.

## Nota de verificación
Precio y specs transcritos literalmente. La fuente **no** publica: SLA con créditos, si los backups son automáticos y con qué retención, ni las condiciones de renovación del precio LEB.

## [NOTA 2026-10-24 — LowEndBox $2]
Fuente: `sources/2026-10-23-lowendbox-2-usd-vps.md`. DediRock publica un **segundo plan LEB**: **2GB KVM VPS, 20GB SSD RAID-10, 1000Mbps Port, 2TB Monthly Bandwidth, $20.88/year**, en "cutting-edge data centers in **Los Angeles and New York**", con las mismas declaraciones de **backups regulares** y soporte **24/7**. Sube de 768 MB / 10 GB / 1 TB a 2 GB / 20 GB / 2 TB por $10,70 más al año, y mantiene el **egreso más bajo de la lista de $2** (2 TB/mes). Es la opción de 2 GB más barata de las cinco. Ver [[2026-1024-lowendbox-2-usd-dedirock-2gb-20-88]].

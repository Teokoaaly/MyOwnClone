---
id: 2026-1026-heroku-postgres-standard-50-a-12000-con-dedicado-y-1-hora-de-parada
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-pricing.md]
links: ["[[2026-1026-heroku-postgres-essential-5-a-20-dolares-con-4-horas-de-parada]]", "[[2026-1024-extravm-escalera-de-precios-14-planes-de-4-50-a-192]]", "[[2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados]]"]
---

## Claim
El tier **Standard** de Heroku Postgres va de **Standard-0 $50/mes** (4 GB RAM, 64 GB disco, **120 conexiones**) a **Standard-10 $12,000/mes** (1 TB RAM, 8 TB disco, 500 conexiones), con nueve escalones intermedios: **Standard-2 $200** (8 GB/256 GB/400), **Standard-3 $400** (15 GB/512 GB/500), **Standard-4 $750** (30 GB/768 GB/500), **Standard-5 $1,400** (61 GB/1 TB/500), **Standard-6 $2,000** (122 GB/1.5 TB/500), **Standard-7 $3,500** (244 GB/2 TB/500), **Standard-8 $4,500** (488 GB/3 TB/500), **Standard-9 $5,800** (768 GB/4 TB/500). Todos declaran "**Dedicated server (not shared)**", "No row limitations", "Increasing amounts of in-memory cache", "**Fork and follow support**", "**Rollback up to 4 days**", "**Max downtime 1 hour per month**", "Credential Management" y "Priority service restoration on disruptions".

## Why It Matters
El salto de **$5 (Essential-0, compartido) a $50 (Standard-0, dedicado)** es un **×10**, y es la primera vez que el vault mide un salto de "compartido a dedicado" en un proveedor de bases de datos gestionadas: la lógica es la misma que en Hetzner ([[2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados]]) pero el multiplicador es **×10 en el primer peldaño**, no ×6,70. Es decir: **en Postgres gestionado el servidor dedicado no es la opción accesible, es la de la mitad alta del catálogo**, y el rango total del tier ($50 → $12,000, ×240) es mucho más largo que el de cualquier VPS del vault (ExtraVM va de $4.50 a $192, ×42,67 — [[2026-1024-extravm-escalera-de-precios-14-planes-de-4-50-a-192]]).
El dato de precio con más consecuencia para el vault es el **"Max downtime 1 hour per month"**: es un **compromiso numérico explícito**, ausente en el tramo VPS barato del vault, donde casi nadie publica SLA. Heroku publica un SLA *de hecho* (una ventana de caída máxima) pero **la página no publica créditos ni el texto del SLA**, así que es un claim de downtime, no un contrato con penalización.
Y los dos features que sí importan para un producto que migra clones con downtime: "**Fork and follow support**" (clonar la base para una migración en caliente) y "**Rollback up to 4 days**" (deshacer un despliegue de esquema).

## Nota de verificación
La página no publica el SLA en texto, ni créditos, ni el precio del Private Space que exigen los planes Private/Shield.

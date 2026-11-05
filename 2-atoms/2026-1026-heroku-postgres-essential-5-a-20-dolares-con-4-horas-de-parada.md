---
id: 2026-1026-heroku-postgres-essential-5-a-20-dolares-con-4-horas-de-parada
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-pricing.md]
links: ["[[2026-1022-neon-postgres-serverless]]", "[[2026-1026-heroku-suelo-5-dolares-eco-con-sleep-y-7-dolares-basic-always-on]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]"]
---

## Claim
El tier **Essential** de Heroku Postgres tiene **tres planes, todos con "Shared RAM" y "RAM 0 Bytes"**: **Essential-0 $5/mes** (1 GB de disco, **20 conexiones**), **Essential-1 $9/mes** (10 GB, 20 conexiones) y **Essential-2 $20/mes** (32 GB, **40 conexiones**). Los tres declaran "**No row limitations**", "**Encryption-at-rest**", "**Max downtime 4 hour per month**" y "**Table Limit: 4,000 tables**".

## Why It Matters
Es el **precio de una base de datos gestionada en el tramo bajo**, y el dato operativo que importa no es el precio sino el **"Max downtime 4 hour per month"**: cuatro horas de caída al mes son **0,56 % de indisponibilidad** (4 h sobre 720 h de mes de 30 días, es decir una disponibilidad del **99,44 %**), un tier que el vault debería clasificar aparte del SLA con créditos que sí publica Hetzner en el tramo barato. Sin SLA, sin créditos y con tope de 4.000 tablas, Essential es "Postgres que no se cae" solo en el sentido de "se cae poco".
Comparado con el stack vivo ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]), el vault paga hoy la base de datos **dentro del VPS** — invisible en la factura. Aquí la base de datos tiene precio de lista propio desde $5/mes, y ese importe es **exactamente el del dyno Eco de $5** y casi el del dyno Basic siempre encendido de $7: es decir, **el coste de la base de datos gestionada es del orden del coste de la compute gestionada**, cosa que no ocurre en el tramo VPS donde la DB va dentro del mismo servidor.
Y el punto de fricción con el stack actual: **20 conexiones** en Essential-0 es un límite bajo para un Postgres + Redis + Flask + Next.js con varios procesos ([[2026-1022-neon-postgres-serverless]] documenta el Postgres serverless con el que se diseñó el producto).

## Nota de verificación
El "RAM 0 Bytes" de la tabla se reproduce tal cual aparece en la captura (columna RAM de los tres planes Essential). La fuente **no publica el precio de un Private Space**, que las filas Private y Shield de las tablas Classic y Advanced exigen explícitamente.

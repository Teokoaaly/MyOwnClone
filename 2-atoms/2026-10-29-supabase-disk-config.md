---
id: 2026-10-29-supabase-disk-config
type: atom
certainty: solid
sources: [sources/2026-10-29-supabase-pricing.md]
links: ["[[2026-10-29-r2-storage]]", "[[2026-1029-aws-ses-ala-carte-pricing]]"]
---

## Claim

Supabase offers two advanced disk configurations: General Purpose (64 TB max, 8 GB included then $0.125 per GB, 3,000 IOPS included then $0.024 per IOPS, 99.9% durability) and High Performance (60 TB max, $0.195 per GB, $0.119 per IOPS, auto-scaling IOPS, 99.999% durability).

## Why It Matters

The choice between General Purpose and High Performance durability and IOPS pricing affects mission-critical workloads — General Purpose balances price and performance for typical applications, while High Performance guarantees 99.999% durability and automatic IOPS scaling for workloads with unpredictable or spiky I/O demands.

## [FRICTION]

> [[2026-10-29-r2-storage]] provides object storage up to 10 TB with different durability characteristics ($0.023 per GB per month for standard, $0.05 per GB per month for glacier), whereas Supabase General Purpose includes 8 GB per project then $0.125 per GB with 99.9% durability — the pricing per GB is higher for Supabase but includes a managed Postgres instance, whereas R2 is raw object storage without database features, making the cost comparison dependent on whether the user values managed Postgres or raw storage savings.

> Ambas proveen almacenamiento duradero, pero Supabase a $0.125/GB incluye Postgres gestionado y R2 a precios mucho menores es storage sin más — el usuario debe evaluar si el valor añadido de Postgres justifica el costo 5x+ por GB. Marcado para juicio humano, no auto-resuelto.
---
id: 2026-1029-render-postgres-pricing
type: atom
certainty: solid
sources: [sources/2026-10-29-render-pricing.md]
links: ["[[2026-1022-admin-bandeja-global-y-spam]]", "[[2026-1022-auth-flask-nextauth-desconectados]]"]
---

## Claim
Render's managed PostgreSQL service scales from $0 (Free: 256 MB RAM, 100 connections) to $11,000/mo (128 CPU, 1024 GB RAM, 500 connections), with logical backup available only on paid plans and expandable storage at $0.30/GB per month.

## Why It Matters
The steep pricing curve for high-CPU Postgres instances (up to 11× the base rate) combined with $0.30/GB storage costs creates a significant cost differential between development and production workloads, particularly for data-intensive applications that require substantial RAM and connection capacity.

## [FRICTION]
> [[2026-1022-neon-postgres-serverless]] records that serverless PostgreSQL alternatives offer compute scaling to 0 with autoscaling, positioning Render's fixed-instance model as potentially over-provisioned for variable workloads. The trade-off is between Render's predictable per-second billing and serverless's true pay-per-use, with serverless introducing cold-start latency that Render's always-warm instances avoid.

## Nota de extensión 2026-11-03
Verificado contra `sources/2026-10-29-render-pricing.md`. Datos adicionales del mismo source: 1 GB de almacenamiento SSD incluido en todas las instancias, PITR disponible en todas, máximo de producto de 128 CPU y 1.024 GB de RAM, ventana de PITR de 3 días en Hobby y 7 días en Pro, Scale y Enterprise, y 100 conexiones en las instancias pequeñas frente a 500 en las de 32 GB o más (200 en 2c-8g, 400 en 2c-16g y 4c-16g). El backup lógico solo está disponible en instancias de pago.

Nota: el claim de este átomo sobre el techo de $11.000/mes es correcto, pero la tabla de Key Value no llega a esa cifra — el detalle real de Key Value está en [[2026-1029-render-keyvalue-tabla-real]].
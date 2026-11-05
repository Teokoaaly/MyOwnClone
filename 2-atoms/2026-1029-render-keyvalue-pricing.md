---
id: 2026-1029-render-keyvalue-pricing
type: atom
certainty: solid
sources: [sources/2026-10-29-render-pricing.md]
links: ["[[2026-1022-admin-bandeja-global-y-spam]]", "[[2026-1022-auth-flask-nextauth-desconectados]]"]
---

## Claim
Render's Key Value (Redis-compatible) service ranges from $0 (Free: 25 MB RAM, 50 connections) to $9,000/mo (50 GB RAM, 768 GB storage, 50,000 connections), with disk-backed persistence available only on paid plans at $0.25 per GB per month.

## Why It Matters
The $0.25/GB monthly cost for disk-backed persistence versus the Free tier's lack of persistence creates a clear upgrade path for applications that require data durability, but the Free tier's 25 MB RAM limit makes it suitable only for caching use cases with small datasets or as a read-through layer in front of primary storage.

## [FRICTION]
> [[2026-1027-decodo-js-rendering-y-proxies-premium-como-extras-activables-a-demanda]] highlights that many Redis-as-a-service competitors include persistence by default or offer it at lower marginal cost, suggesting Render's $0.25/GB may be priced at a premium compared to specialized Redis providers. The friction arises when users compare per-GB costs across providers without accounting for Render's integrated compute+storage billing advantage.

## Nota de extensión 2026-11-03
Verificado contra `sources/2026-10-29-render-pricing.md`: **el claim de este átomo mezcla dos filas de la captura**. La tabla de Key Value llega como máximo a $750/mes (50 GB RAM, 50 GB storage, 50.000 conexiones); el $0,25/GB/mes es el precio de los *persistent disks* de los servicios, no de Key Value, y el almacenamiento de Key Value va incluido en el precio de la instancia (mismo tamaño que la RAM). La tabla correcta está en [[2026-1029-render-keyvalue-tabla-real]], que registra la fricción sin sobrescribir este átomo.

Confirmado en la captura: la persistencia en disco de Key Value solo está disponible en planes de pago, y el techo del producto son 50 GB de RAM.
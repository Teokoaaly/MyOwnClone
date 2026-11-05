---
id: 2026-1031-lambda-gpu-pricing
type: atom
certainty: solid
sources: [sources/2026-10-31-lambda-gpu-pricing.md, sources/2026-11-01-lambda-gpu-pricing.md, sources/2026-11-02-lambda-gpu-pricing.md]
links: ["[[2026-1031-proton-business-vpn-essentials-6-99-minimo-2-usuarios]]", "[[costes-por-categoria-tenant]]", "[[2026-1031-lambda-instancias-8x-precio-por-gpu-hr]]", "[[2026-1101-lambda-presupuesto-4-euros-ordena-de-magnitud-gpu]]"]
---

## Claim
Lambda GPU pricing is per-second GPU allocation with minute-level billing, creating a usage-based cost model for GPU-accelerated workloads where cost scales with GPU time rather than per-user seats.

## Why It Matters
Unlike the per-seat cost dominance model where user count drives cost, Lambda GPU pricing scales with GPU allocation duration. For AI/ML products, this means cost depends on the frequency and duration of GPU-accelerated operations per user. If each user triggers GPU workloads sporadically, the per-second billing can be cost-effective compared to reserved GPU instances. However, for continuous GPU workloads, the cost can exceed fixed-reservation models. The friction is in matching workload patterns to the billing model: bursty, sporadic GPU usage benefits from per-second pricing, while sustained GPU workloads favor reserved instances or dedicated hardware.

## [FRICTION]
> [[2026-1027-proton-business-vpn-plus-incluye-planes-free-de-mail-drive-y-pass]] includes free Mail/Drive/Pass plans at the $3.49/mo tier, while Lambda GPU charges per-second GPU allocation with no included services. Both serve different purposes — Proton provides a full B2B productivity suite per user, while Lambda provides raw GPU compute per second of usage. A product combining GPU inference with user-facing features must track both costs: Lambda GPU cost per second of inference + per-user costs for the surrounding service (similar to Proton's per-user model). Conflating the two would understate total cost, as GPU compute is typically the dominant expense layer separate from user-facing services.

## Nota de extensión 2026-11-03
Fuente: `sources/2026-11-01-lambda-gpu-pricing.md` (captura completa de `lambda.ai/pricing`) y `sources/2026-10-31-lambda-gpu-pricing.md` / `sources/2026-11-02-lambda-gpu-pricing.md` (capturas parciales de las mismas tablas). Aporta las **cifras concretas** que faltaban en este átomo, que hasta ahora afirmaba el modelo de facturación sin ninguna cifra al lado.

**Precios publicados por GPU y hora (Instances, 8x):** B200 SXM6 **$6,69** (180 GB, 208 vCPU, 2900 GiB, 22 TiB SSD), H100 SXM **$3,99** (80 GB, 208 vCPU, 1800 GiB, 22 TiB), A100 SXM 80 GB **$2,79**, A100 SXM 40 GB **$1,99**, Tesla V100 **$0,79** (16 GB, 88 vCPU, 448 GiB). Ver [[2026-1031-lambda-instancias-8x-precio-por-gpu-hr]].

**Precios de 1-Click Clusters (2 semanas – 1 año), por GPU/hora:** B200 $9,86 (16 GPUs) / $9,36 (64) / $8,87 (256+); H100 $6,16 (16) / $5,85 (64) / $5,54 (256). El tramo "1 year+" aparece sin precio. Ver [[2026-1031-lambda-b200-cluster-precio-por-gpu-hr-segun-tamano]] y [[2026-1101-lambda-cluster-h100-precio-por-gpu-hr-segun-tamano]].

**Corrección relevante para el eje coste-por-asiento vs coste-por-infraestructura:** con estas cifras, el cloud GPU queda **muy por encima** del presupuesto duro de ≤ €4/mes del vault — incluso la GPU más barata del catálogo (Quadro RTX 6000 a $0,69/GPU-hora) son ~$504/mes a 24/7, y un H100 1x a $4,29/GPU-hora son ~$3.132/mes (ver [[2026-1101-lambda-presupuesto-4-euros-ordena-de-magnitud-gpu]]). La conclusión que este átomo sostiene se afila: la facturación por uso de Lambda **no vuelve el coste marginal**, lo reescala a un orden de magnitud que el modelo de coste por asiento de [[2026-1022-costes-por-categoria-tenant]] no puede absorber sin cambiar el precio de los planes.

**Fricción pendiente con esta misma nota:** la afirmación del átomo sobre "per-second GPU allocation with minute-level billing" **no aparece en ninguna de las tres capturas** — la página solo publica "PRICE/GPU/HR" y la nota "+ plus applicable sales tax/VAT/GST". La fricción está planteada en [[2026-1031-lambda-instancias-8x-precio-por-gpu-hr]] y **no se auto-resuelve aquí**.
---
id: 2026-1031-lambda-instancias-8x-precio-por-gpu-hr
type: atom
certainty: solid
sources: [sources/2026-10-31-lambda-gpu-pricing.md, sources/2026-11-01-lambda-gpu-pricing.md]
links: ["[[2026-1031-lambda-gpu-pricing]]", "[[2026-1023-hetzner-facturacion-por-hora-0-0096]]", "[[2026-1023-hetzner-costes-por-categoria-vs-infraestructura-propia]]"]
---

## Claim
La tabla de "Instances pricing" de Lambda para el tamaño **8x** publica precios **por GPU y hora**: NVIDIA B200 SXM6 **$6,69** (180 GB VRAM, 208 vCPU, 2900 GiB RAM, 22 TiB SSD), H100 SXM **$3,99** (80 GB, 208 vCPU, 1800 GiB, 22 TiB), A100 SXM 80 GB **$2,79** (240 vCPU, 1800 GiB, 19,5 TiB), A100 SXM 40 GB **$1,99** (124 vCPU, 1800 GiB, 5,8 TiB) y Tesla V100 **$0,79** (16 GB, 88 vCPU, 448 GiB, 5,8 TiB). El precio es por GPU, así que una instancia 8x de H100 cuesta **$31,92/hora** y una 8x de V100 **$6,32/hora**.

## Why It Matters
Este es el dato base para dimensionar la alternativa "GPU cloud" del vault: a $3,99/GPU-hora, una sola instancia 8x de H100 son **$31,92/hora ≈ $23.301/mes** funcionando 24/7, frente al presupuesto duro de ≤ €4/mes de infraestructura ([[2026-1023-hetzner-costes-por-categoria-vs-infraestructura-propia]]). También marca la diferencia de modelo de facturación frente al VPS del corpus: Lambda factura **por hora de GPU asignada**, no por mes ni por asiento, igual que el cómputo por uso de Hetzner a $0,0096/h ([[2026-1023-hetzner-facturacion-por-hora-0-0096]]) pero con tres órdenes de magnitud de diferencia en la tarifa.

## [FRICTION]
> [[2026-1031-lambda-gpu-pricing]] afirma que "Lambda GPU pricing is per-second GPU allocation with minute-level billing".
> Las tres capturas de `lambda.ai/pricing` **no mencionan en ningún punto la facturación por segundo**: la página publica exclusivamente una columna "PRICE/GPU/HR" y declara "+ plus applicable sales tax/VAT/GST". La granularidad por segundo/minuto puede existir en la documentación o en la consola, pero no está en esta fuente.
> Ambas no pueden ser simultáneamente la misma afirmación: o el átomo previo se apoyó en otra página de Lambda (docs, instancia), o la granularidad de billing no es verificable en la página de precios. Marcado para juicio humano, no auto-resuelto.

## Nota de extensión 2026-11-03
Cifras verbatim de la pestaña 8x de `sources/2026-10-31-lambda-gpu-pricing.md` y de `sources/2026-11-01-lambda-gpu-pricing.md`. El desglose 8 × precio unitario es aritmética sobre la columna publicada.

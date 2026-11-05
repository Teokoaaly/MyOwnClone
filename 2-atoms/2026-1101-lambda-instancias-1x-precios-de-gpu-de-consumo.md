---
id: 2026-1101-lambda-instancias-1x-precios-de-gpu-de-consumo
type: atom
certainty: solid
sources: [sources/2026-11-01-lambda-gpu-pricing.md]
links: ["[[2026-1031-lambda-instancias-8x-precio-por-gpu-hr]]", "[[2026-1101-lambda-presupuesto-4-euros-ordena-de-magnitud-gpu]]", "[[2026-1022-gap-dify-como-capa-inferencia-prompts]]"]
---

## Claim
La pestaña **1x** de la tabla de Instances de Lambda —la que multiplica por 1 el conteo de GPUs y por tanto la de menor coste— publica el catálogo más barato del proveedor: **NVIDIA Quadro RTX 6000 $0,69/GPU-hora (24 GB, 14 vCPU, 46 GiB, 512 GiB SSD), A6000 $1,09 (48 GB, 14 vCPU, 100 GiB), A10 $1,29 (24 GB, 30 vCPU, 226 GiB), GH200 $2,29 (96 GB, 64 vCPU, 432 GiB, 4 TiB SSD), H100 PCIe $3,29 y H100 SXM $4,29**, frente a los $3,99/$4,19/$4,29 que cuestan los H100 SXM en 8x/4x/2x. La GPU más barata del catálogo completo cuesta $0,69/GPU-hora.

## Why It Matters
Este es el suelo real del catálogo y el dato que hace comparables las cifras grandes: **el "GPU cloud barato" de Lambda es un Quadro RTX 6000 de 24 GB a $0,69/hora**, no un H100. Para el vault, que baraja inferencia local como alternativa a depender de APIs, la consecuencia es que el precio de GPU no está en la GPU que se sueña (H100/B200) sino en la cola barata: A6000 de 48 GB a $1,09/hora es la opción con VRAM útil para un modelo de tamaño medio, y su coste sigue estando dos órdenes de magnitud por encima del presupuesto del vault. La lista también revela el criterio técnico que la captura no declara: **en 1x, la GPU cara (H100 SXM $4,29) queda por encima de la GH200 ($2,29) y de la A10 ($1,29)**, es decir, la jerarquía de precio en 1x no es solo por VRAM.

## Nota de extensión 2026-11-03
Cifras verbatim de la cuarta tabla (pestaña 1x) de `sources/2026-11-01-lambda-gpu-pricing.md`. Esta tabla completa **no aparece** en las capturas del 2026-10-31 ni del 2026-11-02.

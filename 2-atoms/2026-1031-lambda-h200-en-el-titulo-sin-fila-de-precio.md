---
id: 2026-1031-lambda-h200-en-el-titulo-sin-fila-de-precio
type: atom
certainty: solid
sources: [sources/2026-10-31-lambda-gpu-pricing.md, sources/2026-11-01-lambda-gpu-pricing.md]
links: ["[[2026-1031-lambda-gpu-pricing]]", "[[2026-1024-hostkey-tres-tipos-vps-vds-y-vds-con-gpu]]"]
---

## Claim
El título de la página de precios de Lambda anuncia explícitamente *"GPU cloud pricing: rent NVIDIA H100, H200, and B200"*, pero **ninguna de las tres capturas de la página contiene una fila de precio para H200**: la tabla de 1-Click Clusters solo lista HGX B200 y H100, y la tabla de Instances solo lista B200 SXM6, H100 SXM, H100 PCIe, A100, A6000, A10, GH200, Quadro RTX 6000 y Tesla V100. Lo más cercano a H200 en el catálogo es **GH200 (Grace Hopper) a $2,29/GPU/hora en instancias 1x**, que es una GPU de arquitectura distinta (CPU Grace integrada).

## Why It Matters
Para el vault esto importa como señal de calidad de catálogo, no como dato de precio: la portada de marketing de un proveedor puede anunciar hardware que su propia tabla de precios no publica, y buscar "H200" en la página no produce ninguna cifra. Es el mismo criterio de verificación que el vault ya aplica a otras capturas del corpus (p. ej. las que declaran stock, SLA o specs sin cifras: [[2026-1024-hostkey-tres-tipos-vps-vds-y-vds-con-gpu]]). Regla operativa: **el catálogo efectivo es el de la tabla, no el del título**. La discrepancia H200-vs-GH200 es además un buen ejemplo de por qué no se debe inferir equivalencia entre "H200" (título) y "GH200 $2,29" (tabla): son chips distintos.

## Nota de extensión 2026-11-03
Verificado contra `sources/2026-10-31-lambda-gpu-pricing.md` (título) y `sources/2026-11-01-lambda-gpu-pricing.md` (tabla completa de instancias de 1x/2x/4x/8x: ninguna fila H200).

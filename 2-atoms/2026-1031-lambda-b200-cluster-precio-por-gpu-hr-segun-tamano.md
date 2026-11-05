---
id: 2026-1031-lambda-b200-cluster-precio-por-gpu-hr-segun-tamano
type: atom
certainty: solid
sources: [sources/2026-10-31-lambda-gpu-pricing.md, sources/2026-11-01-lambda-gpu-pricing.md, sources/2026-11-02-lambda-gpu-pricing.md]
links: ["[[2026-1101-lambda-cluster-h100-precio-por-gpu-hr-segun-tamano]]", "[[2026-1031-lambda-gpu-pricing]]", "[[2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados]]"]
---

## Claim
El precio por GPU/hora de los clusters **NVIDIA HGX B200** de Lambda baja escalonadamente con el tamaño del cluster en el tramo "2 weeks – 1 year": **$9,86 con 16 GPUs, $9,36 con 64 GPUs y $8,87 con 256+ GPUs** — un descuento de volumen de aproximadamente **10 %** entre el cluster más pequeño y el más grande de la tabla. La fila "1 year+" aparece para 16+ GPUs pero **sin cifra de precio**.

## Why It Matters
Es el único caso documentado en el vault donde un proveedor de GPU aplica un **descuento por escala explícito y cuantificado** en el mismo producto, y el tamaño del descuento (10 %) es modesto: multiplicar la capacidad no reduce el precio unitario de forma estructural, solo lo aplana. Esto importa al comparar con el eje de hosting barato del vault (cf. [[2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados]]): en el mercado de GPU, el salto de 16 a 256 GPUs sigue dejando la unidad en un orden de magnitud que ningún VPS del corpus se acerca. También fija el suelo de la oferta de Lambda para cualquier comparación posterior: **$8,87/GPU/hora es el mejor precio unitario publicado para B200 en toda la página**, y corresponde a un cluster de 256+ GPUs cuyo coste horario total es de $2.270,72 (256 × 8,87).

## Nota de extensión 2026-11-03
Cifras verbatim de la tabla "NVIDIA HGX B200 systems" de `sources/2026-10-31-lambda-gpu-pricing.md`, idénticas en las capturas del 2026-11-01 y del 2026-11-02. El porcentaje de descuento (10 %) es aritmética sobre esas cifras, no una frase de la fuente.

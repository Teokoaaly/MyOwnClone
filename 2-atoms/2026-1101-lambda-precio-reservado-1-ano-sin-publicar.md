---
id: 2026-1101-lambda-precio-reservado-1-ano-sin-publicar
type: atom
certainty: solid
sources: [sources/2026-11-01-lambda-gpu-pricing.md, sources/2026-10-31-lambda-gpu-pricing.md]
links: ["[[2026-1101-lambda-dos-lineas-de-producto-instances-y-clusters]]", "[[2026-1031-lambda-b200-cluster-precio-por-gpu-hr-segun-tamano]]", "[[2026-1031-lambda-gpu-pricing]]"]
---

## Claim
La página de precios de Lambda publica el tramo **"2 weeks – 1 year"** con cifras para los tres tamaños de cada GPU (16, 64, 256+), y añade una fila **"1 year+" para 16+ GPUs con la columna PRICE/GPU/HR en blanco ("—")** en las tablas de B200 y de H100, con CTA "Talk to our team" en lugar de un enlace de cluster. La cabecera añade: *"Contact us for reserved capacity at our lowest prices."*

## Why It Matters
Es el punto donde el catálogo deja de ser verificable: el compromiso más largo es el que tiene mejor precio ("our lowest prices"), y **ese precio no está publicado**. La consecuencia para el vault es que cualquier comparación de coste de GPU a partir de esta fuente está sistemáticamente sesgada al alza: solo se puede calcular el tramo de 2 semanas a 1 año, y el tramo que de verdad usa un cliente de training (1 año o más) queda fuera de la evidencia. Esto refuerza la regla ya aplicada en el corpus de no rellenar huecos con cifras plausibles: el hueco de la fila "1 year+" queda documentado como hueco, no estimado.

## Nota de extensión 2026-11-03
Filas "1 year+" con precio "—" verbatim en `sources/2026-11-01-lambda-gpu-pricing.md` (tablas B200 y H100) y en `sources/2026-10-31-lambda-gpu-pricing.md` (tabla B200).

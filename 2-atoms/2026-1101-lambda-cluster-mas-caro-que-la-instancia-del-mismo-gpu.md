---
id: 2026-1101-lambda-cluster-mas-caro-que-la-instancia-del-mismo-gpu
type: atom
certainty: tentative
sources: [sources/2026-11-01-lambda-gpu-pricing.md]
links: ["[[2026-1101-lambda-cluster-h100-precio-por-gpu-hr-segun-tamano]]", "[[2026-1031-lambda-b200-cluster-precio-por-gpu-hr-segun-tamano]]", "[[2026-1031-lambda-instancias-8x-precio-por-gpu-hr]]"]
---

## Claim
Para el mismo GPU, el precio por GPU/hora en 1-Click Clusters es **sensiblemente más caro que en Instances**: B200 a $9,86 (cluster 16 GPUs) frente a $6,69 (instancia 8x), y H100 a $6,16 frente a $3,99 — un sobreprecio de aproximadamente **+47 % en B200 y +54 % en H100** a favor de la instancia self-serve.

## Why It Matters
Desmonta la intuición de que "reservar capacidad es más barato" en Lambda: en la página de precios el formato de cluster es el caro, no el barato. La propia página lo dice al revés ("Contact us for reserved capacity at our lowest prices"), lo que sugiere que el precio de cluster publicado es de lista y el de capacidad reservada negociada es otro, no publicado. Para el vault la conclusión es simple y accionable: **si alguien del vault quisiera GPU, el punto de entrada barato es una instancia self-serve de 1x/8x, no un cluster de 16 GPUs**, y aun así el orden de magnitud queda fuera del presupuesto de ≤ €4/mes.

## Nota de extensión 2026-11-03
Los porcentajes (+47 %, +54 %) son aritmética sobre cifras verbatim de `sources/2026-11-01-lambda-gpu-pricing.md` (tablas de 1-Click Clusters y de Instances 8x). La comparación no es una frase de la fuente, y la página no explica qué incluye el sobreprecio (red, orquestación, soporte), por lo que `certainty: tentative`.

---
id: 2026-1101-lambda-precio-sube-al-encoger-la-instancia
type: atom
certainty: solid
sources: [sources/2026-11-01-lambda-gpu-pricing.md]
links: ["[[2026-1101-lambda-recurso-por-gpu-casi-constante-entre-tamanos]]", "[[2026-1031-lambda-instancias-8x-precio-por-gpu-hr]]", "[[2026-1031-lambda-b200-cluster-precio-por-gpu-hr-segun-tamano]]"]
---

## Claim
En Instances, el precio **por GPU/hora sube al encoger la instancia**: el H100 SXM pasa de **$3,99 en 8x** a $4,09 en 4x, $4,19 en 2x y **$4,29 en 1x** (+7,5 % frente al 8x), y el B200 SXM6 de $6,69 en 8x a $6,79/$6,89/**$6,99** en 4x/2x/1x (+4,5 %). En cambio el A100 SXM 40 GB es plano a **$1,99** en los cuatro tamaños y el A6000 a **$1,09**, igual que la H100 PCIe a $3,29 en 1x.

## Why It Matters
Es el reverso exacto del descuento por escala de los clusters: allí crecer baja el precio unitario (de $9,86 a $8,87 en B200, [[2026-1031-lambda-b200-cluster-precio-por-gpu-hr-segun-tamano]]); aquí encoger lo sube. La consecuencia operativa para el vault es que **la instancia grande es la forma barata de comprar GPU por hora en el catálogo self-serve**, pero solo por el mismo modelo de GPU: el 8x de H100 es un 7,5 % más barato por GPU que el 1x. Y el contraste entre las dos families de GPU es instructivo: la prima por H100/B200 es un sobreprecio fijo que se **diluye** al comprar en volumen, mientras que A100 y A6000 no tienen prima ninguna.

## Nota de extensión 2026-11-03
Cifras verbatim de las cuatro tablas de Instances de `sources/2026-11-01-lambda-gpu-pricing.md`; los porcentajes son aritmética sobre esas cifras.

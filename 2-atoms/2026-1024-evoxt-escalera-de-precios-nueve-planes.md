---
id: 2026-1024-evoxt-escalera-de-precios-nueve-planes
type: atom
certainty: solid
sources: [sources/2026-10-23-evoxt-vps-pricing.md]
links: ["[[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]]", "[[2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados]]", "[[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]", "[[2026-1024-evoxt-dos-precios-distintos-para-el-mismo-plan]]"]
---

## Claim
El catálogo de VPS de Evoxt tiene **nueve planes** con esta escalera de precio y specs: **VM-0.5 $2.99** (1 vCore / 512 MB / 5 GB), **VM-0.75 $4.99** (1 / 1 GB / 10 GB), **VM-1 $5.99** (1 / 2 GB / 20 GB), **VM-1.5 $6.95** (2 / 2 GB / 20 GB), **VM-2 $11.99** (2 / 4 GB / 30 GB), **VM-3 $14.99** (4 / 4 GB / 30 GB), **VM-4 $23.99** (4 / 8 GB / 60 GB), **VM-6 $29.99** (8 / 8 GB / 60 GB) y **VM-8 $47.99** (8 / 16 GB / 80 GB). El rango va de $2.99 a $47.99, un factor **×16,06**, y los saltos más baratos son **+$0.96** para pasar de 1 a 2 vCore (VM-1 → VM-1.5) y **+$3.00** para pasar de 2 a 4 vCore (VM-2 → VM-3).

## Why It Matters
Es la contraparte de la escalera de Hetzner que el vault ya tiene documentada ([[2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados]]), pero con una forma de escalado distinta: allí el salto de precio grande venía de cruzar de recursos compartidos a vCPU dedicadas (**×6.70**); aquí **el número de vCore se puede doblar por menos de un dólar** ($5.99 → $6.95) o por tres dólares ($11.99 → $14.99), y lo que escala caro es la **RAM** (16 GB solo en VM-8, a $47.99). Ese es un punto relevante para [[myownclone]]: el recurso que el stack multi-tenant consume de verdad —memoria para Postgres, Redis y concurrencia de streaming SSE— es el que se paga, mientras que los vCore se regalan a precios casi simbólicos. La lógica de "compartido vs dedicado" que el vault usa como criterio de compra ([[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]) no aplica aquí: todos los planes son vCPU dedicados y el criterioPublished es la memoria.

## Nota de verificación
Precios y specs transcritos literalmente de la tabla "Plans". La página **no** publica ancho de banda incluido, SLA, región por plan, ni periodicidad del precio (la captura no indica "per month"). La etiqueta "Industry Leading Single Core CPU Performance" es el argumento de cabecera de esa misma página.

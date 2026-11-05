---
id: 2026-1101-lambda-recurso-por-gpu-casi-constante-entre-tamanos
type: atom
certainty: solid
sources: [sources/2026-11-01-lambda-gpu-pricing.md]
links: ["[[2026-1101-lambda-precio-sube-al-encoger-la-instancia]]", "[[2026-1031-lambda-instancias-8x-precio-por-gpu-hr]]", "[[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]"]
---

## Claim
En las cuatro pestañas de tamaño de Instances (8x / 4x / 2x / 1x), Lambda mantiene **prácticamente constante el recurso por GPU**: B200 SXM6 ofrece siempre 26 vCPU, ~360 GiB de RAM y 2,75 TiB de SSD SSD por GPU (208/2900/22 en 8x; 104/1440/11 en 4x; 52/720/5,5 en 2x; 26/360/2,75 en 1x), y H100 SXM siempre 26 vCPU, 225 GiB y 2,75 TiB por GPU. A100 SXM 40 GB mantiene 30 vCPU y 225 GiB por GPU en todos los tamaños; Tesla V100 ofrece 11 vCPU y 56 GiB por GPU.

## Why It Matters
Significa que **cambiar de 8x a 1x no cambia la densidad de la máquina, solo su cantidad**: la instancia 1x de B200 es la misma máquina que la 8x divided por ocho. Eso tiene una lectura directa para el vault: si MyOwnClone necesitara GPU para inferencia, la decisión no es "qué GPU" sino "cuánta"; y como el recurso por GPU es constante, la economía del renting es enteramente lineal en número de GPUs, sin Economías de escala de hardware. Es el mismo criterio de granularidad que el vault ya usa para saltar de compartido a dedicado ([[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]), pero aquí el eje es multiplicador de GPU.

## Nota de extensión 2026-11-03
Ratios calculados a partir de las cuatro tablas de Instances de `sources/2026-11-01-lambda-gpu-pricing.md` (columnas VRAM/GPU, vCPUs, RAM, STORAGE). La constancia del ratio es una lectura de la tabla, no una frase de la fuente.

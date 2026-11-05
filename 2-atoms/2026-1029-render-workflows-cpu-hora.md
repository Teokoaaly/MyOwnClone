---
id: 2026-1029-render-workflows-cpu-hora
type: atom
certainty: solid
sources: [sources/2026-10-29-render-pricing.md]
links: ["[[2026-1029-render-cron-por-minuto]]", "[[2026-1029-render-compute-per-second]]", "[[2026-1022-gap-workflows-myownclone]]"]
---

## Claim
Render Workflows se cobra por hora activa de CPU y de memoria: $0,20 por CPU-hora activa más $0,05 por GB-hora activa de memoria (hasta 1 CPU, 4 GB de RAM), $0,40/hora en 2c-4g, $0,70/hora en 2c-8g, $1,00/hora en 4c-8g y $2,50/hora en 8c-32g; el producto permite hasta 10.000 CPU y 40.000 GB de RAM de cómputo paralelo, con un techo por workflow de 8 CPU y 32 GB.

## Why It Matters
Workflows es el primitive que Render ofrece para ejecución durable con reintentos automáticos, sub-second spin-up y cómputo paralelo masivo: es exactamente la pieza que [[2026-1022-gap-workflows-myownclone]] describe como ausente en MyOwnClone. El modelo de precio importa porque es por uso real (hora activa), no por asiento: una orquestación de onboarding de 30 segundos en 1 CPU con 4 GB cuesta ~$0,0033, y el mismo trabajo repetido 10.000 veces al mes cuesta ~$33. Frente al cron por minuto de [[2026-1029-render-cron-por-minuto]], la diferencia no es el precio sino la semántica: el cron es un disparo, el workflow conserva estado, reintenta y escala. Para el eje del vault —coste por asiento frente a coste de infraestructura— este es el patrón que empuja el gasto hacia el uso real del cliente, no hacia el número de usuarios.

## [FRICTION]
> No conflicting atom found. This is a pricing atom for a product line with no prior atom in the vault. No [FRICTION] block added.

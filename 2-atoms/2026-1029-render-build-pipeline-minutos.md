---
id: 2026-1029-render-build-pipeline-minutos
type: atom
certainty: solid
sources: [sources/2026-10-29-render-pricing.md]
links: ["[[2026-1029-render-planes-pro-scale]]", "[[2026-1029-render-compute-per-second]]", "[[2026-1022-myownclone-dos-repos-flask-nextjs]]"]
---

## Claim
Render descuenta minutos de pipeline de build según el plan: Hobby incluye 500 min/mes y luego $5 por cada 1.000 min, Pro incluye 1.000 min/mes y Scale 5.000 min/mes por workspace, con el mismo recargo de $5 por 1.000 min; el "Performance pipeline" es un add-on de Pro y Scale a $25 por 1.000 min.

## Why It Matters
Para MyOwnClone, con dos repos (Flask y Next.js, ver [[2026-1022-myownclone-dos-repos-flask-nextjs]]), el pipeline de build no es un detalle: cada despliegue de Next.js 16 con NextAuth consume minutos de compilación. En Hobby, 500 min/mes cubren unos pocos despliegues completos y el excedente se cobra a $5 por 1.000 min, lo que es barato comparado con el cómputo, pero añade una cuarta partida de coste variable al modelo. Lo relevante para el eje del vault es que Render cobra el build con la misma granularidad por uso que el cómputo ([[2026-1029-render-compute-per-second]]): el coste de la infraestructura crece con la frecuencia de despliegue, no con el número de tenants, lo que refuerza el argumento de que el TCO de un SaaS lo domina el gasto por uso y no el asiento.

## [FRICTION]
> No conflicting atom found. This is a metering atom with no direct contradiction in the current vault. No [FRICTION] block added.

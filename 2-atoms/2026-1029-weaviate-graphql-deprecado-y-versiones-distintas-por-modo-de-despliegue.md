---
id: 2026-1029-weaviate-graphql-deprecado-y-versiones-distintas-por-modo-de-despliegue
type: atom
certainty: solid
sources: [sources/2026-10-29-weaviate-deployment-options.md]
links: ["[[2026-1029-weaviate-seis-vias-de-despliegue-y-cual-aplica-al-vps]]", "[[2026-1029-weaviate-self-hosted-misma-base-de-datos-que-weaviate-cloud]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]"]
---
## Claim
Dos avisos de ciclo de vida que la documentación de despliegue de Weaviate publica de forma explícita: (1) **"The GraphQL API is deprecated and will be switched off on Weaviate Cloud on May 1, 2027"**, con guía de migración aparte; (2) **"Weaviate version availability may differ across deployment options, Weaviate Cloud generally has the latest versions of all deployment methods"** — es decir, **la versión disponible depende del modo de despliegue**, y la de la instancia autoalojada puede ir por detrás. La fuente añade además que las imágenes *release candidate* y otro software no liberado **no tienen soporte** y no deben usarse en producción.

## Why It Matters
La fecha **1 de mayo de 2027** es una deuda con plazo fijo que hay que anotear en el roadmap antes de que aparezca, y afecta al camino de migración (GraphQL → gRPC/REST) tanto si se usa Cloud como si se usa self-hosted, porque el motor es el mismo ([[2026-1029-weaviate-self-hosted-misma-base-de-datos-que-weaviate-cloud]]). El segundo aviso es el riesgo operativo del self-hosting: **el autoalojo implica quedar en una versión anterior del motor que la vía gestionada ya actualizó**, es decir, el precio del "gratis" en licencia es un coste de mantenimiento en versiones y en avisos de seguridad que hay que operar. Para un producto que ya tiene su propio ciclo de despliegue en un VPS ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]), eso significa **una imagen más que actualizar y una versión que puede quedarse atrás sin avisar**.

## Nota de verificación
La fuente **no publica qué versión concreta de Weaviate queda congelada en cada modo de despliegue** ni el contenido de la guía de migración a GraphQL; solo enuncia la fecha de apagado y que Cloud va por delante.

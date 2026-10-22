---
id: 2026-1022-multi-tenant-slug-unpublished
type: atom
certainty: solid
sources: [raw/articles/myownclone-technical-research.md, raw/articles/myownclone-frontend-recon.md]
links: ["[[myownclone]]", "[[multi-tenant-saas]]", "[[2026-1022-superficie-oculta-robots-txt]]"]
---
## Claim
El modelo de multi-tenant de [[myownclone]] da a cada creador un slug con subdominio público `[slug].myownclone.com` que queda unpublished por defecto hasta que el creador publica, con dominio personalizado soportado pero no obligatorio y aislamiento entre tenants mencionado explícitamente en el aviso legal. El recon de i18n confirma que la URL pública del clon es `subdomain.myownclone.com` y que el dominio personalizado es una capacidad ya activa del producto.

## Why It Matters
El flag unpublished-by-default hace que un tenant recién creado no sea rastreable por enumeración de subdominios hasta que hay una acción explícita del creador. Es la implementación concreta del patrón [[multi-tenant-saas]] y explica por qué el listado DNS público del producto es corto. La confirmación de que el dominio personalizado ya está soportado (y no es roadmap) refuerza el posicionamiento de marca propia por tenant, y encaja con los prefijos públicos bloqueados en [[2026-1022-superficie-oculta-robots-txt]].

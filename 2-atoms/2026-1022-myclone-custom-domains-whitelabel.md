---
id: 2026-1022-myclone-custom-domains-whitelabel
type: atom
certainty: solid
sources: [raw/articles/myclone-deep-api-osint-2026-06-24.md, raw/articles/myownclone-osint-implementation-plan-2026-06-24.md]
links: ["[[2026-1022-myclone-widget-embed-modos]]", "[[2026-1022-myclone-competidor-arquitectura]]", "[[2026-1022-myclone-api-superficie-227-endpoints]]", "[[2026-1022-gap-custom-domains-campo-inactivo]]"]
---
## Claim
MyClone.is ofrece **whitelabel por dominio**: `GET,POST /api/v1/custom-domains`, `GET /custom-domains/lookup/{domain}` (público, sin auth), `GET,DELETE /custom-domains/{domain_id}` y `POST /custom-domains/{domain_id}/verify`. La verificación de dominio es el mecanismo que habilita servir el widget del clon bajo un dominio propio del creator.

## Why It Matters
El dominio propio es lo que convierte un widget genérico en el producto del creator: el visitante ve `clon.micreador.com`, no `app.myclone.is`. Es la diferencia entre "IA de una plataforma" y "el agente del creator".
[[2026-1022-myclone-widget-embed-modos]] documenta los modos de embed pero no el hecho de que el embed puede servirse en otro dominio. Para [[myownclone]], que ya da subdominio por tenant ([[2026-1022-multi-tenant-slug-unpublished]]), esto es una extensión natural: permitir `slug.mycliente.com` con verificación DNS en lugar de solo `[slug].myownclone.com`.

## Extensión (Plan de implementación 2026-06-24)
El plan añade el dato de **cuota por tier**: 10 dominios en plan pro, 10 en business y -1 (ilimitado) en enterprise. Es decir, los dominios propios son un recurso vendible y jerarquizado, no un extra universal. Del lado de [[myownclone]] el campo `custom_domain` ya existe en `CloneConfig` pero no se usa: falta verificación DNS, SSL y resolución del dominio en el serving del clon. Ver [[2026-1022-gap-custom-domains-campo-inactivo]].

---
id: 2026-1022-dns-superficie-publica-myownclone
type: atom
certainty: solid
sources: [raw/articles/myownclone-technical-research.md, raw/articles/myownclone-frontend-recon.md, raw/articles/myownclone-scrape_web-scrape.md]
links: ["[[myownclone]]", "[[multi-tenant-saas]]", "[[2026-1022-costes-por-categoria-tenant]]", "[[2026-1022-admin-rutas-bilingues-sin-subdominio]]", "[[2026-1022-mutaciones-rsc-sin-api-rest]]"]
---
## Claim
La superficie DNS pública de [[myownclone]] está confinada a la red 216.150.x.x con nueve subdominios (myownclone.com, api, app, admin, www, dashboard, support, status, docs) mapeados a un pool reducido de IPs, y en el momento de la consulta docs/status/dashboard devolvían 404 mientras admin requería autenticación. El recon de bundles añade un dato propio: **`admin.myownclone.com` no existe como subdominio con contenido propio** — el panel vive en `/admin` del dominio principal (ver [[2026-1022-admin-rutas-bilingues-sin-subdominio]]).
El scrape HTTP del 2026-05-25 acota el comportamiento de los tres subdominios públicos: `myownclone.com`, `app.myownclone.com` y `api.myownclone.com` resuelven todos por Vercel (sin CNAME/A visibles vía dig ANY) y devuelven **HTML idéntico**; `/admin` responde 200 redirigiendo a la home con autenticación, `/api/` devuelve 404 o 405, y `/embed/`, `/__t/` y `/c/` devuelven 404.

## Why It Matters
Reduce la superficie atacable observable a un solo host de Vercel y separa el panel de administración del resto. Es el punto de partida para cualquier evaluación de exposición técnica de [[myownclone]] y encaja con el modelo de aislamiento por tenant descrito en [[multi-tenant-saas]]. La equivalencia de los tres hosts (app/www/api sirven el mismo HTML) elimina la hipótesis de un backend separado y deja como única superficie real el mapa de rutas de [[2026-1022-admin-rutas-bilingues-sin-subdominio]].

## [FRICTION]
> El propio informe de esta nota listaba `admin` entre los nueve subdominios DNS de [[myownclone]].
> Esta nota presiona eso porque el recon de bundles no encuentra un subdominio admin operativo: el panel vive en `/admin` del dominio principal y `admin.myownclone.com` no sirve una app propia.
> Ambas no pueden ser exactamente correctas: o el registro DNS existe sin backend detrás (subdominio reservado), o el recon no lo consultó. Marcado para juicio humano, no auto-resuelto.

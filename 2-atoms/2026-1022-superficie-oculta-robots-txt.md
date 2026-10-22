---
id: 2026-1022-superficie-oculta-robots-txt
type: atom
certainty: solid
sources: [raw/articles/myownclone-frontend-recon.md, raw/articles/myownclone-scrape_web-scrape.md, raw/articles/myownclone-vulnerabilities-confirmed.md]
links: ["[[myownclone]]", "[[2026-1022-dns-superficie-publica-myownclone]]", "[[2026-1022-multi-tenant-slug-unpublished]]", "[[2026-1022-i18n-es-first-jurisdiccion-es]]"]
---
## Claim
El `robots.txt` de [[myownclone]] revela prefijos de superficie que no aparecen en el sitemap: además de `/admin` y `/api/`, bloquea `/embed/`, `/__t/` y `/c/`, además de los flujos de onboarding (`/registro/onboarding`, `/registro/exito`, `/en/signup/onboarding`, `/en/signup/success`). Las rutas públicas reales son solo landing, login, signup, contacto y seis páginas legales (`aviso-legal`, `privacidad`, `cookies`, `terminos`, `dpa`, `clon-terms` con sus equivalentes `/en/legal/*`).
El scrape del 2026-05-25 confirma que los prefijos bloqueados no exponen nada (`/embed/`, `/__t/`, `/c/` devuelven 404; `/api/` devuelve 404 o 405), y añade que el footer público enlaza las cinco páginas legales más `dpa` y `clon-terms`, con el Aviso Legal disponible solo en español (ver [[2026-1022-i18n-es-first-jurisdiccion-es]]).

## Why It Matters
Los prefijos bloqueados son la mejor pista residual sobre features no documentadas: `/embed/` sugiere un widget embebible (lo que el informe de MyClone.is sí expone públicamente), `/c/` sugiere rutas públicas por clon o por contexto, y `/__t/` un espacio técnico interno de plantillas o tracking. Todo esto es lo que distingue el modelo de slug público de [[2026-1022-multi-tenant-slug-unpublished]] de una simple landing, y corrige la lectura de la superficie DNS de [[2026-1022-dns-superficie-publica-myownclone]]: el riesgo real no está en los subdominios sino en los prefijos de ruta del host principal. La presencia de `dpa` y `clon-terms` también confirma que el producto se vende a empresas con departamentos legales, no solo a creadores.
La verificación de vulnerabilidades añade que la superficie pública se renderiza con redirecciones client-side (`/registro` descarga 260 KB antes de redirigir por `<meta http-equiv="refresh">`) y que la página 404 no lleva marca, es decir, la superficie pública está optimizada para capturar registros en lugar de proteger datos.

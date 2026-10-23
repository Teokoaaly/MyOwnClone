---
id: 2026-1022-live-verify-robots-sitemap-y-404-como-catchall
type: atom
certainty: solid
sources: [0-raw/archive/2026-10-23-2026-10-22-myownclone-live-reverification.md]
links: ["[[myownclone]]", "[[2026-1022-superficie-oculta-robots-txt]]", "[[2026-1022-api-privada-sin-documentacion]]", "[[2026-1022-live-verify-fuga-admin-cerrada-pero-queda-i18n]]"]
---

## Claim
[[myownclone]] sirve ahora una **ruta catch-all de slug único** que devuelve `HTTP 200` con la página de chat del clon para *cualquier* ruta de un solo segmento: `/admin`, `/pricing`, `/robots.txt`, `/sitemap.xml`, `/sitemap-0.xml` y `/zzz-random-99` devuelven todos 200 con el slug como `<h1>`, y el `<title>` genérico `YouOwnClone`. `robots.txt` y `sitemap.xml` ya no se sirven como texto/XML. Rutas de dos segmentos como `/legal/terminos` y `/admin/platform/tenants` sí devuelven el 404 real de Next.js (`404: This page could not be found.`). La plantilla del clon incluye los botones de modo `Learn` / `Support` / `Sales` y el string de guardarrail `"notEnoughInfo": "I don't have enough information to answer this question accurately. Would you like me to notify the team?"`.

## Why It Matters
Tiene dos consecuencias opuestas. Bueno: el error 404 canónico y el renderizado con slug hacen imposible enumerar o acceder a rutas internas por accidente — no hay fugas por rutas ocultas. Mal: **todo 404 de una sola palabra devuelve 200**, lo que rompe el contrato HTTP (códigos de estado para crawlers y para clientes), hace que `robots.txt` y `sitemap.xml` no existan para los buscadores, y significa que "el panel vive en /admin" era una lectura errónea de un catch-all. Para SEO y para el crawler del propio vault, esto importa.

## [FRICTION]
> [[2026-1022-superficie-oculta-robots-txt]] afirma que el `robots.txt` de [[myownclone]] "revela prefijos de superficie que no aparecen en el sitemap" — bloquea `/admin` y `/api/`, además de `/embed/`, `/__t/` y `/c/`, y de los flujos de onboarding — y que "las rutas públicas reales son solo landing, login, signup, contacto y seis páginas legales".
> Este átomo presiona esa creencia porque hoy no hay `robots.txt` que leer: la ruta devuelve la página de chat del clon con el slug `robots.txt` como encabezado. Lo que el átomo décritó como "superficie oculta" era, en la versión viva, indistinguible de cualquier otra ruta.
> Ambas no pueden ser completamente correctas: o el `robots.txt` real fue retirado en el redespliegue, o el 404 de mayo era en realidad el catch-all y nunca hubo tal archivo.
> Marcado para juicio humano, no auto-resuelto.

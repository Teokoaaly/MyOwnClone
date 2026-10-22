---
id: 2026-1022-onboarding-manual-sin-self-service
type: atom
certainty: solid
sources: [raw/articles/myownclone-scrape_web-scrape.md, raw/articles/myownclone-new-findings-may-2026.md]
links: ["[[myownclone]]", "[[2026-1022-beta-activo-trafico-real]]", "[[2026-1022-sin-pagina-precios-ni-docs]]"]
---
## Claim
El alta en [[myownclone]] no es self-service: `/registro` (y su equivalente `/en/signup`) hace meta-refresh a `/contacto`, de modo que el único camino para entrar es un formulario de contacto (Next.js Server Action, multipart/form-data) con honeypot anti-spam "website" y validación estricta (nombre 2-80 caracteres, email máx. 254, mensaje 20-3000 caracteres). El propio texto de portada declara que la beta entra "caso por caso": "de momento entramos caso por caso. Escríbenos contándonos el tuyo y vemos si encaja".

## Why It Matters
El lead es el cuello de botella del producto: no hay creación de cuenta, no hay trial público y no hay precio público, así que el primer dato que la empresa obtiene de un posible cliente es un mensaje escrito a mano. Eso hace comparables [[2026-1022-sin-pagina-precios-ni-docs]] y [[2026-1022-beta-activo-trafico-real]] y define el coste de adquisición como trabajo humano, no como producto.

## [FRICTION]
> [[2026-1022-beta-activo-trafico-real]] (escrita hace ~21 semanas) afirma que [[myownclone]] tiene signups, MRR, pagos fallidos y cancelaciones en el panel de tenants, es decir, onboarding self-service con facturación activa.
> Esta nota presiona eso porque el scrape del sitio público (misma fecha que la beta) confirma que `/registro` no crea cuenta: redirige a `/contacto` y el onboarding es manual, sin signup self-service accesible públicamente.
> Ambas no pueden ser completamente correctas: o el signup ocurre por una ruta interna no pública (panel de plataforma), o el MRR del panel proviene de clientes ya incorporados vía white-glove. Marcado para juicio humano, no auto-resuelto.

## Extensión (nuevos hallazgos, mayo 2026)
El análisis de bundles de la misma ronda **confirma el estado de beta cerrada**: `/registro` redirige a `/contacto` y la incorporación es manual caso por caso, pero documenta el funnel de alta tal como está implementado en el código — `/registro` → Stripe Checkout → `/registro/exito` (código mágico de 6 dígitos) → `/registro/onboarding`, con dos encuestas de origen y caso de uso (ver [[2026-1022-onboarding-cuatro-pasos-encuestas]]). El funnel existe y está instrumentado; lo que no hay es un acceso público al primer paso. Ver también [[2026-1022-auth-magic-link-codigo-seis-digitos]].

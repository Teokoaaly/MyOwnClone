---
id: 2026-1022-admin-rutas-bilingues-sin-subdominio
type: atom
certainty: solid
sources: [raw/articles/myownclone-frontend-recon.md, raw/articles/myownclone-vulnerabilities-confirmed.md]
links: ["[[myownclone]]", "[[multi-tenant-saas]]", "[[2026-1022-dashboard-de-insights]]", "[[2026-1022-beta-activo-trafico-real]]"]
---
## Claim
El panel de administración de [[myownclone]] vive en `/admin` del dominio principal (no existe subdominio `admin.myownclone.com`) y expone una malla de rutas App Router bilingües ES/EN donde cada sección tiene alias en español (`/admin/clon`, `/admin/cerebro`, `/admin/biblioteca`, `/admin/aprendizajes`, `/admin/productos`, `/admin/conversaciones`, `/admin/contactos`, `/admin/reuniones`, `/admin/inbox`, `/admin/uso`), con las secciones identity, brain, learning, products, meetings, inbox y usage<sub> desglosadas en subpáginas; `/admin` sin sesión redirige a `/login` con `NEXT_REDIRECT;replace;/login;307`.

## Why It Matters
Confirma que la superficie de administración está concentrada en un único host y no repartida en subdominios, lo que simplifica el modelo de aislamiento descrito en [[multi-tenant-saas]] pero también concentra el riesgo en un mismo origen. La duplicación ES/EN de cada ruta (p. ej. `/admin/identity/general` y `/admin/identidad/general`) muestra una internacionalización aplicada también al back-office, no solo al sitio público. El desglose de `/admin/learning` en audience, feedback, gaps y questions es la implementación de rutas de [[2026-1022-dashboard-de-insights]], y la existencia de `/admin/usage/plan` y `/admin/usage/invoices` es coherente con el estado de beta facturando de [[2026-1022-beta-activo-trafico-real]].
La verificación de seguridad del 2026-05-25 añade que la barrera de `/admin` no se aplica en servidor: la ruta devuelve HTTP 200 con el payload RSC del panel admin completo antes de un redirect `<meta http-equiv="refresh">` en cliente (ver [[2026-1022-admin-p2-fuga-codigo-panel-sin-auth]]).

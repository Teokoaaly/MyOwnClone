---
id: 2026-1022-auth-otp-impersonacion-30min
type: atom
certainty: solid
sources: [raw/articles/myownclone-technical-research.md, raw/articles/myownclone-frontend-recon.md]
links: ["[[myownclone]]", "[[multi-tenant-saas]]", "[[2026-1022-platform-admin-tenants-costes-mrr]]", "[[2026-1022-admin-rutas-bilingues-sin-subdominio]]"]
---
## Claim
El flujo de autenticación de [[myownclone]] combina login email/password con OTP para visitantes anónimos, y añade sesiones de suplantación (impersonation) con expiración de 30 minutos y audit log por tenant. El recon de bundles precisa el diseño: el operador entra por `/admin/platform/tenants` (búsqueda, orden, filtro), activa un modo explícito de soporte ("View as" / "Support mode") con banner rojo en pantalla y expiración automática de 30 minutos, y puede además invitar tenants o concederles planes desde la misma pantalla.

## Why It Matters
La impersonación es la función de mayor riesgo operativo de una plataforma multi-tenant: por eso el expiry de 30 min y el audit trail son la evidencia de un diseño de gobernanza, no un accidente. Es el control operativo central del panel de plataforma descrito en [[multi-tenant-saas]]. El banner rojo visible y el "View as" explícito (no silencioso) son mitigaciones de UX que reducen el riesgo de que un operador actúe creyendo que es el tenant — ver [[2026-1022-platform-admin-tenants-costes-mrr]] y el hecho de que no exista subdominio admin separado en [[2026-1022-admin-rutas-bilingues-sin-subdominio]].

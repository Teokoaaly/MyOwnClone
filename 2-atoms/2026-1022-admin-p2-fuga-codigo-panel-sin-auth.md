---
id: 2026-1022-admin-p2-fuga-codigo-panel-sin-auth
type: atom
certainty: solid
sources: [raw/articles/myownclone-vulnerabilities-confirmed.md]
links: ["[[myownclone]]", "[[2026-1022-admin-rutas-bilingues-sin-subdominio]]", "[[2026-1022-platform-admin-tenants-costes-mrr]]", "[[2026-1022-auth-otp-impersonacion-30min]]", "[[2026-1022-dns-superficie-publica-myownclone]]"]
---
## Claim
Una petición GET sin sesión a `/admin` de [[myownclone]] devuelve **HTTP 200 con 266.282 bytes de HTML** en el que el payload RSC ya contiene el código del panel de administración **antes** de cualquier redirección: el redirect se hace con `<meta http-equiv="refresh">` en cliente, no en servidor. Quedan expuestos los componentes `AdminPlatformTenants`, `AdminPlatformInbox`, `AdminPlatformResumen`, `AdminPlatformSpam`, `AdminPlatformFeedback` y `AdminImpersonationBanner`, con **81+ referencias** a features internas (tenant, stripe, brain, triage, templates, booking, labels, mrr, impersonate, spamDomain) y el vocabulario completo de estados de suscripción (active, trialing, past_due, unpaid, canceled, incomplete, complimentary, suspended, deleted). El mismo patrón de meta refresh en `/registro` hace descargar 260 KB para nada.

## Why It Matters
Es la Mayor fuga de superficie de [[myownclone]] verificada por curl el 2026-05-25: la barrera de autenticación del back-office no se aplica en servidor sino en cliente, así que el código del panel —incluido el de impersonación y gestión de tenants descrito en [[2026-1022-platform-admin-tenants-costes-mrr]] y [[2026-1022-auth-otp-impersonacion-30min]]— se descarga completo antes de que el navegador llegue a la pantalla de login. Un atacante automatizado no necesita ejecutar nada: basta con leer el HTML. Y como [[2026-1022-admin-rutas-bilingues-sin-subdominio]] ya había mapeado el panel en `/admin` del dominio principal, esta fuga aplica a toda la malla de rutas admin, no a un subdominio residual.

## [FRICTION]
> [[2026-1022-admin-rutas-bilingues-sin-subdominio]] afirma que "`/admin` sin sesión redirige a `/login` con `NEXT_REDIRECT;replace;/login;307`".
> Esta nota presiona eso porque la verificación directa del 2026-05-25 observa **HTTP 200 con 266.282 bytes** y un redirect `<meta http-equiv="refresh">` en cliente: el 307 con `NEXT_REDIRECT` no impide la descarga del código del panel.
> Ambas no pueden ser completamente correctas: o el 307 se aplica a rutas admin concretas y no a `/admin` raíz, o el comportamiento cambió entre el recon de bundles y la verificación con curl. Marcado para juicio humano, no auto-resuelto.

## [FRICTION]
> [[2026-1022-dns-superficie-publica-myownclone]] afirma que "`/admin` responde 200 redirigiendo a la home con autenticación".
> Esta nota presiona eso porque "200 con autenticación" no es lo que devuelve la verificación: el status 200 viene acompañado del HTML completo del panel admin sin sesión, no de una página de autenticación.
> Ambas no pueden ser completamente correctas: o la autenticación se resuelve en el cliente tras el meta refresh, o la caracterización "con autenticación" del scrape era una inferencia no verificada. Marcado para juicio humano, no auto-resuelto.

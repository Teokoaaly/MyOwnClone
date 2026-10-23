---
id: 2026-1022-live-verify-fuga-admin-cerrada-pero-queda-i18n
type: atom
certainty: solid
sources: [0-raw/archive/2026-10-23-2026-10-22-myownclone-live-reverification.md]
links: ["[[myownclone]]", "[[2026-1022-admin-p2-fuga-codigo-panel-sin-auth]]", "[[2026-1022-admin-rutas-bilingues-sin-subdominio]]", "[[2026-1022-mapa-modulos-internos-desde-bundles-js]]", "[[2026-1022-auth-otp-impersonacion-30min]]"]
---

## Claim
La fuga del panel de administración está **cerrada** en la versión viva: `GET /admin` sin sesión devuelve `HTTP 200` con 32.973 bytes cuyo `<title>` es `YouOwnClone` y cuyo `<h1>` es literalmente `admin` — es la página pública de chat del clon, servida por una ruta catch-all de slug único (`/pricing`, `/robots.txt` y `/zzz-random-99` devuelven la misma plantilla con su propio slug como encabezado). `grep 'AdminPlatform[A-Za-z]+'` no encuentra ninguna coincidencia: el código de los módulos `AdminPlatform*` ya no está en el bundle. Las subrutas reales de administración ahora aplican auth en servidor (`/admin/tenants` → `307` a `/login`) y todas las rutas del dashboard del creador (`/resumen`, `/cerebro`, `/biblioteca`, `/inbox`, `/productos`, `/reuniones`, `/analiticas`, `/facturacion`, `/configuracion`) → `307` a `/login`. **Lo que sí persiste**: el bundle i18n del cliente sigue enviando el namespace `admin` completo (238 cadenas) en las páginas de clon y en `/registro`, incluyendo el flujo de impersonación ("Copy this token and use it in the Authorization header to impersonate the tenant"), el `audit_log` ("Security and activity audit trail"), los `courtesy credits` y el vocabulario de planes y estados de suscripción. La landing `/` no lo lleva (`admin_ns=0`).

## Why It Matters
Resuelve la fricción nº11 y nº12 que el propio átomo de mayo declaraba irresoluble ("requiere re-verificación con curl"): el 307 con `NEXT_REDIRECT` es el comportamiento actual de las subrutas. Pero la corrección no es "todo arreglado": lo que se filtraba era el **código** del panel y ahora lo que se filtra es el **vocabulario** del panel. El mapa interno del back-office sigue siendo descargable sin sesión por cualquiera que abra una página de clon, aunque ahora en forma de etiquetas i18n en lugar de componentes.

## [FRICTION]
> [[2026-1022-admin-p2-fuga-codigo-panel-sin-auth]] afirma que `GET /admin` devuelve **HTTP 200 con 266.282 bytes** con el payload RSC de `AdminPlatformTenants`, `AdminPlatformInbox`, `AdminPlatformResumen`, `AdminPlatformSpam`, `AdminPlatformFeedback` y `AdminImpersonationBanner` antes de la redirección, con 81+ referencias a features internas; [[2026-1022-admin-rutas-bilingues-sin-subdominio]] afirma que `/admin` sin sesión redirige a `/login` con `NEXT_REDIRECT;replace;/login;307`.
> Este átomo presiona ambas creencias porque hoy `/admin` no devuelve ni el panel ni una redirección: devuelve la página de chat del clon con 33 KB, y no hay ni un solo `AdminPlatform*` en el bundle. El 307 sí existe, pero para `/admin/tenants`, no para `/admin` raíz.
> Ambas no pueden ser completamente correctas: o el panel se movió a otra ruta y ahora `/admin` cae al catch-all de clones, o la aplicación se reconstruyó. El catch-all que devuelve 200 para *cualquier* slug de un segmento es un diseño distinto del observado en junio.
> Marcado para juicio humano, no auto-resuelto.

## Extensión (re-verificación 2026-10-22, rutas del back-office)
El desglose de rutas de la versión viva muestra que el árbol **de plataforma** desapareció y el **de creador** se movió de prefijo: `/admin/tenants` → `307` a `/login`, pero `/admin/platform/tenants`, `/admin/clon` y `/admin/cerebro` devuelven **404**; `/dashboard` → `307` a `/resumen`, mientras que `/dashboard/resumen` devuelve **404**. La lectura conjunta es que el panel ya no vive bajo `/admin/*` sino bajo un conjunto de secciones sueltas (`/resumen`, `/cerebro`, `/biblioteca`, `/inbox`, `/productos`, `/reuniones`, `/analiticas`, `/facturacion`, `/configuracion`) que sin sesión redirigen a `/login`, y que la ruta `/admin` raíz quedó absorbida por el catch-all de slug. Es coherente con que `grep 'AdminPlatform[A-Za-z]+'` no encuentre ninguna coincidencia en el bundle actual.

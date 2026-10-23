---
id: 2026-1022-live-verify-csp-y-headers-ahora-presentes
type: atom
certainty: solid
sources: [0-raw/archive/2026-10-23-2026-10-22-myownclone-live-reverification.md]
links: ["[[myownclone]]", "[[2026-1022-ausencia-csp-xss-sin-mitigacion]]", "[[2026-1022-sin-headers-de-seguridad]]", "[[2026-1022-cors-wildcard-en-login-y-registro]]"]
---

## Claim
El hardening HTTP ausente en [[myownclone]] ha sido **implementado**: la verificación del 2026-10-22 observa dos políticas `Content-Security-Policy` (una permisiva con `script-src 'self' 'unsafe-inline' 'unsafe-eval' https:` y otra estricta en `/admin` y `/registro` con `script-src 'self' 'unsafe-inline' https:`, ambas con `object-src 'none'`, `base-uri 'self'`, `form-action 'self'` y `frame-ancestors 'none'`), más `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`, `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `Referrer-Policy: strict-origin-when-cross-origin` y `Permissions-Policy: camera=(), microphone=(), geolocation=()`. El CORS `access-control-allow-origin: *` ha desaparecido: con `Origin: https://evil.example`, `/login` y `/registro` no devuelven ninguna cabecera `access-control-allow-origin`.

## Why It Matters
Tres de los átomos de seguridad del lote describen un producto sin hardening alguno y los marcaban como `solid`. A día de hoy esa descripción es falsa. La prioridad nº2 y nº3 del thread de seguridad ("CSP como mínimo report-only" y "rate limiting") ya no aplica a la primera: está hecha. Queda pendiente solo el rate limiting.

## [FRICTION]
> [[2026-1022-ausencia-csp-xss-sin-mitigacion]] afirma que [[myownclone]] sirve "**cero** `Content-Security-Policy` en sus respuestas" y que la consecuencia reportada es XSS sin mitigación; [[2026-1022-sin-headers-de-seguridad]] afirma que faltan HSTS, X-Frame-Options, Referrer-Policy y Permissions-Policy; [[2026-1022-cors-wildcard-en-login-y-registro]] afirma `access-control-allow-origin: *` en `/login` y `/registro`.
> Este átomo presiona las tres creencias porque la medición del 2026-10-22 observa lo contrario en los tres puntos: CSP presente (dos veces), los cuatro headers de seguridad presentes, y cero cabeceras CORS.
> Ambas no pueden ser completamente correctas: o el hardening se implementó entre el 25 de mayo y el 22 de octubre de 2026, o se está midiendo un despliegue distinto del que se escaneó en mayo. Dado que el mismo corpus detecta un cambio de hosting a VPS nginx, la explicación más probable es que **todo el corpus OSINT describe una generación anterior del producto**.
> Marcado para juicio humano, no auto-resuelto.

## Extensión (re-verificación 2026-10-22, cookies)
No se observó ninguna cabecera `Set-Cookie` en la respuesta de `GET /login`. Es el único dato de cookie que la re-verificación aporta: el bundle ya no emite (o no emite en esa ruta) la cookie `NEXT_LOCALE` sin `HttpOnly`/`Secure` documentada en [[2026-1022-cookie-next-locale-sin-httponly-ni-secure]], lo que es coherente con que la ruta `/es` ya no altere el idioma (ver [[2026-1022-live-verify-identidad-legal-y-diseno-reconstruidos]]).

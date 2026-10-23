---
id: 2026-1022-live-verify-sin-rate-limiting-pero-con-cadena-de-error
type: atom
certainty: solid
sources: [0-raw/archive/2026-10-23-2026-10-22-myownclone-live-reverification.md]
links: ["[[myownclone]]", "[[2026-1022-sin-rate-limiting]]", "[[2026-1022-live-verify-superficie-rest-api-inexistente-antes]]", "[[2026-1022-live-verify-csp-y-headers-ahora-presentes]]"]
---

## Claim
El rate limiting sigue ausente en [[myownclone]] tras el redespliegue: doce peticiones consecutivas a `/login` devuelven doce `HTTP 200` y quince peticiones consecutivas a `/api/clones` devuelven quince `401`, sin ningún `429` ni bloqueo observable. El bundle sí contiene la cadena de error correspondiente — `"rateLimit": "Too many requests. Please wait a moment."` — y también `"errors": { "generic", "notFound", "unauthorized", "rateLimit" }`, lo que indica que la feature está implementada en la capa de cliente pero no activada en la de servidor, o que solo se aplica a otras rutas.

## Why It Matters
Es el único hallazgo de hardening de mayo que **sigue en pie** después de la re-verificación. Todo lo demás (CSP, headers, CORS) ya está arreglado; el rate limiting es el hueco que queda. Y hay un matiz nuevo: el chat público devuelve 404, así que el único objetivo alcanzable sin sesión son las rutas de login y registro — que es justamente donde el brute force y el abuso de magic link importarían.

## [FRICTION]
> [[2026-1022-sin-rate-limiting]] afirma que "[[myownclone]] no aplica rate limiting: diez peticiones rápidas consecutivas devolvieron todas HTTP 200, sin bloqueo, throttling ni respuesta 429".
> Este átomo **confirma** esa creencia en la versión viva, con 12 y 15 repeticiones respectivamente, y añade que la cadena de error `rateLimit` sí existe en el bundle.
> No hay conflicto real entre los dos: son la misma observación replicada cuatro meses después. Se registra aquí porque es la única de las ausencias de hardening que sobrevive al redespliegue, y porque la presencia del string sugiere que la feature existe pero no está conectada al enforcement.
> Marcado para juicio humano, no auto-resuelto.

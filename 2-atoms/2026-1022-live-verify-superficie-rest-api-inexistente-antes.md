---
id: 2026-1022-live-verify-superficie-rest-api-inexistente-antes
type: atom
certainty: solid
sources: [0-raw/archive/2026-10-23-2026-10-22-myownclone-live-reverification.md]
links: ["[[myownclone]]", "[[2026-1022-api-privada-sin-documentacion]]", "[[2026-1022-mutaciones-rsc-sin-api-rest]]", "[[2026-1022-stripe-webhook-confirmado]]", "[[2026-1022-pipeline-chat-actual-myownclone]]"]
---

## Claim
Existe ahora una superficie REST autenticada bajo `/api/` que no existía en el corpus de mayo: `GET /api/clones`, `GET /api/inbox` y `GET /api/clones/x/prompts` devuelven `401` con cuerpo JSON `{"error":"Unauthorized"}` — es decir, son rutas reales con auth, no 404. `GET /api/auth/session` devuelve `200`. Otras rutas probadas dan 404 HTML: `/api/analytics`, `/api/stripe`, `/api/admin`, `/api/tenant`, `/api/me`, `/api/health`, `/api/version`, `/api/myownclone`. `POST /api/webhooks/stripe` devuelve **404** (en mayo devolvía `405 Method Not Allowed`), y `POST /api/myownclone/public/clones/x/chat` sigue devolviendo **404**, lo que confirma que el bug conocido `myownclone_public_bp` no registrado continúa abierto.

## Why It Matters
La tesis de "cero superficie de API" que sostiene el thread comparativo y la atom `api-privada-sin-documentacion` era cierta en junio y es falsa hoy: hay al menos tres endpoints REST con JWT. Esto no cierra la brecha de paridad con los 227 endpoints de MyClone.is, pero cambia el tipo de la brecha: no es "no tenemos API", es "tenemos tres endpoints y no hay contrato público ni documentación". También confirma que el chat público —la función central del producto— sigue sin endpoint accesible.

## [FRICTION]
> [[2026-1022-api-privada-sin-documentacion]] afirma que "la API de [[myownclone]] es completamente privada: no existe docs.myownclone.com funcional ni ruta api.myownclone.com/public-api, y el producto no expone documentación pública de su API", y [[2026-1022-mutaciones-rsc-sin-api-rest]] afirma que "en los bundles analizados no aparecen endpoints REST" y que solo PostHog y Sentry son salidas a terceros.
> Este átomo presiona la parte estructural de ambas creencias: existen rutas REST propias bajo `/api/` con contrato JSON y código 401. La parte de "no hay documentación" sigue en pie: `docs.myownclone.com` no resuelve y no hay OpenAPI.
> La explicación más consistente es que **el corpus entero describe una generación anterior del producto** (mismo indicio que [[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]).
> Marcado para juicio humano, no auto-resuelto.

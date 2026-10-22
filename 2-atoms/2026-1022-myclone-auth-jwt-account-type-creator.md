---
id: 2026-1022-myclone-auth-jwt-account-type-creator
type: atom
certainty: solid
sources: [raw/articles/myclone-deep-api-osint-2026-06-24.md]
links: ["[[2026-1022-myclone-api-superficie-227-endpoints]]", "[[2026-1022-auth-otp-impersonacion-30min]]", "[[2026-1022-myclone-access-control-por-persona]]"]
---
## Claim
El login de MyClone.is (`POST /api/v1/auth/login`) devuelve `{message, user_id, token, account_type}` y el **JWT contiene el payload en claro** `{sub, email, fullname, account_type: "creator", exp}` — es decir, nombre y email del usuario viajan dentro del token sin cifrar. La cuenta de prueba usada en el OSINT estaba `FULLY_ONBOARDED`, con `email_confirmed: true` y `account_type: "creator"`.

## Why It Matters
El campo `account_type` confirma que la plataforma tiene **roles de usuario** (creator frente a otro tipo de cuenta), coherente con que exista un endpoint separado `POST /users/expert/onboarding` y con que los clones se publiquen bajo un `username` que los visitantes 'consumen' sin ser creators. Ese es el mismo eje de separación que en [[myownclone]] resuelve el rol de plataforma/admin con impersonation ([[2026-1022-auth-otp-impersonacion-30min]]): aquí el aislamiento es por rol y por acceso al clon, no por tenant.
Además, meter PII en el JWT (email, nombre completo) es una decisión de diseño observable: el token es autocontenido y portable, pero auditable por cualquier logarithmic del lado cliente.

## [FRICTION]
> [[2026-1022-myclone-api-rest]] (escrita hace unas horas) describe el patrón de llamada de MyClone.is como `Authorization: <token>` + `Content-Type: application/json` con envoltorio `{data, error}`, sin mencionar JWT ni la estructura del token.
> Este átomo presiona esa creencia porque el token es un JWT (no opaco) cuyo payload se decodifica sin clave, y porque el envoltorio `{data, error}` no aparece en la respuesta de login, que devuelve campos planos (`message`, `token`, `account_type`).
> Ambas no pueden ser completamente correctas: o la envoltura `{data, error}` es solo de los endpoints de datos y el login es la excepción, o la observación del payload indica un contrato distinto del inferido. Marcado para juicio humano, no auto-resuelto.

---
id: 2026-1026-heroku-soporte-tres-acciones-rapidas-general-query-reset-mfa-y-account-billing
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-support-home.md]
links: ["[[2026-1026-heroku-alta-en-signup-y-login-en-id-dominio-separado]]", "[[2026-1026-heroku-alta-sin-plan-ni-precio-ni-dyno-ni-verificacion-de-correo]]", "[[2026-1026-heroku-tres-variantes-de-privacy-por-region-y-consentimiento-de-marketing]]"]
---

## Claim
Bajo el título *"Welcome to Heroku Support"* la home ofrece **tres acciones de autoservicio, no un buscador genérico**: **"General query"**, **"Reset my MFA"** y **"Account & billing"**. La captura las reproduce como una fila contigua, sin más contexto. **"Reset my MFA" es una acción de primer nivel, no una sección enterrada**: el reset del segundo factor es una de las tres puertas del soporte. Arriba, la barra de navegación añade tres entradas más: **"My tickets"** (`help.heroku.com/tickets`), **"Create a ticket"** (`help.heroku.com/?t=true`) y **"Enterprise Resources"** (`help.heroku.com/enterprise`).

## Why It Matters
El vault ya tenía una anomalía sin explicar en el alta: el formulario de `signup.heroku.com` **no pide contraseña ni verificación de correo**, y el login vive en `id.heroku.com`, otro dominio ([[2026-1026-heroku-alta-en-signup-y-login-en-id-dominio-separado]]), sin ningún paso de verificación de correo en el flujo ([[2026-1026-heroku-alta-sin-plan-ni-precio-ni-dyno-ni-verificacion-de-correo]]). Esta captura deja claro que **la credencial de Heroku no la crea el alta**: la gestiona un proveedor de identidad en `id.heroku.com` y su **MFA se recupera desde la home de soporte**, entre dos acciones más.
Eso tiene consecuencia operativa directa para el thread de verificación y reventa: **el segundo factor de una cuenta Heroku es un activo recuperable por el proveedor y ligado a la facturación** ("Account & billing" es la tercera acción), es decir, **una cuenta comprada de segunda mano no es una cuenta desacoplada**: su MFA se resetea en el mismo mostrador donde se factura la suscripción.
El marco legal también encaja: ese mismo pie que declara el procesamiento de datos por Salesforce ([[2026-1026-heroku-tres-variantes-de-privacy-por-region-y-consentimiento-de-marketing]]) es el que opera el reset de credencial.

## [FRICTION]
> [[2026-1026-heroku-alta-en-signup-y-login-en-id-dominio-separado]] afirma que el alta **no crea la credencial**, porque el formulario no tiene campo de contraseña y el login está en `id.heroku.com`.
> Este átomo presiona esa afirmación en un punto: si el alta no crea la credencial y el soporte ofrece **"Reset my MFA"** en primer plano, entonces **existe una segunda superficie de creación/revocación de credenciales —la del mostrador de soporte— que el vault no tenía medida**. La captura no dice quién verifica al solicitante del reset, ni con qué criterio. Marcado para juicio humano, no auto-resuelto: no se puede saber si el reset exige verificación de identidad, si queda registrado, ni si es self-service real o una solicitud enrutada a un humano.

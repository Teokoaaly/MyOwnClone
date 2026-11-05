---
id: 2026-1026-heroku-lockout-de-cuenta-entre-los-cinco-articulos-mas-leidos
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-support-home.md]
links: ["[[2026-1026-heroku-alta-en-signup-y-login-en-id-dominio-separado]]", "[[2026-1026-heroku-soporte-tres-acciones-rapidas-general-query-reset-mfa-y-account-billing]]", "[[2026-1026-heroku-alta-protegida-por-recaptcha-enterprise-de-imagenes]]"]
---

## Claim
Uno de los **cinco** artículos de "Trending articles" de la home de soporte de Heroku es **"What should I do if I'm locked out of my Heroku account?"** (identificador `7IDU8QZZ`). Es decir, **el bloqueo de acceso a la cuenta es uno de los cinco problemas más frecuentes del soporte de un PaaS enterprise**. En paralelo, la home ofrece entre sus acciones de primer nivel un **"Reset my MFA"**, y entre sus enlaces de navegación un **"My tickets"** y un **"Enterprise Resources"** (`help.heroku.com/enterprise`).

## Why It Matters
El vault tiene, por separado, tres piezas que esta captura conecta: (1) el alta vive en `signup.heroku.com` y el login en `id.heroku.com`, otro dominio ([[2026-1026-heroku-alta-en-signup-y-login-en-id-dominio-separado]]); (2) el alta está protegida por un reCAPTCHA Enterprise de imágenes que **reemite el desafío** en lugar de aceptarlo ([[2026-1026-heroku-alta-protegida-por-recaptcha-enterprise-de-imagenes]]); (3) el soporte tiene una acción de primer nivel "Reset my MFA" ([[2026-1026-heroku-soporte-tres-acciones-rapidas-general-query-reset-mfa-y-account-billing]]). Esta captura añade el dato que faltaba: **el bloqueo de cuenta no es un incidente raro sino carga de soporte recurrente**, hasta el punto de tener su propio artículo entre los más leídos.
La consecuencia para el thread de reventa de cuentas es directa y dura: **una cuenta de infraestructura cuyo lockout es un top-5 de soporte y cuyo MFA se resetea en un mostrador no es un activo transferible**. La primera línea de defensa del titular de la cuenta es la que bloquea, y su desbloqueo pasa por el proveedor. Si la cuenta se ha revendido, el proceso de recuperación **no es propiedad del comprador**: es una petición al original.
Y hay un segundo efecto, ya medido en otros proveedores del vault: **el bloqueo es la palanca de Application Security que sirve de antidisturbios**. El mismo corpus que ofrece alta y reventa necesita poder cerrar cuentas ([[2026-1023-lzt-categoria-llm-accounts-para-reventa]]).

Nota: la captura **no** reproduce el artículo: no dice las causas del bloqueo, ni si hay verificación de identidad, ni si el desbloqueo es automático o por ticket.

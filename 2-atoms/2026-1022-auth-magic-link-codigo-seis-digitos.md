---
id: 2026-1022-auth-magic-link-codigo-seis-digitos
type: atom
certainty: solid
sources: [raw/articles/myownclone-new-findings-may-2026.md]
links: ["[[2026-1022-auth-otp-impersonacion-30min]]", "[[2026-1022-ia-y-auth-totalmente-servidor]]", "[[2026-1022-onboarding-manual-sin-self-service]]", "[[myownclone]]"]
---
## Claim
El método de autenticación principal de [[myownclone]] es el **magic link con código de 6 dígitos enviado por email**, con Google OAuth como alternativa; el código se pide tras el pago (paso "éxito" del registro) y el sistema reconoce al menos seis estados de error diferenciados: email inválido, código incorrecto, código caducado, Google cancelado, email no verificado, cuenta sin tenant y pago requerido.

## Why It Matters
Los estados de error son el contrato real del funnel: "cuenta sin tenant" y "pago requerido" solo tienen sentido si existe un camino de registro que crea una cuenta antes de que exista un tenant subscribed — es decir, la autenticación está diseñada para un alta self-service aunque la incorporación sea manual (ver [[2026-1022-onboarding-manual-sin-self-service]]). El magic link sin contraseña encaja con la arquitectura server-side descrita en [[2026-1022-ia-y-auth-totalmente-servidor]] y es la pieza de identidad que se combina con la impersonación de 30 minutos en [[2026-1022-auth-otp-impersonacion-30min]].

## [FRICTION]
> [[2026-1022-onboarding-manual-sin-self-service]] (escrita hace ~21 semanas) afirma que el alta en [[myownclone]] **no es self-service**: no hay creación de cuenta, y el único camino es un formulario de contacto con la beta entrando caso por caso.
> Este átomo presiona esa creencia porque el código implementa un flujo de registro completo (email + nombre + subdominio, Stripe Checkout, código mágico de 6 dígitos, onboarding) con estados de error que presuponen cuentas creadas sin intervención humana.
> Ambas no pueden ser completamente correctas: o el flujo de registro es código muerto/inerte mientras la beta esté cerrada, o el alta existe pero está oculta a propósito por el filtro de acceso. Marcado para juicio humano, no auto-resuelto.

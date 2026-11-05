---
id: 2026-1026-heroku-soporte-categoria-billing-verification-y-payments
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-support-home.md]
links: ["[[2026-1026-heroku-soporte-catorce-categorias-con-identificadores-numericos]]", "[[2026-1026-heroku-alta-protegida-por-recaptcha-enterprise-de-imagenes]]", "[[2026-1026-heroku-tres-variantes-de-privacy-por-region-y-consentimiento-de-marketing]]"]
---

## Claim
La home de soporte de Heroku incluye una categoría llamada exactamente **"Billing, Verification & Payments"** con identificador **`n/2`** — el segundo identificador más bajo de las 14 categorías, por detrás solo de "General Platform Features" (236). Es decir, **la verificación de cuenta no es un paso del alta sino un asunto de soporte permanente, con su propio espacio de preguntas frecuentes**. La home además expone un buscador que se etiqueta **"Ask Me Anything"** con un widget marcado **"HELLO"**, y el pie cierra con **"© 2026 Salesforce.com"**.

## Why It Matters
El vault tenía el alta de Heroku medida como un formulario con reCAPTCHA Enterprise y **sin verificación de correo, sin tarjeta y sin precio** ([[2026-1026-heroku-alta-sin-plan-ni-precio-ni-dyno-ni-verificacion-de-correo]]), y ahora aparece que **la verificación de la cuenta tiene categoría propia en el manual de soporte**. Eso reordena el coste de un alta: **no es el formulario lo que cuesta, es el proceso posterior** — el que resuelve si esa cuenta queda verificada para facturar. Es la misma observación que el vault ya tiene sobre NoOnes, donde "la identidad verificada ES la capacidad" ([[2026-1024-noones-verificacion-basica-l1plus-revision-manual-hasta-72h]]), pero aquí en el otro extremo: **Heroku no cobra por la verificación, la da por hecha y la sostiene con soporte humano**, porque su ingreso es la facturación del plan.
Y el detalle "© 2026 Salesforce.com" más el buscador "Ask Me Anything" confirman que el portal entero es **una instancia de producto de Salesforce**: el mismo proveedor que procesa los datos del alta ([[2026-1026-heroku-tres-variantes-de-privacy-por-region-y-consentimiento-de-marketing]]) y que opera el reset de MFA.

Nota: la captura **no** reproduce ninguna FAQ de esa categoría, ni enumera requisitos de verificación, ni publica plazos.

## [FRICTION]
> [[2026-1026-heroku-alta-sin-plan-ni-precio-ni-dyno-ni-verificacion-de-correo]] afirma que el alta de Heroku **no publica ninguna verificación**: ni de correo, ni de pago, ni de tarjeta, y que "lo único que separa el formulario del alta es el reCAPTCHA y los consentimientos legales".
> Este átomo presiona esa afirmación en un punto: **la propia home de soporte de Heroku mantiene una categoría entera llamada "Billing, Verification & Payments"** (`n/2`), es decir, **la verificación de la cuenta es un proceso vivo con FAQ propio, sostenido por soporte humano**, no una ausencia. Las dos cosas no pueden ser verdad a la vez, o el alta publica más de lo que la captura del formulario dejó ver (por ejemplo, un paso tras el "Verify" del reCAPTCHA que no se renderizó), o **la verificación es un proceso posterior al alta, gestionado por tickets y por un agente de identidad externo** (`id.heroku.com`). Marcado para juicio humano, no auto-resuelto: la captura del soporte **no** reproduce ninguna FAQ de esa categoría y no permite decidir entre las dos hipótesis.

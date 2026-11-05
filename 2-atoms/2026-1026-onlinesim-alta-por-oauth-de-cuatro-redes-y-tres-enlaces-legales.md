---
id: 2026-1026-onlinesim-alta-por-oauth-de-cuatro-redes-y-tres-enlaces-legales
type: atom
certainty: solid
sources: [sources/2026-10-25-onlinesim-virtual-sms.md]
links: ["[[2026-1023-5sim-smart-buy-y-tasa-entrega-visible]]", "[[2026-1024-noones-superficie-publica-productos-y-dominios-espejo]]", "[[2026-1023-5sim-catalogo-servicios-precios-y-stock]]"]
---

## Claim
La home ofrece **"Sign in with social networks"** con cuatro proveedores OAuth: **Google, Telegram, VK y Facebook** (el de Facebook es un `dialog/oauth` con `client_id=183708272263544`, `scope=email`, `redirect_uri=https://onlinesim.io/auth/oauth/facebook/callback`). Bajo el bloque de login aparece el texto de aceptación: "By logging into the service, you accept **Public offer**, **Personal data** And **Returns Policy**", con enlaces a `/documentation/offer`, `/documentation/privacy` y `/documentation/refund`.

## Why It Matters
El alta de OnlineSim es, estructuralmente, la más simple del corpus de proveedores de números: **cuatro redes sociales, sin correo, sin teléfono, sin KYC y sin tarjeta**. Es el reverso exacto de la escalera de NoOnes, donde la verificación documental es un producto con niveles L1 a L3 y una revisión manual de hasta 72 h ([[2026-1024-noones-superficie-publica-productos-y-dominios-espejo]]), y el reverso del funnel de 5sim, donde el alta exige cuenta y saldo ([[2026-1023-5sim-catalogo-servicios-precios-y-stock]]).
La consecuencia de seguridad es directa: **la identidad del cliente es la de su perfil social** —una identidad de Google o Telegram que puede ser una cuenta desechable— y el mismo perfil es la clave de acceso al histórico de números y códigos. Por eso el advice de "no vincular métodos de pago" del propio proveedor ([[2026-1026-onlinesim-reexpedicion-de-sim-a-los-2-3-meses-y-no-vincular-2fa]]) llega hasta el punto correcto: el punto débil de esta arquitectura no es el número, es la **cuenta que lo gobierna**.
El bloque legal —oferta pública, política de datos personales y **política de devoluciones** publicada— es un rasgo positivo del proveedor: es el único de los tres del sector con su "Returns Policy" enlazada desde la home ([[2026-1023-5sim-smart-buy-y-tasa-entrega-visible]]).

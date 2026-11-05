---
id: 2026-1027-mail-tm-acceso-gratuito-sin-api-key-ni-signup-ni-tiers
type: atom
certainty: solid
sources: [sources/2026-10-26-mail-tm-api-docs.md]
links: ["[[2026-1027-mail-tm-limite-de-8-qps-por-ip-address]]", "[[2026-1026-mail-tm-gratis-sin-cifras-con-financiacion-por-anuncios]]", "[[2026-1026-mail-tm-buzon-y-contrasena-nacen-al-abrir-el-sitio]]"]
---

## Claim
La sección "Pricing" de `docs.mail.tm/` publica el régimen de acceso con cuatro frases literales: "**Completely free. No API key, no signup, no paid tiers.**"; "**No API key required**"; "Just call the endpoints. **No signup, no tokens to start.**" El encabezado de la página lo repite: "Create temporary email accounts and receive emails via REST API. **No API key required.**"

## Why It Matters
Es la **primera vez que el corpus del correo tiene un régimen de acceso declarado por el proveedor, no inferido por el lector**. Hasta aquí el vault tenía tres registros del sector: NotLetters **vende por unidad** a 0.05 ₽, EmailOnDeck **no publica nada** y solo insinúa un plan PRO, y mail.tm declaraba "no hidden conditions, no paid extras" en su home —una **claim de marketing sin ninguna cifra** ([[2026-1026-mail-tm-gratis-sin-cifras-con-financiacion-por-anuncios]]). Ahora el propio proveedor, en la página de documentación, dice **gratis, sin API key, sin registro y sin planes de pago**. Eso no es un precio: es un **cero monetario con cuatro condiciones de acceso**, y es la primera vez que el vault puede escribir "coste de entrada = 0" sin disclaimer.

El detalle que más importa para el producto no es el precio sino la **ausencia de fricción de registro**: "no signup, no tokens to start" significa que **no hay cuenta, ni onboarding, ni clave que comprar ni plan que gestionar**. Todo el coste de acceso al buzón desechable programable es **cero registros y cero integraciones de pago**. En una tabla de coste por insumo eso es una categoría nueva: **coste monetario cero y coste de integración distinto de cero** — porque, como sí muestran las otras capturas, lo que cuesta no es el alta sino el **tramo de más abajo del flujo**: el proxy que el destino exige y, si el destino es un servicio de IA, el captcha ([[2026-1026-mail-tm-la-promesa-de-captcha-solving-evitada-por-el-buzon]]).

Y hay una lectura de mercado que esta frase sostiene y que el vault no había podido hacer: la ausencia de "API key required" **es coherente con el modelo de financiación por publicidad** declarado en la home ([[2026-1026-mail-tm-gratis-sin-cifras-con-financiacion-por-anuncios]]). Un proveedor funded by ads no necesita autenticación: **no hay que cobrarle nada a nadie porque no hay nadie a quien cobrarle**. Y la contrapartida es la que ya se ve en la misma página: **no hay SLA, ni cuotas de unidades, ni contrato** — solo un **8 QPS por IP** ([[2026-1027-mail-tm-limite-de-8-qps-por-ip-address]]). Es decir, **el acceso más abierto del sector es también el único cuyo límite es solo técnico**.

## [FRICTION]
> [[2026-1026-mail-tm-alta-masiva-de-buzones-y-api-declaradas-en-la-home]] sostiene que "**el vault no puede cotizar el correo de mail.tm** —no hay precio, ni cuota de buzones, ni condiciones— aunque tenga, por primera vez en el sector, un enlace a documentación", y su fricción afirma que "`docs.mail.tm/` **no ha sido abierto**".
> Este átomo abre esa documentación y la encuentra con un régimen de acceso publicado: "Completely free. No API key, no signup, no paid tiers" y "No API key required" ([[2026-1027-mail-tm-acceso-gratuito-sin-api-key-ni-signup-ni-tiers]]). En coste monetario, en condiciones de acceso y en techo de cadencia ([[2026-1027-mail-tm-limite-de-8-qps-por-ip-address]]), **el correo de mail.tm ya es cotizable**; lo que sigue sin cotizar es el precio unitario —que es cero— y cualquier SLA. Ambas no pueden ser la misma descripción del mismo proveedor. Marcado para juicio humano, no auto-resuelto: la captura no publica SLA, ni cuota de unidades, ni el comportamiento al superar las 8 QPS, ni la fecha de vigencia de los términos.

## Nota de verificación
Las cuatro frases y el encabezado son **transcripción literal** de `sources/2026-10-26-mail-tm-api-docs.md`. La captura **no** publica: si la gratuidad tiene condiciones de uso no recogidas en la sección "Terms of Use", si existe un límite de unidades o de tiempo distinto del 8 QPS, ni de dónde sale el dinero más allá de la publicidad que declara la home. La afirmación de que "no hay coste de integración" es **interpretación del vault**: la captura no enumera tareas de integración.

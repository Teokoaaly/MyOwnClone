---
id: 2026-1027-mail-tm-prohibicion-de-reventa-y-de-proxy-de-su-api
type: atom
certainty: solid
sources: [sources/2026-10-26-mail-tm-api-docs.md]
links: ["[[2026-1026-mail-tm-alta-masiva-de-buzones-y-api-declaradas-en-la-home]]", "[[2026-1023-herosms-api-y-partners-de-registro-masivo]]", "[[2026-1024-chatgpt-creator-correo-temporal-y-otp-automatico-con-generator-email]]"]
---

## Claim
La sección "Terms of Use" de `docs.mail.tm/` publica cuatro restricciones, con su texto literal: "**No illegal activity** — Usage of our API for illegal activity is strictly prohibited."; "**No reselling** — Don't build a paid product that just wraps our API."; "**No proxy services** — Don't mirror or proxy our API under a different domain."; "**Attribution required** — If you use our API, link back to mail.tm somewhere visible."

## Why It Matters
Son **condiciones de uso del proveedor, no features del producto**, y el vault no tenía ninguna: hasta ahora el corpus del correo publicaba marketing, precios de 0.05 ₽ y ausencias de especificación, pero **nunca un término que delimite qué se puede construir encima**. Esto convierte a mail.tm en el primer proveedor del corpus con **licencia de uso explícita**, y la licencia tiene dos dientes: "No reselling" —no montar un producto de pago que envuelva la API— y "No proxy services" —no espejar ni proxificar la API bajo otro dominio—.

La lectura operativa para el vault es directa y incómoda. La prohibición de reventa significa que **mail.tm no puede ser la partida de proveedor de un producto de pago**: el buzón temporal puede ser insumo interno de un servicio, pero la API no puede ser el producto. Y la prohibición de proxy significa que **el triage de email no puede montarse como un endpoint propio que reescriba `api.mail.tm`**: si el producto del vault consume mail.tm, tiene que hablar con `api.mail.tm` directamente y con su propia lógica encima, no con un mirror.

El contraste con el otro extremo del corpus es el que da la lectura: HeroSMS **invita explícitamente** a que el software de registro se integre y publica partners que venden cuentas en un "exchange", con "Register thousands of accounts daily" ([[2026-1023-herosms-api-y-partners-de-registro-masivo]]); mail.tm, siendo gratis, pone la línea en el lado contrario. Es decir, **la gratuidad del proveedor de correo no significa permiso de reventa**: son dos contratos de negocio distintos dentro del mismo sector de la verificación, y el bot de registro de ChatGPT —que se trae su propio generador de buzones ([[2026-1024-chatgpt-creator-correo-temporal-y-otp-automatico-con-generator-email]])— está del lado del que no necesita pedirle permiso a nadie.

## [FRICTION]
> [[2026-1026-mail-tm-alta-masiva-de-buzones-y-api-declaradas-en-la-home]] sostiene, sobre la base de la home, que mail.tm es el **tercer modelo del sector**: "producto de consumo gratuito con una vía documentada de producción de buzones encima, sin canal de venta a revendedores", y que su caso de uso declarado es "running multiple accounts in online games, social networks and elsewhere".
> Este átomo presiona esa lectura en dos puntos que la home no podía mostrar. El primero: "API access" y "register disposable mailboxes in bulk" no significan que el producto **se pueda revender**, sino que **no se puede revender la API**: el término es "Don't build a paid product that just wraps our API", es decir, la prohibición recae sobre el producto de pago que envuelve la API, no sobre el uso de la API dentro de un producto. El segundo: el término "No proxy services" cierra por el otro lado la puerta que la home abría —si el sector del correo tiene una vía de producción de buzones documentada, también tiene una prohibición explícita de convertirla en servicio. O la lectura correcta de la home era "vía documentada de producción de buzones **sin canal de venta**" —y entonces el término de reventa lo confirma y cierra el modelo de negocio del sector— o mail.tm **quiere** clientes que usen la API en su propio producto y lo que prohíbe es solo el reenvío. Marcado para juicio humano, no auto-resuelto: la captura no publica la **licencia completa**, ni un contacto ni una URL de términos legales, ni el alcance exacto de "paid product", ni qué cuenta como "mirror or proxy under a different domain" (un cliente que cachea dominios, ¿es proxy?).

## Nota de verificación
Los cuatro términos están transcritos literalmente de la sección "Terms of Use" de `sources/2026-10-26-mail-tm-api-docs.md`. La captura **no** publica versión de los términos, fecha de vigencia, sanciones, ni la definición de "paid product".

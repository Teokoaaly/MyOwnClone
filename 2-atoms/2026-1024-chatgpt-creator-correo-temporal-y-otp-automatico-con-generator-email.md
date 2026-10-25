---
id: 2026-1024-chatgpt-creator-correo-temporal-y-otp-automatico-con-generator-email
type: atom
certainty: solid
sources: [sources/2026-10-24-chatgpt-creator-verssache.md]
links: ["[[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]", "[[2026-1024-notletters-correo-masivo-para-registros-y-lolzteam]]", "[[2026-1022-auth-magic-link-codigo-seis-digitos]]"]
---

## Claim
El bot **no recibe correo por webhook ni por API**: genera el buzón él mismo. La feature es **"Auto Email Generation — Generates temporary emails via generator.email or custom domains"**, con el módulo `internal/email/generator.go  # Temporary email generation`. La configuración añade que el dominio por defecto sale **"random from generator.email"** si `default_domain` está vacío, y el prompt interactivo lo muestra con el texto `(current: (random from generator.email), press Enter to use, or enter new)`. La verificación es **"OTP Verification — Automatic email OTP retrieval and validation"**, es decir, el bot **recoge el código del correo por su cuenta**. En la traza de ejemplo el código OTP aparece en claro: `Validate OTP [483291] | 200`, y el correo generado en el ejemplo es `johndoe8x2kq@smartmail.de`. El nombre de persona se genera con `internal/util/names.go  # Random name generation (gofakeit)` y la contraseña con `internal/util/password.go  # Random password generation`, con la regla de que la contraseña por defecto debe tener **12+ caracteres** o se genera al azar.

## Why It Matters
Esta es la **pata de correo resuelta de la manera más simple posible y con un solo proveedor**: un generador de buzones desechables, `generator.email`, y polling del código. Es la misma clase de insumo que NotLetters vende por unidades ([[2026-1024-notletters-correo-masivo-para-registros-y-lolzteam]]), pero aquí **el propio bot trae el generador integrado**, así que no hay proveedor de correo que integrar, ni API que documentar, ni clave que comprar: el coste marginal de un buzón es cero y el coste marginal del OTP es el tiempo de espera.
La consecuencia para el modelo de coste del thread es concreta: **en esta ruta no hay partida de correo que cotizar**. La tabla de coste por insumo de la §7 del thread arrancaba con "correo ≪ captcha ≪ proxy ≪ SMS"; aquí el correo no tiene precio porque es una función de la biblioteca, y el SMS desaparece entero del flujo. Lo único que queda como partida monetaria es el **proxy**, y el único recurso escaso es el **tiempo** (25 s por cuenta, seis intentos para cinco cuentas).
Y hay un detalle de diseño que conecta con el producto del vault: **el código de verificación es un OTP numérico corto** (6 dígitos en el ejemplo), igual en forma que el magic link de 6 dígitos de MyOwnClone ([[2026-1022-auth-magic-link-codigo-seis-digitos]]). La diferencia es de fondo: el vault pide ese código a un humano por email; este bot lo pide al buzón temporal y lo teclea solo. La misma forma de UX, automatizada de extremo a extremo.

## Nota de verificación
El README **no publica ni el precio, ni la API, ni los términos, ni los límites** de `generator.email` —solo el enlace al sitio en la feature. El vault no puede cotizar el buzón temporal a partir de esta fuente.

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


## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-emailondeck-temp-mail.md`. Este átomo describe la **pata de correo resuelta como función de biblioteca**: el bot genera el buzón él mismo vía `generator.email`, recoge el OTP solo, y el vault concluye que "en esta ruta no hay partida de correo que cotizar" y que "el coste marginal de un buzón es cero".

EmailOnDeck documenta el **extremo contrario del mismo producto**: el mismo objeto técnico —una dirección desechable— servido por un proveedor que **no publica ninguna vía de consumo programable**. Su superficie es un formulario de dos pasos en el navegador ("Step 1", "Step 2", "Get Email"), y los cinco usos que declara son **QA testing de emails, free trials, perfiles de citas, compraventa de Bitcoin y trading en exchanges**; **no menciona ni una vez** el registro masivo, el mercado de cuentas, la automatización ni una API ([[2026-1026-emailondeck-casos-de-uso-de-consumo-y-no-de-registro-masivo]]).

Eso obliga a precisar la afirmación del átomo en un punto que el vault necesita para el §7: **"coste marginal cero" y "no cotizable" no son lo mismo**. En la ruta del bot, el buzón no tiene precio **porque el bot lo genera**; en la ruta de EmailOnDeck, el buzón no tiene precio **porque el proveedor no lo publica y su automatización no está disponible** —y la automatización por API es justamente lo que un flujo de registro masivo necesita. La regla correcta para el vault es: **el correo desechable tiene tres regímenes distintos** —biblioteca (coste marginal cero, sin proveedor), proveedor **pagado y automatizable** (NotLetters: 0.05 ₽, web + API + IMAP), y proveedor **gratuito y manual** (EmailOnDeck: sin precio, sin API)— y solo el segundo es cotizable por unidad.

La fricción que esto abre para el §7 es de **elegibilidad del insumo**: un correo gratuito que hay que usar a mano no puede servir de pata de correo a un pipeline automatizado, aunque su precio nominal sea cero. El vault no puede modelar el correo como "la partida más barata" sin distinguir antes **para qué uso** es gratis.


## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-mail-tm-temp-mail.md`.

Este átomo establece la **función de biblioteca** del correo: el bot genera el buzón con `generator.email` —"Auto Email Generation — Generates temporary emails via generator.email or custom domains"—, recoge el OTP por polling y **no hay partida de correo que cotizar**. Mail.tm es el **proveedor externo que hace lo mismo sin código**, y además lo publica: el alta es un efecto colateral de abrir la página —"gives you an email address and a password for it **the moment you open the site**", "**no personal details required**", "**The mailbox is created automatically**"— y la credencial es "a **unique, automatically generated password**" ([[2026-1026-mail-tm-buzon-y-contrasena-nacen-al-abrir-el-sitio]]).

Consecuencia para el Editor: el átomo debe precisar su frase "el coste marginal de un buzón es cero". Con mail.tm, ese coste marginal cero **deja de ser una inferencia de diseño del bot y pasa a ser un hecho de mercado** —un proveedor lo ofrece gratis, con API y con documentación enlazada ([[2026-1026-mail-tm-alta-masiva-de-buzones-y-api-declaradas-en-la-home]]). Pero el coste no es cero en todas las dimensiones: mail.tm declara **40 MB de cuota por buzón** como única cifra de la página ([[2026-1026-mail-tm-unica-cifra-de-la-captura-40-mb-de-cuota]]) y **"kept forever" con "no limit" de unidades** ([[2026-1026-mail-tm-buzon-conservado-para-siempre-y-sin-limite-de-unidades]]), lo que convierte el buzón en **activo acumulativo** y no en consumible —la diferencia decisiva frente al modelo del bot, que retira y tira.


## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-mailsac-test-email.md`. Este átomo documenta el flujo "OTP Verification — Automatic email OTP retrieval and validation" del bot de registro masivo, con el buzón generado vía `generator.email` y el código impreso en claro en la traza (`Validate OTP [483291] | 200`).

MailS.ac aporta el **dato de higiene que el corpus no tenía**, enunciado por un proveedor del mismo sector: **el buzón desechable público no es privado**, y el propio proveedor lo dice y lo estructura en dos niveles. "Public and free: anyone can read an @mailsac.com inbox, so use made-up data. Private when it matters: the free plan includes one private address, and paid plans from $18 a month add custom test domains that only your team can read". Y en la misma línea, para el caso de agentes: "Use a private address or private custom domain for sensitive test emails" ([[2026-1026-mailsac-los-buzones-publicos-son-legibles-por-cualquiera]], [[2026-1026-mailsac-el-faq-declara-explicitamente-que-los-agentes-de-ia-pueden-usarlo]]).

Esto **no corrige** este átomo, que sigue siendo una lectura fiel del README, pero **le añade una variable que el README no documenta**: si el buzón que el bot genera es del tipo público —anónimo y compartido—, el OTP que el bot teclea automáticamente estuvo, durante la ventana de espera, en una bandeja que **cualquiera podía leer**, y la validación automática lo convierte en un dato que además se imprime en el log. El vault no puede resolverlo porque el README **no publica el modelo de privacidad de `generator.email`**; lo que sí puede hacer es dejar la pregunta explícita y tratarla como riesgo asumido, no como flujo verificado.


## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-mail-tm-api-docs.md`.

Este átomo documenta la **función de biblioteca** del correo en el bot: generación con `generator.email`, recogida del OTP por polling y **cero partida de correo que cotizar**. La API de mail.tm ofrece el mismo resultado como producto, y además publica **el mecanismo de espera como opción de contrato**: el paso 4 de `GET https://api.mail.tm/messages` admite "Fetch messages via the API **or listen in real-time with SSE**" ([[2026-1027-mail-tm-flujo-de-cuatro-peticiones-para-obtener-un-buzon]]).

Consecuencia para el Editor: el **polling del OTP deja de ser una limitación del bot y pasa a ser una decisión de diseño del pipeline**. Con SSE, la espera del código de activación es un evento, no un temporizador, y eso elimina una latencia periódica por buzón —el modo de trabajo actual es "generar buzón, esperar, hacer polling" ([[2026-1024-chatgpt-creator-correo-temporal-y-otp-automatico-con-generator-email]]). La comparación de coste entre la función de biblioteca y el proveedor externo sigue sin resolverse por precio (mail.tm es gratis en dinero pero limitado a 8 QPS por IP, [[2026-1027-mail-tm-limite-de-8-qps-por-ip-address]]), pero **el modo de entrega del mensaje sí es ahora un parámetro de contrato del proveedor**, no un detalle de implementación.

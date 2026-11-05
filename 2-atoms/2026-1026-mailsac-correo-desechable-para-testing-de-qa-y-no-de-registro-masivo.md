---
id: 2026-1026-mailsac-correo-desechable-para-testing-de-qa-y-no-de-registro-masivo
type: atom
certainty: solid
sources: [sources/2026-10-25-mailsac-test-email.md]
links: ["[[2026-1024-notletters-correo-masivo-para-registros-y-lolzteam]]", "[[2026-1023-5sim-casos-de-uso-qa-y-privacidad]]", "[[2026-1026-emailondeck-gratis-con-paso-pro-sin-cifras]]"]
---

## Claim
MailS.ac (`mailsac.com`) se presenta explícitamente como **correo desechable para testing**, no como insumo de registro masivo. El titular de la home es "Receive test emails with confidence" y el subtítulo "Immediately test your application's email delivery with our disposable email services. Designed to empower QA and Software teams with integrations throughout the testing process". La sección de producto se titula **"Test email addresses"** y el subtítulo de la oferta es "Free test email addresses for developers and QA"; el FAQ lo remata: "Mailsac is built for testing email. QA and development teams use it to check sign-up confirmations, password resets and one-time codes, by hand in the web inbox or from automated tests and CI pipelines through the REST API". El único ejemplo de dirección que da es `signup42@mailsac.com`, y el claim de escala es "We support hundreds of Quality Assurance teams".

## Why It Matters
Es el **tercer modelo de producto** que el vault registra en el sector del correo desechable, y no es una variante de los dos anteriores: NotLetters vende "Fast and reliable mail for bulk tasks" con el objetivo declarado de "create multiple mailboxes for site registrations" y su banner cita "Great for Lolzteam Market" ([[2026-1024-notletters-correo-masivo-para-registros-y-lolzteam]]); EmailOnDeck es una utilidad de consumo de dos pasos ([[2026-1026-emailondeck-gratis-con-paso-pro-sin-cifras]]); MailS.ac es **infraestructura de QA**, con integración en CI y un precio y una escala **por equipo**, no por buzón.

La conexión con el vault es directa y es el caso de uso que 5sim ya declaraba solo para el canal SMS: "desarrollo y QA" de flujos OTP y notificaciones ([[2026-1023-5sim-casos-de-uso-qa-y-privacidad]]). MailS.ac es la **contraparte de correo** de ese caso de uso — y por tanto el insumo que un producto con magic link de 6 dígitos por email necesitaría para probar su propio flujo de alta sin gastar correos reales.

## [FRICTION]
> [[2026-1024-notletters-correo-masivo-para-registros-y-lolzteam]] define el producto del sector del correo desechable como **buzones creados para registrarse en un sitio** —la unidad que se compra es el buzón, y la operación que se facilita es el registro masivo— con el mercado de cuentas de lzt.market citado en el banner como caso de uso.
> Este átomo presiona esa creencia en un punto: **MailS.ac, del mismo sector y con el mismo nombre de producto ("disposable email services"), declara lo contrario por escrito**. Su correo existe para **probar el flujo de una aplicación propia** ("check sign-up confirmations, password resets and one-time codes"), y su punto de fricción declarado es que el buzón público "@mailsac.com" lo puede leer cualquiera, de modo que "use made-up data" ([[2026-1026-mailsac-los-buzones-publicos-son-legibles-por-cualquiera]]).
> Ambas no pueden ser completamente correctas a la vez: o "correo desechable" es **una sola categoría** con un uso único (registro masivo) y MailS.ac es un caso atípico que se autolimita, o son **dos categorías con requisitos incompatibles** —buzón anónimo para alta de terceros frente a buzón de equipo para QA de código propio— y entonces la tabla de coste por insumo del thread no puede tratar "el correo" como una partida única. Marcado para juicio humano, no auto-resuelto.

Nota de verificación: las citas están transcritas literalmente de la captura; **no se ha visitado** `/pricing`, `/register`, `/pages/email-testing-api/` ni `docs.mailsac.com`.

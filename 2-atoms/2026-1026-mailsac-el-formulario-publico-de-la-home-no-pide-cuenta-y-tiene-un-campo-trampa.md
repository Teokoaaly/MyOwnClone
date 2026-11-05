---
id: 2026-1026-mailsac-el-formulario-publico-de-la-home-no-pide-cuenta-y-tiene-un-campo-trampa
type: atom
certainty: solid
sources: [sources/2026-10-25-mailsac-test-email.md]
links: ["[[2026-1026-mail-tm-el-email-como-pasaporte-digital-y-el-buzon-como-escudo]]", "[[2026-1024-notletters-captura-minima-sin-dominios-ni-limites-ni-condiciones]]", "[[2026-1026-mailsac-los-buzones-publicos-son-legibles-por-cualquiera]]"]
---

## Claim
La home de MailS.ac abre con un **visor de buzón público sin registro** y con un campo trampa: el formulario se titula "Mailsac Inbox Form", el botón es "Check the mail!", y debajo de los campos hay un campo oculto con la etiqueta "**If you are human, leave this field blank.**". La lectura del correo no requiere cuenta: "Read the mail in the inbox checker above, or from your tests with the REST API", y el FAQ confirma que "You don't need to create one. Choose any address at @mailsac.com, send your test email to it, then open that inbox on mailsac.com or read it with the API". La captura **no publica ningún límite** de este visor: ni buzones consultables, ni frecuencia, ni retención.

## Why It Matters
Es la **superficie de adquisición** del proveedor, y por tanto la lectura de qué está dispuesto a regalar: un visor de buzón público, sin cuenta, con throttling declarado pero sin cifra ([[2026-1026-mailsac-los-buzones-publicos-son-legibles-por-cualquiera]]), más el gancho de automatización ("your tests can wait for a message and read its code or links over the API, from any language or CI system"). El honeypot "leave this field blank" indica que el formulario **se integra con un bot de registro**: el campo vacío es el discriminante.

La comparación con el resto del sector del vault es instructiva porque ahí la prueba de calidad era la opacidad: NotLetters y el resto de proveedores de buzonesIp se resumen en "captura mínima sin dominios, sin límites ni condiciones" ([[2026-1024-notletters-captura-minima-sin-dominios-ni-limites-ni-condiciones]]), y mail.tm llega al mismo producto por el discurso de identidad ([[2026-1026-mail-tm-el-email-como-pasaporte-digital-y-el-buzon-como-escudo]]). MailS.ac es el caso opuesto: **marketing verboso y muy específico, con la única cifra ("$18 a month") en la home y todo el resto escondido detrás de un enlace a `/pricing`**.

Nota de verificación: la captura no incluye el código del formulario ni la imagen del honeypot; lo verificado es el texto literal del campo. No se ha enviado ningún correo a ningún buzón de MailS.ac ni se ha consultado ningún buzón.

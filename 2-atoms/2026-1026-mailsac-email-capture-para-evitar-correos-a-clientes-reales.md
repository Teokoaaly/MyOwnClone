---
id: 2026-1026-mailsac-email-capture-para-evitar-correos-a-clientes-reales
type: atom
certainty: solid
sources: [sources/2026-10-25-mailsac-test-email.md]
links: ["[[2026-1022-email-inbound-contacto-sin-dominio-propio]]", "[[2026-1026-mailsac-subdominios-en-segundos-y-idioma-de-dominio-propio]]", "[[2026-1022-soporte-al-cliente-separado-y-escalado]]"]
---

## Claim
MailS.ac ofrece un servicio con nombre propio para **capturar el correo que un test envía por error a un cliente real**: "Prevent unintended emails to customers using our **Email Capture service**". Es la segunda de las tres funciones declaradas bajo "What we offer", junto a los subdominios y las APIs, y aparece también en el bloque de propósito: "Let us take care of the hassles of building inboxes, setting up servers and **ensuring email doesn't get sent to live users**". La página no publica nada más del servicio: ni qué ocurre con el correo capturado, ni su precio, ni si es un plan aparte.

## Why It Matters
Es la **función que invierte el signo del riesgo** de todo el corpus de correo desechable. En el resto del sector —NotLetters, EmailOnDeck, el 卡网— el riesgo documentado es que **el buzón falso reciba** algo (un código, un alta) o que **el dato se filtre**; aquí MailS.ac monetiza el caso inverso: que el sistema **en producción escriba en el buzón de test** y ese correo llegue a un usuario real. Es decir, el proveedor asume el **fallo de routing**, no el fallo de lectura.

Para el vault la lectura es de arquitectura de soporte, y es directa: el producto tiene una única casilla inbound genérica `contacto@myownclone.com` y los dominios inbound por tenant están "Coming soon" ([[2026-1022-email-inbound-contacto-sin-dominio-propio]]), con un handoff a humano y captura de feedback de clientes concentrados ahí ([[2026-1022-soporte-al-cliente-separado-y-escalado]]). Es decir, **el fallo "correo enviado al destinatario equivocado" es un riesgo operativo del propio producto**, y MailS.ac lo trata como un producto de terceros con nombre, exactamente igual que "[[2026-1026-mailsac-subdominios-en-segundos-y-idioma-de-dominio-propio]]" externaliza la configuración DNS. Lo que el proveedor **no** puede externalizar es la marca del remitente: un producto con dominio propio necesita su propio dominio inbound, no un subdominio de un tercero.

Nota de verificación: la captura **no** publica el precio del Email Capture service, ni su alcance, ni si aplica a los planes de pago. No se hacreates ninguna cuenta ni probado el servicio.

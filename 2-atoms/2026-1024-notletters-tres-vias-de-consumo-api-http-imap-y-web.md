---
id: 2026-1024-notletters-tres-vias-de-consumo-api-http-imap-y-web
type: atom
certainty: solid
sources: [sources/2026-10-23-notletters-mail.md]
links: ["[[2026-1023-herosms-api-y-partners-de-registro-masivo]]", "[[2026-1022-myclone-api-rest]]", "[[2026-1023-5sim-asistente-ia-integrado]]"]
---
## Claim
La home de NotLetters publica **tres vías de consumo del correo**, y las describe explícitamente como "Connecting to emails": **Web** en `notletters.com` ("A Web interface familiar to many", botón "Go over" a `notletters.com/email`), **API** en `api.notletters.com` ("The most popular method via the HTTP API", con un botón "Copy") y **IMAP** en `imap.notletters.com` ("Via port 993 with SSL", con botón "Copy"). El texto que las engloba es "We have implemented the most convenient ways for you to receive emails".

## Why It Matters
Es la diferencia estructural entre este proveedor y el resto del sector que el vault tiene registrado. HeroSMS publica **una API sin documentación** y externaliza la automatización a socios ([[2026-1023-herosms-api-y-partners-de-registro-masivo]]); 5sim integra la compra dentro del chat ([[2026-1023-5sim-asistente-ia-integrado]]). NotLetters publica las tres superficies —API HTTP, IMAP con SSL en el puerto 993 y web— pero **no publica la documentación de ninguna**: la captura no contiene endpoint, esquema de petición, autenticación, formato de respuesta ni parámetros de IMAP. Es un diseño "toda superficie, ninguna especificación", el mismo patrón de opacidad que ya se registró en otro proveedor del sector, con la diferencia de que aquí la superficie IMAP es nueva.
Para el producto del vault la lectura es de diseño, no de uso: un buzón de registro masivo es un **endpoint de entrada de un token**, y IMAP con SSL es exactamente el protocolo que un pipeline de lectura automatizada necesitaría — pero el vault no consume correo ajeno, consume el suyo con magic link ([[2026-1022-myclone-api-rest]] para la superficie de API propia, que hoy es mínima y server-side). El valor de esta nota para el vault es de **vocabulario de la categoría**: en este mercado el correo no es un canal de soporte sino un **recurso consumible y automatizable**, y hay al menos un proveedor que lo empaqueta así.

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


## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-mail-tm-temp-mail.md` (home de `https://mail.tm/`, 698 palabras, capturada el 2026-10-25).

Este átomo sostiene que NotLetters **publica tres vías de consumo sin documentar ninguna**: web, HTTP API en `api.notletters.com` e IMAP en `imap.notletters.com` por el 993 con SSL. Mail.tm invierte el patrón en un punto exacto: **publica menos vías y además enlaza la documentación** —el nav lleva `API` → **`https://docs.mail.tm/`**, una URL de documentación, no un rótulo— y, en el bloque "Flexible", declara la capacidad que faltaba en NotLetters: "The latter [power users] get **API access** and a **quick way to register disposable mailboxes in bulk**" ([[2026-1026-mail-tm-alta-masiva-de-buzones-y-api-declaradas-en-la-home]]).

Consecuencia para el Editor: la observación "superficies sin especificación" del átomo **no es una regla del sector del correo**, sino de NotLetters y EmailOnDeck. Con tres capturas del sector, la formulación defendible pasa a ser: **el corpus de correo del vault tiene tres proveedores con tres comportamientos de documentación opuestos** —NotLetters (tres vías, cero documentación), EmailOnDeck (cero vías programables, cero especificación) y mail.tm (una vía enlazada a documentación, aunque sin cifras ni condiciones en la home). El matiz que **no** cambia: **el vault no ha abierto `docs.mail.tm/`**, de modo que sigue sin poder cotizar ninguna de las tres.


## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-mailsac-test-email.md`. Este átomo documenta que NotLetters publica tres vías de consumo —web, HTTP API en `api.notletters.com` e IMAP en `imap.notletters.com` por el 993 con SSL— y que **ninguna** viene documentada.

MailS.ac es el contrapunto útil del corpus para esa ausencia, porque es **el otro extremo del mismo sector**: publica un contrato de respuesta explícito ("The API supports checking mail for any address, and will return **200 with an empty array** if no mail exists there"), una lista de protocolos de integración ("REST, Web Sockets, and Webhooks"), una lista nominal de sistemas de CI soportados ("Jenkins, GitHub Actions, Selenium, GitLab CI, Bamboo, etc") y enlaces a documentación propia (`docs.mailsac.com`, `mailsac.com/pages/email-testing-api/`) ([[2026-1026-mailsac-la-api-devuelve-200-con-array-vacio-si-no-hay-correo]]).

La consecuencia para este átomo es de **criterio de clasificación**, no de rankings: la ausencia de especificación que este átomo registra en NotLetters **no es una propiedad del sector del correo desechable**, sino una propiedad de ese proveedor. En el mismo sector hay un operador que publica al menos el contrato de error —la ausencia de correo no es un error sino un `200` con array vacío— y que enlaza documentación. El matiz que debe añadirse: MailS.ac **tampoco publica los endpoints, los esquemas ni los parámetros**, de modo que sigue sin ser una especificación completa; la diferencia es que **declara que la tiene** y da un enlace verificable, lo que la hace auditable en principio ([[2026-1026-mailsac-la-direccion-de-reenvio-privado-exige-reservarla-primero]]).


## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-mail-tm-api-docs.md`.

Este átomo sostiene que NotLetters publica **tres vías de consumo sin documentar ninguna**: web, HTTP API en `api.notletters.com` e IMAP en `imap.notletters.com` por el 993 con SSL, y que el patrón "toda superficie, ninguna especificación" es una propiedad del proveedor. La captura de `docs.mail.tm/` **consolida la contraste**: mail.tm publica el **spec OpenAPI v3 descargable** (`https://api.mail.tm/docs.jsonld`), los **docs interactivos** (`https://api.mail.tm/`) y la sección "General Information" que lo anuncia ("The API follows the OpenAPI v3 spec. Download it or explore interactively.") ([[2026-1027-mail-tm-spec-openapi-v3-descargable-y-docs-interactivas]]).

Consecuencia para el Editor: la formulación defendible se estrecha a un criterio binario y verificable —**publicar el contrato o no publicarlo**. NotLetters (tres vías, cero especificación) y EmailOnDeck (cero vías) quedan en un polo; mail.tm, en el otro, y es **el primer proveedor de correo del corpus cuyo contrato técnico es descargable y parseable**, lo que permite auditar sus endpoints y esquemas mecánicamente en lugar de por lectura de prosa. Matiz que hay que conservar: **el `.jsonld` no ha sido descargado** y la captura no publica su contenido, el número de endpoints que contiene ni sus esquemas de respuesta.

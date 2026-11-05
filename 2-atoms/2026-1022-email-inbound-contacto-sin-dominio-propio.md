---
id: 2026-1022-email-inbound-contacto-sin-dominio-propio
type: atom
certainty: solid
sources: [raw/articles/myownclone-frontend-recon.md, sources/2026-10-23-notletters-mail.md]
links: ["[[myownclone]]", "[[2026-1022-soporte-al-cliente-separado-y-escalado]]", "[[marea-kiss-llc]]"]
---
## Claim
El único destinatario de email entrante en [[myownclone]] es `contacto@myownclone.com` (el mismo que publica [[marea-kiss-llc]]); el soporte de dominios inbound propios por tenant aparece explícitamente como "Coming soon".

## Why It Matters
Es un límite real de la oferta de soporte: mientras el inbox existe y el Triage procesa correo, no puede recibir desde la marca del creator. Para el modo soporte de [[2026-1022-soporte-al-cliente-separado-y-escalado]] significa que hoy el handoff a humano y la captura de feedback de clientes convergen en una única casilla genérica de la plataforma — un cuello de botella de marca y de datos, y un punto que un competidor con whitelabel de email propio ya cubre.

## [NOTA 2026-10-24 — NotLetters]
A partir de `sources/2026-10-23-notletters-mail.md`. En el otro extremo del eje hay un mercado de **buzones de correo como recurso consumible**: `notletters.com` vende "Fast and reliable mail for bulk tasks" con la promesa de "create multiple mailboxes for site registrations", a **0.05 ₽ por correo**, y publica tres vías de consumo —web, HTTP API (`api.notletters.com`) e IMAP en `imap.notletters.com` por el puerto 993 con SSL ([[2026-1024-notletters-correo-masivo-para-registros-y-lolzteam]], [[2026-1024-notletters-tres-vias-de-consumo-api-http-imap-y-web]]). Para el producto del vault la lectura es de contraste: MyOwnClone resuelve su correo entrante con **una sola casilla genérica** y sin dominios inbound por tenant, mientras que el mercado compra buzones en volumen y los automatiza por API e IMAP. Es decir, la restricción que este átomo registra como límite de la oferta de soporte no es una carencia técnica del mercado: hay proveedores que la han convertido en producto. Lo que no se puede afirmar es que ese proveedor resuelva el problema del vault — su correo es de un solo uso y sin marca propia, que es justo lo contrario de lo que el soporte por tenant necesita.


## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-mailsac-test-email.md`. Este átomo documenta la pata de entrada del producto: un único destinatario genérico `contacto@myownclone.com` y los dominios inbound por tenant en "Coming soon".

MailS.ac ofrece dos piezas que ese "Coming soon" tendría que resolver, y que el vault puede usar como especificación de referencia. La primera es la **dirección de entrada por tenant sin configuración**: el "Zero Setup Subdomain service" —"Create subdomains in seconds"— con la capacidad de "quickly generate and assign email subdomains", más un **BYOD** explícito ("You can also bring your own domain!") ([[2026-1026-mailsac-subdominios-en-segundos-y-idioma-de-dominio-propio]]). La segunda es el **Email Capture service**, que existe para el caso de routing erróneo: "Prevent unintended emails to customers using our Email Capture service" y "ensuring email doesn't get sent to live users" ([[2026-1026-mailsac-email-capture-para-evitar-correos-a-clientes-reales]]).

La lectura para el producto: el proveedor externo **resuelve bien la parte de configuración** y la parte de **contención del error**, pero **no puede resolver la parte de marca** —un producto multi-tenant necesita que el remitente vea su propio dominio, no un subdominio de un tercero. El "Coming soon" no es por tanto un gap subsanable con un proveedor: es la parte que solo puede resolver el titular del dominio.

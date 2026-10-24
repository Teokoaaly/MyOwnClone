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

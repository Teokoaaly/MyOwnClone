---
id: 2026-1026-mailsac-la-api-devuelve-200-con-array-vacio-si-no-hay-correo
type: atom
certainty: solid
sources: [sources/2026-10-25-mailsac-test-email.md]
links: ["[[2026-1024-2captcha-flujo-api-en-cinco-pasos-con-captcha-id]]", "[[2026-1022-myclone-scraping-ingestion-pipeline]]", "[[2026-1024-notletters-tres-vias-de-consumo-api-http-imap-y-web]]"]
---

## Claim
MailS.ac publica un **contrato de consulta sin error**: "The API supports checking mail for any address, and will return **200 with an empty array** if no mail exists there". La página de documentación enlazada describe el flujo como "Receive test emails in disposable inboxes. Use the REST API to check signup confirmations, password resets and other email workflows in your automated tests", con dos puntos de entrada: "How the email testing API works" y "Read email with the REST API". Y la sección de capacidades de la API lista "Fetch body links, list messages, download attachments and more with our fully documented API". Para integraciones: "mailsac uses standard open protocols like **REST, Web Sockets, and Webhooks** to allow you to integrate testing pipelines with any system – **Jenkins, GitHub Actions, Selenium, GitLab CI, Bamboo**, etc.".

## Why It Matters
El detalle "**200 con array vacío**" es una decisión de diseño de API que el vault puede reutilizar tal cual: **la ausencia de correo no es un error**, es un resultado válido con código 200. Eso importa porque es exactamente el contrato que necesita un pipeline de CI con *polling* —el patrón job-id + polling que el vault ya usa en la ingesta asíncrono ([[2026-1022-myclone-scraping-ingestion-pipeline]]) y en el flujo de cinco pasos de 2Captcha, donde el captcha ID se consulta hasta obtener respuesta ([[2026-1024-2captcha-flujo-api-en-cinco-pasos-con-captcha-id]]). La diferencia es que MailS.ac **no necesita un identificador de trabajo**: la dirección *es* la clave, y el resultado es un array, no un objeto con estado.

El contraste con el resto del sector del correo es lo que da valor al dato: NotLetters publica tres vías de consumo —web, HTTP API en `api.notletters.com` e IMAP en `imap.notletters.com` por el 993 con SSL— **sin documentar ninguna** ([[2026-1024-notletters-tres-vias-de-consumo-api-http-imap-y-web]]); MailS.ac publica **documentación enlazada, un contrato de respuesta y una lista nominal de integraciones de CI**. Es la diferencia entre una superficie de API y una especificación de API, y es el criterio que el thread necesita para no llamar "API" a un endpoint.

## Nota de verificación
La captura **no** contiene los endpoints, ni los esquemas de petición y respuesta, ni los nombres de los parámetros, ni los precios de los planes, ni los límites de retención. Lo verificado es el texto citado y la existencia de los enlaces a `docs.mailsac.com`; **no se ha ejecutado ninguna llamada a la API ni se ha creado ninguna cuenta**.

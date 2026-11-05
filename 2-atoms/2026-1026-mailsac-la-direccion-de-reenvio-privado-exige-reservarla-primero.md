---
id: 2026-1026-mailsac-la-direccion-de-reenvio-privado-exige-reservarla-primero
type: atom
certainty: solid
sources: [sources/2026-10-25-mailsac-test-email.md]
links: ["[[2026-1024-notletters-tres-vias-de-consumo-api-http-imap-y-web]]", "[[2026-1022-myclone-scraping-ingestion-pipeline]]", "[[2026-1024-2captcha-flujo-api-en-cinco-pasos-con-captcha-id]]"]
---

## Claim
MailS.ac tiene **dos regímenes de dirección**, con precondiciones opuestas. El régimen abierto: "You can send immediately to any address @mailsac.com or @ your custom domain. **No need to create the inbox first**" y "You don't need to create one. Choose any address at @mailsac.com, send your test email to it, then open that inbox on mailsac.com or read it with the API". El régimen cerrado: "To access custom forwarding features (**to web socket, webhook, slack, etc**), you must **'reserve' that address first**. This is called a **custom private forwarding address**". La página lo repite en dos sitios distintos: "**No need to create any of your inboxes ahead of time**" frente a la reserva obligatoria de la dirección de reenvío.

## Why It Matters
Es la **contradicción interna** más útil de la captura, y es de lectura de contrato: **"no hace falta crear nada" es cierto para consumir y falso para recibir en push**. Es decir, la dirección es lazily creada para lectura (web o API) pero debe ser **pre-reservada** para escribir hacia una integración (web socket, webhook, Slack), porque una dirección no reservada no puede tener un destino de reenvío asociado.

La consecuencia para un pipeline automatizado es directa: el modo **pull** (REST, [[2026-1026-mailsac-la-api-devuelve-200-con-array-vacio-si-no-hay-correo]]) no requiere ningún estado previo, mientras que el modo **push** (webhook, web socket, Slack) exige una operación de reserva que la captura **no documenta**: ni el endpoint, ni los parámetros, ni si la reserva expira. En un sistema de integración, esa asimetría entre pull y push es exactamente la clase de detalle que separa "API documentada" de "superficie anunciada" — el mismo límite que el vault ya marcó en NotLetters, donde se publicaban tres vías de consumo sin documentar ninguna ([[2026-1024-notletters-tres-vias-de-consumo-api-http-imap-y-web]]), pero aquí al menos el contrato de lectura sí está enunciado.

También tiene lectura de seguridad: la dirección reservada es la que se declara privada ([[2026-1026-mailsac-los-buzones-publicos-son-legibles-por-cualquiera]]), de modo que **reservar es la operación que compra privacidad**, y esa es una noción de estado que el vault no tenía registrada para ningún proveedor del sector.

Nota de verificación: no se ha creado cuenta ni reservado ninguna dirección; el endpoint de reserva **no está publicado en la captura**.

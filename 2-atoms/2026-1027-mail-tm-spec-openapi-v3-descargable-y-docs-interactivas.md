---
id: 2026-1027-mail-tm-spec-openapi-v3-descargable-y-docs-interactivas
type: atom
certainty: solid
sources: [sources/2026-10-26-mail-tm-api-docs.md]
links: ["[[2026-1027-mail-tm-flujo-de-cuatro-peticiones-para-obtener-un-buzon]]", "[[2026-1027-hero-sms-openapi-3-2-0-con-api-key-en-la-cabecera-authorization]]", "[[2026-1024-notletters-tres-vias-de-consumo-api-http-imap-y-web]]"]
---

## Claim
La sección "General Information" de `docs.mail.tm/` declara: "**The API follows the OpenAPI v3 spec. Download it or explore interactively.**", con dos enlaces: "**Download OpenAPI Spec**" → `https://api.mail.tm/docs.jsonld` y "**Interactive API Docs**" → `https://api.mail.tm/`. La propia cabecera de la página lleva además un enlace rotulado "**OpenAPI Spec**" al mismo `https://api.mail.tm/`.

## Why It Matters
Es la **primera especificación OpenAPI descargable del corpus de correo desechable**, y con ella la primera **superficie de correo programmaticamente consumible**: el `.jsonld` es un fichero que un cliente puede descargarse y con el que puede **generar su propio cliente o validar el suyo**, sin parsing escrito a mano. Esto separa a mail.tm del resto del sector con un criterio binario y verificable: **NotLetters publica tres vías de consumo y no documenta ninguna** ([[2026-1024-notletters-tres-vias-de-consumo-api-http-imap-y-web]]), EmailOnDeck no publica nada, y mail.tm publica **spec + docs interactivos**.

El valor para el vault no es la mera existencia del fichero, sino lo que habilita: un `docs.jsonld` permite **auditar mecánicamente** los endpoints, métodos y esquemas de respuesta del proveedor, que es la diferencia entre "la documentación dice que hay un `GET /messages`" y "el contrato publicado lo confirma". Y abre una comparación que el corpus del vault todavía no tenía: **los dos proveedores que publican especificación de API —mail.tm y HeroSMS— lo hacen en el mismo formato y con el mismo tipo de explorador** (HeroSMS declara OpenAPI 3.2.0 en JSON y YAML, servido por Scalar.com). Es decir, **hay un estándar de facto del sector de la verificación**, y el vault puede dejar de tratar "API del proveedor" como una caja negra por proveedor.

Y hay un ángulo de cumplimiento directamente conectado con las restricciones que esta misma página publica: las condiciones de uso ([[2026-1027-mail-tm-prohibicion-de-reventa-y-de-proxy-de-su-api]]) son **texto legible en la página**, no cláusulas dentro del spec. Eso significa que **el contrato técnico y el contrato legal viven en documentos distintos**, y que un integrador que solo descarga el `.jsonld` —que es lo que harían los generadores de clientes automáticos— **se queda sin las prohibiciones**. El "Attribution required" y el "No proxy services" no están en el `.jsonld`: hay que leerlos en la página.

## [FRICTION]
> [[2026-1024-notletters-tres-vias-de-consumo-api-http-imap-y-web]] sostiene que en el sector del correo **toda superficie va sin especificación** —NotLetters publica web, API HTTP e IMAP y **no documenta ninguna**—, y de ahí la tesis de que el patrón del proveedor de correo desechable es "superficie sin contrato".
> El `.jsonld` de OpenAPI v3 y los docs interactivos de mail.tm **rompen ese patrón por primera vez**: el contrato técnico es **descargable, parseable y explorable sin cuenta** ([[2026-1027-mail-tm-spec-openapi-v3-descargable-y-docs-interactivas]]). O la propiedad era de NotLetters y no del sector, o mail.tm es la excepción que hay que registrar como tal. Y hay un matiz que el `.jsonld` deja al descubierto: **el contrato técnico y el contrato legal viven en documentos distintos** —los "Terms of Use" están en prosa, fuera del spec—, de modo que un generador automático de clientes hereda los endpoints y **no** hereda las prohibiciones ([[2026-1027-mail-tm-prohibicion-de-reventa-y-de-proxy-de-su-api]]). Marcado para juicio humano, no auto-resuelto: **el `.jsonld` no ha sido descargado** y la captura no publica su contenido, ni el número de endpoints, ni sus esquemas de respuesta, ni si los términos de uso están enlazados desde el spec.

## Nota de verificación
Las tres frases y las dos URLs (`https://api.mail.tm/docs.jsonld`, `https://api.mail.tm/`) son **transcripción literal** de `sources/2026-10-26-mail-tm-api-docs.md`. La captura **no** publica: el contenido del `.jsonld`, la versión exacta de OpenAPI declarada por mail.tm (dice "v3" sin número), el número de endpoints que contiene, ni si la spec incluye los esquemas de respuesta y error. No se ha descargado el `.jsonld` ni se ha abierto `https://api.mail.tm/`.

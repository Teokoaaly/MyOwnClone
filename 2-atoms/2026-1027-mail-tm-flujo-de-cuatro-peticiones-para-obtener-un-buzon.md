---
id: 2026-1027-mail-tm-flujo-de-cuatro-peticiones-para-obtener-un-buzon
type: atom
certainty: solid
sources: [sources/2026-10-26-mail-tm-api-docs.md]
links: ["[[2026-1026-mail-tm-alta-masiva-de-buzones-y-api-declaradas-en-la-home]]", "[[2026-1024-chatgpt-creator-alta-por-correo-sin-telefono-en-el-flujo]]", "[[2026-1024-notletters-tres-vias-de-consumo-api-http-imap-y-web]]"]
---

## Claim
La documentación de `docs.mail.tm/` publica el flujo completo de la API REST en **cuatro peticiones**, transcritas literalmente: (1) `GET https://api.mail.tm/domains` — "Get available domain names from the API"; (2) `POST https://api.mail.tm/accounts` con cuerpo `{"address":"user@domain.com","password":"secret"}` — "Create a temporary email account with one request"; (3) `POST https://api.mail.tm/token` con **el mismo cuerpo de credenciales**; (4) `GET https://api.mail.tm/messages` con cabecera `Authorization: Bearer ***`. El paso 4 tiene dos modos: "Fetch messages via the API or **listen in real-time with SSE**". La página "How it works" describe la secuencia como *Fetch domains → Create account → Use the address → Message arrives → Fetch messages*.

## Why It Matters
Es la **primera especificación ejecutable del correo del corpus**: los tres proveedores anteriores del sector publicaban o nada o tres vías sin documentar ([[2026-1024-notletters-tres-vias-de-consumo-api-http-imap-y-web]]). Aquí el buzón desechable deja de ser "un click" y pasa a ser **cuatro llamadas HTTP con una cabecera Bearer**, es decir, una integración de verdad.

El valor comparativo está en el **coste de integración**, no en el precio. El bot de registro de ChatGPT resuelve lo mismo con nueve peticiones HTTP a la web de OpenAI y un buzón que se genera a sí mismo ([[2026-1024-chatgpt-creator-alta-por-correo-sin-telefono-en-el-flujo]]): si el buzón se externaliza a mail.tm, ese tramo del flujo pasa a ser un cliente REST de 4 endpoints, sin navegador ni captcha propio. Y la variante SSE es el detalle que decide el diseño del pipeline: **con SSE el correo deja de ser un polling y pasa a ser un evento**, lo que elimina la espera periódica por el código de activación — que es exactamente el modo de trabajo del bot.

La consecuencia de lectura para el thread de la economía de la verificación: **la partida de correo ya tiene contrato de integración, no solo de precio**. El flujo documentado es de 4 llamadas por buzón, lo que fija la aritmética de rendimiento bajo el techo de cuota del proveedor ([[2026-1027-mail-tm-limite-de-8-qps-por-ip-address]]).

## [FRICTION]
> [[2026-1026-mail-tm-alta-masiva-de-buzones-y-api-declaradas-en-la-home]] registró, desde la home, que mail.tm declara "API access" y "a **quick way to register disposable mailboxes in bulk**", y продает esa idea como **capacidad sin especificación**: el átomo afirma que la documentación enlazada **no había sido abierta** y que el flujo, las condiciones y la escala del alta masiva **no eran verificables**.
> La documentación publicada **sí** describe el flujo, y lo hace como una secuencia cerrada de **cuatro peticiones** —`GET /domains`, `POST /accounts`, `POST /token`, `GET /messages`— con la lectura final en dos modos, API o SSE ([[2026-1027-mail-tm-flujo-de-cuatro-peticiones-para-obtener-un-buzon]]). O "alta masiva" es un claim de home que ahora tiene contrato detrás, o el claim no era lo que parecía. Marcado para juicio humano, no auto-resuelto: la captura no publica esquemas de respuesta, códigos de error, paginación, ni el nombre del endpoint SSE, y **no se ha ejecutado ninguna alta real** contra mail.tm.

## Nota de verificación
Las cuatro URLs, los dos cuerpos JSON y la cabecera `Authorization: Bearer ***` están transcritos literalmente de `sources/2026-10-26-mail-tm-api-docs.md`. La captura **no** publica: esquemas de respuesta, códigos de error, campos de los mensajes, paginación, ni el nombre del endpoint SSE. "listen in real-time with SSE" es la única mención del mecanismo de streaming y **no viene con la URL del stream**.

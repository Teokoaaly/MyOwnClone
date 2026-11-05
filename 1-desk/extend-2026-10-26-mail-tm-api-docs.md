# Extensiones a átomos existentes — captura 2026-10-26-mail-tm-api-docs

Fuente: `sources/2026-10-26-mail-tm-api-docs.md` (captura `0-raw/2026-10-26-mail-tm-api-docs.md`), la página `docs.mail.tm/` de la API de mail.tm.
Ninguno de los átomos siguientes se ha modificado: las extensiones se proponen para el Editor.

=== EXTEND 2-atoms/2026-1026-mail-tm-alta-masiva-de-buzones-y-api-declaradas-en-la-home
## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-mail-tm-api-docs.md` (página `docs.mail.tm/`, capturada el 2026-10-26).

Este átomo registró, desde la home, que mail.tm declara "API access" y "a **quick way to register disposable mailboxes in bulk**" y que enlaza `docs.mail.tm/`, y que **el vault no había abierto esa documentación**. La captura nueva **abre la página**, y convierte el claim en documentación ejecutable: la API REST publica un flujo de **cuatro peticiones** —`GET https://api.mail.tm/domains`, `POST https://api.mail.tm/accounts`, `POST https://api.mail.tm/token`, `GET https://api.mail.tm/messages`— con la sección "How it works" describiendo la secuencia *Fetch domains → Create account → Use the address → Message arrives → Fetch messages* ([[2026-1027-mail-tm-flujo-de-cuatro-peticiones-para-obtener-un-buzon]]), un **spec OpenAPI v3 descargable** en `https://api.mail.tm/docs.jsonld` y docs interactivas en `https://api.mail.tm/` ([[2026-1027-mail-tm-spec-openapi-v3-descargable-y-docs-interactivas]]).

Consecuencia para el Editor: la frase "el vault no puede cotizar el correo de mail.tm" **queda desactualizada en su premisa**: ya se puede cotizar el correo de mail.tm en **coste de integración** (4 llamadas, sin API key, sin signup) y en **cadencia** (8 QPS por IP, [[2026-1027-mail-tm-limite-de-8-qps-por-ip-address]]), aunque siga sin poder cotizarlo en **precio unitario** —que es gratuito ([[2026-1027-mail-tm-acceso-gratuito-sin-api-key-ni-signup-ni-tiers]])—. Y aparece un dato de uso que la home no contenía: el paso 4 admite "**listen in real-time with SSE**", es decir, el correo como evento y no como polling ([[2026-1027-mail-tm-flujo-de-cuatro-peticiones-para-obtener-un-buzon]]), que es el modo de trabajo del bot de registro ([[2026-1024-chatgpt-creator-correo-temporal-y-otp-automatico-con-generator-email]]).
=== END

=== EXTEND 2-atoms/2026-1026-mail-tm-gratis-sin-cifras-con-financiacion-por-anuncios
## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-mail-tm-api-docs.md`.

Este átomo registró que la home de mail.tm declara "no hidden conditions, no paid extras" y que se financia con publicidad, y que **ninguna cifra del sector del correo podía cotizarse**. La sección "Pricing" de `docs.mail.tm/` publica ahora el régimen de acceso con cuatro frases literales: "**Completely free. No API key, no signup, no paid tiers.**"; "**No API key required**"; "Just call the endpoints. **No signup, no tokens to start.**" ([[2026-1027-mail-tm-acceso-gratuito-sin-api-key-ni-signup-ni-tiers]]).

Consecuencia para el Editor: el "gratis" deja de ser un **claim de marketing sin cifra** y pasa a ser un **régimen de acceso declarado por el proveedor**, con tres condiciones que sí son cotizables: coste monetario cero, **cero fricción de registro** (ni cuenta, ni onboarding, ni clave) y **cero planes de pago**. La contrapartida es que **el único límite publicado es técnico** —8 QPS por IP ([[2026-1027-mail-tm-limite-de-8-qps-por-ip-address]])—, sin SLA, sin cuota de unidades y sin contrato. Y la coherencia con el modelo de financiación por publicidad queda reforzada: un proveedor funded by ads no necesita autenticar a nadie porque no le cobra a nadie.
=== END

=== EXTEND 2-atoms/2026-1024-notletters-tres-vias-de-consumo-api-http-imap-y-web
## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-mail-tm-api-docs.md`.

Este átomo sostiene que NotLetters publica **tres vías de consumo sin documentar ninguna**: web, HTTP API en `api.notletters.com` e IMAP en `imap.notletters.com` por el 993 con SSL, y que el patrón "toda superficie, ninguna especificación" es una propiedad del proveedor. La captura de `docs.mail.tm/` **consolida la contraste**: mail.tm publica el **spec OpenAPI v3 descargable** (`https://api.mail.tm/docs.jsonld`), los **docs interactivos** (`https://api.mail.tm/`) y la sección "General Information" que lo anuncia ("The API follows the OpenAPI v3 spec. Download it or explore interactively.") ([[2026-1027-mail-tm-spec-openapi-v3-descargable-y-docs-interactivas]]).

Consecuencia para el Editor: la formulación defendible se estrecha a un criterio binario y verificable —**publicar el contrato o no publicarlo**. NotLetters (tres vías, cero especificación) y EmailOnDeck (cero vías) quedan en un polo; mail.tm, en el otro, y es **el primer proveedor de correo del corpus cuyo contrato técnico es descargable y parseable**, lo que permite auditar sus endpoints y esquemas mecánicamente en lugar de por lectura de prosa. Matiz que hay que conservar: **el `.jsonld` no ha sido descargado** y la captura no publica su contenido, el número de endpoints que contiene ni sus esquemas de respuesta.
=== END

=== EXTEND 2-atoms/2026-1024-chatgpt-creator-correo-temporal-y-otp-automatico-con-generator-email
## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-mail-tm-api-docs.md`.

Este átomo documenta la **función de biblioteca** del correo en el bot: generación con `generator.email`, recogida del OTP por polling y **cero partida de correo que cotizar**. La API de mail.tm ofrece el mismo resultado como producto, y además publica **el mecanismo de espera como opción de contrato**: el paso 4 de `GET https://api.mail.tm/messages` admite "Fetch messages via the API **or listen in real-time with SSE**" ([[2026-1027-mail-tm-flujo-de-cuatro-peticiones-para-obtener-un-buzon]]).

Consecuencia para el Editor: el **polling del OTP deja de ser una limitación del bot y pasa a ser una decisión de diseño del pipeline**. Con SSE, la espera del código de activación es un evento, no un temporizador, y eso elimina una latencia periódica por buzón —el modo de trabajo actual es "generar buzón, esperar, hacer polling" ([[2026-1024-chatgpt-creator-correo-temporal-y-otp-automatico-con-generator-email]]). La comparación de coste entre la función de biblioteca y el proveedor externo sigue sin resolverse por precio (mail.tm es gratis en dinero pero limitado a 8 QPS por IP, [[2026-1027-mail-tm-limite-de-8-qps-por-ip-address]]), pero **el modo de entrega del mensaje sí es ahora un parámetro de contrato del proveedor**, no un detalle de implementación.
=== END

=== EXTEND 2-atoms/2026-1026-mail-tm-el-farm-del-vault-ya-lo-usa-con-dominio-propio-y-clave-determinista
## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-mail-tm-api-docs.md`.

Este átomo registra el único uso real de mail.tm que el vault tiene documentado —dominio propio, usuario derivado de timestamp y **clave derivada del mismo timestamp, literal en [REDACTED]**— y sus dos problemas: una clave derivable no es una clave aleatoria, y "kept forever" convierte el buzón en un pasivo que hay que rotar. La API publicada **confirma que ese patrón es la forma de la interfaz programada, no una rareza del vault**: el `POST https://api.mail.tm/accounts` exige que el cliente **elija** dirección y contraseña (`{"address":"user@domain.com","password":"secret"}`) y el `POST /token` repite el mismo par, de modo que **el proveedor no genera nada** ([[2026-1027-mail-tm-la-api-permite-fijar-address-y-password-a-diferencia-de-la-web]]).

Consecuencia para el Editor: el átomo puede precisar su comparación con la web. La web promete credencial **autogenerada** ("a unique, automatically generated password"); la API **transfiere la elección al cliente**, con lo que la derivabilidad de la clave pasa de **accidente del uso del vault** a **decisión documentada del integrador**. Y aparece un matiz nuevo que el átomo no tenía: el ejemplo de la propia documentación usa un dominio **fuera del pool publicado** (`domain.com` frente al único `maxxspace.com` de `GET /domains`, [[2026-1027-mail-tm-un-solo-dominio-publicado-en-la-api-en-vivo]]), lo que deja abierto si la API acepta dominios externos —y por tanto si el "dominio propio" del farm del vault es una capacidad real de la API o un uso que el vault aún no ha verificado.
=== END

=== EXTEND 2-atoms/2026-1026-mail-tm-buzon-y-contrasena-nacen-al-abrir-el-sitio
## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-mail-tm-api-docs.md`.

Este átomo sostiene, desde la home, que en mail.tm la dirección y la contraseña "**nacen al abrir el sitio**", que el buzón "**is created automatically**" y que la credencial es "a **unique, automatically generated password**". La documentación de la API publica un **segundo camino de alta con modelo de credencial distinto**: el cliente envía `address` y `password` y el proveedor no genera ninguno ([[2026-1027-mail-tm-la-api-permite-fijar-address-y-password-a-diferencia-de-la-web]]).

Consecuencia para el Editor: el átomo debe **acotar su alcance a la vía web**, porque la formulación actual —"nacen al abrir el sitio"— es cierta de la interfaz y **falsa como descripción del servicio**: hay dos interfaces con dos modelos de credencial, la web con autogeneración y la API con elección del cliente. No es una contradicción del proveedor sino una distinción que la captura de la home no podía ver. La consecuencia operativa es de seguridad: **"autogenerada" era el atributo que hacía aceptable el buzón de mail.tm para un flujo de alta**, y por tanto ese atributo **no se puede extender a la vía API**, donde la unicidad y la aleatoriedad de la clave pasan a ser responsabilidad del integrador.
=== END

=== EXTEND 2-atoms/2026-1024-gptgrok2api-icloud-privacy-mail-fabrica-de-correo-con-techo-decreciente
## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-mail-tm-api-docs.md`.

Este átomo sostiene que el valor del sidecar de iCloud Privacy Mail es su **contrato explícito** —20/5/25 buzones por hora, tope de 750 acumulados por cuenta, temporizador de 60 minutos— y que sin contrato el buzón es un coste sin techo. mail.tm publica ahora **un contrato de otro tipo**: "The general quota limit is **8 queries per second (QPS) per IP address**", con el flujo de alta en **cuatro peticiones** ([[2026-1027-mail-tm-limite-de-8-qps-por-ip-address]], [[2026-1027-mail-tm-flujo-de-cuatro-peticiones-para-obtener-un-buzon]]).

Consecuencia para el Editor: el thread puede **comparar dos clases de contrato de recurso**, que antes no tenía. El del sidecar **acota unidades** y deja el ritmo sin techo; el de mail.tm **acota la cadencia y deja las unidades virtualmente ilimitadas** ("no limit" de unidades, [[2026-1026-mail-tm-buzon-conservado-para-siempre-y-sin-limite-de-unidades]]). Derivado del segundo contrato, que es aritmética del vault y no cifra del proveedor: **8 QPS ÷ 4 llamadas = 2 buzones/s y 7.200 buzones/hora por IP**, o **2,67 buzones/s y 9.600 buzones/hora** si `GET /domains` se cachea —frente a los **20 buzones/hora** del sidecar, es decir, **360 veces más rápido con una IP y sin contrato de unidades**. La hipótesis operativa que hay que dejar escrita: **el contrato útil es el que acota unidades**, y por eso el 8 QPS no sustituye al techo de 750, sino que lo hace irrelevante frente a un pasivo acumulativo sin cadencia de gasto.
=== END

=== EXTEND 2-atoms/2026-1026-mail-tm-correo-temporal-como-canal-de-codigos-de-activacion
## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-mail-tm-api-docs.md`.

Este átomo registró que la home de mail.tm declara el caso de uso "Receive messages and **account activation codes**", sin ningún mecanismo asociado. La documentación aporta el mecanismo: el buzón se crea con dos llamadas (`POST /accounts`, `POST /token`), se **lee** con `GET /messages` y esa lectura admite **dos modos** —consulta o "**listen in real-time with SSE**" ([[2026-1027-mail-tm-flujo-de-cuatro-peticiones-para-obtener-un-buzon]]).

Consecuencia para el Editor: la línea de "correo temporal como canal de códigos de activación" deja de ser un **caso de uso declarado por el proveedor** y pasa a tener un **contrato de entrega con dos modos**, lo que la hace comparable con la partida de SMS del mismo sector: HeroSMS, en cambio, **no puede sostener la cuenta** porque su número verifica el alta pero la recuperación de OpenAI se hace por email ([[2026-1023-hero-sms-numeros-de-un-solo-uso-y-recuperacion-por-email]]). Es decir, **el correo es el canal que sostiene la cuenta y el SMS solo el que la abre**, y ahora el canal del correo tiene además modo push.
=== END

=== EXTEND 2-atoms/2026-1024-notletters-tres-vias-de-consumo-api-http-imap-y-web
## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-mailsac-test-email.md`. Este átomo documenta que NotLetters publica tres vías de consumo —web, HTTP API en `api.notletters.com` e IMAP en `imap.notletters.com` por el 993 con SSL— y que **ninguna** viene documentada.

MailS.ac es el contrapunto útil del corpus para esa ausencia, porque es **el otro extremo del mismo sector**: publica un contrato de respuesta explícito ("The API supports checking mail for any address, and will return **200 with an empty array** if no mail exists there"), una lista de protocolos de integración ("REST, Web Sockets, and Webhooks"), una lista nominal de sistemas de CI soportados ("Jenkins, GitHub Actions, Selenium, GitLab CI, Bamboo, etc") y enlaces a documentación propia (`docs.mailsac.com`, `mailsac.com/pages/email-testing-api/`) ([[2026-1026-mailsac-la-api-devuelve-200-con-array-vacio-si-no-hay-correo]]).

La consecuencia para este átomo es de **criterio de clasificación**, no de rankings: la ausencia de especificación que este átomo registra en NotLetters **no es una propiedad del sector del correo desechable**, sino una propiedad de ese proveedor. En el mismo sector hay un operador que publica al menos el contrato de error —la ausencia de correo no es un error sino un `200` con array vacío— y que enlaza documentación. El matiz que debe añadirse: MailS.ac **tampoco publica los endpoints, los esquemas ni los parámetros**, de modo que sigue sin ser una especificación completa; la diferencia es que **declara que la tiene** y da un enlace verificable, lo que la hace auditable en principio ([[2026-1026-mailsac-la-direccion-de-reenvio-privado-exige-reservarla-primero]]).
=== END

=== EXTEND 2-atoms/2026-1024-notletters-correo-masivo-para-registros-y-lolzteam
## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-mailsac-test-email.md`. Este átomo describe el producto de NotLetters como **correo masivo para registros** ("Fast and reliable mail for bulk tasks", "create multiple mailboxes for site registrations", con el banner citando "Great for Lolzteam Market").

MailS.ac, del mismo sector y con el mismo tipo de producto declarado ("our **disposable email** services"), escribe explícitamente lo contrario: su producto es **correo de prueba de QA**, su caso de uso declarado es "check sign-up confirmations, password resets and one-time codes" en **pruebas automatizadas y pipelines de CI**, y su escala son "hundreds of Quality Assurance teams" ([[2026-1026-mailsac-correo-desechable-para-testing-de-qa-y-no-de-registro-masivo]]).

Eso obliga a matizar la lectura de este átomo: **"correo desechable" no es una categoría única con un uso único**. El corpus ya tiene al menos tres declaraciones de propósito explícitamente distintas para el mismo tipo de insumo —alta masiva de cuentas (NotLetters), aislamiento de identidad (mail.tm) y QA de software (MailS.ac)—, y esta última viene con el aviso formal de que **el buzón `@mailsac.com` es legible por cualquiera** ("anyone can read an @mailsac.com inbox, so use made-up data"), lo que la hace inservible para el uso de registro masivo que este átomo describe ([[2026-1026-mailsac-los-buzones-publicos-son-legibles-por-cualquiera]]).
=== END

=== EXTEND 2-atoms/2026-1022-email-inbound-contacto-sin-dominio-propio
## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-mailsac-test-email.md`. Este átomo documenta la pata de entrada del producto: un único destinatario genérico `contacto@myownclone.com` y los dominios inbound por tenant en "Coming soon".

MailS.ac ofrece dos piezas que ese "Coming soon" tendría que resolver, y que el vault puede usar como especificación de referencia. La primera es la **dirección de entrada por tenant sin configuración**: el "Zero Setup Subdomain service" —"Create subdomains in seconds"— con la capacidad de "quickly generate and assign email subdomains", más un **BYOD** explícito ("You can also bring your own domain!") ([[2026-1026-mailsac-subdominios-en-segundos-y-idioma-de-dominio-propio]]). La segunda es el **Email Capture service**, que existe para el caso de routing erróneo: "Prevent unintended emails to customers using our Email Capture service" y "ensuring email doesn't get sent to live users" ([[2026-1026-mailsac-email-capture-para-evitar-correos-a-clientes-reales]]).

La lectura para el producto: el proveedor externo **resuelve bien la parte de configuración** y la parte de **contención del error**, pero **no puede resolver la parte de marca** —un producto multi-tenant necesita que el remitente vea su propio dominio, no un subdominio de un tercero. El "Coming soon" no es por tanto un gap subsanable con un proveedor: es la parte que solo puede resolver el titular del dominio.
=== END

=== EXTEND 2-atoms/2026-1024-chatgpt-creator-correo-temporal-y-otp-automatico
## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-mailsac-test-email.md`. Este átomo documenta el flujo "OTP Verification — Automatic email OTP retrieval and validation" del bot de registro masivo, con el buzón generado vía `generator.email` y el código impreso en claro en la traza (`Validate OTP [483291] | 200`).

MailS.ac aporta el **dato de higiene que el corpus no tenía**, enunciado por un proveedor del mismo sector: **el buzón desechable público no es privado**, y el propio proveedor lo dice y lo estructura en dos niveles. "Public and free: anyone can read an @mailsac.com inbox, so use made-up data. Private when it matters: the free plan includes one private address, and paid plans from $18 a month add custom test domains that only your team can read". Y en la misma línea, para el caso de agentes: "Use a private address or private custom domain for sensitive test emails" ([[2026-1026-mailsac-los-buzones-publicos-son-legibles-por-cualquiera]], [[2026-1026-mailsac-el-faq-declara-explicitamente-que-los-agentes-de-ia-pueden-usarlo]]).

Esto **no corrige** este átomo, que sigue siendo una lectura fiel del README, pero **le añade una variable que el README no documenta**: si el buzón que el bot genera es del tipo público —anónimo y compartido—, el OTP que el bot teclea automáticamente estuvo, durante la ventana de espera, en una bandeja que **cualquiera podía leer**, y la validación automática lo convierte en un dato que además se imprime en el log. El vault no puede resolverlo porque el README **no publica el modelo de privacidad de `generator.email`**; lo que sí puede hacer es dejar la pregunta explícita y tratarla como riesgo asumido, no como flujo verificado.
=== END

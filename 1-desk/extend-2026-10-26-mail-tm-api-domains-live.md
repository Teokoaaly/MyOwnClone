# Extensiones a átomos existentes — captura 2026-10-26-mail-tm-api-domains-live

Fuente: `sources/2026-10-26-mail-tm-api-domains-live.md` (captura `0-raw/2026-10-26-mail-tm-api-domains-live.md`), respuesta en vivo de `GET https://api.mail.tm/domains`.
Ninguno de los átomos siguientes se ha modificado: las extensiones se proponen para el Editor.

=== EXTEND 2-atoms/2026-1026-mail-tm-mail-gw-como-marca-hermana-en-la-navegacion
## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-mail-tm-api-domains-live.md` (llamada en vivo a `GET https://api.mail.tm/domains`, capturada el 2026-10-26).

Este átomo registró que el nav de mail.tm publica **dos marcas de dominio** —`mail.tm` y `Mail.gw`— y **cero geografía**, y de ahí la lectura de que "**las marcas de dominio de un proveedor de correo desechable son la cobertura real**" y que la segunda marca es "rotación de superficie". La llamada en vivo devuelve **un único dominio disponible**, `maxxspace.com`, con el identificador `6aa6b995482bea6f4a97f585` y **dos marcas de tiempo idénticas**, `2026-09-13T00:00:00+00:00` —43 días antes de la captura— ([[2026-1027-mail-tm-un-solo-dominio-publicado-en-la-api-en-vivo]]).

Consecuencia para el Editor: la interpretación de "rotación de superficie" **queda presionada en su punto central**. Si `mail.gw` es la puerta a otro pool, la rotación existe y es invisible desde `api.mail.tm/domains`; si comparte pool, entonces **dos marcas de dominio no son dos dominios disponibles**, y la regla "las marcas son la cobertura real" pasa a ser una afirmación que la medición en vivo no sostiene para el pool de la API. Matiz que hay que mantener: **no se ha consultado `api.mail.gw/domains`**, y la captura **no conserva las claves del JSON** —solo los valores—, de modo que no puede leerse el nombre del campo de actividad. Verificación en vivo del 2026-10-27: la consulta devuelve el **mismo** dominio, el **mismo** identificador y las **mismas** dos fechas, y añade `hydra:totalItems: 1` —el estado capturado es reproducible.
=== END

=== EXTEND 2-atoms/2026-1024-chatgpt-creator-blacklist-de-dominios-persistida-en-archivo
## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-mail-tm-api-domains-live.md`.

Este átomo documenta la **memoria de fallos del bot**: un `blacklist.json` donde persisten los dominios de correo que no funcionan, con el argumento de que **un solo pool de dominios es un punto único de bloqueo**. La captura de la API en vivo convierte ese argumento en una **medición**: el pool publicado por `api.mail.tm/domains` es de **un solo nombre**, `maxxspace.com`, sin rotación observable durante los 43 días que separan su registro de la captura ([[2026-1027-mail-tm-un-solo-dominio-publicado-en-la-api-en-vivo]]).

Consecuencia para el Editor: el átomo puede **sustituir su hipótesis por una cota**. La blacklist del bot existe "porque un pool único es un punto único de bloqueo"; con un proveedor que **publica** un pool de capacidad 1, esa blacklist no tiene a dónde rotar: cuando `maxxspace.com` se bloquea en un destino, el flujo de correo externo no tiene dónde ir. Es la versión extrema del problema que el bot ya resuelve con memoria, y por eso el dato **sí es cotizable**: el pool de un proveedor gratuito y automatizable es, en el punto de bloqueo, **capacidad 1**. La otra cara de la moneda, y hay que escreverla: **eso no invalida el `blacklist.json` del bot**, porque el bot usa dominio propio y no el pool del proveedor —de hecho, esa es la razón de que el vault tenga un generador propio ([[2026-1024-chatgpt-creator-correo-temporal-y-otp-automatico-con-generator-email]]).
=== END

=== EXTEND 2-atoms/2026-1026-mail-tm-alta-masiva-de-buzones-y-api-declaradas-en-la-home
## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-mail-tm-api-domains-live.md`.

Este átomo registró el claim de la home: "API access" y "a **quick way to register disposable mailboxes in bulk**", sin ninguna cifra que permitiera dimensionarlo. Las dos capturas nuevas dan la dimensión que faltaba, y dan **dos límites distintos**: el pool de dominios publicado es de **un solo nombre** (`maxxspace.com`, [[2026-1027-mail-tm-un-solo-dominio-publicado-en-la-api-en-vivo]]) y el techo de llamadas es de **8 QPS por IP** ([[2026-1027-mail-tm-limite-de-8-qps-por-ip-address]]), con un flujo de **cuatro peticiones por buzón** ([[2026-1027-mail-tm-flujo-de-cuatro-peticiones-para-obtener-un-buzon]]).

Consecuencia para el Editor: el "alta masiva" de mail.tm **tiene ahora techo medible, y el techo no es de unidades sino de pool**. Derivado, aritmética del vault: con 4 llamadas por buzón y 8 QPS por IP, el máximo teórico es de **2 buzones/s y 7.200 buzones/hora por IP** (o **2,67/s y 9.600/h** cacheando `GET /domains`), lo que parece una cifra de alta masiva — pero **todo ese caudal sale de un único dominio disponible**, de modo que el rendimiento y la redundancia no escalan juntos. Es un matiz que hay que escribir en la tabla de coste por insumo: **cadencia alta y tolerancia a bloqueo cero** en el mismo proveedor.
=== END

=== EXTEND 2-atoms/2026-1024-gptgrok2api-icloud-privacy-mail-fabrica-de-correo-con-techo-decreciente
## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-mail-tm-api-domains-live.md`.

Este átomo sostiene que el sidecar de iCloud Privacy Mail es valuable por su **contrato explícito** de 20/5/25 buzones por hora y tope de 750 acumulados, y que sin contrato el buzón es un coste sin techo. La captura de mail.tm añade la pieza que faltaba en la comparación: **el contrato de cadencia sin contrato de unidades no se sostiene solo**, porque el pool de dominio disponible es de **uno** ([[2026-1027-mail-tm-un-solo-dominio-publicado-en-la-api-en-vivo]]).

Consecuencia para el Editor: el átomo puede **cerrar una tesis** que estaba abierta. El argumento de que "el contrato útil es el que limita unidades" queda respaldado por un caso donde el contrato público limita **lo otro** —la cadencia— y aun así el recurso no es gobernable, porque **un techo de 8 QPS con un pool de un dominio no limita nada de lo que importa**: ni las unidades, ni el riesgo de que el único dominio se bloquee. Es la lectura de governance completa: **cadencia, unidades y diversidad de pool son tres ejes de contrato distintos**, y un proveedor puede publicar uno y callar los otros dos.
=== END

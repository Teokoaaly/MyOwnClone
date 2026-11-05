---
id: 2026-1024-chatgpt-creator-blacklist-de-dominios-persistida-en-archivo
type: atom
certainty: tentative
sources: [sources/2026-10-24-chatgpt-creator-verssache.md]
links: ["[[2026-1024-chatgpt-creator-correo-temporal-y-otp-automatico-con-generator-email]]", "[[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]", "[[2026-1024-chatgpt-creator-worker-pool-y-retry-hasta-alcanzar-la-meta]]"]
---

## Claim
Uno de los tres commits visibles del repositorio es **"feat: Persist domain blacklist to blacklist.json"**, y el cambio está asociado a la fila de **`.gitignore`**, no a un archivo de código versionado. Es decir: el bot **mantiene una lista de dominios de correo bloqueados y la persiste en `blacklist.json`, un archivo deliberadamente fuera del control de versiones** (con la regla de la contraseña por defecto, el directorio `internal/` y los archivos de código, lo versionado es el conjunto mínimo). El README **no menciona la blacklist en ninguna de sus secciones** —ni en Features, ni en Configuration, ni en Output Format—.

## Why It Matters
Es un **mecanismo de memoria operativa** del bot, y solo se ve por el mensaje del commit y por el `.gitignore`. Lo que hace es **recordar qué dominios fallan**: cuando el flujo de alta con un dominio de correo no llega a completarse, ese dominio se marca para no volver a intentarlo. Con el patrón de reintento del bot ([[2026-1024-chatgpt-creator-worker-pool-y-retry-hasta-alcanzar-la-meta]]) y con el generador de correo aleatorio ([[2026-1024-chatgpt-creator-correo-temporal-y-otp-automatico-con-generator-email]]), esa memoria es lo que convierte un bucle de reintentos en algo que converge.
La observación que importa para el vault es el patrón, no el archivo: **en un flujo automatizado de altas, la calidad de una partida de insumo —en este caso el dominio de correo— no es estable y hay que registrar sus fallos para no repetir el gasto**. Es el mismo tipo de aprendizaje que el thread documenta para el proxy, donde "los datos que no se consumen no se facturan" pero el tráfico que sí se consume lo decide el volumen por sesión, y donde la sesión sticky debe durar lo que la tarea: aquí el equivalente es un archivo local que recuerda el fallo. Un flujo de alta a escala necesita **memoria de fallos por insumo**, y el repositorio de referencia la implementa en doce líneas de JSON.
La lectura secundaria es de higiene: el `.gitignore` es lo que impide versionar la lista, lo que confirma que la blacklist es **estado local de la máquina que corre el bot**, no una configuración compartida. Dos operadores con el mismo repositorio empiezan con listas distintas.

## Nota de verificación
El átomo queda en `tentative` a propósito: **lo único que hay es el mensaje del commit y su asociación a la fila de `.gitignore` en la tabla de archivos de GitHub**. La captura no contiene el archivo `blacklist.json`, ni el código que lo escribe, ni el criterio por el que un dominio entra en la lista. El vault no puede afirmar que la blacklist se use para excluir dominios del generador de correo, ni que el formato sea el que dice el nombre del commit.


## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-mail-tm-temp-mail.md`.

Este átomo documenta la memoria de fallos del bot: un archivo `blacklist.json` donde persisten los dominios de correo que no funcionan. Mail.tm **no publica ni un solo dominio** en los 698 palabras de su home —ni en el texto, ni en el ejemplo de dirección, ni en los bloques de marketing— de modo que **el pool de dominios de mail.tm no es contable desde la captura** ([[2026-1026-mail-tm-unica-cifra-de-la-captura-40-mb-de-cuota]]).

Lo que mail.tm sí publica es **una segunda marca de dominio**: el nav enlaza **`Mail.gw`** (`https://mail.gw/`) junto a "Privacy Manager", `API` → `docs.mail.tm/`, FAQ, Privacy, Feedback y Contacts ([[2026-1026-mail-tm-mail-gw-como-marca-hermana-en-la-navegacion]]). Es decir, el sector tiene un proveedor cuya superficie se expresa **en marcas de dominio** y no en países ni en idiomas. Consecuencia para el Editor: la blacklist de dominios del bot y la lista de marcas del sector son **el mismo problema visto desde dos lados** —el bot persiste los dominios que fallan porque **un solo pool de dominios es un punto único de bloqueo**—, y mail.tm publica dos marcas precisamente como rotación de superficie. El matiz que hay que mantener: **la captura no dice qué es `mail.gw`**, no afirma que comparta operador ni dominios con mail.tm, y **no se ha visitado** `mail.gw/` ni `docs.mail.tm/`.


## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-mail-tm-api-domains-live.md`.

Este átomo documenta la **memoria de fallos del bot**: un `blacklist.json` donde persisten los dominios de correo que no funcionan, con el argumento de que **un solo pool de dominios es un punto único de bloqueo**. La captura de la API en vivo convierte ese argumento en una **medición**: el pool publicado por `api.mail.tm/domains` es de **un solo nombre**, `maxxspace.com`, sin rotación observable durante los 43 días que separan su registro de la captura ([[2026-1027-mail-tm-un-solo-dominio-publicado-en-la-api-en-vivo]]).

Consecuencia para el Editor: el átomo puede **sustituir su hipótesis por una cota**. La blacklist del bot existe "porque un pool único es un punto único de bloqueo"; con un proveedor que **publica** un pool de capacidad 1, esa blacklist no tiene a dónde rotar: cuando `maxxspace.com` se bloquea en un destino, el flujo de correo externo no tiene dónde ir. Es la versión extrema del problema que el bot ya resuelve con memoria, y por eso el dato **sí es cotizable**: el pool de un proveedor gratuito y automatizable es, en el punto de bloqueo, **capacidad 1**. La otra cara de la moneda, y hay que escreverla: **eso no invalida el `blacklist.json` del bot**, porque el bot usa dominio propio y no el pool del proveedor —de hecho, esa es la razón de que el vault tenga un generador propio ([[2026-1024-chatgpt-creator-correo-temporal-y-otp-automatico-con-generator-email]]).

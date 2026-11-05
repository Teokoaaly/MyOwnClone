---
id: 2026-1027-mail-tm-un-solo-dominio-publicado-en-la-api-en-vivo
type: atom
certainty: solid
sources: [sources/2026-10-26-mail-tm-api-domains-live.md]
links: ["[[2026-1027-mail-tm-flujo-de-cuatro-peticiones-para-obtener-un-buzon]]", "[[2026-1026-mail-tm-mail-gw-como-marca-hermana-en-la-navegacion]]", "[[2026-1024-chatgpt-creator-blacklist-de-dominios-persistida-en-archivo]]"]
---

## Claim
La llamada en vivo a `GET https://api.mail.tm/domains` capturada el 2026-10-26 devuelve **un único dominio**: `maxxspace.com`. La captura conserva los valores de la respuesta pero no las claves del JSON —el extractor dejó la línea como una concatenación sin comas, llaves ni dos puntos—, de modo que lo que la fuente sostiene de forma literal es: **un solo valor de dominio**, `maxxspace.com`, junto al identificador `6aa6b995482bea6f4a97f585`, el fragmento `10` y **dos marcas de tiempo idénticas**, `2026-09-13T00:00:00+00:00` y `2026-09-13T00:00:00+00:00`. El puntero de captura en `0-raw/` titula el fichero "(1 domain available)".

## Why It Matters
Es la **primera medición en vivo del pool de dominios del sector de correo desechable del vault**, y el dato es fuerte: la home de mail.tm publica dos marcas de dominio —`mail.tm` y `Mail.gw`— y **cero geografía**, y el átomo que registró ese hecho lo interpretó como "rotación de superficie", es decir, cobertura ([[2026-1026-mail-tm-mail-gw-como-marca-hermana-en-la-navegacion]]). La API en vivo dice otra cosa: **el pool publicado por `api.mail.tm/domains` es de un solo nombre**. Una marca de la API y otra marca de la web no son dos pools: son dos puertas al mismo pool, o la segunda marca tiene su propio pool que esta captura no midió. El vault no puede distinguirlo todavía.

La consecuencia operativa es de **punto único de bloqueo**, y aquí el corpus sí tiene la contraejemplo documentada: el bot de registro persiste en un `blacklist.json` los dominios de correo que fallan ([[2026-1024-chatgpt-creator-blacklist-de-dominios-persistida-en-archivo]]). Con **un** dominio, la blacklist no tiene a qué rotar: cuando `maxxspace.com` se bloquea en un destino, el flujo no tiene dónde ir. Es la versión extrema del problema que el bot ya resuelve con memoria de fallos, y por eso el dato **sí** es cotizable para el producto: el pool de un proveedor gratuito y automatizable es, en el punto de bloqueo, un pool de capacidad 1.

Y hay un segundo detalle que solo se ve en vivo: **las dos fechas del registro son la misma**, `2026-09-13T00:00:00+00:00`, en una captura del 2026-10-26 —43 días antes. El registro del dominio no se ha movido desde que se creó, lo que encaja con un pool estático y sin rotación.

## [FRICTION]
> [[2026-1026-mail-tm-mail-gw-como-marca-hermana-en-la-navegacion]] concluye que "**las marcas de dominio de un proveedor de correo desechable son la cobertura real**" y que, al publicar una segunda marca (`mail.gw`), mail.tm hace "rotación de superficie para no depender de un único dominio bloqueable".
> Este átomo presiona esa lectura en su punto central: **el pool publicado por la API es de un solo dominio**, `maxxspace.com`, con un registro de 43 días sin cambios. O `mail.gw` es la puerta de entrada a **otro pool** —y entonces hay dos pools que esta captura no ha medido y la "rotación de superficie" sí existe pero es invisible desde `api.mail.tm/domains`—, o `mail.gw` y `mail.tm` comparten un único pool de un dominio, en cuyo caso la segunda marca **no aporta cobertura de dominio** y la regla "las marcas son la cobertura real" queda presionada por la medición en vivo. Marcado para juicio humano, no auto-resuelto: **no se ha consultado `api.mail.gw/domains`** ni ninguna ruta de `mail.gw`, y la captura **no conserva las claves del JSON**, así que no puede leerse el nombre del campo de actividad ni confirmarse que el registro esté activo más allá del valor que aparece en la línea. La consulta de control del 2026-10-27 sí devuelve `isActive: true` e `isPrivate: false` para ese mismo registro.

## Nota de verificación
La fuente (`sources/2026-10-26-mail-tm-api-domains-live.md`) es una línea de valores sin delimitadores: `6aa6b995482bea6f4a97f585maxxspace.com102026-09-13T00:00:00+00:002026-09-13T00:00:00+00:00`. La afirmación "**un único dominio**" se apoya en que solo aparece **una** cadena de dominio, corroborada por el título del puntero de captura en `0-raw/` ("1 domain available"); el nombre de los campos JSON **no** es recuperable de la captura.

**Verificación en vivo del 2026-10-27**: una consulta de control a `https://api.mail.tm/domains` (HTTP 200) devuelve el **mismo** único dominio `maxxspace.com`, con el **mismo** identificador `6aa6b995482bea6f4a97f585` y las **mismas** dos marcas de tiempo `2026-09-13T00:00:00+00:00`, y añade el metadato que la captura perdió: la colección declara `hydra:totalItems: 1` y el miembro trae `isActive: true`, `isPrivate: false`. El fragmento `10` de la línea capturada **coincide con esos dos booleanos concatenados**, lo que sugiere que el extractor sí conservó los valores de todos los campos y solo perdió las claves. Es decir, **el estado capturado es reproducible**, no un transitorio.

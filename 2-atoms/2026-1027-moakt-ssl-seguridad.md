---
id: 2026-1027-moakt-ssl-seguridad
type: atom
certainty: solid
sources: [sources/2026-10-27-moakt.md]
links: ["[[2026-1024-notletters-tres-vias-de-consumo-api-http-imap-y-web]]", "[[2026-1026-mail-tm-buzon-y-contrasena-nacen-al-abrir-el-sitio]]"]
---

## Claim
Todos los emails recibidos en la bandeja de email temporal se envían al usuario a través de una conexión SSL, garantizando privacidad y confidencialidad de los mensajes intercambiados.

## Why It Matters
La encriptación SSL protege el contenido de los correos interceptados durante la transmisión, lo cual es crítico para usuarios que manejan información sensible aunque sea en un contexto temporal.

## [FRICTION]
> [[2026-1024-notletters-tres-vias-de-consumo-api-http-imap-y-web]] declara que NotLetters publica tres vías de consumo (web, HTTP API, IMAP por 993 con SSL) sin documentar ninguna, mientras que Moakt declara explícitamente SSL para todos los emails entrantes. La discrepancia está en el alcance: Notletters no declara SSL por defecto en su home, mientras que Moakt lo declara como política global. Ambas pueden ser correctas para sus respectivos productos, pero la diferencia de transparencia es notable. Marcado para juicio humano, no auto-resuelto.
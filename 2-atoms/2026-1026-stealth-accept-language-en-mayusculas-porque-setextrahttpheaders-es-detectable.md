---
id: 2026-1026-stealth-accept-language-en-mayusculas-porque-setextrahttpheaders-es-detectable
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-stealth.md]
links: ["[[2026-1024-chatgpt-creator-token-sentinel-y-cabeceras-de-traza-datadog]]", "[[2026-1024-chatgpt-creator-tls-fingerprinting-con-perfiles-chrome-aleatorios]]", "[[2026-1026-stealth-user-agent-override-y-navigator-vendor-como-capa-de-identidad]]", "[[2026-1026-puppeteer-extra-604-commits-559-tags-y-ultimo-commit-en-marzo-de-2023]]"]
---

## Claim
El changelog documenta una detección a nivel de **cabecera HTTP**, no de objeto de JavaScript: en `v2.4.0`, "New: `accept-language` — Adds a missing `Accept-Language` header in headless (**capitalized correctly**, `page.setExtraHTTPHeaders` is all lowercase which can be detected)". En `v2.4.2`/`v2.4.1`: "Improved: `accept-language` — More robust and it's now possible to set a custom locale if needed". Y en `v2.4.7`: "New: `user-agent-override` — Used to set a stealthy UA string, language & platform. **This also fixes issues with the prior method of setting the `Accept-Language` header through request interception** (#104, kudos to @Niek)".

## Why It Matters
Es el dato más fino de toda la captura sobre **qué signals son detectables**, porque no es la señal la que se tapa: es **la forma de introducirla**. La diferencia entre `Accept-Language` y `accept-language` —mayúsculas contra minúsculas— es visible en el borde del navegador y en cualquier proxy, y el propio plugin la detecta como tal. Es decir: **el mecanismo de ofuscación puede ser la señal**. Y en `v2.4.7` el autor admite que el método anterior (interceptar la petición para poner la cabecera) **era defectuoso y fue retirado**, sustituido por un override a nivel de cliente.
El vault ya tenía registrado el extremo opuesto de esta capa: el bot Go de `chatgpt-creator` **no solo imita la huella TLS del cliente legítimo, sino que emite cabeceras de traza con el formato Datadog** —es decir, también ahí el formato de la cabecera es parte de la señal ([[2026-1024-chatgpt-creator-token-sentinel-y-cabeceras-de-traza-datadog]]). Y al otro lado del vault, la huella TLS con perfiles Chrome aleatorizados es la capa donde el cliente HTTP **sí tiene que construir su identidad a mano** ([[2026-1024-chatgpt-creator-tls-fingerprinting-con-perfiles-chrome-aleatorios]]). Las tres fuentes, leídas juntas, dan una **regla transferible**: en la elusión, **la caja de la señal importa tanto como el valor**, y además la señal se reparte en capas —transporte, cabeceras, objeto de navegador— que no se arreglan con la misma herramienta. Un `Accept-Language` mal escrito no es un detalle cosmético: es un *tell* que delata automatización.
Y hay una lectura de arquitectura: `user-agent-override` **sustituye** a la interceptación de peticiones, es decir, el plugin resuelve el problema **en la capa de cliente y no en la capa de red**. Eso reduce superficie de parcheo y evita que el proxy de interceptación se convierta en un vector de detección.

Nota de verificación: las tres citas son literales del changelog. La captura **no** publica el código de la evasión ni su documentación de directorio, ni una lista de cabeceras controladas más allá de `Accept-Language`.

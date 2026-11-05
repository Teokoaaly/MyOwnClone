---
id: 2026-1026-emailondeck-captura-minima-344-palabras-y-cero-especificacion-operativa
type: atom
certainty: tentative
sources: [sources/2026-10-25-emailondeck-temp-mail.md]
links: ["[[2026-1024-notletters-captura-minima-sin-dominios-ni-limites-ni-condiciones]]", "[[2026-1024-notletters-tres-vias-de-consumo-api-http-imap-y-web]]", "[[2026-1023-lzt-captura-parcial-sin-precios-ni-stock]]"]
---

## Claim
La captura de `emailondeck.com` es una **home de marketing de 344 palabras** y, leída entera, **no publica ninguna especificación operativa**: no hay lista ni formato de dominios, ni patrón de direcciones, ni límite de buzones, ni plazo de retención, ni forma de pago, ni reembolso, ni SLA, ni condiciones (solo un enlace "Terms"), ni documentación de API. Lo que sí publica, enumerado, es: **11 idiomas** (English, Français, Español, Deutsch, Nederlands, Português, Türkçe, Русский, bahasa Indonesia, 中文(台灣), العربية), un contador de **"Over 215,158,204 temporary emails processed"**, un aviso **"SSL and TLS certified"**, el claim **"As Seen On CBS News, FOX, NBC, abc"**, un enlace **"Spy Pixel Scanner"**, y cinco enlaces de navegación (**TEMPORARY EMAIL BLOG, FAQ, RECOVER EMAIL, PRO**, más Glossary y "Browse Popular Temp Mail Uses" en el pie).

## Why It Matters
Es la segunda confirmación del patrón que el vault ya había registrado con NotLetters: **la opacidad del sector de correo desechable no es una peculiaridad de un proveedor, es la norma**. El primer caso lo catalogó como ausencia singular —"el proveedor de correo masivo más explícitamente orientado a registros que ha caído en la captura" publicaba 172 palabras y ninguna especificación ([[2026-1024-notletters-captura-minima-sin-dominios-ni-limites-ni-condiciones]])— y ahora aparece **otro** proveedor, de otro país, de otro modelo de negocio y de otra escala, con el mismo perfil: cero catálogo operativo.
Y hay un contraste de **superficie** que es lo único medible: NotLetters publica tres vías de consumo —web, HTTP API en `api.notletters.com` e IMAP en `imap.notletters.com` por el 993 con SSL— sin documentar ninguna ([[2026-1024-notletters-tres-vias-de-consumo-api-http-imap-y-web]]), mientras que EmailOnDeck **no publica ninguna vía de consumo programable**: su superficie es un formulario de dos pasos en el navegador. La automatización del buzón disposable no está ni siquiera insinuada en la API de este último. El resto del contenido es de **escritura de marketing**, no de datos: los once idiomas, el sello de SSL/TLS, los logos de medios y el contador de 215 millones son afirmaciones sin desglose, en la misma línea que el precedente ya registrado de render parcial sin un solo precio ([[2026-1023-lzt-captura-parcial-sin-precios-ni-stock]]).
La consecuencia para el vault es una regla de lectura, no un dato: **una home de correo temporal no es una fuente de coste ni de rendimiento**, por mucho que en ella se anuncien SSL, prensa y cientos de millones de correos. Sirve como fuente de categoría.

## [FRICTION]
> [[2026-1024-notletters-captura-minima-sin-dominios-ni-limites-ni-condiciones]] presenta la ausencia de especificación de NotLetters como un hecho **de ese proveedor** ("lo verificable es que la captura no lo trae, no que el servicio no lo tenga") y delimita el alcance: del proveedor más orientado a registros del corpus "el vault solo puede afirmar precio nominal, orden de magnitud y superficies de acceso".
> Este átomo presiona ese alcance en un punto: si la segunda captura del sector reproduce exactamente el mismo perfil —cero dominios, cero límites, cero retención, cero condiciones, cero API— entonces la ausencia **no es una característica de NotLetters sino del sector**, y el enunciado correcto pasa a ser de alcance general ("las homes públicas de correo desechable no son fuentes de coste"), no específico ("este proveedor es opaco"). Ambas no pueden ser la lectura correcta a la vez: o la opacidad es accidental de dos proveedores independientes, o es una característica estructural del producto que se presenta en marketing. Marcado para juicio humano, no auto-resuelto: dos capturas no hacen una regla, y no se ha visitado ninguna de las páginas enlazadas.

Nota de verificación: la enumeración de idiomas, el contador, el sello de SSL/TLS, el claim de prensa y los enlaces de navegación están transcritos del texto de la captura; la ausencia de especificación operativa está comprobada sobre el texto completo (**no** se han visitado `FAQ`, `Terms`, `recover_email_address.php`, `pro.emailondeck.com` ni "Spy Pixel Scanner").


## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-mail-tm-temp-mail.md`.

Este átomo generaliza, tras dos capturas del sector, que "**una home de correo temporal no es una fuente de coste ni de rendimiento**" y la usa como **fuente de categoría**. La tercera captura del sector **obliga a matizar esa generalización en tres puntos verificables**:

1. **Una capacidad cuantificada aparece**: "**0 B/40 MB**", única cadena numérica de los 698 palabras ([[2026-1026-mail-tm-unica-cifra-de-la-captura-40-mb-de-cuota]]). No es precio ni rendimiento, pero sí es un límite de capacidad.
2. **Una documentación enlazada aparece**: `docs.mail.tm/`, y con ella la mención explícita de "API access" y de "a quick way to register disposable mailboxes in bulk" ([[2026-1026-mail-tm-alta-masiva-de-buzones-y-api-declaradas-en-la-home]]).
3. **Un ciclo de vida explícito aparece**: "kept forever", "unlimited number", "no limit" ([[2026-1026-mail-tm-buzon-conservado-para-siempre-y-sin-limite-de-unidades]]).

La formulación que el Editor debería dejar escrita: **"las homes de correo desechable no son fuentes de coste ni de rendimiento" sigue siendo cierto, pero ya no es cierto que no publiquen especificación operativa**. La regla correcta pasa a ser: **el coste sigue sin publicarse en ningún proveedor del sector**; lo que se publica es capacidad, documentación y ciclo de vida. Y el matiz metodológico que hay que conservar: la captura **no etiqueta** la cadena "0 B/40 MB", de modo que el vault puede citarla como **capacidad observada**, no como especificación.

---
id: 2026-1026-emailondeck-borrado-seguro-y-pagina-de-recuperacion
type: atom
certainty: solid
sources: [sources/2026-10-25-emailondeck-temp-mail.md]
links: ["[[2026-1024-gptgrok2api-icloud-privacy-mail-fabrica-de-correo-con-techo-decreciente]]", "[[2026-1024-notletters-captura-minima-sin-dominios-ni-limites-ni-condiciones]]", "[[2026-1024-chatgpt-creator-correo-temporal-y-otp-automatico-con-generator-email]]"]
---

## Claim
La home de `emailondeck.com` incluye entre sus cinco ventajas, con icono propio, **"Emails are constantly being securely deleted"**, y en la barra de navegación ofrece un enlace con etiqueta **"RECOVER EMAIL"** que apunta a `www.emailondeck.com/recover_email_address.php`. La captura **no describe** el mecanismo de recuperación: ni qué datos pide, ni en qué plazo, ni en qué condiciones, ni si aplica a cualquier buzón o solo a direcciones concretas.

## Why It Matters
Es la primera vez que el corpus del vault encuentra un proveedor de correo desechable que **vende las dos cosas opuestas**: el borrado como promesa de privacidad y, a la vez, la **recuperación como función de navegación**. Es decir, el buzón no es un puro *burner* unidireccional: el proveedor reconoce que el destinatario puede necesitar volver a él. Eso importa porque el único átomo del corpus que hasta ahora especificaba el **ciclo de vida** de un buzón desechable era el sidecar de iCloud Privacy Mail del bot, con su contrato explícito —20 buzones/hora, 5/hora, tope de **750 buzones acumulados**, temporizador de 60 minutos y **retirada de correos por plataforma** ([[2026-1024-gptgrok2api-icloud-privacy-mail-fabrica-de-correo-con-techo-decreciente]])— y allí la operación de correo era un recurso con techo y estado, no un ciclo ignorado.
La diferencia de fondo es de **modelo de producto**: el sidecar trata el correo como insumo de registro y lo consume; EmailOnDeck trata el correo como un buzón de usuario y por eso ofrece **recuperarlo**. Para el producto del vault, esto es la señal de que el buzón desechable tiene dos formas de vida que se mezclan en la páginas: la de **insumo de alta** (una dirección por registro, se agota) y la de **casilla personal desechable** (una dirección que se consulta, se recupera, se vuelve a mirar). El bot de registro con generador integrado ([[2026-1024-chatgpt-creator-correo-temporal-y-otp-automatico-con-generator-email]]) solo conoce la primera.

## [FRICTION]
> [[2026-1024-gptgrok2api-icloud-privacy-mail-fabrica-de-correo-con-techo-decreciente]] describe el correo del corpus como un recurso con **ciclo de vida medible y retirable** —techo de 750 buzones por cuenta, correos de registro retirados de forma aislada por plataforma— y [[2026-1024-notletters-captura-minima-sin-dominios-ni-limites-ni-condiciones]] señala que la captura de NotLetters no publica ni un plazo de retención.
> Este átomo presiona esa lectura del buzón desechable en un punto: si el borrado es la promesa central ("constantly being securely deleted") **y** la recuperación es una función publicada, entonces **el borrado y la recuperación son la misma operación en dos direcciones** y no puede ser verdad a la vez comoexclusive: o el proveedor borra de forma que no se puede recuperar —y entonces "RECOVER EMAIL" es marketing o cubre solo casos distintos, que la captura no describe— o el buzón conserva su contenido y "securely deleted" describe otra cosa, por ejemplo el borrado de los mensajes no leídos. Marcado para juicio humano, no auto-resuelto: **no se ha visitado `recover_email_address.php`**, así que el vault no puede arbitrarlo.

Nota de verificación: la ventaja y el enlace están transcritos literalmente; el contenido de la página de recuperación **no ha sido capturado**.

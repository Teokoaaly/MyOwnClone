---
id: 2026-1024-noones-superficie-publica-productos-y-dominios-espejo
type: atom
certainty: solid
sources: [sources/2026-10-23-noones-p2p.md]
links: ["[[2026-1024-noones-bloquea-ip-estadounidense-con-mensaje-explicito]]", "[[2026-1023-herosms-api-y-partners-de-registro-masivo]]", "[[2026-1024-noones-verificacion-basica-l1plus-revision-manual-hasta-72h]]"]
---
## Claim
Incluso en la página de bloqueo, la navegación y el pie de NoOnes exponen su superficie completa: productos **P2P** (`/trading`), **SnapX** (`/buy-sell-gift-card`), **Swap** (`/en/swap`) y **NoOnes wallet** (`/explore-wallet`); enlaces a **"API documentation"** (`dev.noones.com`), **"Partner program"**, **"NoOnes status"** (`status.noones.com`), **"Crypto calculator"** y **"Import feedback"**; y una sección **"Mirror domains"** con tres dominios: **noones.com, noones.app, noones.global**.

## Why It Matters
Tres cosas en un mismo pie. (1) **Tres dominios espejo** = tres puertas de entrada distintas: un solo dominio caído o bloqueado no es el fin de la operación, y la diferencia entre `.com` y `.app`/`.global` puede ser de enforcement, no de marca. (2) **API documentada + partner program** es exactamente la superficie que el vault ya vio en HeroSMS —API sin documentación y socios cuyo producto es el registro automatizado ([[2026-1023-herosms-api-y-partners-de-registro-masivo]])—; aquí, en cambio, la API está **enlazada y documentada**, lo que apunta a un modelo de integradores serio y no a un intermediario opaco. (3) Los cuatro productos (P2P, SnapX, swap, wallet) más el "Import feedback" indican un producto con **on-ramp, off-ramp y feedback loop de importación**, no solo un exchange. Ninguna de estas afirmaciones dice que el acceso funcione desde una IP bloqueada: la página que las expone es, precisamente, la que rechaza la conexión ([[2026-1024-noones-bloquea-ip-estadounidense-con-mensaje-explicito]]).


## Nota de extensión 2026-10-26
El átomo afirma que la superficie pública de NoOnes expone un enlace **"API documentation"** que apunta a `dev.noones.com`, y lo lee como señal de "un modelo de integradores serio y no a un intermediario opaco" frente a HeroSMS. La captura del 2026-10-25 permite precisar **qué es exactamente `dev.noones.com`**: son **547 palabras de landing de marketing** —cuatro bullets ("Automate your trading", "Receive trade activity notifications", "Trade on behalf of your clients", "Automatically update offer margins"), cuatro bloques de caso de uso con su "Read more" y un selector "Choose Your Format" con dos CTA a `dev.noones.com/dashboard/direct-access` y `dev.noones.com/dashboard/delegated-access`. **No hay ni un endpoint, ni un esquema de autenticación, ni un rate limit, ni un precio, ni un SLA.** El botón "Get Started" apunta a `#chooseYourFormat`, un ancla de la misma página, no a un panel de referencia.

El matiz que la extensión añade sin contradecir el átomo: el enlace no está roto ni es decorado —el subdominio **funciona y responde con contenido**—, pero lo que se enlaza desde el pie no es "documentación", sino **el escaparate de dos formatos de acceso**, y lo técnico vive detrás del login. La distinción que conviene conservar es, por tanto, entre "hay un sitio propio para desarrolladores" (cierto, y sigue siendo una diferencia real con HeroSMS, que no publica ni el suyo) y "hay documentación técnica accesible" (no verificable con esta captura).

Ver también: [[2026-1026-noones-dev-noones-sin-precios-ni-limites-ni-documentacion-publica]] y [[2026-1026-noones-api-dos-formatos-directo-y-delegado]].

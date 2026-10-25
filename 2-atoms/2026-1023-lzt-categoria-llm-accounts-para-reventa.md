---
id: 2026-1023-lzt-categoria-llm-accounts-para-reventa
type: atom
certainty: solid
sources: [sources/2026-10-22-lzt-market-home.md, sources/2026-10-23-notletters-mail.md]
links: ["[[2026-1023-5sim-catalogo-28-servicios-ia]]", "[[2026-1023-lzt-venta-individual-y-masiva-por-categoria]]", "[[2026-1023-lzt-categorias-gaming-y-social-network]]", "[[2026-1023-5sim-chatgpt-verificacion-stock-13-7-millones]]"]
---

## Claim
`LLM Accounts` es una **categoría de primera clase del lado vendedor** de lzt.market, con las dos vías: alta individual (`/llm/item/add`) y carga masiva (`/mass-upload/llm/start`). Aparece junto a `VPN`, `Hytale` y `OnlyFans`, y esas cuatro son precisamente las categorías que **no** figuran en la navegación de compra visible de la captura, que solo muestra Gaming (17) y Social network (5) ([[2026-1023-lzt-categorias-gaming-y-social-network]]). El nombre de la ruta es `llm`, sin desglose de proveedor: la captura **no** dice qué modelos concretos se venden (ChatGPT, Claude, Gemini…), ni en qué país o con qué estado de verificación.

## Why It Matters
Confirma que el mercado de **cuentas de IA ya hechas** existe como Vertical con suministro por lotes, no solo como infraestructura de verificación: 5sim y HeroSMS venden el *número* con el que se crea la cuenta ([[2026-1023-5sim-chatgpt-verificacion-stock-13-7-millones]]), y lzt.market vende la cuenta ya creada y verificada, con categoría propia y con carga masiva incluida ([[2026-1023-lzt-venta-individual-y-masiva-por-categoria]]). Eso significa que el coste de una identidad de IA usable en producción no es solo el del SMS: hay un segundo mercado, el de la cuenta revocada o de stock ya exista, cuyo precio la captura no publica.
El orden de las dos categorías en la URL también delata la línea del producto: `item/add` (una cuenta) y `mass-upload` (lotes) son la misma operación a distinta escala, o sea que el vendedor es un *farmer* con volumen, no un usuario final.

## [FRICTION]
> [[2026-1023-5sim-catalogo-28-servicios-ia]] (escrita hoy, a partir del catálogo de 5sim) afirma que la verificación por SMS de cuentas de IA "es una categoría de primer orden del proveedor", que el coste de la identidad verificada de IA "es una partida con mercado propio y con inventario propio", y que esa categoría "es exactamente la que un flujo de captación automatizada tendría que resolver **por su cuenta, sin que ningún proveedor de LLM del vault la cubra hoy**".
> Este átomo presiona esa creencia en un punto concreto: la parte de "resolver por su cuenta" ya está cubierta por un tercero. lzt.market ofrece cuentas de IA listas, con vía de alta individual y de carga masiva, lo que convierte el aprovisionamiento de identidades de IA en un **input comprable a terceros**, no en una construcción propia. El proveedor de LLM del vault no lo cubre, pero el mercado sí.
> Ambas no pueden ser completamente correctas: o la categoría `LLM Accounts` es marginal (y entonces no merece la categoría de primera clase ni la ruta de carga masiva que la captura sí muestra), o el insumo de identidad verificada del vault tiene un precio de mercado que no es el del SMS y que todavía no está medido. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
Los nombres de categoría y las rutas están transcritos literalmente. La captura **no** publica: qué modelos de IA se venden, precio unitario, stock, país de la cuenta, estado de verificación ni garantía.

## [NOTA 2026-10-24 — NotLetters]
A partir de `sources/2026-10-23-notletters-mail.md`. La cadena de valor que este átomo describe (proveedor de número → registro masivo → cuenta revendida en lzt.market) tiene ahora **una pata de correo con su propio proveedor de mercado**: la home de `notletters.com` lleva en el banner literal "**Great for Lolzteam Market**" y vende buzones para "site registrations" ([[2026-1024-notletters-correo-masivo-para-registros-y-lolzteam]]). Es decir, el mercado que este átomo documenta como destino es también el **caso de uso declarado** de un proveedor de su cadena de insumos. El matiz que sigue vigente es que ese aviso de "Lolzteam Market" es un claim de marketing de un tercero, no una prueba de que sus buzones alimenten esas cuentas concretas ([[2026-1024-notletters-captura-minima-sin-dominios-ni-limites-ni-condiciones]]).

## [NOTA 2026-10-24 — la pieza que faltaba: el bot que produce las cuentas]
A partir de `sources/2026-10-24-chatgpt-creator-verssache.md`. Este átomo documentaba el **destino** de la cadena (lzt.market revendiendo cuentas de IA por lotes) y el thread documentaba los **insumos** (número, correo, captcha, proxy), pero faltaba el **eslabón de producción**: la herramienta que consume esos insumos y genera el fichero de credenciales que se sube a `/mass-upload/llm/start`. Existe y es pública: `verssache/chatgpt-creator`, MIT, 338 estrellas, 90 forks, Go 1.21+, con pool de workers, TLS fingerprinting, correo temporal propio vía `generator.email`, OTP automático y salida en `email|password` ([[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]], [[2026-1024-chatgpt-creator-salida-en-archivo-email-contrasena]]).
Dos consecuencias para este átomo. La primera: **el formato de la carga masiva es ahora legible** — `email|password`, separador de pipe, sin metadatos ([[2026-1024-chatgpt-creator-salida-en-archivo-email-contrasena]]). La segunda, y es la que aprieta: **el pipeline de producción no transporta estado de calidad**. No hay campo de país, de verificación, ni de caducidad, mientras que el mercado chino sí declara todo eso en el título de venta ([[2026-1023-priceai-channels-modos-de-entrega-declarados-en-los-titulos]]). El fichero de salida de la fábrica no lleva la garantía que el mercado luego vende.

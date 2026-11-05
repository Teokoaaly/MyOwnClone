---
id: 2026-1026-github-search-suno-api-plus-pool-de-cuentas-y-captcha-comprado
type: atom
certainty: solid
sources: [sources/2026-10-25-github-search-suno-openai.md]
links: ["[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1024-gptgrok2api-registro-protocolo-sin-navegador-y-captcha-solver-integrado]]", "[[2026-1026-anticaptcha-trece-tipos-con-precio-por-1000]]"]
---

## Claim
`ShowSnowBlood/suno-api-plus` —**1 estrella, 1 fork, TypeScript, LGPL-3.0, 50.893 KB, 6 topics** (`docker`, `music-generation`, `nextjs`, `openai-api`, `self-hosted`, `suno`), `homepage` apuntando a su propia URL de GitHub, `created_at` 2026-07-19T11:22:01Z y `pushed_at` 2026-07-20T01:45:13Z, o sea **14 horas y 23 minutos de vida de código**— describe su función en una línea: *"Enhanced Suno API with admin dashboard, multi-account pool, OpenAI-compatible auth, YesCaptcha/2Captcha, cookie tools"*. Es el único item del corpus que **nombra proveedores de captcha** y el único que declara **pool de cuentas** además de autenticación compatible con OpenAI.

## Why It Matters
Este item es el que convierte la categoría de "curiosidad de GitHub" en **arquitectura de coste medible**, porque sus cuatro piezas son exactamente las partidas que el vault tiene cotizadas en la thread de economía de la verificación: **pool de cuentas** (la partida de credenciales), **captcha comprado por catálogo** —el propio repo nombra a **2Captcha** y **YesCaptcha**— , **autenticación compatible con OpenAI** (el formato que los relays de `new-api` ya hablan) y **cookie tools** (extracción y rotación de sesión). Es la versión "todo comprado" del arquetipo: el mismo que `gptGrok2api` resolvió internalizando el captcha con navegador real en Docker ([[2026-1024-gptgrok2api-registro-protocolo-sin-navegador-y-captcha-solver-integrado]]).
El vault ya tiene el precio de lista del captcha commoditizado —$0,5 a $2,99 por 1000 en los tipos estándar, con outliers como FunCaptcha a $50 ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]) y un segundo proveedor con 13 tipos publicados ([[2026-1026-anticaptcha-trece-tipos-con-precio-por-1000]])— y por tanto **puede cotizar este item**: una API de Suno self-hosted con pool de cuentas y captcha de catálogo tiene una partida de captcha que es $/1000, no infraestructura. Ese es el dato que faltaba para decidir si este tipo de repo es barato de operar o caro.
El dato colateral también importa: **14 horas de código y 1 estrella**, con un `pushed_at` que es posterior en 96 días al momento de la captura pero cuyo `updated_at` (2026-10-24T14:45:40Z) es del día anterior a la captura. Es decir, el repositorio **sigue moviéndose en metadatos sin que el código cambie** — el mismo reloj doble que el vault ya documentó para el corpus de registro ([[2026-1024-github-search-updated-at-no-es-actividad-de-codigo]]).

## [FRICTION]
> [[2026-1024-gptgrok2api-registro-protocolo-sin-navegador-y-captcha-solver-integrado]] afirma que en `gptGrok2api` el captcha está **internalizado** —`captcha-solver/` con Chromium/CloakBrowser en Docker/Xvfb, concurrencia dinámica, proxy por petición y reciclaje del navegador—, y de ahí se sigue que el coste de esa partida pasa de "dólares por 1000" a "coste de infraestructura que escala con altas simultáneas".
> Este átomo presiona esa creencia desde el otro lado del mercado: en la categoría de Suno, el item más completo del corpus **nombra dos proveedores de captcha de catálogo** (YesCaptcha y 2Captcha) en su propia descripción, es decir **el sector tiene las dos estrategias a la vez**. Ambas no pueden ser la forma dominante de resolver el captcha en un servicio de pool de cuentas: o internalizar porque el coste por 1000 no escala con el volumen, o comprar porque a la escala de estos repositorios sí sale a cuenta.
> Marcado para juicio humano, no auto-resuelto: **la captura no publica ni precios, ni volúmenes, ni rates**, y no permite saber en qué punto de volumen deja de compensar el catálogo.

## Nota de verificación
Metadatos leídos del `item` del JSON capturado el 2026-10-25. Los nombres YesCaptcha/2Captcha, el pool multi-cuenta y las "cookie tools" son **claims de la descripción del repositorio**; el vault no ha visitado la página ni el README. La ventana de 14 h 23 min entre `created_at` y `pushed_at` es un cálculo del vault sobre esas dos marcas.

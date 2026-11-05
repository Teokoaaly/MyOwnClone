---
id: 2026-1026-github-search-suno-pool-de-cookies-y-relay-newapi-oneapi
type: atom
certainty: solid
sources: [sources/2026-10-25-github-search-suno-openai.md]
links: ["[[2026-1023-new-api-gateway-unificado-de-modelos]]", "[[2026-1024-gptgrok2api-gateway-unificado-gpt-y-grok-en-api-compatible]]", "[[2026-1024-github-search-el-tercer-puesto-no-es-describible-desde-el-json]]"]
---

## Claim
El repo más popular de la consulta `suno openai api` — `wlhtea/Suno2openai`, **275 estrellas, 49 forks, Python, MIT, 3.202 KB, sin topics y sin homepage**— se define en su `description` (bilingüe, chino e inglés) como una llamada a la API de Suno **en formato OpenAI** que además **guarda las cookies en una base de datos para realizar las llamadas desde un pool de cookies**, y declara estar **integrado en las estaciones de reventa newapi y oneapi**, con adapters para front-ends como `chat-next-web`. El segundo, `Suno-API/Suno-API` (**159 estrellas, 26 forks, Go, MIT, 357 KB, 6 topics**), se describe como una API de Suno no oficial en Go que "supports generating songs, lyrics, and OpenAI Chat" — es decir, también expone un endpoint de chat compatible con OpenAI, pero no declara pool de cuentas ni integración con relays.

## Why It Matters
Este es el **eslabón que faltaba entre las dos categorías que el vault ya midió por separado**. El vault tiene medido el "arquetipo" del puente no oficial —Discord → API en `midjourney-proxy` ([[2026-1023-midjourney-proxy-convierte-discord-en-api-rest]])— y tiene medido el escalón de "registrar" frente a "operar capacidad" en el corpus de registro de cuentas ([[2026-1024-github-search-el-tercer-puesto-no-es-describible-desde-el-json]]). Esta captura muestra **las dos categorías fundidas en un solo repositorio**: la cabecera del corpus de Suno no es un proxy, es un **gestor de credenciales de cookie con endpoint compatible con OpenAI** — es decir, la capa de *pool de cuentas* y la capa de *API compatible* en el mismo artefacto, exactamente el salto que el thread describe entre producir capacidad y venderla.
Y lo hace **conectándose directamente a `newapi` y `oneapi`**: es decir, el puente de Suno no es un servicio aislado, es un **upstream más de los gateways de agregación** que el vault ya tiene modelados ([[2026-1023-new-api-gateway-unificado-de-modelos]]). La comparación con `gptGrok2api` es directa y no le hace ningún favor a nadie: allí el pool se alimentaba de un registrador integrado con captcha solver propio ([[2026-1024-gptgrok2api-gateway-unificado-gpt-y-grok-en-api-compatible]]); aquí el pool se alimenta de **cookies ya existentes**, guardadas en base de datos y rotadas. Es la misma arquitectura de negocio —vender capacidad de una plataforma sin API oficial— con un coste de aprovisionamiento radicalmente distinto.

## Nota de verificación
Cifras y metadatos leídos del `item` correspondiente del JSON capturado el 2026-10-25 (`stargazers_count`, `forks_count`, `language`, `license.spdx_id`, `size`, `topics`, `homepage`, `description`). La descripción se ha **traducido del chino al español**; el vault no ha clonado el repositorio ni leído su README, de modo que la existencia de un esquema de base de datos de cookies, la integración con newapi/oneapi y los adapters para `chat-next-web` son **claims del autor del repositorio**, no mediciones del vault.


## Nota de extensión 2026-10-26
Fuente adicional: `sources/2026-10-25-suno2openai.md` (README de `wlhtea/Suno2openai`, página del repositorio, capturada el 2026-10-25).

Esta nota atomizada a partir de la sola `description` bilingüe queda **verificada en su parte operacional** por el README, que documenta lo que el átomo tenía como claim del autor:

- **Pool de cookies en base de datos**: confirmado literalmente — *"save the cookie as a database to realize the cookie pool call"*; los prerrequisitos exigen **MySQL >= 5.7** y el despliegue pasa por `SQL_NAME`, `SQL_PASSWORD`, `SQL_IP` y `SQL_DK` (3306). No hay modo en memoria ([[2026-1026-suno2openai-el-pool-de-cookies-exige-mysql-como-requisito]]).
- **Rotación de cookies**: confirmada como capacidad ya implementada — *"Multiple Cookie Management: Implements rotation of multiple cookies"*, con cuatro endpoints REST de administración del pool (`PUT`/`POST`/`DELETE` sobre `/<COOKIES_PREFIX>/cookies` y `GET` sobre `/<COOKIES_PREFIX>/refresh/cookies`) ([[2026-1026-suno2openai-cuatro-endpoints-de-gestion-de-cookies]]).
- **Integración con `newapi`/`oneapi` y adapters para `chat-next-web`**: la `description` china lo afirma y el README lo confirma como compatibilidad declarada con front-ends de chat, pero **no documenta cómo se configura la conexión a un relay** —ni URL, ni canal, ni tipo de modelo. Sigue siendo claim, ahora con detalle de contrato: el único endpoint de generación es `POST /v1/chat/completions` en formato OpenAI, con `model` de ejemplo `gpt-3.5-turbo` ([[2026-1026-suno2openai-el-contrato-publico-es-el-formato-de-chat-con-streaming]]).
- **Dato nuevo que el átomo no tenía**: la sección *Future Plans* incluye **"Introduce request queueing optimizations"**, es decir, **la rotación está implementada y la cola de peticiones no** ([[2026-1026-suno2openai-rotacion-de-cookies-declarada-sin-cola-de-peticiones]]).
- **Aprovisionamiento de la credencial**: el apartado *"How to get cookie"* es una captura de pantalla con la instrucción *"copy all content about the cookie"* — la credencial **se recoge a mano**, no se fabrica ni se compra ([[2026-1026-suno2openai-la-cookie-se-copia-a-mano-del-navegador]]).

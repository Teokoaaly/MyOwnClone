---
id: 2026-1023-midjourney-proxy-arquitectura-token-discord-y-wss
type: atom
certainty: solid
sources: [sources/2026-10-22-midjourney-proxy-github.md]
links: ["[[2026-1023-midjourney-proxy-convierte-discord-en-api-rest]]", "[[2026-1023-midjourney-proxy-funcion-multicuenta-con-cola-por-cuenta]]", "[[2026-1023-midjourney-proxy-riesgo-de-cuenta-por-frecuencia-de-dibujo]]"]
---

## Claim
El proxy **no se autentica contra Midjourney**, sino contra Discord, y necesita tres identificadores además de una cuenta de pago. Es el reverso del patrón "Discord → API" que define al proyecto ([[2026-1023-midjourney-proxy-convierte-discord-en-api-rest]]). El apartado **"使用前提"** (requisitos) del README enumera: (1) **"注册并订阅 MidJourney，创建自己的服务器和频道"** — suscribirse a Midjourney y crear un servidor y un canal propios de Discord; (2) **"获取用户Token、服务器ID、频道ID"** — obtener el token de usuario, el ID de servidor y el ID de canal. Y la lista de funciones incluye **"user-token 连接 wss，可以获取错误信息和完整功能"**: la conexión por WebSocket con el **token de usuario** es la que permite obtener los mensajes de error y las funciones completas.

## Why It Matters
La arquitectura revela dónde está el acoplamiento real: el proxy no habla con Midjourney, habla con **Discord en nombre de un usuario humano**. Eso significa que el activo crítico no es una clave de API del proveedor sino **un token de sesión de usuario y un canal de Discord propio**, y que el rendimiento del proxy depende de que Discord no corte la sesión.
De ahí se derivan las dos dinámicas que el resto del README documenta: la necesidad de **múltiples cuentas** ([[2026-1023-midjourney-proxy-funcion-multicuenta-con-cola-por-cuenta]]) y la advertencia de que el uso frecuente puede **provocar un aviso o baneo de la cuenta** ([[2026-1023-midjourney-proxy-riesgo-de-cuenta-por-frecuencia-de-dibujo]]).
Para el vault, el aprendizaje es de diseño: cualquier integración con un proveedor que no da API hereda esta tríada — cuenta de pago + identidad de sesión + superficie de mensajes — y por tanto hereda su fragilidad.

## Nota de verificación
El README **no** usa el término "self-bot" ni especifica si el token se obtiene de una cuenta de usuario o de un bot de Discord; solo dice "用户Token". Esa distinción (y su estatus frente a los términos de Discord) no es verificable con esta fuente y queda abierta.

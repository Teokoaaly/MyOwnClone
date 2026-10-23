---
id: 2026-1023-midjourney-proxy-convierte-discord-en-api-rest
type: atom
certainty: solid
sources: [sources/2026-10-22-midjourney-proxy-github.md]
links: ["[[2026-1023-midjourney-proxy-arquitectura-token-discord-y-wss]]", "[[2026-1023-midjourney-proxy-ecosistema-de-aplicaciones-que-lo-consumen]]", "[[2026-1022-gap-dify-como-capa-inferencia-prompts]]"]
---

## Claim
`novicezk/midjourney-proxy` es un proxy que **convierte el canal de Discord de Midjourney en una llamada por API de dibujo por IA**. La descripción del propio repositorio, repetida en el encabezado y en la sección *About*, es literal: **"代理 MidJourney 的discord频道，实现api形式调用AI绘图"** — proxy del canal de Discord de Midjourney para poder invocar el dibujo por IA en forma de API. Es software libre bajo **licencia Apache-2.0** y el README ofrece además una sección **"开放API"** de API abierta.

## Why It Matters
Es el **patrón canónico del sector para una herramienta de IA sin API oficial**: el generador expone todo su producto dentro de un chat (Discord), y un tercero construye el puente HTTP que permite consumirlo desde código. El vault ya tiene la misma estructura con otro proveedor: Dify actúa como capa de inferencia sobre modelos LLM ([[2026-1022-gap-dify-como-capa-inferencia-prompts]]); aquí el puente es un proceso Java que habla con Discord por WebSocket, y la autenticación es la que aporta el token de usuario ([[2026-1023-midjourney-proxy-arquitectura-token-discord-y-wss]]).
La consecuencia para el vault es de estrategia de producto: la disponibilidad de este tipo de puente significa que **cualquiera puede consumir Midjourney por API sin esperar permiso del proveedor**, lo que abre la puerta tanto a productos derivados ([[2026-1023-midjourney-proxy-ecosistema-de-aplicaciones-que-lo-consumen]]) como a un modelo de negocio paralelo de API no oficial ([[2026-1023-midjourney-proxy-oferta-comercial-de-api-no-oficial]]).
Importante para el vault, que construye clones con IA: el eje de diferenciación de estos proxies no es el modelo (usa el del proveedor) sino la **envolvente**: API, traducción, filtrado, cuentas y observabilidad.

## Nota de verificación
La frase china es la única descripción del propósito en el README capturado. Los endpoints concretos viven en `docs/api.md`, que **no está capturado**: el vault no puede afirmar rutas, métodos ni formas de payload a partir de esta fuente.

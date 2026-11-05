---
id: 2026-1026-suno2openai-auth-key-por-defecto-es-el-timestamp-actual
type: atom
certainty: solid
sources: [sources/2026-10-25-suno2openai.md]
links: ["[[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]", "[[2026-1023-midjourney-proxy-config-tareas-y-autenticacion]]"]
---

## Claim
La tabla de parámetros del README declara que **`AUTH_KEY` —"Authorization key, default is the current timestamp"**— es la credencial de todas las rutas (los cuatro endpoints de cookies y `/v1/chat/completions`), todas con cabecera `Authorization: Bearer`. Es decir: **si el operador no fija `AUTH_KEY`, la clave por defecto es la hora del sistema**, que es un valor conocido por cualquiera que sepa la hora aproximada, o que el propio despliegue expone. El resto de defaults del README son igualmente permisivos o forfaitarios: `BASE_URL` = `https://studio-api.suno.ai`, `SQL_DK` = 3306, `RETRIES` = 5, `BATCH_SIZE` = 10, `MAX_TIME` = 5 (minutos), y los valores de ejemplo del `.env` son literales triviales.

## Why It Matters
El vault tiene ya dos referencias opuestas sobre cómo debe ser el control de borde de un gateway, y este README las recorre a los dos extremos. `new-api` exige **`SESSION_SECRET` persistente y compartido entre nodos**, `CRYPTO_SECRET`, `SESSION_COOKIE_SECURE`, `TRUSTED_PROXIES` declarado explícitamente y advierte que copiar `.env.example` no inyecta nada ([[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]); `midjourney-proxy` va al otro extremo con **`mj.api-secret` vacío = autenticación desactivada** ([[2026-1023-midjourney-proxy-config-tareas-y-autenticacion]]). Aquí hay un **tercer patrón**: la autenticación está **activada**, pero su valor por defecto es **cualquier marca de tiempo**, es decir, un secreto que no es secreto y que además **cambia por defecto en cada arranque**.
La consecuencia práctica para el vault es que **la seguridad de este gateway depende de una variable que el README presenta como opcional**. Un despliegue que copie `env.example` sin tocar `AUTH_KEY` queda con una bearer key derivada del reloj: no es una credencial robable de forma estable, pero es una credencial que **cambia sola** (rompiendo clientes) y que **no protege nada** frente a quien conozca la hora del servidor. El aprendizaje transferible es el que el vault ya conoce: *la clave por defecto insegura es el peor de los dos mundos* — ni seguridad real ni estabilidad de contrato.

## [FRICTION]
> [[2026-1023-midjourney-proxy-config-tareas-y-autenticacion]] (escrita el 2026-10-23) afirma que en el sector de proxies la **"autenticación es opt-in por diseño"**, con `mj.api-secret` vacío dejando la API abierta, y lo valora como "una decisión explícita y reversible por configuración" frente a la ausencia de control del producto del vault.
> Este átomo presiona esa clasificación desde un caso intermedio que el modelo de dos extremos no cubre: aquí **la autenticación no está desactivada sino habilitada con un default que es el timestamp del sistema**, y la misma clave gobierna las cuatro rutas de **administración del pool de credenciales** y la de inferencia. Es decir, no es "sin control" ni es "control con secreto persistente": es **control con secreto efímero y compartido entre plano de administración y plano de servicio**, lo que hace que obtener la inferencia dé acceso al pool.
> Ambas no pueden ser la misma taxonomía del sector: o "opt-in o nada" describe el patrón dominante, o hay un tercer patrón —default activo pero no secreto— que la taxonomía no contiene. Marcado para juicio humano, no auto-resuelto: el vault no ha ejecutado el contenedor ni observado qué clave acepta realmente el servicio en ausencia de `AUTH_KEY` explícito.

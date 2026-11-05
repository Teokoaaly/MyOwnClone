---
id: 2026-1026-suno2openai-rotacion-de-cookies-declarada-sin-cola-de-peticiones
type: atom
certainty: solid
sources: [sources/2026-10-25-suno2openai.md]
links: ["[[2026-1023-midjourney-proxy-funcion-multicuenta-con-cola-por-cuenta]]", "[[2026-1026-github-search-suno-pool-de-cookies-y-relay-newapi-oneapi]]"]
---

## Claim
La sección *Project Highlights* declara cuatro capacidades: **"OpenAI Format Calls: Supports streaming output"**, **"Front-end Compatibility: Compatible with front-end projects like `chat-next-web`"**, **"Docker Deployment"** y **"Multiple Cookie Management: Implements rotation of multiple cookies"**. Pero la sección *Future Plans* incluye, todavía pendiente, **"Introduce request queueing optimizations"**, además de **soporte de parámetros propios** (`tags`, `prompt`, `style`, y continuación de canción) y **"Explore development of official-like frontend pages"**. Es decir: la **rotación de cookies está implementada** y **la cola de peticiones no**.

## Why It Matters
El vault tiene medido el patrón equivalente en el sector Discord→API: allí el multi-cuenta viene **con una cola de tareas asignable a cada cuenta**, y esa cola por cuenta es precisamente lo que convierte una identidad frágil en un recurso que se degrada de forma parcial ([[2026-1023-midjourney-proxy-funcion-multicuenta-con-cola-por-cuenta]]). Aquí **la rotación está y la cola no**: el pool reparte sesiones, pero **no hay ningún reparto publicado de carga, ni límite por cookie, ni encolado**, solo tres parámetros de ajuste —`RETRIES` = 5, `BATCH_SIZE` = 10, `MAX_TIME` = 5 minutos— cuyo efecto sobre el reparto entre cookies el README **no explica**.
Para el producto propio la lectura es de **lo que falta en un upstream**: los tres parámetros sí son un dato reutilizable (batch de 10, 5 reintentos, techo de 5 minutos por request son valores de dimensionamiento de un pool pequeño), pero **sin cola el pool es round-robin best-effort**, y quien lo opera tiene que construir la disciplina de reparto por su cuenta.
El segundo dato, la compatibilidad declarada con **`chat-next-web`**, es la vía por la que un usuario final no técnico consume música: **el gateway no vende una API, vende un chat que suena**. Es el mismo movimiento de distribución que el vault vio en los bundles de skills para agentes: **la distribución se está moviendo del API-key al front-end y al harness**, y aquí el front-end de referencia es un chat de IA genérico.

## [FRICTION]
> [[2026-1023-midjourney-proxy-funcion-multicuenta-con-cola-por-cuenta]] (escrita el 2026-10-23) establece, para el arquetipo de proxy con pool, que **"cada identidad lleva su propia cola"** y de ahí que "el reparto de trabajo entre cuentas es una decisión operativa manual o heurística, no una abstracción limpia de capacidad".
> Este átomo presiona esa creencia con un caso donde **falta la pieza que el átomo da por existente**: en `Suno2openai` la rotación de cookies es una capacidad declarada y ya implementada, pero **la cola está listada explícitamente como plan futuro**. Es decir, existe el pool sin la cola, un estado que el átomo de `midjourney-proxy` no contemplaba.
> Ambas no pueden ser la misma lectura del arquetipo: o "pool con cola por cuenta" es el patrón completo del sector y este repo es un caso a medio camino, o **la rotación sin reparto es suficiente** en esta categoría —posible, porque la música se genera en minutos y no en segundos, y la latencia es tolerable. Marcado para juicio humano, no auto-resuelto: el vault no ha ejecutado el gateway ni ha observado cómo reparte peticiones entre cookies en operación real.

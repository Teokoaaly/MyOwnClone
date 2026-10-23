---
id: 2026-1023-midjourney-proxy-config-tareas-y-autenticacion
type: atom
certainty: solid
sources: [sources/2026-10-22-midjourney-proxy-github.md]
links: ["[[2026-1023-midjourney-proxy-convierte-discord-en-api-rest]]", "[[2026-1023-midjourney-proxy-funcion-multicuenta-con-cola-por-cuenta]]", "[[2026-1022-sin-rate-limiting]]"]
---

## Claim
El apartado **"配置项"** del README declara cuatro claves con semántica explícita, que gobiernan cómo el puente expone el servicio hacia el consumidor final ([[2026-1023-midjourney-proxy-convierte-discord-en-api-rest]]). **`mj.task-store.type`**: forma de almacenar las tareas, **por defecto `in_memory` (en memoria, se pierde al reiniciar)**, con **`redis` como opción**. **`mj.task-store.timeout`**: caducidad del almacenamiento de tareas, **30 días por defecto**, tras la cual se borra. **`mj.api-secret`**: clave de interfaz, **"为空不启用鉴权"** — si está vacía **no se activa la autenticación**; al llamar a la API hay que enviar la cabecera **`mj-api-secret`**. **`mj.translate-way`**: método de traducción de prompt chino a inglés, con opciones **`null` (por defecto), `baidu`, `gpt`**.

## Why It Matters
Tres consecuencias operativas que el vault debe copiar o descartar explícitamente:
1. **El estado por defecto es volátil.** En memoria, reiniciar el proceso pierde las tareas. Un producto que promete "progreso en tiempo real" ([[2026-1023-midjourney-proxy-funciones-imagen-base64-y-describe]]) necesita persistencia real, y aquí eso es una decisión de configuración, no un default: Redis es la opción, no el valor inicial.
2. **La autenticación es opt-in por diseño.** Con `mj.api-secret` vacío, la API queda abierta sin ningún header. Es una decisión coherente con "instálalo y pruébalo en un minuto", pero es exactamente el patrón que el vault ya sabe defectuoso en su propio producto ([[2026-1022-sin-rate-limiting]]): una superficie sin control de borde, con un default abierto.
3. **La traducción tiene tres modos y uno es no traducir.** El valor por defecto `null` significa que el proxy no toca el prompt: el prompt chino se envía crudo. El filtrado de palabras sensibles sí es parte del núcleo.

## [FRICTION]
> [[2026-1022-sin-rate-limiting]] afirma que [[myownclone]] no aplica rate limiting: diez peticiones rápidas consecutivas devolvieron todas HTTP 200, sin bloqueo, throttling ni respuesta 429.
> Este átomo presiona esa creencia en un punto concreto: el proxy documenta **el mecanismo que el producto del vault no tiene** —una clave de interfaz opcional (`mj-api-secret`) que se envía en cada llamada y que, por defecto, está desactivada. Es decir, en el proxy la ausencia de control de acceso es **una decisión explícita y reversible por configuración**, no un olvido; en el producto del vault no hay ni siquiera el interruptor. La diferencia es de naturaleza: una cosa es una decisión de producto y otra es una ausencia de control.
> Ambas no pueden ser completamente correctas como descripción del riesgo: o el producto del vault tiene el control en otra capa no observable (edge, WAF, gateway), o comparte con el proxy el mismo patrón de "sin autenticación por defecto" que la captura del vault no ha detectado. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
El README no dice si `mj-api-secret` se compara en texto plano, ni documenta otras claves más allá de estas cuatro (remite a `docs/config.md`, no capturado).

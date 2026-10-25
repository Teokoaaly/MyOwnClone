---
id: 2026-1024-chatgpt-creator-worker-pool-y-retry-hasta-alcanzar-la-meta
type: atom
certainty: solid
sources: [sources/2026-10-24-chatgpt-creator-verssache.md]
links: ["[[2026-1024-chatgpt-creator-flujo-de-registro-en-nueve-pasos]]", "[[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]", "[[2026-1024-chatgpt-creator-salida-en-archivo-email-contrasena]]"]
---

## Claim
El control de volumen del bot tiene **dos parámetros, ambos interactivos**, y el prompt los muestra con sus valores por defecto: `Total accounts to register: 5` y `Max concurrent workers (default: 3): 2`. Las features lo nombran **"Concurrent Registration — Configurable worker pool for parallel account creation"** y **"Retry Loop — Automatically retries failed registrations until target count is reached"**; el módulo responsable es `internal/register/batch.go  # Batch orchestration, worker pool, retry logic`. El ejemplo de salida cierra con un **resumen de lote** con cinco campos: `Target: 5`, `Success: 5`, `Attempts: 6`, `Failures: 1`, `Elapsed: 1m 45s`. Es decir, **6 intentos para 5 cuentas: un fallo se reintenta sin abortar el lote**, y el objetivo se cumple aunque haya errores intermedios. La ejecución del ejemplo es de un solo trabajador (`[W1]`), con 25 segundos por cuenta.

## Why It Matters
Establece el **modelo de coste y de éxito del bot**, que es distinto del modelo de coste del thread. En el thread, cada pata del alta —SMS, captcha, proxy— se paga **por unidad** y su fiabilidad se mide en porcentaje. Aquí la unidad de éxito es **la cuenta**, y el mecanismo de éxito no es comprar más insumo: es **reintentar el mismo flujo hasta que salga**. El resumen de lote separa explícitamente `Attempts` de `Success`, lo que significa que **el número de intentos consumidos es mayor que el número de cuentas obtenidas** y que el coste real de la operación hay que calcularlo sobre intentos, no sobre cuentas.
La consecuencia operativa es la que más importa para un lector: **el fallo no es un error, es una unidad de trabajo**. Un flujo con 44 % de números de SMS que nunca llegan ([[2026-1023-5sim-openai-tasa-entrega-techo-56]]) y, en esta ruta, además con detección por fingerprint TLS, produce lotes donde `Attempts` supera con holgura a `Success`. El thread ya tenía el dato estructural de que **el tiempo y el gasto, no el número de cuentas, es lo que escala**; este README lo confirma en la forma de un contador que el propio autor pone delante del usuario.
Y hay un segundo dato de diseño: el **pool de workers configurable con defecto 3**. Es un número pequeño y deliberado, coherente con una estrategia de no llamar la atención. Un pool grande multiplicaría la señal.

## Nota de verificación
El ejemplo de salida muestra un lote de 5 cuentas con 6 intentos y 1 fallo, ejecutado con un solo trabajador visible, aunque el prompt del ejemplo indica 2. El vault no puede generalizar una **tasa de fallo** a partir de un único lote de muestra: 1 fallo sobre 6 intentos es un dato, no una distribución.

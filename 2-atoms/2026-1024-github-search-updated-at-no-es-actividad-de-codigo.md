---
id: 2026-1024-github-search-updated-at-no-es-actividad-de-codigo
type: atom
certainty: solid
sources: [sources/2026-10-24-github-search-chatgpt-account-creator.md]
links: ["[[2026-1024-github-search-diez-de-catorce-se-pushearon-en-las-veinticuatro-horas]]", "[[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]", "[[2026-1023-midjourney-proxy-popularidad-y-actividad-del-repo]]"]
---

## Claim
Cada objeto `item` trae tres marcas temporales con significados distintos, y solo dos de ellas miden actividad de código: `created_at` (creación del repositorio), `pushed_at` (último push a la rama por defecto) y `updated_at` (última modificación de **cualquier metadato**, incluidos estrellas, issues y descripciones). La diferencia se ve con claridad en `verssache/chatgpt-creator`: `created_at` 2026-03-10T16:21:59Z, `pushed_at` 2026-04-06T04:00:01Z —**27 días de código**— y `updated_at` 2026-10-24T03:21:16Z, **la misma madrugada de la captura**, seis meses y medio después del último push. Los 14 repositorios del corpus tienen `updated_at` posterior a `pushed_at` en **los 14 casos sin excepción**, con desfases que van de 2 h 15 min (`zbaxstore`) a 744 días (`Nilsber/CookieProfileCreator`, `updated_at` 2025-07-22 frente a un push de octubre de 2024). `AuuCoder/gptGrok2api` es el caso más extremo: push el 2026-07-27 y `updated_at` 2026-10-23, tres meses después.

## Why It Matters
Esto cierra el patrón de mantenimiento con una precisión que el vault no tenía y que le importa directamente, porque **es exactamente el error que una captura por API induce**. Al leer un JSON de repositorios, la marca "última actualización" es el campo que un lector desatento descuenta como actividad; aquí significa otra cosa: **popularidad**. Los seis meses y medio de `verssache` sin código pero con `updated_at` de hoy son la demostración de que un repositorio puede "moverse" cada vez que le llega una estrella, sin que nadie toque el repositorio.
La consecuencia para el método del vault es una regla: **para medir mantenimiento hay que leer `pushed_at`, nunca `updated_at`**, y para medir popularity hay que leer `updated_at` con cuidado porque mezcla cualquier cambio de metadato. Es la generalización de lo que ya se había registrado en Midjourney-Proxy —5,4k estrellas con el código congelado desde junio de 2024 ([[2026-1023-midjourney-proxy-popularidad-y-actividad-del-repo]])— y del átomo de `verssache` con sus cuatro commits ([[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]): **estrellas y mantenimiento son dos relojes distintos**, y la API de búsqueda los expone en campos distintos precisamente para que no se confundan.
La cifra agregada que sale de esto es la del corpus: **14 de 14 con `updated_at` posterior a `pushed_at`**, es decir, en el 100 % de los casos la señal visible de "actividad" es posterior a la última línea de código escrita.

## Nota de verificación
Las tres marcas temporales de los 14 `items` del JSON capturado el 2026-10-24 se han comparado una a una; la afirmación "14 de 14" es un recuento del vault sobre esos objetos. El vault **no ha ejecutado ninguna llamada a la API de commits** ni ha modificado repositorios: la atribución de `updated_at` a cambios de estrellas o issues es la lectura estándar del campo, no un dato que la captura documente de forma explícita — la captura solo muestra que `updated_at` cambia sin que `pushed_at` lo haga.

---
id: 2026-1023-midjourney-proxy-popularidad-y-actividad-del-repo
type: atom
certainty: solid
sources: [sources/2026-10-22-midjourney-proxy-github.md]
links: ["[[2026-1023-midjourney-proxy-edicion-plus-ampliada]]", "[[2026-1023-midjourney-proxy-ecosistema-de-aplicaciones-que-lo-consumen]]", "[[2026-1022-sin-repos-publicos-github]]"]
---

## Claim
La barra lateral de GitHub del repositorio muestra **5,4k stars**, **2,4k forks**, **46 watchers**, **229 commits** en `main`, **4 branches** y **27 tags**, con **licencia Apache-2.0** y los topics `midjourney` y `midjourney-api`. Las fechas de la tabla de archivos dibujan una línea clara: el último commit es **"feat: update readme"** (3 de agosto de 2025), el último cambio de código en `src/main` y `docs` es de **12 de junio de 2024** ("修复wss重连失败问题; 优化任务消息匹配", PR #341) y lo más antiguo es de mayo-junio de 2023. El autor que figura en el último commit es **litter-coder**, el mismo que mantiene la edición plus.

## Why It Matters
El dato relevante es la **forma de la curva de mantenimiento**: la comunidad autogeneró el valor (5,4k stars, 2,4k forks, siete aplicaciones derivadas), pero el **código propio está congelado desde junio de 2024** y lo único que se ha movido desde entonces es el README. Es decir, **la popularidad no se ha convertido en mantenimiento** — la explicación más probable es que el esfuerzo se ha desplazado a la edición plus, que es donde están las funciones nuevas ([[2026-1023-midjourney-proxy-edicion-plus-ampliada]]).
Para el vault, esto da dos lecturas. Primera, sobre **adopción sin mantenimiento**: un repositorio muy popular puede quedarse atrás en silencio, así que "5,4k stars" no es una garantía de que el código funcione con la versión actual del proveedor. Segunda, y más útil como precedente: el propio sector financia la continuidad con una **edición de pago separada**, no con el código abierto.
También contrasta con la situación del producto del vault: allí no hay repositorios públicos ([[2026-1022-sin-repos-publicos-github]]); aquí el código abierto es el activo comercial principal. Es un eje de decisión de estrategia que el vault tiene pendiente.

## Nota de verificación
Las cifras (5,4k / 2,4k / 46 / 229 / 4 / 27) y las fechas son lectura directa de la página de GitHub capturada el 2026-10-22. GitHub muestra las fechas relativas ("3 years ago", "2 years ago", "last year") junto a las absolutas; el vault usa las absolutas que la propia página muestra en la cabecera de cada commit.

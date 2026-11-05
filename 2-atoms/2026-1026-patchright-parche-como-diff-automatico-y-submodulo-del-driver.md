---
id: 2026-1026-patchright-parche-como-diff-automatico-y-submodulo-del-driver
type: atom
certainty: solid
sources: [sources/2026-10-25-patchright-playwright.md]
links: ["[[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]", "[[2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos]]", "[[2026-1026-patchright-fork-parcheado-de-playwright-como-sustituto-directo]]", "[[2026-1026-patchright-mil-commits-y-cinco-mil-estrellas-actividad-activa]]"]
---

## Claim
El árbol de archivos del repositorio muestra la arquitectura del proyecto: un directorio **`driver_patches`** con el código de los parches, un fichero **`patchright.patch`** que contiene el diff completo, un **`patchright_driver_patch.ts`** en la raíz, un **submódulo git** `patchright-nodejs @ 5d40f66` (con `.gitmodules` presente), y un paquete `utils`. Los commits que tocan `driver_patches` son **commits automáticos con etiqueta de comparación**: *"[Patch-Comparison] Automatic Commit: Fix Playwright 1.64.1 compatibility and MediaRouter detection (#256)"*. El TODO incluye, ya marcado como hecho, *"Implement .patch Updater to easily show Patchright's patches"*. Además, la lista de detectores superados incluye **Brotector (with CDP-Patches)** — es decir, **un segundo repositorio del mismo autor es requisito para pasar esa prueba**.

## Why It Matters
El vault gana aquí una **estructura de maintenance** que ninguna otra fuente del corpus tenía: el parche **no se mantiene a mano**, se genera y se compara automáticamente contra cada release de Playwright. Eso explica por qué el proyecto puede tener 1.036 commits y compatibilidades con 1.62.1, 1.64.0 y 1.64.1 en pocos meses ([[2026-1026-patchright-mil-commits-y-cinco-mil-estrellas-actividad-activa]]): **la unidad de trabajo no es el parche, es el diff contra upstream**.
La consecuencia de diseño es la que importa para quien quiera reutilizarlo: **el parche está acoplado a una versión concreta de Playwright**, y el repositorio guarda el diff como fichero versionable — `.patch` — precisamente para que sea aplicable y auditable sobre un árbol de Playwright limpio. Es la forma en que este tipo de proyecto resuelve el problema de "parchear algo que no controlas".
Y el dato de CDP-Patches introduce una **dependencia de segundo orden**: para pasar Brotector no basta este repositorio, hace falta otro (`Kaliiiiiiiiii-Vinyzu/CDP-Patches`). Es decir, la " undetectable" del README es **compuesta**, y el vault debe leer la lista de catorce detectores como una lista de dependencias, no de achievements.

## Nota de verificación
Los nombres de directorio y fichero, el submódulo y los títulos de commit están transcritos literalmente. La captura **no** incluye el contenido de `patchright.patch` ni de los ficheros de `driver_patches`, ni el diff real, ni el alcance de `CDP-Patches`. La caracterización del parche como "generado automáticamente" se apoya en el prefijo de los títulos de commit y en el ítem del TODO, no en una inspección del proceso.

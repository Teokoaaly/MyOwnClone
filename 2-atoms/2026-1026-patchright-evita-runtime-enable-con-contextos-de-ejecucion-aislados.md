---
id: 2026-1026-patchright-evita-runtime-enable-con-contextos-de-ejecucion-aislados
type: atom
certainty: solid
sources: [sources/2026-10-25-patchright-playwright.md]
links: ["[[2026-1024-chatgpt-creator-token-sentinel-y-cabeceras-de-traza-datadog]]", "[[2026-1024-gptgrok2api-registro-protocolo-sin-navegador-y-captcha-solver-integrado]]"]
---

## Claim
La sección "Patches" abre con la fuga que el README llama **"the biggest Patch Patchright uses"**: **"To avoid detection by this leak, patchright avoids using `Runtime.enable` by executing Javascript in (isolated) ExecutionContexts."** Es decir, la primera y más importante corrección no cambia flags ni cabeceras: cambia **el mecanismo por el que se ejecuta JavaScript en la página**, evitando por completo la llamada CDP que delata el driver. El TODO del proyecto confirma que la capacidad está implementada: *"Implement Option to choose Execution Context (Main/Isolated)"* aparece marcado como hecho (`[x]`).

## Why It Matters
Es el ejemplo más claro del vault de **detección que vive en el protocolo de control, no en el contenido de la página**. No hay nada que "parecer humano" en lo que la página ve: lo que se ve es una sesión CDP donde `Runtime.enable` fue invocado, y eso es una señal que ningún ajuste de contenido puede tapar.
El contraste con lo ya atomizado sobre `chatgpt-creator` es de **capas distintas**: allí el mecanismo es imitar la instrumentación del proveedor —un "sentinel token" y cabeceras de traza con formato Datadog ([[2026-1024-chatgpt-creator-token-sentinel-y-cabeceras-de-traza-datadog]])— que es una capa de **cabecera HTTP**, por encima del protocolo. Patchright opera un nivel más abajo, en el **canal CDP entre el driver y el navegador**, y ese nivel ni siquiera existe en un bot HTTP puro como el de `gptGrok2api` ([[2026-1024-gptgrok2api-registro-protocolo-sin-navegador-y-captcha-solver-integrado]]).
Para el vault, la consecuencia es de **coste de construcción** y ya la había anunciado la §11 del thread: la capa dominante de un flujo de alta no es una compra, es una construcción. Pero esta fuente matiza la afirmación: **esa construcción ya está hecha y publicada** en forma de parche reutilizable, con el coste de integrar una dependencia en lugar de mantener un protocolo propio.

## Nota de verificación
El README describe el mecanismo y su motivo en una frase; la captura **no contiene el código del parche**, ni la referencia al issue donde se descubrió la fuga, ni el procedimiento de detección concreto. La afirmación "la fuga más importante" es del autor. Que la ejecución en contextos aislados la elimine **por completo** no es algo que el vault pueda verificar.


## Nota de extensión 2026-10-26
La misma captura de `sources/2026-10-25-rebrowser-patches.md` documenta **una segunda implementación del mismo fix, con criterios por defecto distintos**. `rebrowser/patches` ofrece **tres estrategias** para obtener el contexto sin `Runtime.Enable`: `addBinding` (binding en el mundo principal, **modo por defecto**, conserva acceso al main world y funciona en web workers e iframes), `alwaysIsolated` (`Page.createIsolatedWorld`, que coincide con la elección de Patchright pero **sin acceso a variables del contexto principal** y **sin poder ejecutar código dentro de un worker**) y `enableDisable` (llamar a `Runtime.Enable` y de inmediato a `Runtime.Disable`, con una ventana breve de riesgo). El modo es conmutable en caliente por `REBROWSER_PATCHES_RUNTIME_FIX_MODE`. Además, el README de rebrowser reconoce a Patchright explícitamente en "Special thanks" como *"set of patches to fix Playwright leaks"*, lo que confirma que son **proyectos hermanos**, no alternativas independientes. Ver [[2026-1026-rebrowser-tres-estrategias-para-obtener-el-contexto-y-sus-tradeoffs]] y [[2026-1026-rebrowser-agradece-cinco-proyectos-que-le-abrieron-el-camino]].

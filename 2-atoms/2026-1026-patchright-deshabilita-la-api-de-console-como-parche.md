---
id: 2026-1026-patchright-deshabilita-la-api-de-console-como-parche
type: atom
certainty: solid
sources: [sources/2026-10-25-patchright-playwright.md]
links: ["[[2026-1024-chatgpt-creator-token-sentinel-y-cabeceras-de-traza-datadog]]", "[[2026-1024-gptgrok2api-registro-protocolo-sin-navegador-y-captcha-solver-integrado]]", "[[2026-1026-patchright-evita-runtime-enable-con-contextos-de-ejecucion-aislados]]"]
---

## Claim
Segunda fuga del bloque "Patches": **"Patchright patches this leak by disabling the Console API all together."** El README no oculta el coste: **"This means, console functionality will not work in Patchright."** Y ofrece un sustituto con una advertencia explícita: *"If you really need the console, you might be better off using Javascript loggers, although they also can be easily detected."* Es decir, la vía alternativa que el propio proyecto sugiere está **reconocible como detectable** por el propio autor.

## Why It Matters
Es un caso de **funcionalidad sacrificada por el stealth** que el vault no tenía registrado: el mismo patrón que la §11 del thread ya vio en el bot Go, donde la imitación de la instrumentación del proveedor (token sentinel, cabeceras Datadog) no es gratis en ninguna dimensión ([[2026-1024-chatgpt-creator-token-sentinel-y-cabeceras-de-traza-datadog]]). Pero aquí el sacrificio es **de negocio**: se pierde una herramienta de depuración entera.
La observación operativa que la fuente sí permite es precisa: **deshabilitar la Console API no es una configuración, es una funcionalidad que se pierde para siempre en el entorno de automatización**. Un pipeline que dependa de logs de `console.log` del sitio objetivo para extraer datos —o para detectar estados de UI— deja de funcionar, y la alternativa que ofrece el README (loggers de JavaScript) el propio autor la marca como fácilmente detectable. Es decir: **no hay sustituto limpio**, y eso es una decisión de arquitectura, no un matiz de documentación.
Relacionado con la fuga anterior: ambas correcciones atacan el mismo canal, el CDP, y ambas se resuelven **suprimiendo capacidad** en vez de imitando comportamiento ([[2026-1026-patchright-evita-runtime-enable-con-contextos-de-ejecucion-aislados]]).

## Nota de verificación
Todo el párrafo está transcrito literalmente del README, incluida la advertencia sobre los loggers de JavaScript. La captura **no** documenta qué APIs de depuración alternativa existen (Chrome DevTools Protocol directo, `page.on('console')`, etc.), ni si la supresión es total o por contexto. El vault no ha ejecutado Patchright.

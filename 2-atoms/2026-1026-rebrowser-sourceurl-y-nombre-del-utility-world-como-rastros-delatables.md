---
id: 2026-1026-rebrowser-sourceurl-y-nombre-del-utility-world-como-rastros-delatables
type: atom
certainty: solid
sources: [sources/2026-10-25-rebrowser-patches.md]
links: ["[[2026-1026-rebrowser-runtime-enable-la-fuga-que-usan-todos-los-antibot]]", "[[2026-1026-rebrowser-parchea-el-codigo-fuente-porque-no-hay-configuracion-que-lo-arregle]]", "[[2026-1024-chatgpt-creator-token-sentinel-y-cabeceras-de-traza-datadog]]", "[[2026-1026-puppeteer-extra-783-forks-sobre-7-4k-estrellas-un-ratio-de-0-11]]"]
---

## Claim
El README describe **dos rastros adicionales** que la librería deja en la página, más allá de la fuga de CDP. **(a) `sourceURL`**: por defecto Puppeteer añade `//# sourceURL=pptr:...` a cada script ejecutado con `page.evaluate()`, y *"A remote website can detect this behavior and raise red flags"*; el parche lo cambia a `//# sourceURL=app.js`, configurable con `REBROWSER_PATCHES_SOURCE_URL` (cualquier nombre genérico, o `0` para desactivar). **(b) Nombre del utility world**: el valor por defecto es `'__puppeteer_utility_world__' + packageVersion` —es decir, **el nombre incluye la versión del paquete**— y el parche lo cambia a `util`, configurable con `REBROWSER_PATCHES_UTILITY_WORLD_NAME`; esa variable **no se puede cambiar en caliente**, porque se usa en el momento en que se importa el módulo. El README anota que este rastro **no es detectable por los scripts del sitio**, pero que *"Google might use this information in their proprietary Chrome; we never know"*.

## Why It Matters
Son **huellas de cadena de texto** dentro de la página, no señales de protocolo: el nombre de la librería y su versión quedan escritos en el JavaScript que se ejecuta. Eso tiene una lectura que el vault no tenía: **la versión del paquete es parte de la superficie de detección**, no solo del mantenimiento. Un paquete con una versión desconocida es un paquete cuyo rastro de versión no se puede correlacionar.

El segundo apunte es metodológico y encaja con lo que el thread ya sabe hacer con las fuentes que se contradicen: aquí la propia fuente se contradice en tono —el parche del utility world **no lo detecta el sitio**, pero el README justifica el proyecto entero por lo que detecta el sitio. Es decir, **el repo incluye al menos un parche cuyo valor es defensivo frente a un detector hipotético** (Google en su Chrome propietario), no frente a los anti-bot que el propio README nombra (Cloudflare, DataDome). El vault no puede leer eso como una medida de eficacia.

La comparación con el bot en Go es directa y reveladora: allí la imitación es de **cabeceras de traza Datadog y token sentinel** —imitando la instrumentación del proveedor ([[2026-1024-chatgpt-creator-token-sentinel-y-cabeceras-de-traza-datadog]])—; aquí la imitación es de **constantes internas de la librería de automatización**. Son dosocopios de la misma tarea: hacer que el cliente parezca el que el proveedor espera.

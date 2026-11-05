---
id: 2026-1026-rebrowser-tres-estrategias-para-obtener-el-contexto-y-sus-tradeoffs
type: atom
certainty: solid
sources: [sources/2026-10-25-rebrowser-patches.md]
links: ["[[2026-1026-rebrowser-runtime-enable-la-fuga-que-usan-todos-los-antibot]]", "[[2026-1024-chatgpt-creator-el-flujo-no-resuelve-captcha-de-manera-explicita]]", "[[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]"]
---

## Claim
El parche **desactiva el `Runtime.Enable` automático en cada frame** y en su lugar **crea manualmente contextos con IDs desconocidos**; para ejecutar código hay tres vías declaradas. **(1) `addBinding`**: crear un binding en el main world, llamarlo y guardar su context ID — "the ultimate approach that keeps access to the main world and works with web workers and iframes", sin necesidad de tocar el código existente, y **"None are discovered so far"** como contras. **(2) `alwaysIsolated`**: crear un contexto aislado con `Page.createIsolatedWorld` — el código se ejecuta en un mundo separado, lo que **impide que los scripts de la página detecten los cambios mediante `MutationObserver` u otras técnicas** — pero **no se puede acceder a variables del contexto principal** y **los web workers no permiten crear mundos nuevos**, de modo que no se puede ejecutar código dentro de un worker. **(3) `enableDisable`**: llamar a `Runtime.Enable` y **de inmediato** a `Runtime.Disable`, lo que dispara los eventos `Runtime.executionContextCreated` y permite capturar el context ID correcto — da **acceso completo al contexto principal** a cambio de una **ventana breve** en la que la página podría ejecutar el código de detección; el riesgo se considera bajo porque el código de detección suele correr en acciones concretas (páginas de CAPTCHA, formularios de login/registro) justo tras la carga, mientras que la lógica de negocio suele ir más tarde.

## Why It Matters
Es el único caso del corpus donde el vault tiene **el coste real de la elusión cuantificado como un menú de compromisos**: cada modo compra undetectable a cambio de una capacidad concreta (main world / aislamiento frente a MutationObserver / ventana de riesgo). La fuente cierra con un claim explícito: **"our tests show that all these approaches are currently undetectable by Cloudflare or DataDome"** — claim del autor, sin metodología.

La lectura para el vault es de **arquitectura de flujo**, no de coste: el modo `alwaysIsolated` es incompatible con el patrón "leer variables de la página desde el contexto principal" y con la ejecución dentro de web workers, y el modo `enableDisable` es incompatible con las páginas donde el reto se dispara en la carga inicial. Es decir, **el modo de elusión no es una configuración global del proyecto: es una decisión por destino**, exactamente igual que el criterio "elegir por el tipo de captcha que aparece en el destino" que el thread ya tenía ([[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]).

Y hay una conexión incómoda con el bot de Go: su flujo documentado de nueve pasos devuelve 200 y no resuelve captcha, porque **no hay navegador** ([[2026-1024-chatgpt-creator-el-flujo-no-resuelve-captcha-de-manera-explicita]]). Esta fuente dice qué pasa en el caso contrario: cuando **sí** hay navegador, aparece una fuga de protocolo que hay que neutralizar, y esa neutralización **no es gratis de configurar**.

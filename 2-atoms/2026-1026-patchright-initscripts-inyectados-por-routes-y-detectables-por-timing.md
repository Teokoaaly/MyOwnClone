---
id: 2026-1026-patchright-initscripts-inyectados-por-routes-y-detectables-por-timing
type: atom
certainty: solid
sources: [sources/2026-10-25-patchright-playwright.md]
links: ["[[2026-1024-gptgrok2api-stack-warp-privoxy-flaresolverr-como-salida-estable]]", "[[2026-1024-chatgpt-creator-tls-fingerprinting-con-perfiles-chrome-aleatorios]]", "[[2026-1026-patchright-evita-runtime-enable-con-contextos-de-ejecucion-aislados]]"]
---

## Claim
El README dedica un apartado con el nombre **"Init Script Shenanigans"** a explicar un compromiso interno del proyecto. En "Explanation": *"To be able to use InitScripts without `Runtime.enable`, Patchright uses Playwright Routes to inject JavaScript into HTML requests."* En "Bugs": *"Playwright Routes may cause some bugs in other parts of your code. Patchright InitScripts won't cause any bugs that wouldn't be caused by normal Playwright Routes. If you want any of these bugs fixed, you will have to contact the Playwright team."* Y en "Leaks": *"Patchright InitScripts can be detected by Timing Attacks. However, no antibot currently checks for this kind of Timing Attack and they probably won't for a good amount of time. We consider them not to be a big risk of detection."*

## Why It Matters
Es el átomo con la información más valioso del README, porque **documenta un límite explícito de la undetectable**. El autor no afirma que Patchright sea indetectable: afirma que Patchright es indetectable *en la práctica, hoy*, y luego dice en voz alta que **hay una clase de detección —timing attacks— que lo detecta y que se deja sin cubrir a propósito**, con un razonamiento de riesgo explícito ("no antibot currently checks for this kind of Timing Attack and they probably won't for a good amount of time"). Eso es un **argumento de riesgo, no una garantía**, y es la diferencia entre una afirmación reutilizable y una reutilizable con fecha.
El mecanismo explica además por qué el parche de `Runtime.enable` tiene un precio: para poder usar `InitScripts` sin esa llamada, Patchright inyecta el JavaScript **interceptando las peticiones HTML con Playwright Routes**, es decir, interponiéndose en la carga de la página. De ahí la advertencia de que los errores que aparezcan serán **los de Routes**, y de que arreglarlos exige hablar con el equipo de Playwright —no con Patchright. Es dependencia operativa real.
El contraste con lo que el vault ya tiene es directo: `gptGrok2api` resuelve los enlaces que exigen reto de navegador **externalizándolo a FlareSolverr**, un servicio aparte que hace el trabajo con su propio navegador ([[2026-1024-gptgrok2api-stack-warp-privoxy-flaresolverr-como-salida-estable]]). Patchright toma la decisión contraria: **internaliza el reto en el propio driver**, y paga el precio en timing attacks.

## [FRICTION]
> [[2026-1026-patchright-evita-runtime-enable-con-contextos-de-ejecucion-aislados]] afirma, transcribiendo el README, que la fuga de `Runtime.enable` —"the biggest Patch Patchright uses"— queda **eliminada** por ejecutar JavaScript en contextos de ejecución aislados.
> Este átomo presiona esa afirmación: la eliminación es **parcial y condicional**. Para usar `InitScripts` sin `Runtime.enable`, el proyecto tiene que **cambiar de estrategia** —inyectar el JavaScript por `Playwright Routes` en las peticiones HTML— y esa inyección alternativa **es detectable por ataques de temporización**, según el propio README. Es decir: se cierra una puerta y se abre otra, y el vault no puede afirmar "el parche elimina la fuga" sin la condición "y abre un vector de timing". Marcado para juicio humano, no auto-resuelto: la captura no describe el mecanismo del timing attack ni sus condiciones de detección real.

## Nota de verificación
Los tres subapartados están transcritos literalmente. La captura **no** cuantifica el sobrecoste temporal de la inyección por Routes, ni cita a ningún antibot concreto que no compruebe timing attacks, ni da fecha de la afirmación "probably won't for a good amount of time" — que es una predicción sin anclaje temporal.

---
id: 2026-1026-rebrowser-versiones-probadas-chrome-único-y-page-pause-roto
type: atom
certainty: solid
sources: [sources/2026-10-25-rebrowser-patches.md]
links: ["[[2026-1026-rebrowser-parchea-el-codigo-fuente-porque-no-hay-configuracion-que-lo-arregle]]", "[[2026-1026-rebrowser-npm-install-sobrescribe-los-parches-y-hay-que-reaplicarlos]]", "[[2026-1024-gptgrok2api-stack-warp-privoxy-flaresolverr-como-salida-estable]]", "[[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]"]
---

## Claim
El README fija **versiones de soporte concretas y fechadas**: para Puppeteer, *"Latest fully tested version: **24.8.1** (released 2025-05-06)"*; para Playwright, *"Latest fully tested version: **1.52.0** (released 2025-04-17)"*. Y acota el alcance: **"These patches work only for Chrome for now"** —para WebKit o Firefox hay que abrir una issue. Las **limitaciones declaradas para Playwright** son: los parches incluyen el fix de `Runtime.enable` **solo en los modos `addBinding` y `alwaysIsolated`**, el cambio de utility world name por variable de entorno, y que **"more patches are coming"**. Además, **"`page.pause()` method doesn't work with the enabled fix, it needs more investigation"**, con el consejo de desactivar el fix con `REBROWSER_PATCHES_RUNTIME_FIX_MODE=0` mientras se depura. Para **Java, Python y .NET**, las versiones de Playwright "are just wrappers around the Node.js version": hay que encontrar la carpeta `driver` dentro del paquete de Playwright y aplicar el parche ahí con `--packagePath`.

## Why It Matters
Es la parte del README que más se parece a un **ficha de soporte**, y es la que hace utilizable el dato. Sin ella, "rebrowser-patches funciona" sería un claim sin condiciones; con ella, el dato operativo es: **una versión exacta de Puppeteer, una versión exacta de Playwright, un solo navegador**.

La consecuencia para el vault es que **el parche no es una mejora de la elusión sino un contrato de versiones**, y ese contrato tiene una **fecha de caducidad visible**: Puppeteer 24.8.1 es de mayo de 2025 y Playwright 1.52.0 de abril de 2025, con la captura fechada el 2026-10-25. Es decir, **las versiones "fully tested" que el README declara tienen entre 17 y 18 meses**, y el README sigue presentándolas como las últimas. El vault no puede afirmar que esos números sigan siendo vigentes — la captura no da la fecha de la última release del propio repo — pero sí puede registrar el **desfase entre la fecha de la versión probada y la fecha de la captura**, que es exactamente el tipo de dato que el thread usa para fechar cifras y para distinguir "proyecto con releases" de "proyecto con cuatro commits" ([[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]).

El `page.pause()` roto es un detalle pequeño con lectura grande: **la función de depuración del navegador es incompatible con la evasión activa**. Quien depura un flujo automatizado necesita poder pausar el navegador en vivo; con el fix puesto, no se puede. Es un recordatorio de que la evasión y la diagnosticabilidad **tienen un coste de ergonomía**, no solo de eficacia.

Y la nota sobre Java, Python y .NET tiene una lectura que el vault ya tenía en otra capa: las versiones no-JavaScript de Playwright **son envoltorios del driver de Node**, así que el parche no se puede aplicar al paquete de Python sino al `driver` que va dentro. Es el mismo patrón que el bot de Go: **el cliente final es fino y la imitación ocurre por debajo, en una capa que el producto de superficie no expone** ([[2026-1024-gptgrok2api-stack-warp-privoxy-flaresolverr-como-salida-estable]]).

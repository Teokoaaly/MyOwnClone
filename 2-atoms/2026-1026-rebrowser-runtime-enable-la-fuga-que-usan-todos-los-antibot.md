---
id: 2026-1026-rebrowser-runtime-enable-la-fuga-que-usan-todos-los-antibot
type: atom
certainty: solid
sources: [sources/2026-10-25-rebrowser-patches.md]
links: ["[[2026-1026-rebrowser-parchea-el-codigo-fuente-porque-no-hay-configuracion-que-lo-arregle]]", "[[2026-1024-chatgpt-creator-tls-fingerprinting-con-perfiles-chrome-aleatorios]]", "[[2026-1024-gptgrok2api-stack-warp-privoxy-flaresolverr-como-salida-estable]]"]
---

## Claim
La señal central que el repo neutraliza es el uso del comando CDP **`Runtime.Enable`**: Puppeteer y Playwright lo necesitan para recibir eventos del dominio `Runtime.` y así gestionar los contextos de ejecución con los que se evalúa JavaScript en la página. Pero **"there's a technique that detects the usage of this command, revealing that the browser is controlled by automation software like Puppeteer or Playwright"**, y esa técnica **"is used by all major anti-bot software such as Cloudflare, DataDome"**. El README describe la detección como **"a few lines of JavaScript on the page that are automatically called if `Runtime.Enable` was used"**, y remite al post de DataDome *How New Headless Chrome & the CDP Signal Are Impacting Bot Detection*.

## Why It Matters
El vault tenía el **nivel de transporte** de la elusión (huella TLS, token sentinel, cabeceras Datadog en el bot en Go: [[2026-1024-chatgpt-creator-tls-fingerprinting-con-perfiles-chrome-aleatorios]]) y el **nivel de infraestructura** (FlareSolverr como navegador de verdad para resolver retos: [[2026-1024-gptgrok2api-stack-warp-privoxy-flaresolverr-como-salida-estable]]). Esta fuente añade el **nivel de protocolo**: hay una señal que delata al *controlador* del navegador, no al navegador ni a la red, y esa señal **la usan todos los grandes anti-bot**.

La consecuencia operativa es de una sola línea: **con proxies buenos, huellas buenas y scripts de comportamiento buenos, sin este parche "you're just a big red flag for any major website"**. Es decir, la calidad de la elusión de red no compensa una fuga de protocolo —lo que reordena el criterio de selección de partidas: el orden "correo ≪ captcha ≪ proxy ≪ SMS" del thread no dice nada de esta partida, y esta no tiene precio de catálogo, tiene precio de **mantenimiento de parche** (ver [[2026-1026-rebrowser-parchea-el-codigo-fuente-porque-no-hay-configuracion-que-lo-arregle]]).

También fija un hecho de taxonomía útil: **la detección por CDP es lo que distingue a un bot de navegador de un cliente HTTP**. El bot de Go no usa CDP —no hay navegador detrás— y por eso no tiene esta fuga, pero sí tiene que imitar la huella TLS y la instrumentación del proveedor a mano. Son dos capas distintas de "imitar al cliente real", con costes distintos.

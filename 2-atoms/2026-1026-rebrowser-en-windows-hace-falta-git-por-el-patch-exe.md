---
id: 2026-1026-rebrowser-en-windows-hace-falta-git-por-el-patch-exe
type: atom
certainty: solid
sources: [sources/2026-10-25-rebrowser-patches.md]
links: ["[[2026-1026-rebrowser-npm-install-sobrescribe-los-parches-y-hay-que-reaplicarlos]]", "[[2026-1024-extravm-despliegue-tras-confirmacion-en-15-30-minutos]]", "[[2026-1024-evoxt-firewall-capa-3-sin-conexion-al-servidor]]"]
---

## Claim
El README dedica una sección propia, **"Patch command on Windows"**, a un obstáculo operativo que no aparece en ninguna otra plataforma: *"When you try to run this patcher on a Windows machine, you will probably encounter an error because the patch command is not found. To fix this, you need to install Git, which includes patch.exe."* La solución es añadir `C:\Program Files\Git\usr\bin\` al `PATH` y verificar con `patch -v`. En Linux y macOS no hay equivalente: el `patch` del sistema está presente.

## Why It Matters
Es un detalle pequeño de instalación, pero revela la **naturaleza del mecanismo**: el parcheo no es una edición programática del paquete, es la aplicación de un **diff con la utilidad `patch` del sistema operativo**. Eso tiene tres consecuencias operativas que el vault puede usar como criterio de despliegue.

La primera es que **la operación de "parchear" es un paso de build, no un paso de código**: vive en el `node_modules` y hay que re-ejecutarlo, con lo que eso implica en CI ([[2026-1026-rebrowser-npm-install-sobrescribe-los-parches-y-hay-que-reaplicarlos]]). La segunda es que **el entorno de ejecución añade un requisito de sistema**: Windows necesita un Git instalado y en el PATH, lo que en un contenedor o en una imagen de build mínima hay que instalar explícitamente. La tercera es la más relevante para el vault: **el mecanismo es de Unix**, con `patch` como dependencia del sistema, de modo que la ruta de menor fricción es siempre Linux.

Eso conecta con un patrón que el vault viene registrando en la parte de hosting: los proveedores con **panel y despliegue de un clic** son más cómodos que los que exigen un servidor donde uno mismo compone el stack ([[2026-1024-evoxt-firewall-capa-3-sin-conexion-al-servidor]]). Aplicado aquí, la lectura es que **la elusión de navegador no es un producto de panel sino una dependencia de proyecto**, y por tanto **es un coste de composición, no de suscripción**. Para una arquitectura como la del vault —que exige control del entorno— eso es una partida favorable; para un usuario que quiere "navegador indetectable en un minuto", es una barrera real, y es exactamente el hueco que ocupa la nube de rebrowser ([[2026-1026-rebrowser-nube-propia-como-salida-comercial-del-parche-gratuito]]).

## Nota de verificación
Las tres frases están transcritas literalmente del README. La captura **no** publica el número de versiones de Windows soportadas, ni indica si el error es un mensaje de `npx` o del propio script. La caracterización del mecanismo como "aplicación de un diff con la utilidad `patch`" es **inferencia del vault** a partir de la existencia de `patch.exe` y del comando `patch -v`; el código del parcheador no está capturado.

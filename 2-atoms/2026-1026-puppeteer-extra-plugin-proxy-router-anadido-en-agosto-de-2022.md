---
id: 2026-1026-puppeteer-extra-plugin-proxy-router-anadido-en-agosto-de-2022
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-repo.md]
links: ["[[2026-1024-dataimpulse-gateway-unico-y-protocolos]]", "[[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]"]
---

## Claim
El commit más reciente de la carpeta `.github` es **"feat: Add plugin proxy-router (#693)"**, fechado el **8 de agosto de 2022**, y `yarn.lock` lleva ese mismo commit como último cambio. El paquete aparece en el commit de publicación con su propio nombre y versión: **`@extra/proxy-router@3.1.6`**. Es decir, **el enrutado de proxy es un plugin del framework**, con ciclo de versión propio, y no una función del núcleo.

## Why It Matters
El vault ya midió la capa de proxy como un **gateway con credenciales embebidas y siete lenguajes** ([[2026-1024-dataimpulse-gateway-unico-y-protocolos]]) y como un problema de **geometría de sesión** —rotating frente a sticky, con la sesión como unidad real de trabajo y no el gigabyte ([[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]). Ese trabajo de enrutado es exactamente lo que un framework de navegador necesita resolver: reparto de IPs, autenticación por URL, rotación por petición.
La observación de método es la útil: **el enrutado es la parte que se puede dejar de construir**, porque existe como plugin publicado y versionado (`3.1.6`). Es el mismo patrón que el plugin recaptcha: lo que en el thread era "una partida de coste" o "una línea de código a escribir" en un caso es **software reutilizable con versión**. Es un recordatorio de que en un pipeline de automatización el coste de ingeniería no está solo en el captcha: está también en decidir y cablear la rotación de IPs, y eso puede ser un `npm install`.
Dato de frescura: la fecha de este commit es **agosto de 2022**, anterior al último commit del repositorio (marzo de 2023), así que el plugin pertenece a la última ventana de actividad del proyecto.
Nota de verificación: la captura **no** describe qué hace el plugin ni qué proveedores o esquemas de proxy soporta; solo consta su nombre, su versión publicada y su fecha de incorporación.

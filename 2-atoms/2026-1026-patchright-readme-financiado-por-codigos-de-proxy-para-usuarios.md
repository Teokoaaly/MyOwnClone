---
id: 2026-1026-patchright-readme-financiado-por-codigos-de-proxy-para-usuarios
type: atom
certainty: solid
sources: [sources/2026-10-25-patchright-playwright.md]
links: ["[[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]", "[[2026-1024-chatgpt-creator-tls-fingerprinting-con-perfiles-chrome-aleatorios]]", "[[2026-1026-patchright-declara-pasar-catorce-detectores-publicados]]"]
---

## Claim
El README ocupa su parte central con **cinco bloques de patrocinio de proveedores de proxy**, cada uno con **códigos de descuento propios para usuarios de Patchright**: NodeMaven (**PATCHRIGHT35** = 35 % en proxies móviles y residenciales, **PATCHRIGHT40** = 40 % en ISP estáticos; promete 99,9 % de uptime, *fraud score < 97 %* y *no KYC*), Swiftproxy (**PROXY90** = 10 %; 195+ ubicaciones, trial de 500 MB), RapidProxy (**RAPID10** = 10 %; 90M+ IPs residenciales, desde **$0.65/GB** rotando y **$5/IP** estático de 30 días), Scrappey (**PATCHRIGHT** = 10 %; **Clearcote**, un Chromium parcheado propio, y **un endpoint**, *per request* sin mínimo mensual) y ProxyLane (**PATCHLANE35** = 35 %; 28M IPs residenciales, sticky hasta 72 h, desde **$2/GB**). Además, Scrappey declara explícitamente que su problema es **"keeping proxies rotating, fingerprints current and sessions alive"** —es decir, el mantenimiento operativo de la elusión— mientras que Patchright se ocupa de *"Getting the browser past detection"*.

## Why It Matters
Es un **modelo de financiación observable** que no tenía el vault, y explica una parte de la forma del proyecto: una herramienta de elusión open source **se financia con referidos de proxy**, lo que conecta directamente el proyecto con la partida de coste que el thread sí cotiza —el proxy por gigabyte, con su geometría de sesión ([[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]). No es un dato trivial: significa que **la elusión de navegador y la red forman un único paquete comercial**, y que el mantenedor tiene incentivo económico en que sus usuarios compren proxy.
El reparto de responsabilidades entre Scrappey y Patchright que hace el propio README es una **taxonomía de la capa de elusión** que el vault no tenía escrita: *detección* (Patchright: hacer que el navegador pase) frente a *operación* (Scrappey: proxies rotando, fingerprints al día, sesiones vivas). Y el propio Scrappey describe su producto como **"a real session, not a fetch proxy"** — con `click, type, wait and scroll` sobre la API — que es exactamente la frontera entre las dos capas.
Para la economía del thread, el dato duro es que los **precios de proxy con descuento para esta comunidad** ($0.65/GB rotando, $2/GB en ProxyLane, $5/IP estático) están **publicados en el README de la herramienta**, no en el catálogo del proveedor: la ruta de compra del sector pasa por el propio proyecto de elusión.

## Nota de verificación
Los cinco proveedores, sus códigos, cifras y promesas están transcritos literalmente del README. Todos esos datos son **claims del patrocinador y claims del README**, no mediciones del vault. La captura **no** incluye el precio de lista de los proveedores sin descuento, ni las condiciones de los códigos. La lectura del modelo de financiación es inferencia del vault a partir de la estructura de patrocinio.

---
id: 2026-1023-midjourney-proxy-edicion-plus-ampliada
type: atom
certainty: solid
sources: [sources/2026-10-22-midjourney-proxy-github.md]
links: ["[[2026-1023-midjourney-proxy-funciones-imagen-base64-y-describe]]", "[[2026-1023-midjourney-proxy-riesgo-de-cuenta-por-frecuencia-de-dibujo]]", "[[2026-1023-midjourney-proxy-funcion-multicuenta-con-cola-por-cuenta]]"]
---

## Claim
El README de la edición abierta remite explícitamente a una **edición ampliada en otro repositorio**: **"🚀 更多功能请查看 midjourney-proxy-plus"** (repo `litter-coder/midjourney-proxy-plus`), cuya lista declara: soporta todas las funciones de la versión abierta, **Shorten (análisis de prompt)**, **Pan**, **Zoom**, **Vary (Region)** (repintado parcial), **casi todos los botones asociados y el modo 🎛️ Remix**, **obtención del seed**, **"账号池持久化，动态维护"** (pool de cuentas persistente y mantenido dinámicamente), consulta de **/info y /settings** de la cuenta y **ajuste de settings**, soporte del **bot niji**, del bot **InsightFace** de sustitución de rostros, **panel de administración embebido**, **configuración dinámica en el backend**, **resolución de la caída frecuente de token**, **verificación automática de popups**, **apelación automática de "Action needed to continue"**, **"最新的MidJourney V7 Alpha版本"** y **"视频生成相关接口"** (interfaces de generación de vídeo).

## Why It Matters
La línea de producto separa **núcleo** y **superficie**: todo lo que es "operación sobre el proveedor" (pool de cuentas, settings, captcha, apelación, panel de admin, configuración dinámica) vive en la edición plus, mientras que lo que es "uso del modelo" (Imagine, Blend, Describe, traducción, sensible) está en la versión abierta ([[2026-1023-midjourney-proxy-funciones-imagen-base64-y-describe]]).
Para el vault esto mapea casi exactamente contra su propio eje: el core público de `myownclone` es el clon; lo que se cobra aparte es la operación. Aquí el core abierto es "llamar al dibujo por API" y lo premium es "que no te baneen".
Dos datos de mercado que importan: la edición plus declara soportar **V7 Alpha** y **generación de vídeo**, es decir, el proxy tiene que perseguir las versiones del proveedor — y el repositorio abierto tiene **229 commits**, con el último cambio de código relevante en junio de 2024 (el README se actualizó en agosto de 2025). La versión abierta queda atrás; la plus sigue.
Y el reparto es coherente con la lógica de cuentas: el pool persistente ([[2026-1023-midjourney-proxy-funcion-multicuenta-con-cola-por-cuenta]]) solo tiene sentido si hay una operación de mantenimiento de sesión que lo justifique, y esa es exactamente la función que se cobra.

## Nota de verificación
La lista de la edición plus es **declarada por el README del repositorio abierto**, no verificada: el vault no ha capturado el repositorio `midjourney-proxy-plus` ni su código. No hay precios, licencia ni forma de acceso a esta edición en la fuente.

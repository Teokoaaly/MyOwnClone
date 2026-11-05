---
id: 2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar
type: atom
certainty: solid
sources: [sources/2026-10-23-2captcha-solver.md]
links: ["[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1024-2captcha-arkose-funcaptcha-50-dolares-por-1000]]", "[[2026-1024-2captcha-flujo-api-en-cinco-pasos-con-captcha-id]]"]
---
## Claim
La columna "Solving speed" de la tabla da **1 segundo** para Image Captcha y reCAPTCHA v3, y **2 segundos** para reCAPTCHA v2, Cloudflare Turnstile, reCAPTCHA Enterprise y Amazon captcha. Los únicos tipos fuera de ese rango son Arkose/FunCaptcha (**16 sec**) y ALTCHA (**17 sec**).

## Why It Matters
Fija el **presupuesto de latencia** de una automatización que dependa de esto: 1-2 segundos es compatible con un pipeline interactivo y con polling agresivo; 16-17 segundos ([[2026-1024-2captcha-arkose-funcaptcha-50-dolares-por-1000]], [[2026-1024-2captcha-altcha-299-y-17-segundos-el-mas-lento]]) rompe cualquier suposición de sincronía.
Y el "99.9% uptime" más "el server load no afecta al precio" es una promesa comercial doble: el proveedor garantiza que su capacidad no se degrada con la carga, lo que en la práctica significa que el cuello de botella se traslada al lado del cliente (reintentos) o al del trabajador. Es un argumento de venta explícitamente contrario al de los proveedores de VPS del vault, donde la capacidad sí se degrada por carga ([[2026-1022-costes-por-categoria-tenant]] no aplica aquí, pero el contraste de modelo de capacidad es directo: aquí el precio es estable por diseño).
Nota: la captura **no** publica percentiles de latencia, ni el tiempo de espera en cola, ni qué significa operativamente "99.9% uptime" para la API.


## Nota de extensión 2026-10-26
Este átomo define un "presupuesto de latencia" para automatización —1-2 segundos compatibles con pipeline interactivo, 16-17 segundos incompatibles con sincronía— y lo deriva de una columna "Solving speed" que va de 1 a 17 segundos. La captura de AntiCaptcha muestra que **la latencia es una constante de proveedor, no del tipo**: los **trece** tipos del catálogo resuelven en **5 s**, incluidos los dos que en 2Captcha eran los lentos ([[2026-1026-anticaptcha-velocidad-uniforme-de-5-segundos]]). La consecuencia para la lectura del átomo es que "1-2 segundos" y "16-17 segundos" no son dos clases de captcha sino **dos proveedores**: el presupuesto de latencia de un pipeline se cotiza por proveedor (1-2 s en 2Captcha, 5 s en AntiCaptcha) y el tipo de captcha solo cambia el precio. Eso **debilita la inferencia** que el thread repite en la §8.6 —"solo los dos tipos caros son además los lentos... el solapamiento entre precio y latencia"—, porque el solapamiento desaparece en el segundo catálogo: allí Enterprise ($5) y Arkose ($3) resuelven en el mismo 5 s que Images ($0.5–$0.7). La advertencia final del átomo ("la captura no publica percentiles de latencia, ni el tiempo de espera en cola") se refuerza: ahora hay dos proveedores y **ninguno** publica percentiles.


## Nota de extensión 2026-10-27
La captura del 2026-10-26 (tabla de 48 filas) **contradice tres afirmaciones de este átomo con la misma operación**: la banda "1–2 sec" y la banda "16–17 sec" eran una foto de la tabla de ocho filas del 2026-10-23, y **en tres días cuatro de las ocho velocidades cambiaron** — **ALTCHA de 17 a 15 sec**, **Arkose/FunCaptcha de 16 a 18 sec**, **Amazon captcha de 2 a 3 sec** y **reCAPTCHA Enterprise de 2 a 1 sec** — **sin que cambiara un solo precio**. Ver [[2026-1027-2captcha-cuatro-velocidades-cambiaron-en-tres-dias]].

Con el catálogo completo, la banda lenta **no tiene techo**: **KeyCAPTCHA a 37 sec** es el tipo más lento, seguido de **Cutcaptcha y Prosopo Procaptcha a 24 sec**, **Lemin a 20 sec**, **Yidun a 17 sec**, **TSPD a 16 sec** y **ALTCHA a 15 sec** — nueve tipos en total por encima de 15 segundos (siete lo superan, dos lo igualan). Ver [[2026-1027-2captcha-keycaptcha-37-segundos-como-nuevo-techo-de-latencia]]. Y hay un conjunto de tipos **de precio medio ($1.45–$2.99) con latencia de 8–13 segundos** —DataDome e Imperva (11 sec), MTCaptcha (8 sec), Capy Puzzle (8 sec), Friendly captcha (11 sec), atbCAPTCHA (11 sec), CyberSiARA (13 sec), Basilisk (12 sec), Alibaba (12 sec)— que **no son outliers de precio pero sí de latencia**, de modo que la conclusión del átomo "solo los dos tipos caros son además los lentos" necesita la precisión de que **el precio alto y la latencia alta son cosas distintas**: el tipo más lento del catálogo cuesta $2.99 (el peldaño habitual) y el segundo más lento $1.45.

La conclusión operativa del átomo ("un captcha estándar no es un cuello de botella de tiempo") **se mantiene para la familia de texto y los captchas de Google**, que resuelven en 1–5 segundos, pero el umbral operativo correcto para dimensionar un pipeline debe fijar **8–11 segundos como banda media del catálogo**, no 1–2. Y toda cifra de latencia de este corpus debe citarse **con fecha y proveedor**, porque la deriva medida entre dos capturas es de ±1–2 segundos en la mitad de los tipos comunes.

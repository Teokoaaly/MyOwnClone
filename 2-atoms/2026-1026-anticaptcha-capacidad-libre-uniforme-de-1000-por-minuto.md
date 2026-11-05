---
id: 2026-1026-anticaptcha-capacidad-libre-uniforme-de-1000-por-minuto
type: atom
certainty: solid
sources: [sources/2026-10-25-anti-captcha-pricing.md]
links: ["[[2026-1024-2captcha-capacidad-libre-por-minuto-como-proxy-de-cola]]", "[[2026-1024-2captcha-altcha-299-y-17-segundos-el-mas-lento]]", "[[2026-1026-anticaptcha-velocidad-uniforme-de-5-segundos]]"]
---

## Claim
La columna "Free Capacity" del catálogo de AntiCaptcha da **1000 / per minute para los trece tipos, sin variación**, y la columna "Workers" da **"Busy: 1000 / Idle: 1200"** en las trece filas.

## Why It Matters
Es la **contrapartida directa** del átomo que interpreta la capacidad libre como un proxy de la profundidad del pool de trabajadores por tipo: en 2Captcha esa columna va de **12.000** (Image Captcha) a **203** (ALTCHA), una dispersión de 59×, y el vault la lee como "la profundidad del pool humano" ([[2026-1024-2captcha-capacidad-libre-por-minuto-como-proxy-de-cola]]). AntiCaptcha publica un número **plano**: 1000/min para todo, incluidos los tipos que en el otro catálogo son los más caros y los de menor capacidad.
Eso hace que la "capacidad libre por minuto" **no sea una propiedad del tipo de captcha** sino, como mucho, un dato de disponibilidad global del proveedor — frente al dato de 2Captcha, donde el mismo número es un indicador de nicho ([[2026-1024-2captcha-capacidad-libre-por-minuto-como-proxy-de-cola]]). La consecuencia operativa es práctica: con 1000/min en todos los tipos, un pipeline que resuelva ALTCHA **no tiene que aceptar cola por nicho** — el caso de 2Captcha, donde ALTCHA era el tipo con 203/min y el más lento ([[2026-1024-2captcha-altcha-299-y-17-segundos-el-mas-lento]]), y el argumento del vault de que "el tipo de captcha más caro es el que además tiene menos capacidad" queda acotado a 2Captcha.
La segunda es que la velocidad es **uniforme** en los trece tipos, lo que hace que capacidad y latencia no se crucen ([[2026-1026-anticaptcha-velocidad-uniforme-de-5-segundos]]). Y hay un dato estructural que AntiCaptcha publica y 2Captcha no: la columna **"Workers"** con dos cifras (1000 ocupados / 1200 libres). Es una medida de **dotación de workforce**, no de cola, y por tanto no es la misma magnitud que "free capacity per minute" aunque ambos son atos de capacidad.
Nota: la captura **no** define si "free capacity" es capacidad garantizada o cola, ni qué significa exactamente "Busy" e "Idle" (¿trabajadores ocupados en un instante, o media?).

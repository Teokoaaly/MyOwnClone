---
id: 2026-1027-dataimpulse-intervalo-rotacion-sticky-configurable-1-a-120-minutos
type: atom
certainty: solid
sources: [sources/2026-10-26-dataimpulse-docs-types-of-connections.md]
links: ["[[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]", "[[2026-1027-dataimpulse-sticky-por-puerto-en-rango-10000-20000]]", "[[2026-1026-decodo-sesion-sticky-hasta-30-minutos-contra-30-120-de-dataimpulse]]", "[[2026-1027-dataimpulse-sesion-sticky-movil-hasta-120-minutos]]"]
---

## Claim
El intervalo de rotación de la sesión sticky **es un parámetro configurable por el cliente**, y la página lo publica con tres cifras: **"The rotation interval for sticky proxies can range from 1 to 120 minutes, with the average duration being 30 minutes."** El valor por defecto está escrito literalmente: **"If no Rotation Interval is specified for a Sticky connection or is set to \"0\", the default interval will be 30 minutes."** Es decir, el rango completo es **1–120 minutos**, la **media** es **30 minutos** y el **default** es **30 minutos**, con un valor centinela explícito (`"0"`) que significa "usa el default".

## Why It Matters
Esto convierte la duración de la sesión sticky de una **constante del proveedor** en un **parámetro de la llamada**, y corrige de paso la lectura que el vault tenía heredada de la home: el átomo de sesiones ([[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]) recogía "residencial — remain active for **30-120 minutes on average**" y "up to **120 minutes**", es decir el rango 30–120 leído como un rango de **duración**; la documentación dice otra cosa distinta y más precisa: el rango 1–120 es el del **intervalo de rotación que el cliente elige**, y el 30 es la **media**, no el suelo. La consecuencia práctica es que **el suelo de 1 minuto es el dato nuevo y es el que aprieta**: con una sesión sticky de 1 minuto, un flujo de verificación que necesita la misma IP entre el registro, el SMS y la confirmación por email puede consumir **tres sesiones de 1 minuto** en lugar de tres de 30 ([[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]]).
El valor `"0"` es además una pieza de diseño útil: el cliente puede **declarar explícitamente "sin intervalo propio"** y heredar el default, en lugar de omitir el parámetro y no saber qué ha pasado. Y el hecho de que el proveedor publique un rango de 1 a 120 con media 30 es lo que permite fechar la **duración sticky de los pools que el corpus aún no tenía** — el móvil, cuyo tope de 120 minutos ya está medido en [[2026-1027-dataimpulse-sesion-sticky-movil-hasta-120-minutos]] — dentro de un mismo contrato: el 120 del móvil es **el techo del contrato**, no un tope propio del pool.

## [FRICTION]
> [[2026-1024-dataimpulse-sesiones-rotating-y-sticky]] afirma que para el pool **residencial** las sesiones "remain active for **30-120 minutes on average**" y que el bloque Key Features resume "the same IP **up to 30 minutes by default**".
> Este átomo presiona ese dato: la documentación técnica dice que el **rango configurable es 1 a 120 minutos** y que la **media** es 30, no que el rango de durations sea 30–120. Si la lectura de la home ("30-120 minutes on average") era un rango de duración, entonces la home omite el suelo real de 1 minuto; si era (como ahora parece) una manera laxa de describir el intervalo, entonces el corpus del vault ha estado usando un rango de sesión más estrecho del que el producto permite, y todos los cálculos de "sesiones por flujo" que salen de él están mal dimensionados por arriba.
> Ambas no pueden ser completamente correctas: o la duración sticky residential no puede bajar de 30 minutos, o el rango real es 1–120 y el "30-120" de la home era marketing de "media y máximo". Marcado para juicio humano, no auto-resuelto: la captura no publica si el intervalo mínimo de 1 minuto aplica a todos los pools ni si el pool móvil comparte el mismo contrato.

## Nota de verificación
Cifras y frases transcritas literalmente de la página, incluido el valor centinela `"0"`. La captura **no** publica: en qué unidad o parámetro de la API se declara el intervalo, si el intervalo puede fijarse por sesión o solo por cuenta, ni si el mínimo de 1 minuto aplica a todos los tipos de proxy.

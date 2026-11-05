---
id: 2026-1027-2captcha-recaptcha-v3-se-factura-por-el-score-obtenido
type: atom
certainty: solid
sources: [sources/2026-10-26-2captcha-pricing-captcha.md]
links: ["[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1027-2captcha-catalogo-completo-de-48-filas-de-captcha]]", "[[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]]"]
---
## Claim
La tabla de 48 filas de `2captcha.com/pricing` del 2026-10-26 separa **reCAPTCHA v3 en dos filas distintas según el score que entrega**: **"reCAPTCHA v3(score <= 0.3)" a $1.45 por 1000** y **"reCAPTCHA v3(score > 0.3)" a $2.99 por 1000**. Las dos filas comparten **1 sec** de velocidad de resolución y **757** de capacidad libre por minuto, y ambas apuntan a la misma página de producto (`/p/recaptcha_v3`).

## Why It Matters
Es la primera vez que el vault ve un captcha cuyo **precio depende de una propiedad del resultado** y no del tipo de reto. Todo lo demás del catálogo se factura por tipo; el v3 se factura por **banda de score**. Y el signo es contraintuitivo: **el score bajo es el barato** ($1.45) y el score alto es el caro ($2.99), es decir, la diferencia de precio (×2,06) va en sentido contrario a la diferencia de valor para el destino —un sitio que exige score alto paga más por el mismo tipo de reto.

La consecuencia para el modelo de coste es de **estructura del contrato**: la partida de captcha deja de ser "precio por unidad" y pasa a tener **una dimensión de calidad implícita en el precio**, como el proxy por gigabyte o el SMS por par (país, operador). Quien compra v3 está comprando dos productos con el mismo nombre, y el proveedor está publicando la frontera de producto. Para el hilo, esto importa porque [[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]] ("se paga solo por captchas resueltos") era hasta ahora una descripción completa del contrato comercial: **no lo es**, porque la calidad del token entra en la factura.

También abre una comparación directa con los otros dos catálogos: AntiCaptcha publica reCAPTCHA v3 como fila única con asterisco y CapSolver lo publica a **$1.0/1k (< 3S)** ([[2026-1026-capsolver-nueve-tipos-con-precio-y-latencia]]). Es decir, **la granularidad de precio de un mismo tipo es también una variable de proveedor**: 2Captcha publica dos bandas, CapSolver una sola cifra, AntiCaptcha un precio con nota de volumen.

## [FRICTION]
> [[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]] describe reCAPTCHA v3 como **"reCAPTCHA v3 $1.45 — $2.99"**, un rango con la misma forma que el de reCAPTCHA v2 ("$1 — $2.99") y el de FunCaptcha ("$1.45 — $50"), y de ahí saca que el catálogo "va de $0.5 a $2.99 por 1000" con "dos outliers muy por encima".
> Este átomo presiona esa lectura en un punto: en 2Captcha **no todos los rangos son incertidumbre de precio por tipo**. El rango del v3 está **desglosado en dos filas con criterio explícito y distinto** —el score— y solo ese. O el rango del v3 se lee como un intervalo de precio por tipo (y entonces la tabla no dice qué determina el precio dentro del rango), o se lee como dos SKUs con criterio de calidad (y entonces el resto de los rangos del catálogo —v2 y FunCaptcha— son **también** algo más que un intervalo, y el vault no puede atribuirlos al tipo). Ambas no pueden ser completamente ciertas a la vez. Marcado para juicio humano, no auto-resuelto: la captura solo publica la tabla, sin explicar la regla de asignación de banda.
> La consecuencia operativa sí queda establecida: **la regla de precio del v3 es pública y la del v2 no**, y el vault no puede tratar "$1 — $2.99" como una misma categoría de dato en las dos filas.

Nota: la captura **no** explica cómo se asigna el score a la fila, ni publica umbral o volumen de score, ni dice si el precio es por token entregado o por token entregado con score de esa banda.

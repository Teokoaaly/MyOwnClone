---
id: 2026-1104-hetzner-ahorro-medio-cambia-con-operandos-identicos-al-11-03
type: atom
certainty: solid
sources: [sources/2026-11-04-hetzner-cloud.md]
links: ["[[2026-1102-hetzner-ahorro-medio-de-trafico-fluctua-entre-capturas]]", "[[2026-1023-hetzner-comparativa-trafico-20tb-contra-hyperscalers]]", "[[2026-1103-hetzner-cinco-capturas-estabilidad-catalogo-vs-widgets-dinamicos]]"]
---

## Claim
Con la perilla de tráfico en **20 TB**, la captura del **2026-11-04** del comparador de Hetzner Cloud muestra **exactamente los mismos tres operandos que la captura del 2026-11-03** — **AWS € 1,560.28/mo, Azure € 1,287.00/mo, Google € 1,326.50/mo, Hetzner € 0.00/mo** — pero un "Average traffic cost savings with Hetzner" distinto: **€ -4,633.59/mes** frente a los **€ -5,378.26/mes** del día anterior. La variación del ahorro medio es de **€ 744.67/mes con la tabla idéntica byte a byte**. La atribución a **sparecores.com** sigue literal en la página ("All figures are based on independent data from sparecores.com").

## Why It Matters
Esta es la **tercera vez** que el patrón "la media se mueve sin que cambien los operandos" aparece en la serie, y la primera vez que se produce con los operandos **byte a byte idénticos** a la captura anterior (el caso 10-31 vs 11-02 y el 10-31 vs 11-02/11-03 compara conjuntos de hyperscaler distintos o solo parcialmente iguales). La consecuencia metodológica no cambia y se refuerza: **el "ahorro medio" de la página no es una función de los números que la propia tabla muestra**, así que no puede usarse como dato duro en el thread `escala-de-hosting-barato-y-el-limite-de-4-euros`. Lo que sí es citable sigue siendo el dato del vault: **Hetzner € 0,00/mo de egreso a 20 TB frente a más de €1.280/mes en los tres hyperscalers** (AWS € 1.560,28 · Azure € 1.287,00 · Google € 1.326,50), una diferencia de un orden de magnitud que hace irrelevante cualquier discrepancia de ~€700/mes en la propaganda del ahorrado ([[2026-1023-hetzner-comparativa-trafico-20tb-contra-hyperscalers]]). Para el objetivo de ≤ €4/mes la decisión tampoco cambia: el egreso no es la palanca de coste de este proveedor, el precio de entrada lo es ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]).

## [FRICTION]
> [[2026-1102-hetzner-ahorro-medio-de-trafico-fluctua-entre-capturas]] (escrita hace 3 semanas) afirmaba que "la cifra de 'ahorro medio' se mueve entre capturas sin que cambien los operandos que se muestran a la derecha", y su nota de re-verificación del 2026-11-03 matizaba que "por primera vez los operandos y la media se mueven juntos en la misma dirección", lo que leía como si el widget recalculara el conjunto completo de forma consistente.
> Este átomo presiona esa matización porque el **2026-11-04 vuelve al caso simple**: operandos idénticos al 11-03 y media distinta en **€ 744.67**. Si el widget recalculase la tabla entera de forma consistente, los operandos no podrían permanecer byte a byte iguales mientras la media se mueve. La lectura correcta es la original del átomo —**la media es un valor independiente del render, no una agregación de la tabla**— y la "primera vez" del 11-03 era un artefacto del muestreo.
> Ambas no pueden ser completamente correctas en su lectura completa: o el 11-03 fue una coincidencia de operands y media, o el 11-04 es un render inconsistente. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
La captura transcribe literalmente "AWS € 1,560.28/mo. / Azure € 1,287.00/mo. / Google € 1,326.50/mo. / Hetzner € 0.00/mo." y "-€ -4,633. / 59 / Average traffic cost savings with Hetzner / month". El contraste con la captura del 11-03 es directo (mismos tres operandos, ahorro € -5.378,26). La aritmética de la tabla sigue sin cuadrar con la media declarada: la suma de las tres diferencias frente a Hetzner (€ 0,00) es **€ 4.173,78** y su media **€ 1.391,26**, mientras la cifra declarada es **€ 4.633,59** — superior a la media de las diferencias que la tabla muestra. La fuente (sparecores.com) **no está verificada en la captura**: no hay desglose ni metodología.

---
id: 2026-1104-workos-el-render-de-soporte-confirma-que-scale-no-incluye-revision-trimestral
type: atom
certainty: solid
sources: [sources/2026-11-04-workos-pricing.md]
links: ["[[2026-1102-workos-el-plan-scale-perdio-revision-trimestral-y-configuracion]]", "[[2026-1101-workos-plan-scale-de-soporte-1000-al-mes]]", "[[2026-1104-workos-vuelve-la-seccion-de-soporte-pero-sin-precios]]"]
---

## Claim
La escala de niveles de soporte del **2026-11-04** sitúa **"Quarterly architecture review"** y **"End-user configuration support"** **exclusivamente en el "Enterprise plan"**, y **no** en el "Scale plan" (que solo lista Video calls, Private Slack channel, Technical onboarding guidance y Guaranteed response SLAs). Esto **coincide con la tabla del 2026-11-02** (donde ambas filas son "—" en Scale) y **contradice la tabla del 2026-11-01** (donde ambas eran "✓" en Scale). Decisivo: la captura cruda del **2026-10-31**, con 3.187 palabras, ya traía la **misma lista de niveles** (Scale sin revisión trimestral ni configuración end-user), de modo que el texto de la página y la tabla del 11-02 coinciden y la tabla del 11-01 es la única que discrepa.

## Why It Matters
Es la primera evidencia de página (no de transcripción condensada) sobre la composición del plan Scale, y con el cruce del 10-31 **presiona con dos fuentes crudas la versión del 11-02** de [[2026-1102-workos-el-plan-scale-perdio-revision-trimestral-y-configuracion]] frente a la del 11-01: dos volcados crudos de la página real, en formatos distintos y separados por cuatro días, coinciden en que la revisión de arquitectura trimestral y el soporte de configuración end-user **no** están en el plan de $1.000/mes. La hipótesis más económica es que **la tabla condensada del 11-01 transcribió mal esas dos celdas** y que no hubo ningún cambio real de oferta el 11-02.

La lectura operativa para el vault es que el valor diferencial del plan Scale se reduce a **accesibilidad del soporte** (videollamadas, Slack privado, onboarding técnico, SLAs de respuesta garantizados) y que la **revisión de arquitectura con un ingeniero** —el entregable que un cliente enterprise valoriza de verdad— está detrás del contrato Enterprise de precio no publicado. En términos de coste, esto **relaja** la preocupación de que el plan de $1.000/mes se hubiera degradado.

Límite honesto de la evidencia: el render del 11-04 **no da los tiempos de respuesta concretos** de Scale ("Guaranteed response SLAs", sin cifras) ni los del Enterprise más allá de "24 x 7 x 365", y no publica precios. Por tanto **no cierra** del todo la fricción: los P1 = 1 hora hábil / P2 = 3 horas hábiles y el horario lunes-viernes 6:00–17:00 Pacific Time que documenta [[2026-1101-workos-plan-scale-de-soporte-1000-al-mes]] **siguen sin corroboración literal** en ninguna captura cruda.

## [FRICTION]
> [[2026-1101-workos-plan-scale-de-soporte-1000-al-mes]] afirma que el plan Scale a $1.000/mes incluye "revisión de arquitectura trimestral" y "soporte de configuración para end-users", y le asigna "P1 en 1 hora hábil y P2 en 3 horas hábiles".
> Este átomo presiona esa creencia en la primera mitad: las listas de niveles del 10-31 y del 11-04, con un formato de página distinto al de la tabla del 11-01, **omiten** ambas filas en Scale y las dejan solo en Enterprise, alineándose con la captura del 11-02.
> Ambas no pueden ser completamente correctas: o la tabla condensada del 11-01 transcribió mal esas dos celdas, o la oferta del plan Scale cambió entre el 10-31 y el 11-02 (y volvió a cambiar antes del 10-31 o el 11-04, lo que es improbable). Marcado para juicio humano, no auto-resuelto. En la segunda mitad (los tiempos P1/P2 y el horario hábil) **no hay conflicto**: ninguna captura cruda del vault lo publica, así que ese dato sigue apoyándose solo en el 11-01.

## Nota de verificación
sources/2026-11-04-workos-pricing.md, líneas 477-496: la lista "### Scale plan" (477-486) contiene cuatro ítems y ninguno es "Quarterly architecture review" ni "End-user configuration support"; la lista "### Enterprise plan" (488-496) contiene ambos. Fuentes 2026-11-01 y 2026-11-02, líneas 80-81 de cada una: "Quarterly architecture review" y "End-user configuration support" con ✓ en Scale el 11-01 y con — en Scale el 11-02. Fuente cruda sources/2026-10-31-workos-pricing.md, líneas 349-374: "### Scale plan" con "Video calls / Private Slack channel / Technical onboarding guidance / Guaranteed response SLAs" y "### Enterprise plan" con "Dedicated support account manager / Quarterly architecture review / End-user configuration support / 24 x 7 x 365 response SLAs".

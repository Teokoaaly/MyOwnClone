---
id: 2026-1103-workos-captura-cruda-no-trae-tabla-de-soporte
type: atom
certainty: solid
sources: [sources/2026-11-03-workos-pricing.md]
links: ["[[2026-1102-workos-el-plan-scale-perdio-revision-trimestral-y-configuracion]]", "[[2026-1101-workos-plan-scale-de-soporte-1000-al-mes]]", "[[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]]"]
---

## Claim
La captura del **2026-11-03** de workos.com/pricing es un **volcado crudo de la página** (580 palabras, con marcadores "..." donde el extractor truncó bloques) y su contenido **no incluye la tabla "Support Plans"**, ni la sección "Definitions", ni la sección "Enterprise" que sí aparecían en las capturas condensadas del 2026-10-31, 2026-11-01 y 2026-11-02. Tampoco reproduce el rung tabular "101+ | Custom | Contact sales" de la escalera SSO: en esta versión el tramo por encima de 100 conexiones se enuncia como **"Need additional scale? Talk to us"**.

## Why It Matters
Es un aviso metodológico para el vault: la cuarta captura de la misma URL **no es comparable celda a celda** con las tres anteriores porque las anteriores eran condensaciones tabulares y esta es el volcado crudo. Por tanto **no puede usarse ni para confirmar ni para refutar** la tabla de soporte, y la fricción abierta entre el plan Scale del 11-01 y del 11-02 ([[2026-1102-workos-el-plan-scale-perdio-revision-trimestral-y-configuracion]]) **queda sin resolver**: el 11-03 no aporta ninguna evidencia sobre la "Quarterly architecture review" ni sobre el "End-user configuration support" del plan de $1.000/mes ([[2026-1101-workos-plan-scale-de-soporte-1000-al-mes]]).

La lectura operativa: mientras no exista una captura que vuelva a incluir la tabla de soporte, el vault **no puede cotizar** el plan Scale de WorkOS más allá del precio ($1.000/mes) y hay que dejar constancia de que la composición de ese plan es dato pendiente, no dato confirmado. Y la diferencia de forma del rung 101+ ("Custom | Contact sales" en la tabla condensada vs "Need additional scale? Talk to us" en el volcado crudo) refuerza la conclusión del átomo de la calculadora ([[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]]): **más allá de cierto punto el precio no está publicado, se negocia**.

## [FRICTION]
> [[2026-1102-workos-el-plan-scale-perdio-revision-trimestral-y-configuracion]] afirma que las capturas del 2026-11-01 y del 2026-11-02 se diferencian **solo** en dos filas de la tabla de soporte, y da por cerrado que "todos los precios son idénticos en ambas capturas".
> Este átomo presiona esa creencia porque la captura del **2026-11-03** de la misma URL **no contiene ninguna tabla de soporte**, de modo que no se puede afirmar que la oferta "sigue igual" ni que "ha cambiado": la secuencia de tres capturas solo cubre la tabla de soporte en dos días, y el tercero es un volcado crudo sin esa sección.
> Ambas no pueden ser completamente correctas: o el 11-03 es un volcado crudo de la misma página (y entonces las diferencias del 11-01 vs 11-02 son transcripción y no cambios reales), o la página cambió de forma entre el 11-02 y el 11-03 y el soporte se retiró de la página. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
Comparación literal entre sources/2026-11-03-workos-pricing.md y sources/2026-11-02-workos-pricing.md: la captura del 11-03 contiene "## Pay as you go", "## Annual Credits", "## Estimate your costs", "## Frequently asked questions" y "## Why WorkOS?", y **no** contiene "## Support Plans", "## Definitions" ni "## Enterprise". El tramo >100 conexiones aparece como "Need additional scale? Talk to us" bajo "### Number of connections".

## Actualización 2026-11-04
La quinta captura de workos.com/pricing (**2026-11-04, 1.067 palabras, también volcado crudo**) **vuelve a renderizar la sección de soporte**, pero **no como la tabla de tres columnas**: lo hace como la escala de niveles "## Support SLAs" → "Included for all accounts" / "Scale plan" / "Enterprise plan", **sin ningún precio** y con un enlace "View support plans" a `workos.com/support-plans`. Esta forma por niveles es **idéntica** a la del volcado crudo del **2026-10-31** (líneas 349-374), mientras que la tabla con precios "Standard (Free) / Scale ($1,000/mo) / Enterprise (Custom)" solo existe en las capturas **condensadas** del 11-01 y 11-02. En consecuencia, la secuencia alterna entre "niveles sin precios" (10-31, 11-04), "tabla con precios" (11-01, 11-02 condensadas) y "sección ausente" (11-03), lo que apunta a un **problema de render/extractor** más que a un cambio de oferta, y deja el **precio de $1.000/mes del plan Scale sin respaldo de captura cruda**. Ver [[2026-1104-workos-vuelve-la-seccion-de-soporte-pero-sin-precios]].

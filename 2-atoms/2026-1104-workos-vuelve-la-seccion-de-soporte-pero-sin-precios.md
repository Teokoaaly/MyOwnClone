---
id: 2026-1104-workos-vuelve-la-seccion-de-soporte-pero-sin-precios
type: atom
certainty: solid
sources: [sources/2026-11-04-workos-pricing.md]
links: ["[[2026-1103-workos-captura-cruda-no-trae-tabla-de-soporte]]", "[[2026-1101-workos-plan-scale-de-soporte-1000-al-mes]]", "[[2026-1102-workos-el-plan-scale-perdio-revision-trimestral-y-configuracion]]", "[[2026-1104-workos-precios-estables-en-cinco-capturas]]"]
---

## Claim
La captura del **2026-11-04** de workos.com/pricing **vuelve a renderizar la sección de soporte** — ausente por completo en el volcado del 11-03 (ver [[2026-1103-workos-captura-cruda-no-trae-tabla-de-soporte]]) — pero **no como la tabla de tres columnas** de las capturas condensadas del 11-01 y 11-02, sino como **tres listas de niveles** bajo el encabezado "## Support SLAs": **"Included for all accounts"** (Email support, In-dashboard web support, API status notifications, Docs and example apps), **"Scale plan"** (Video calls, Private Slack channel, Technical onboarding guidance, Guaranteed response SLAs) y **"Enterprise plan"** (Dedicated support account manager, Quarterly architecture review, End-user configuration support, 24 x 7 x 365 response SLAs). El bloque **no publica ningún precio** (ni los $1.000/mes del plan Scale), **no da tiempos de respuesta P1/P2** y **no incluye la nota de horario hábil**; añade un enlace "View support plans" a `workos.com/support-plans`. Esta forma por niveles es **idéntica** a la del volcado crudo del 10-31.

## Why It Matters
Es un **delta de render de manual de lectura**, no de contenido: la página tiene una forma "escala de niveles sin precios" (10-31 y 11-04) y una forma "tabla de precios" (solo en las capturas condensadas del 11-01 y 11-02), y el 11-03 no trae ninguna de las dos. La consecuencia práctica para el vault es directa y ya fue anticipada por [[2026-1101-workos-plan-scale-de-soporte-1000-al-mes]]: **el plan Scale de $1.000/mes es un precio sin ninguna captura cruda que lo respalde** — el 11-04 vuelve a mostrar la estructura de niveles y **vuelve a omitir el precio**. El vault puede citar los $1.000/mes solo como dato de captura condensada, no como precio verificado en la página.

La parte útil de la captura es que la escala de niveles sí permite contrastar la fricción abierta en [[2026-1102-workos-el-plan-scale-perdio-revision-trimestral-y-configuracion]]: la composición exacta del plan Scale está documentada en [[2026-1104-workos-el-render-de-soporte-confirma-que-scale-no-incluye-revision-trimestral]]. Y en conjunto, las dos formas de la página sugieren que `workos.com/support-plans` es la ubicación donde vive el detalle comercial de soporte, coherente con que la página de precios derive a "Schedule a call" en cada calculadora ([[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]]).

## [FRICTION]
> [[2026-1103-workos-captura-cruda-no-trae-tabla-de-soporte]] afirma que la captura del 2026-11-03 "**no incluye la tabla 'Support Plans'**" y que por tanto "no puede usarse ni para confirmar ni para refutar la tabla de soporte".
> Este átomo presiona esa creencia en un punto verificable: el 11-03 no traía la sección **en absoluto**, pero el 11-04 **sí** la trae, con otro formato (niveles en lista, sin precios) y con un enlace a una página de soporte aparte. Es decir, la secuencia de capturas de la misma URL alterna entre "sección presente como escala de niveles" (10-31, 11-04), "sección presente como tabla de precios" (11-01, 11-02, condensadas) y "sección ausente" (11-03), lo que apunta a un problema de render/extractor más que a un cambio deliberado de la oferta.
> Marcado para juicio humano, no auto-resuelto: la hipótesis más parsimoniosa es que el extractor del 11-03 recortó la página, y que la tabla de precios del 11-01/11-02 fue una condensación manual de la lista de niveles — en cuyo caso el precio de $1.000/mes y los P1/P2 no provienen de la página, sino de esa condensación.

## Nota de verificación
sources/2026-11-04-workos-pricing.md, líneas 462-499: "## Support SLAs", "### Included for all accounts" (466-474), "### Scale plan" (477-486), "### Enterprise plan" (488-496), "View support plans" (499). Ausencia de "$1.000", "P1", "P2" y "Pacific Time" en todo el fichero: verificado por búsqueda de "1,000|1000/mo" en la fuente, cero coincidencias. Comparación con sources/2026-10-31-workos-pricing.md líneas 349-374: listas de niveles idénticas.

---
id: 2026-1104-workos-precios-estables-en-cinco-capturas
type: atom
certainty: solid
sources: [sources/2026-11-04-workos-pricing.md]
links: ["[[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]]", "[[2026-1031-workos-pricing]]", "[[2026-1031-workos-sso-escalera-de-conexiones-125-100-80-65]]", "[[2026-1031-workos-audit-logs-125-por-siem-y-99-por-millon-de-eventos]]"]
---

## Claim
Los **precios de producto publicados** de WorkOS son **idénticos en las cinco capturas** del 10-31, 11-01, 11-02, 11-03 y 11-04: AuthKit **1M de MAU gratis + $2,500/mes por cada millón adicional**; SSO y Directory Sync **$125/ea (1–15), $100/ea (16–30, 20% off), $80/ea (31–50, 36% off), $65/ea (51–100, 48% off)** y "Need additional scale? Talk to us" por encima de 100; Audit Logs **$125/mes por conexión SIEM** y **$99/mes por millón de eventos almacenados**; Radar **primeros 1.000 checks gratis + $100/mes por cada 50k checks**; Custom Domain **$99/mes**. El precio del plan **Annual Credits sigue sin publicarse** (custom) y el precio del **plan de soporte Scale ($1.000/mes)** solo aparece en las capturas condensadas del 11-01 y 11-02, **no** en los volcados crudos del 10-31, 11-03 ni 11-04.

## Why It Matters
Es el átomo de estabilidad de la quinta captura y fija la línea base del modelo de identidad del vault: **ningún precio de producto WorkOS ha cambiado en cinco días de recaptura**, así que la única incertidumbre real del modelo no es el precio sino **qué página lo renderiza** y **qué secciones sobreviven al extractor** — exactamente el problema metodológico que documentan [[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]] y la propia forma de este átomo.

La segunda parte es la que más pesa para el modelo de costes: **$1.000/mes del plan Scale no está en ninguna fuente cruda del vault**. Las dos únicas apariciones del importe son la tabla condensada del 11-01 y la del 11-02 (idénticas salvo dos celdas), ambas de la misma transcripción. Es decir, el vault tiene **un precio de soporte sin respaldo de captura cruda**, lo que obliga a citarlo como "precio reportado en captura condensada" y no como precio verificado en la página — y refuerza la conclusión operativa de [[2026-1031-workos-pricing]]: la partida de identidad de WorkOS es determinista y barata en producto ($0 hasta 1M de MAU, $0 hasta 15 conexiones SSO), y cara solo en el garnish enterprise.

## [FRICTION]
> [[2026-1103-workos-vs-100-para-construir-sso-o-scim-uno-mismo]] afirma que el literal **"vs $100 to build it yourself"** aparece en el pie de **ambos** calculadores (SSO y Directory Sync), y lo apoya solo en la captura del 2026-11-03.
> Este átomo presiona esa creencia en un punto de respaldo, no de precio: la captura cruda del **2026-10-31** solo contenía ese literal **una vez**, en el bloque de **Directory Sync** (línea 195), y **no** en el de SSO. Los precios de la escalera no cambian, pero el **ancla de venta se añadió al bloque de SSO en algún momento entre el 10-31 y el 11-03**.
> Ambas no pueden ser completamente correctas solo si se leen como "el ancla siempre estuvo en ambos bloques": en el 10-31 no estaba en SSO. Marcado para juicio humano, no auto-resuelto. La lectura operativa de [[2026-1103-workos-vs-100-para-construir-sso-o-scim-uno-mismo]] (la primera conexión a $125 supera el ancla de $100) **no se ve afectada**: sigue siendo cierto en ambos bloques.

## Nota de verificación
Comparación literal de sources/2026-10-31-workos-pricing.md (468 líneas), sources/2026-11-01-workos-pricing.md y sources/2026-11-02-workos-pricing.md (98 líneas, tablas), sources/2026-11-03-workos-pricing.md (303 líneas) y sources/2026-11-04-workos-pricing.md (613 líneas). Búsqueda de "1,000|1000/mo" en la fuente del 11-04: cero coincidencias; la única aparición de "1000" es "First 1,000 checks" (Radar). Búsqueda de "vs $100" en el 11-04: coincidencias en líneas 150 (SSO) y 253 (Directory Sync); en el 10-31, solo línea 195 (Directory Sync).

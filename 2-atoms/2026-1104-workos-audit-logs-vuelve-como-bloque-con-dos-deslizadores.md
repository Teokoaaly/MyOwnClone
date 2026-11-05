---
id: 2026-1104-workos-audit-logs-vuelve-como-bloque-con-dos-deslizadores
type: atom
certainty: solid
sources: [sources/2026-11-04-workos-pricing.md]
links: ["[[2026-1031-workos-audit-logs-125-por-siem-y-99-por-millon-de-eventos]]", "[[2026-1103-workos-captura-cruda-no-trae-tabla-de-soporte]]", "[[2026-1104-workos-precios-estables-en-cinco-capturas]]"]
---

## Claim
El volcado crudo del **2026-11-04** de workos.com/pricing vuelve a renderizar **Audit Logs como bloque propio con encabezado**, cosa que el volcado del 11-03 no hacía: aparecen el encabezado "### Audit Logs", el descriptor **"Capture and export compliance events from your app"** y **dos deslizadores independientes** — "SIEM connections" con escala **0 / 10 / 20 / 30 / 40 / 50+** y "events retained" con escala **0 / 10M / 20M / 30M / 40M / 50M+** — antes de las dos filas de precio "Log streaming — Per SIEM connection — $125 / mo" y "Event Retention — Per million events stored — $99 / mo".

## Why It Matters
Corrige la observación estructural que la captura del 11-03 dejó escrita en [[2026-1031-workos-audit-logs-125-por-siem-y-99-por-millon-de-eventos]]: allí se afirmaba que el streaming y la retención "aparecen **bajo el calculador, no bajo un encabezado 'Audit Logs'**, junto a Custom Domain", es decir, como partidas sueltas. El 11-04 demuestra que la página **sí** presenta Audit Logs como un módulo con encabezado propio y, además, con **dos variables de escala separadas** (destinos SIEM y eventos retenidos) en lugar de una sola línea plana.

Para el modelo de costes del vault esto es operativo: son **dos medidores independientes que hay que cotizar por separado** — $125/mes por destino SIEM y $99/mes por millón de eventos almacenados — y ambos tienen tope público en la calculadora (**50+ conexiones SIEM** y **50M+ eventos retenidos**), más allá del cual la página deriva a "Talk to us". La segunda variable es **consumo acumulativo**: los eventos retenidos se cobran por almacenamiento, no por uso de la auditoría, así que un tenant corporativo muy activo genera coste variable no controlable desde el lado del producto.

## [FRICTION]
> [[2026-1031-workos-audit-logs-125-por-siem-y-99-por-millon-de-eventos]] afirma, en su nota de re-verificación del 11-03, que "en el volcado crudo estas dos líneas aparecen **bajo el calculador ('Estimate your costs'), no bajo un encabezado 'Audit Logs'**", y lo interpretó como que la página presenta streaming y retención "como partidas de coste independientes del paquete de identidad, no como un módulo de 'Audit Logs' con precio propio".
> Este átomo presiona esa lectura estructural porque la captura del **2026-11-04** renderiza literalmente el encabezado **"### Audit Logs"** con su descriptor "Capture and export compliance events from your app", con lo que la página **sí** estructura esas dos líneas como un módulo con precio propio.
> Ambas no pueden ser simultáneamente correctas: o el render del 11-03 se saltó el encabezado (y entonces la inferencia "no es un módulo" era un artefacto del extractor, no de la página), o la página cambió de estructura entre el 11-03 y el 11-04. Marcado para juicio humano, no auto-resuelto. **Los dos importes ($125 y $99) no cambian en ningún caso.**

## Nota de verificación
sources/2026-11-04-workos-pricing.md, líneas 310-374: encabezado "### Audit Logs" (310), descriptor (314), escalas "SIEM connections 0 10 20 30 40 50+" (318-330) y "events retained 0 10M 20M 30M 40M 50M+" (332-344), y las filas "Log streaming — Per SIEM connection — $125 / mo" (354-362) y "Event Retention — Per million events stored — $99 / mo" (365-373). La comparación con el render del 11-03 es lectura literal de sources/2026-11-03-workos-pricing.md, líneas 139-153.

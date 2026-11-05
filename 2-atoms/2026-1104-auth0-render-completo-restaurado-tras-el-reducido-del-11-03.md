---
id: 2026-1104-auth0-render-completo-restaurado-tras-el-reducido-del-11-03
type: atom
certainty: solid
sources: [sources/2026-11-04-auth0-pricing.md]
links: ["[[2026-1103-auth0-captura-reducida-sin-tablas-ni-feature-matrix]]", "[[2026-1104-backblaze-b2-render-completo-restaurado-resuelve-la-friccion-del-11-03]]", "[[2026-1102-auth0-precios-sin-cambios-en-48-horas]]", "[[2026-1103-auth0-precios-35-y-240-bajo-el-encabezado-b2b-billing]]"]
---

## Claim
La captura de `auth0.com/pricing` del **2026-11-04 (4.068 palabras, 596 líneas)** vuelve a ser un **render completo**: devuelve las tablas de precios por MAU (B2C y B2B, mensual y anual), las tablas de add-ons (AI Agents, M2M tokens), el feature matrix B2C y B2B completo y la sección "How to Use This Document" con la fórmula de cotización "Total = Base Price + sum of all applicable add-on prices". El contenido es **byte a byte idéntico al de las capturas del 2026-11-01 y del 2026-11-02**: el `diff` entre los tres archivos solo arroja la línea `captured:` del frontmatter.

## Why It Matters
Confirma que la captura reducida del 2026-11-03 fue un **artefacto del extractor**, no una versión reducida de la página: dos días después la página vuelve a renderizarse completa y sin una sola diferencia de contenido. Es el mismo patrón que ya se había registrado en Backblaze el mismo día ([[2026-1104-backblaze-b2-render-completo-restaurado-resuelve-la-friccion-del-11-03]]) y el mismo mecanismo que dejó al vault sin tabla de precios el 11-03 ([[2026-1103-auth0-captura-reducida-sin-tablas-ni-feature-matrix]]). Dos consecuencias operativas: (a) las cifras que el 11-03 dejó "sin re-verificar" (escalones de MAU, precios de add-on, límites del feature matrix) **quedan re-verificadas** por esta captura, porque el material es idéntico al de las capturas completas del 11-01 y 11-02; (b) la página se renderiza por JS con toggles y el extractor captura el estado por defecto de esos toggles, de modo que una misma URL entrega documentos de 4.068 o de 829 palabras según el día. Regla operativa reinforced: **una captura reducida no es evidencia de nada** — ni de estabilidad, ni de cambio, ni de retirada.

## [FRICTION]
> [[2026-1103-auth0-precios-35-y-240-bajo-el-encabezado-b2b-billing]] (escrita el 2026-11-03, `certainty: tentative`) afirmaba que la captura del 11-03 mostraba los importes Essentials $35 y Professional $240 **bajo un encabezado literal "B2B BILLING"**, y lo dejaba como fricción abierta con dos hipótesis sin resolver: (a) el extractor no distingue columnas B2C/B2B y el encabezado es un etiqueta pegada al contenido B2C, o (b) Auth0 cambió la cifra de entrada de B2B.
> Esta captura **no puede seguir sosteniendo la lectura literal** de ese átomo: en el render completo los importes $35/$240 están **explícitamente etiquetados como B2C** en la tabla "Plans Overview" y en las tablas "B2C Base Price by MAUs", mientras que los de B2B ($150/$800) están en sus propias tablas, con el mismo formato de documento. La hipótesis (a) queda confirmada y la (b) desmentida por el material.
> Ambas no pueden ser completamente correctas solo si se mantiene la lectura literal del 11-03; el átomo viejo conserva su `tentative` porque su texto sigue describiendo correctamente lo que la captura del 11-03 renderizaba, y su `## Claim` no se reescribe (ver [[2026-1104-auth0-el-render-completo-confirma-que-35-y-240-son-b2c-y-150-800-son-b2b]]). Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
La identidad byte a byte se verificó con `diff` entre `sources/2026-11-01-auth0-pricing.md`, `sources/2026-11-02-auth0-pricing.md` y `sources/2026-11-04-auth0-pricing.md`: la única diferencia es `captured: 2026-11-0X`. El recuento de 4.068 palabras y 596 líneas procede del frontmatter y del recuento directo del archivo. La sección "How to Use This Document" y su fórmula de total son lectura literal de las líneas 15-25 de la fuente.

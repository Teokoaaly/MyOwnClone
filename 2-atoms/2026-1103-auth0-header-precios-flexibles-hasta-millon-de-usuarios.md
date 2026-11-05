---
id: 2026-1103-auth0-header-precios-flexibles-hasta-millon-de-usuarios
type: atom
certainty: solid
sources: [sources/2026-11-03-auth0-pricing.md]
links: ["[[2026-1101-auth0-precios-por-mau-no-por-evento]]", "[[2026-1101-auth0-definicion-de-mau-y-cobro-al-escalon-superior]]", "[[2026-1101-auth0-addon-agentes-ai-suma-50-por-ciento]]", "[[2026-1103-auth0-workflows-agentes-ai-incluidos-en-plan-free]]"]
---

## Claim
El encabezado de la página de precios de Auth0 es "**Flexible pricing for all your apps and AI agents from user 1 to 1,000,000+**", y la página abre con dos llamadas a la acción ("Start building for free" y "Talk to our Sales team"). La promesa comercial es una única plataforma que cubre desde el usuario 1 hasta más de 1.000.000, y que sirve a la vez a "apps" y a "agentes de IA".

## Why It Matters
Es el marco de lectura de todo lo demás de la página: el rango "1 → 1.000.000+" presenta Auth0 como plataforma de identidad universal, mientras que el plan Free corta en 25.000 MAU y a partir de 30.000 MAU el precio ya no está publicado. Para el vault la lectura correcta es que el encabezado es una **afirmación de alcance comercial**, no una garantía de coste: el único tramo del rango que el presupuesto de ≤ €4/mes puede habitar es el Free (ver [[2026-1101-auth0-plan-free-25000-mau-sin-tarjeta]]). Que "AI agents" venga en el mismo encabezado que "apps" es relevante porque los agentes son el vector de coste que más crece en el vault y en Auth0 se factura como add-on del +50 % ([[2026-1101-auth0-addon-agentes-ai-suma-50-por-ciento]]), aunque el propio Free ya lista workflows agénticos ([[2026-1103-auth0-workflows-agentes-ai-incluidos-en-plan-free]]). El mismo encabezado introduce la palabra "Flexible", que hay que contrastar con el modelo real de cobro.

## [FRICTION]
> [[2026-1101-auth0-definicion-de-mau-y-cobro-al-escalon-superior]] (escrita el 2026-11-01) establece que Auth0 cobra **por escalón superior**: "Pricing is available only at the listed MAU tiers. If your usage falls between tiers, you are billed at the next tier up."
> Este átomo presiona eso porque el encabezado de la misma página vende "Flexible pricing" — una palabra que sugiere precio continuo o negociable, no una función escalonaria con saltos discretos al pasar cada umbral de MAU.
> Ambas no pueden ser completamente correctas: o "flexible" es solo lenguaje de marketing sin contenido tarifario, o existe una negotiated/pricing continuum que la captura del 2026-11-03 (que no incluye la tabla de precios por MAU) no muestra. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
El texto del encabezado y los dos CTAs son lectura literal de las líneas 9-13 de `sources/2026-11-03-auth0-pricing.md`. La crítica al uso de "Flexible" es lectura de este átomo.

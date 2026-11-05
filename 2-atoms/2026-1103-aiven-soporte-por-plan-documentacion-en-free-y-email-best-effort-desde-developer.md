---
id: 2026-1103-aiven-soporte-por-plan-documentacion-en-free-y-email-best-effort-desde-developer
type: atom
certainty: solid
sources: [sources/2026-11-03-aiven-pricing.md]
links: ["[[2026-1101-aiven-soporte-base-incluido-y-tiers-de-soporte-como-add-on]]", "[[2026-1102-aiven-escalera-de-precios-postgresql-de-0-a-270-dolares]]", "[[2026-1102-aiven-guia-de-plan-por-entorno-de-trabajo]]"]
---

## Claim
La fila "Support" de la tabla de planes de Aiven PostgreSQL **sí diferencia entre planes**: el plan **Free solo ofrece "Support via documentation"**, mientras que **Developer, Hobbyist, Startup, Business y Premium ofrecen "Support through email with best-effort responses during the same or next business day"**. La fila añade además que el plan ofrece **tres tiers de soporte adicionales con cargo aparte**, que incluyen tiempos de respuesta más rápidos y soporte telefónico.

## Why It Matters
Convierte "soporte incluido" en una escala medible por plan, que es el detalle que faltaba en [[2026-1101-aiven-soporte-base-incluido-y-tiers-de-soporte-como-add-on]] (que solo registraba que existe un tier base sin coste y dos tiers de pago). El dato operativo para el vault: **el plan Free ($0) no tiene canal humano**, así que cualquier duda de un tenant que usa el free tier se resuelve solo con documentación — mientras que a partir de Developer ($5/mes, según [[2026-1102-aiven-escalera-de-precios-postgresql-de-0-a-270-dolares]]) ya hay correo con respuesta best-effort en el mismo o siguiente día laborable. Combinado con la guía oficial ([[2026-1102-aiven-guia-de-plan-por-entorno-de-trabajo]]), el plan Developer es exactamente el escalón de "desarrollo affordable, no productivo" con un canal de soporte que no llega a ser producción: el soporte con tiempos garantizados y teléfono es el add-on de pago, no la base.

## [FRICTION]
> [[2026-1102-aiven-funciones-operativas-estandar-en-todos-los-planes]] afirma que las funciones de la tabla están incluidas en "los seis planes" y que "las dos únicas exclusiones o condicionamientos de la tabla son PITR y dynamic disk sizing". Esta nota presiona esa afirmación porque la propia tabla distingue el soporte de Free (solo documentación) del de los otros cinco planes (correo con respuesta best-effort), y añade tres tiers de soporte de pago como partida separada. Ambas no pueden ser completamente correctas: o "incluido en los seis planes" describe solo las filas marcadas sin matiz y el soporte es en realidad gradado, o el soporte de pago es una excepción no registrada. Marcado para juicio humano, no auto-resuelto.

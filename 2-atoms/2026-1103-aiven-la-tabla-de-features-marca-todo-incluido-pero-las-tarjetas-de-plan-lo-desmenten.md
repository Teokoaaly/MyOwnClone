---
id: 2026-1103-aiven-la-tabla-de-features-marca-todo-incluido-pero-las-tarjetas-de-plan-lo-desmenten
type: atom
certainty: solid
sources: [sources/2026-11-03-aiven-pricing.md]
links: ["[[2026-1102-aiven-funciones-operativas-estandar-en-todos-los-planes]]", "[[2026-1101-aiven-postgresql-plan-gratuito-1gb-sin-region]]", "[[2026-1102-aiven-sla-99-99-solo-desde-el-plan-startup]]"]
---

## Claim
La página de precios de Aiven **se contradice a sí misma entre la tarjeta de plan y la tabla de features**. En la tabla, las filas "Connection pooling", "Read-only access to DB replica nodes", "Multiple logical databases per instance", "Database forks", "VPC peering in AWS, GCP, and Microsoft Azure", "Seamless upgrade/downgrade to other plans" y "One-click version upgrade" aparecen marcadas en **las seis columnas**; pero las tarjetas de los planes **Free y Developer dicen literalmente "No integrations or connection pooling"**. Además, la tarjeta de Business es "Everything in Startup, plus high availability" y la de Premium "Everything in Business, plus a second standby node", mientras la FAQ afirma que "there are no separate line items for high availability, or routine maintenance" — es decir, la HA no es una partida separada, pero sí es un **escalón de plan** desde Business ($180/mes).

## Why It Matters
Obliga a no leer la tabla de features como un contrato de paridad: **las filas marcadas vacías no equivalen a "incluido en todos los planes"**, porque al menos connection pooling está desmentido explícitamente en la tarjeta de dos de los seis planes. Para el vault esto importa en el modelo multi-tenant: si una capa de aplicación necesita connection pooling (pgbouncer), los planes Free y Developer quedan descartados y el salto real es a Hobbyist ($12/mes), tal como ya anticipaba [[2026-1101-aiven-postgresql-plan-gratuito-1gb-sin-region]] al registrar que Free y Developer no incluyen integraciones ni pooling. Y la frase de la FAQ debe leerse con cuidado: "no separate line items" significa que la HA **no se factura como extra**, no que esté en todos los planes — el escalón sigue siendo el mismo de [[2026-1102-aiven-sla-99-99-solo-desde-el-plan-startup]].

## [FRICTION]
> [[2026-1102-aiven-funciones-operativas-estandar-en-todos-los-planes]] afirma que "connection pooling" está incluida en "**los seis planes**, del Free al Premium" y que "las dos únicas exclusiones o condicionamientos de la tabla son PITR y dynamic disk sizing". La captura del 2026-11-03 muestra que la tarjeta de los planes Free y Developer dice "No integrations or connection pooling", de modo que la afirmación no puede sostenerse para esos dos planes. Ambas no pueden ser completamente correctas: o la tabla marca availability y la tarjeta matiza, o el átomo viejo leyó las celdas vacías como un "sí" universal. Marcado para juicio humano, no auto-resuelto.

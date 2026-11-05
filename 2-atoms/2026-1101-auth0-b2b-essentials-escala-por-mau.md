---
id: 2026-1101-auth0-b2b-essentials-escala-por-mau
type: atom
certainty: solid
sources: [sources/2026-11-01-auth0-pricing.md]
links: ["[[2026-1101-auth0-b2c-essentials-escala-por-mau]]", "[[2026-1101-auth0-precios-por-mau-no-por-evento]]", "[[2026-1022-arquitectura-rac-tres-modos-por-clon]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
Auth0 Essentials **B2B** cuesta **$150/mes en 500 MAU** (vs $35 en B2C) y escala a $300 (1.000), $700 (2.500), $1.300 (5.000), $1.725 (7.500), $2.100 (10.000), $3.800 (20.000) y "Contact us" a partir de 30.000 MAU. Professional B2B parte de **$800/mes** en 500 MAU, $1.200 en 2.500, $1.500 en 5.000, $1.800 en 7.500, $2.400 en 10.000, y ya es "Contact us" en 20.000 MAU.

## Why It Matters
La prima B2B es brutal y es la que más afecta a un SaaS B2B multi-tenant como MyOwnClone: **$150/mes en el plan de entrada B2B contra $35 en B2C**, y en Professional **$800 contra $240**. Puesto en euros al cambio aproximado, el plan B2B de entrada (~€137/mes) es más de 30 veces el presupuesto de infra de ≤ €4/mes del vault, y **el Professional B2B de $800/mes es el doble de los $400/mes que costaría el propio producto a 99/mes de precio base** ([[2026-1022-precio-99-mensual]]). La razón estructural está en la tabla de features: el B2B Essentials trae **Organizations ilimitadas** y **3 conexiones SSO Enterprise**, que son exactamente lo que necesita el modelo multi-tenant documentado en [[2026-1022-arquitectura-rac-tres-modos-por-clon]], donde cada tenant es una organización. La conclusión operativa: para MyOwnClone, B2B en Auth0 no es una opción de coste, es una opción de **compliance/enterprise** — y si el producto necesita SSO/SCIM para clientes corporativos, el precio por organización es la variable a cotizar, no el precio por MAU.

## Nota de verificación
Cifras leídas literalmente de las tablas "B2B Base Price by MAUs". La conversión a euros y la comparación con el precio base del producto son cálculos/lecturas de este átomo, no frases de la fuente.

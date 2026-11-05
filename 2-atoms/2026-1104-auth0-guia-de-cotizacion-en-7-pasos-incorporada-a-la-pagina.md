---
id: 2026-1104-auth0-guia-de-cotizacion-en-7-pasos-incorporada-a-la-pagina
type: atom
certainty: solid
sources: [sources/2026-11-04-auth0-pricing.md]
links: ["[[2026-1104-auth0-render-completo-restaurado-tras-el-reducido-del-11-03]]", "[[2026-1101-auth0-precios-por-mau-no-por-evento]]", "[[2026-1104-auth0-enterprise-mfa-incluido-en-b2c-essentials-pero-addon-en-b2b]]", "[[2026-1101-auth0-definicion-de-mau-y-cobro-al-escalon-superior]]"]
---

## Claim
El render completo de auth0.com/pricing no es solo un catálogo de precios: incluye una sección "**How to Use This Document**" con un **procedimiento de cotización en 7 pasos** y una fórmula explícita de coste total. Los pasos son: (1) determinar el caso de uso (B2C / B2B), (2) identificar el escalón de MAU — "If usage falls between tiers, use the next tier up", (3) elegir el plan mínimo comparando contra las tablas de features, (4) buscar el precio base en la tabla B2C o B2B (mensual o anual), (5) sumar los add-ons que apliquen (AI Agents, M2M tokens adicionales, Enterprise SSO connections, Enterprise MFA), (6) calcular **"Total = Base Price + sum of all applicable add-on prices"**, y (7) si cualquier componente dice "Contact us", derivar a ventas. La página incluye además una sección "Key Definitions" que define MAU, Organizations y Enterprise Connections.

## Why It Matters
El proveedor publica su **propio manual de cotización**, lo que convierte la página en un documento operable y no solo en marketing: cualquiera con el render puede replicar el cálculo que haría el equipo de ventas de Auth0. Para el vault esto es material porque convierte la pregunta "¿cuánto cuesta Auth0?" en una **función determinista y auditable** (plan × escalón de MAU + add-ons), lo que encaja con la lógica del propio hilo de economía de la verificación: el precio se puede recalcular y comprobar contra una segunda captura sin depender de un comercial. Y fija una regla operativa que el vault ya intuye con los datos sueltos: **"Contact us" no es una casilla, es una frontera** — en cuanto un solo componente (plan o add-on) cae en "Contact us", el total deja de ser verificable desde la página. También deja claro que la fórmula de Auth0 **no incluye los escalones del Enterprise** ni ningún recargo por volumen oculto: el total es la suma literal de base + add-ons, lo que hace auditable cualquier cotización, incluida la de reventa de cuentas.
Advertencia de lectura: esta sección es la que el render reducido del 11-03 no trajo, y la que la captura del 11-04 restaura ([[2026-1104-auth0-render-completo-restaurado-tras-el-reducido-del-11-03]]).

## Nota de verificación
Sección "How to Use This Document" y sección "Key Definitions" (líneas 15-33) de `sources/2026-11-04-auth0-pricing.md`, lectura literal. La lectura sobre la frontera "Contact us" es interpretación de este átomo sobre los datos de la fuente.

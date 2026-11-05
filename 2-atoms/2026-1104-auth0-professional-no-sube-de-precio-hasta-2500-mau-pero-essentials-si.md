---
id: 2026-1104-auth0-professional-no-sube-de-precio-hasta-2500-mau-pero-essentials-si
type: atom
certainty: solid
sources: [sources/2026-11-04-auth0-pricing.md]
links: ["[[2026-1101-auth0-b2c-essentials-escala-por-mau]]", "[[2026-1101-auth0-b2b-essentials-escala-por-mau]]", "[[2026-1101-auth0-precios-por-mau-no-por-evento]]", "[[2026-1104-auth0-render-completo-restaurado-tras-el-reducido-del-11-03]]"]
---

## Claim
La escalera de Auth0 **no es uniforme entre planes**: en el primer tramo (500 → 1.000 MAU) el plan **Essentials duplica su precio** mientras que **Professional lo mantiene plano**. B2C: Essentials $35 (500 MAU) → $70 (1.000 MAU), mientras que Professional $240 (500 MAU) → $240 (1.000 MAU). B2B: Essentials $150 → $300, Professional $800 → $800. A partir de 2.500 MAU ambos planes vuelven a escalar (B2C Professional $545, B2B Professional $1.200) y, en cada escalón superior, **la diferencia de precio entre Essentials y Professional se estrecha**: en B2C 500 MAU es $35 vs $240 (×6,9) y en 20.000 MAU es $1.400 vs $3.200 (×2,3); en B2B 500 MAU es $150 vs $800 (×5,3) y en 10.000 MAU es $2.100 vs $2.400 (×1,14).

## Why It Matters
Es una propiedad estructural del modelo de coste que cambia el cálculo del vault y que no se veía con los datos sueltos de las capturas anteriores. Primero: **Professional tiene 1.000 MAU "de cortesía"** — un producto que crece de 500 a 1.000 usuarios mensuales paga lo mismo, mientras que en Essentials ese mismo crecimiento duplica la factura. Segundo, y más relevante para un SaaS multi-tenant como MyOwnClone ([[2026-1022-arquitectura-rac-tres-modos-por-clon]]): **la prima de Professional es una prima de entrada, no un recargo por escala**. Pagar $240 en vez de $35 buys seguridad y límites, no un coste por MAU más barato; de hecho, a partir de 10.000 MAU en B2B, Professional ($2.400) está **más cerca** de Essentials ($2.100) que del propio punto de partida de la prima. Eso significa que la decisión "Free o de pago" (plan mínimo por features, paso 3 de la guía de cotización de la página) no se puede hacer solo por precio base: hay que mirar **dónde se cruzan las dos escaleras**, y ese cruce está en un punto mucho más alto de lo que sugiere el precio de entrada. Tercera lectura: la propia página define la MAU como usuario no interno que se autentica en el mes **por tenant** ([[2026-1101-auth0-definicion-de-mau-y-cobro-al-escalon-superior]]), así que este "primer tramo gratis" del plan Professional es por tenant: en un producto con 10 tenants de 100 MAU cada uno, cada tenant paga su propio escalón, y la suma **no** es el precio de la tabla de 1.000 MAU sino 10 × el precio de 500 MAU.

## Nota de verificación
Cifras leídas literalmente de las tablas "B2C Base Price by MAUs (monthly)" (líneas 105-116) y "B2B Base Price by MAUs (monthly)" (líneas 257-266) de `sources/2026-11-04-auth0-pricing.md`. Los ratios (×6,9, ×2,3, ×5,3, ×1,14) y la lectura del cruce de escaleras y del efecto por tenant son cálculos e interpretación de este átomo, no frases de la fuente.

## Techo de la escalera (nota lateral)
El mismo render revela dónde **deja de existir** el plan: en la tabla B2C, Professional pasa a "Contact us" en 30.000 MAU y a "**Not available**" en 40.000 y 50.000 MAU, mientras que Essentials conserva precio publicado hasta 50.000 MAU ($2.800 y $3.500/mes). La tabla B2B no publica ningún precio por encima de 20.000 MAU: su última fila es "30,000+ | Contact us | Contact us". El detalle de este átomo: el "primer tramo gratis" de Professional (500 → 1.000 MAU) existe solo en el tramo bajo; **no hay ninguna gestión de descuento por volumen más allá de 10.000 MAU en B2B, y a partir de 20.000 la única vía es Enterprise** (ver [[2026-1101-auth0-enterprise-contact-us-sla-y-30-dias-de-logs]]).

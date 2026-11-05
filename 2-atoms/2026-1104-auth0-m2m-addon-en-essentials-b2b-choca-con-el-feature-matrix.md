---
id: 2026-1104-auth0-m2m-addon-en-essentials-b2b-choca-con-el-feature-matrix
type: atom
certainty: solid
sources: [sources/2026-11-04-auth0-pricing.md]
links: ["[[2026-1101-auth0-m2m-tokens-5k-incluidos-en-professional]]", "[[2026-1104-auth0-enterprise-mfa-incluido-en-b2c-essentials-pero-addon-en-b2b]]", "[[2026-1104-auth0-render-completo-restaurado-tras-el-reducido-del-11-03]]", "[[2026-1101-auth0-b2b-essentials-escala-por-mau]]"]
---

## Claim
La página de precios de Auth0 se contradice a sí misma sobre el add-on de tokens M2M. La **sección de add-ons B2B** se titula "**M2M Tokens — Essentials and Professional plan** (Professional plan 5,000 included)" y publica una tabla de 19 escalones que **empieza en 2.500 tokens = $10/mes** y llega a 300.000 = $1.200/mes — sin fila "Included" en ningún punto, de modo que **5.000 tokens figuran a $20/mes** en B2B. Pero el **feature matrix** dice, en la fila "M2M Add-on": "**No | No | Yes | Yes**" (Free / Essentials / Professional / Enterprise), tanto en la matriz B2C (línea 390) como en la B2B (línea 494). Y la tabla B2C, en cambio, sí incluye la fila "5,000 | **Included**" y se titula "**Professional plan only**".

## Why It Matters
Tres incompatibilidades en el mismo documento, y todas afectan a la partida que el vault ya identificó como variable independiente del MAU ([[2026-1101-auth0-m2m-tokens-5k-incluidos-en-professional]]). (1) El add-on M2M se anuncia para Essentials B2B pero el feature matrix lo niega en Essentials. (2) En B2B los 5.000 tokens "incluidos" en Professional **se cobran a $20/mes** en la tabla, lo que contradice el propio "(Professional plan 5,000 included)" del encabezado. (3) La simetría B2C/B2B del feature matrix ("No" en Essentials en ambas) no cuadra con la tabla B2C, que es "Professional plan only". La consecuencia práctica es que **cualquier cálculo de coste de M2M para un producto en Essentials B2B es hoy no fiable**: hay que saber si a un cliente B2B en Essentials se le pueden comprar tokens M2M y si los 5.000 tokens de Professional están o no incluidos. Esto es exactamente el tipo de ambigüedad que hay que cerrar **antes** de cotizar, no después — y es el mismo patrón que el vault ya registró con la nota al pie "Upgrade to B2B to continue using EC, Self-Service SSO, and SCIM" ([[2026-1101-auth0-sso-scim-en-free-pero-no-en-essentials-b2c]]): la página promete por un lado y restringe por otro.

## [FRICTION]
> [[2026-1101-auth0-m2m-tokens-5k-incluidos-en-professional]] (escrita el 2026-11-01) afirma en su Claim que "**Free y Essentials incluyen 1.000 tokens M2M, Professional incluye 5.000**, y el add-on empieza en $30/mes por 7.500 tokens […] (en B2B el add-on arranca en $10 por 2.500 tokens)".
> Este átomo presiona esa creencia en un punto: la tabla B2B **no tiene fila "Included"**. Los 5.000 tokens que el Claim da por incluidos en Professional figuran a **$20/mes** en la escala B2B, mientras que la tabla B2C sí los marca "Included". Además, el Claim dice "el add-on empieza en $30/mes por 7.500 tokens" sin desdoblar que **en B2B el primer escalón pagable es 2.500 tokens = $10/mes**, que es una compra por debajo del included de 5.000 y por tanto solo tiene sentido si el contador del add-on es acumulable.
> Ambas no pueden ser completamente correctas: o la escala B2B omite por error la fila "Included", o los 5.000 tokens de Professional **no** están incluidos y se pagan. Marcado para juicio humano, no auto-resuelto: el átomo viejo conserva su `Claim` sin reescribir, y su cifra de partida ($30/7.500 → $1.200/300.000, ratio $0,004/token) sigue siendo correcta.

## Nota de verificación
Títulos y filas son lectura literal de `sources/2026-11-04-auth0-pricing.md`: línea 171 (título B2C), línea 177 ("5,000 | Included"), línea 314 (título B2B), línea 320 ("2,500 | $10"), línea 322 ("5,000 | $20"), línea 390 (fila B2C "M2M Add-on") y línea 494 (fila B2B "M2M Add-on"). La captura del 11-04 es byte a byte idéntica a la del 11-01 ([[2026-1104-auth0-render-completo-restaurado-tras-el-reducido-del-11-03]]), así que la contradicción es de la página, no del render.

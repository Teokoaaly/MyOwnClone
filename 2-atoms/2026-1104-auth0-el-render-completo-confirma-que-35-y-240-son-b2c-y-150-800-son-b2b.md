---
id: 2026-1104-auth0-el-render-completo-confirma-que-35-y-240-son-b2c-y-150-800-son-b2b
type: atom
certainty: solid
sources: [sources/2026-11-04-auth0-pricing.md]
links: ["[[2026-1103-auth0-precios-35-y-240-bajo-el-encabezado-b2b-billing]]", "[[2026-1101-auth0-b2c-essentials-escala-por-mau]]", "[[2026-1101-auth0-b2b-essentials-escala-por-mau]]", "[[2026-1104-auth0-render-completo-restaurado-tras-el-reducido-del-11-03]]"]
---

## Claim
El render completo de la página de precios de Auth0 separa explícitamente las dos columnas B2C y B2B en la tabla "Plans Overview": **Free $0/$0, Essentials $35/mes (B2C) frente a $150/mes (B2B), Professional $240/mes (B2C) frente a $800/mes (B2B)**, todos con "500 MAUs" como MAU de entrada. Las mismas cifras se repiten en las tablas de base por MAU: "B2C Base Price by MAUs (monthly)" arranca en 500 → $35 / $240, y "B2B Base Price by MAUs (monthly)" arranca en 500 → $150 / $800. Los importes de B2B son además **exactamente 4,3× (Essentials) y 3,3× (Professional)** los de B2C en el escalón de entrada.

## Why It Matters
Resuelve empíricamente la fricción que el render del 2026-11-03 había dejado abierta ([[2026-1103-auth0-precios-35-y-240-bajo-el-encabezado-b2b-billing]]): en la página real, $35 y $240 son **B2C** y $150 y $800 son **B2B**, sin ambigüedad posible, porque cada columna tiene su propia tabla rotulada. La consecuencia para el vault es una **regla de lectura** que reaparece en toda la escalera de precios documentada: los dos casos donde Auth0 duplica su precio —Free vs Essentials y B2C vs B2B— [[2026-1101-auth0-b2c-essentials-escala-por-mau]] y [[2026-1101-auth0-b2b-essentials-escala-por-mau]] son la regla de la página, y el 11-03 los confundió por un artefacto de extracción, no porque Auth0 los hubiera cambiado. La lectura operativa que sale de esto es la que el vault ya usa para el resto de proveedores: **el precio de Auth0 que hay que cotizar es el de la columna B2B si el producto es multi-tenant corporativo** (organizations, SSO, 3+ conexiones Enterprise), y el B2C solo aplica a un producto de consumo. La prima B2B no es un recargopor feature: es el precio de las Organizations, el SSO y las conexiones Enterprise que el producto multi-tenant necesita ([[2026-1022-arquitectura-rac-tres-modos-por-clon]]).

## [FRICTION]
> [[2026-1103-auth0-precios-35-y-240-bajo-el-encabezado-b2b-billing]] (escrita el 2026-11-03, `certainty: tentative`) afirma que la captura del 11-03 imprime "$35" y "$240" bajo un encabezado que dice literalmente "B2B BILLING", y deja abierta la hipótesis de que Auth0 hubiera cambiado el precio de entrada B2B.
> Este átomo presiona esa creencia porque el render completo de la misma página **rotula** $35/$240 como B2C y $150/$800 como B2B, con tablas separadas para cada columna. Si la lectura literal del 11-03 fuera correcta, la tabla "B2B Base Price by MAUs (monthly)" no podría empezar en $150 en el escalón de 500 MAU.
> Ambas no pueden ser completamente correctas: o el render del 11-03 estaba en modo B2C con el encabezado de un toggle pegado al contenido, o la página cambió entre el 11-03 y el 11-04. La captura del 11-04 es **byte a byte idéntica** a las del 11-01 y 11-02 ([[2026-1104-auth0-render-completo-restaurado-tras-el-reducido-del-11-03]]), en las que los valores B2B ya eran $150/$800, lo que deja la hipótesis del cambio de precio sin ningún apoyo material. Marcado para juicio humano, no auto-resuelto: el átomo viejo conserva su `tentative` y su texto original.

## Nota de verificación
Las cuatro cifras y el par de columnas son lectura literal de la tabla "Plans Overview" (líneas 41-46) y de las dos primeras filas de "B2C Base Price by MAUs (monthly)" (líneas 105-107) y "B2B Base Price by MAUs (monthly)" (líneas 257-259) de `sources/2026-11-04-auth0-pricing.md`. Los ratios 4,3× y 3,3× son un cálculo de este átomo sobre esas cifras.

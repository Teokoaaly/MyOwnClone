---
id: 2026-1103-auth0-organizaciones-5-en-free-y-10-en-essentials
type: atom
certainty: solid
sources: [sources/2026-11-03-auth0-pricing.md]
links: ["[[2026-1101-auth0-numero-de-tenants-por-plan]]", "[[2026-1101-auth0-b2b-essentials-escala-por-mau]]", "[[2026-1022-arquitectura-rac-tres-modos-por-clon]]", "[[2026-1101-auth0-plan-free-25000-mau-sin-tarjeta]]"]
---

## Claim
Las tarjetas de plan de Auth0 muestran un contador de **"Organizations"** por plan, con la aclaración en el plan Essentials de que son "(How we model your customers)": **5 Organizations en Free** y **10 Organizations en Essentials**. Professional y Enterprise no muestran contador de Organizations en esta captura.

## Why It Matters
"Organizations" es, literalmente según la propia página, el modo en que Auth0 modela a los clientes — es decir, la dimensión equivalente a "tenant" en el modelo multi-tenant de MyOwnClone ([[2026-1022-arquitectura-rac-tres-modos-por-clon]]). Esto significa que el Free de $0 **no** está limitado a un solo cliente: permite 5, y el salto a Essentials solo lo lleva a 10. Consecuencia operativa: para un producto cuyo eje de gasto es el número de tenants ([[2026-1022-costes-por-categoria-tenant]]), el umbral real de fricción en Auth0 está en **el 6º cliente**, no en el 2º. Es un dato favorable frente a la lectura que daba el feature matrix (1 tenant en Free, ver el conflicto abajo) y por tanto cambia el cálculo de "cuándo hay que pagar" en el vault.

## [FRICTION]
> [[2026-1101-auth0-numero-de-tenants-por-plan]] (escrita el 2026-11-01) afirma: "**Free 1 tenant, Essentials 3, Professional 12, Enterprise ilimitado**", leído de la fila "Number of Tenants Included" del feature matrix.
> Este átomo presiona eso porque la tarjeta de planes de la misma página dice "5 Organizations" en Free y "10 Organizations" en Essentials, con la aclaración de que las Organizations son "How we model your customers". Si "Organizations" y "Tenants" son la misma dimensión, los números no pueden ser 1/3 y 5/10 a la vez.
> Ambas no pueden ser completamente correctas: o el feature matrix mide otra cosa (tenants de la cuenta, con un límite distinto del número de organizaciones visibles para el cliente), o la tarjeta de planes muestra un techo distinto del contractual. Marcado para juicio humano, no auto-resuelto.

## [FRICTION]
> [[2026-1101-auth0-b2b-essentials-escala-por-mau]] (escrita el 2026-11-01) razona que "el B2B Essentials trae **Organizations ilimitadas**", citando el feature matrix.
> Este átomo presiona eso porque la tarjeta de planes del 2026-11-03 muestra un número acotado y explícito para Essentials: "10 Organizations". Si fuera ilimitado, la tarjeta no tendría por qué imprimir un contador.
> Ambas no pueden ser completamente correctas: o "ilimitadas" era una lectura errónea del feature matrix del 2026-11-01, o el tope de 10 Organizations es una cifra de la página de marketing distinta del contrato. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
"5 Organizations" y "10 Organizations (How we model your customers)" son lectura literal de las tarjetas Free y Essentials de `sources/2026-11-03-auth0-pricing.md`. La equivalencia entre "Organizations" y "tenant" es interpretación de este átomo sobre la aclaración de la propia página.

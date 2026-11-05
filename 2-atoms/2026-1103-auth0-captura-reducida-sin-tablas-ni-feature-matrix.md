---
id: 2026-1103-auth0-captura-reducida-sin-tablas-ni-feature-matrix
type: atom
certainty: solid
sources: [sources/2026-11-03-auth0-pricing.md]
links: ["[[2026-1102-auth0-precios-sin-cambios-en-48-horas]]", "[[2026-1101-auth0-precios-por-mau-no-por-evento]]", "[[2026-1103-auth0-precios-35-y-240-bajo-el-encabezado-b2b-billing]]", "[[2026-1026-emailondeck-captura-minima-344-palabras-y-cero-especificacion-operativa]]"]
---

## Claim
La captura de auth0.com/pricing del **2026-11-03** es un render **reducido** de la misma página que las capturas del 2026-11-01 y del 2026-11-02: 540 palabras frente a las ~22.023 bytes de las anteriores. Contiene las tarjetas de los cuatro planes (Free, Essentials, Professional, Enterprise), el catálogo de add-on enterprise y los programas especiales, pero **no contiene las tablas de precios por MAU, ni el feature matrix B2C/B2B, ni las definiciones de MAU y de facturación anual**.

## Why It Matters
Convierte una captura repetida en un **dato sobre el pipeline de captura**, no solo sobre Auth0: la extracción de la misma URL tres días después entrega un documento distinto, y el vault debe registrar que la página de precios de Auth0 **se renderiza por JS con toggles** (Billing B2C/B2B, Monthly/Yearly, selector de MAU) y que el extractor captura lo que el render decide mostrar. Por eso este render imprime un encabezado "B2B BILLING" con precios de B2C ([[2026-1103-auth0-precios-35-y-240-bajo-el-encabezado-b2b-billing]]) y por eso las cifras que el vault tiene fijadas desde el 2026-11-01 ([[2026-1101-auth0-precios-por-mau-no-por-evento]], [[2026-1102-auth0-precios-sin-cambios-en-48-horas]]) **no se pueden re-verificar ni refutar con esta captura**: el 2026-11-03 no las contradice, simplemente no las contiene. Es el mismo patrón ya documentado con EmailOnDeck, cuya captura mínima de 344 palabras dejó cero especificación operativa ([[2026-1026-emailondeck-captura-minima-344-palabras-y-cero-especificacion-operativa]]). Regla operativa que se deriva: **una captura reducida no es evidencia de estabilidad ni de cambio** — solo es evidencia de qué parte de la página sobrevivió al render.

## Nota de verificación
El recuento de 540 palabras procede del frontmatter de `sources/2026-11-03-auth0-pricing.md`; la ausencia de tablas de precios y de feature matrix se verificó por lectura completa del archivo (236 líneas). La comparación con las capturas del 2026-11-01/02 en tamaño y contenido es lectura de este átomo.

---
id: 2026-1101-clerk-machine-auth-2500-m2m-y-100000-verificaciones
type: atom
certainty: solid
sources: [sources/2026-11-01-clerk-pricing.md]
links: ["[[2026-1101-auth0-m2m-tokens-5k-incluidos-en-professional]]", "[[2026-1101-clerk-plan-gratuito-50000-mru-y-3-asientos]]", "[[2026-1022-myclone-api-rest]]"]
---

## Claim
La **autenticación de máquina** de Clerk tiene cuotas propias: en Hobby, **1.000 creaciones y 100.000 verificaciones de API Keys** y **2.500 creaciones y 100.000 verificaciones de M2M Tokens** al mes; en Pro y Business, **1.000 creaciones de API Key y 2.500 de M2M incluidos**, con el excedente a **$0,001 por creación** y **$0,00001 por verificación**.

## Why It Matters
Es la partida que casi nadie mira y que aquí tiene dos lecturas útiles. La primera: **verificar un M2M token cuesta $0,00001** — 100.000 verificaciones al mes ya son el techo gratis, y un servicio interno que verifique tokens en cada llamada (el patrón M2M entre microservicios, relevante si el clon expone API REST propia, ver [[2026-1022-myclone-api-rest]]) agota ese margen enseguida: 1M de verificaciones/mes = **$10/mes**, y 10M = **$100/mes**. La segunda, comparada con Auth0, donde los M2M tokens van **5.000 incluidos en Professional** ([[2026-1101-auth0-m2m-tokens-5k-incluidos-en-professional]]), la cuota de Clerk es **más generosa en el tramo Hobby** (2.500 vs el plan de pago de Auth0), lo que refuerza que **el tramo gratuito de Clerk aguanta un backend de microservicios decente** sin salto de plan. Pero la lección de fondo para el eje del vault es la misma que en el resto de la tabla: **casi todas las líneas de Clerk son de uso (MRU, MRO, checks, verificaciones) y solo una es porcentaje sobre el negocio**; el coste por asiento domina en cuanto el producto deja de ser pequeño.

## Nota de verificación
Filas "API Keys" y "M2M Tokens" de la tabla "Full price breakdown" de la captura del 2026-11-01, verbatim ("Creations 1,000 Included per month / 1,001+ $0.001 each / Verifications 100,000 Included per month / 100,001+ $0.00001 each"). La aritmética de 1M/10M verificaciones es lectura operativa del átomo.

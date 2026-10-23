---
id: 2026-1023-hetzner-presupuesto-4-euros-no-alcanza
type: atom
certainty: tentative
sources: [sources/2026-10-22-hetzner-cloud.md]
links: ["[[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]", "[[2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados]]", "[[2026-1022-costes-por-categoria-tenant]]", "[[2026-1022-platform-admin-tenants-costes-mrr]]"]
---

## Claim
El plan más barato de Hetzner Cloud cuesta **€ 5.99/mes sin IVA**, es decir **un 50 % por encima del objetivo de ≤ €4/mes** que la captura que originó esta nota fijaba como presupuesto de referencia para un VPS, y con el IVA el desvío es mayor. La lectura que se infiere (no está afirmada en la fuente) es que **ningún plan del catálogo de Hetzner Cloud cabe en un presupuesto de €4/mes**: el suelo de lista es €5.99 sin IVA, y el siguiente escalón está en €6.49.

## Why It Matters
Convierte el objetivo de presupuesto de infra en una restricción real y no en una aspiración: o se acepta ~€6/mes como suelo de la infraestructura cloud, o el VPS de €4 tiene que venir de otro proveedor o de un modelo distinto (pago por uso a €0.0096/h, que a media carga baja la factura muy por debajo del mínimo mensual). Es un número que hay que poner al lado del resto de la estructura de coste del producto — el corte por categoría de [[2026-1022-costes-por-categoria-tenant]] y el seguimiento de MRR y costes del panel de [[2026-1022-platform-admin-tenants-costes-mrr]] — porque el hosting no aparece en ninguna de las dos categorías documentadas (clon responses e ingestion) y sería una tercera línea de coste fijo de plataforma. La comparación de precio base del producto (99/mes en [[2026-1022-precio-99-mensual]]) es lo que da contexto a ese suelo.

## Nota de verificación
La cifra €5.99 es lectura directa de la calculadora de la página; la conclusión "no hay plan por debajo de €4" es una inferencia de este átomo, no una frase de la fuente.

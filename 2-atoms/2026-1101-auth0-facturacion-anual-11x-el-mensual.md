---
id: 2026-1101-auth0-facturacion-anual-11x-el-mensual
type: atom
certainty: solid
sources: [sources/2026-11-01-auth0-pricing.md]
links: ["[[2026-1101-auth0-b2c-essentials-escala-por-mau]]", "[[2026-1027-proton-business-vpn-precios-publicados-por-usuario-en-cuatro-planes]]", "[[2026-1031-clerk-pricing]]"]
---

## Claim
La facturación anual de Auth0 es **exactamente 11× el precio mensual** ("Yearly billing is 11× the monthly price (equivalent to 1 month free)"), no un porcentaje de descuento: Essentials B2C a 500 MAU es $35/mes o $385/año; Professional B2C $240/mes o $2.640/año; Essentials B2B $150/mes o $1.650/año; Professional B2B $800/mes o $8.800/año.

## Why It Matters
El descuento real del prepago es de **1/12 = 8,33 %**, un valor modesto que no cambia ninguna decisión de arquitectura: pagar por adelantado en Auth0 es una optimisation menor al lado del hecho de que el propio plan de entrada B2B ya cuesta 30 veces el presupuesto de infra del vault. Comparado con el sector que el vault ya documenta — donde el prepago anual a veces es la palanca real (HostBrr a €2/mes, cf. [[2026-1027-proton-business-vpn-precios-publicados-por-usuario-en-cuatro-planes]] y la escalera de VPS baratos) — Auth0 no ofrece palanca por compromiso de volumen: **el descuento es idéntico en el escalón de 500 MAU y en el de 50.000**. Para MyOwnClone, la lectura es que el compromiso anual no sirve para la planificación financiera de la identidad: la única palanca real es quedarse en el plan Free de $0 ([[2026-1101-auth0-plan-free-25000-mau-sin-tarjeta]]), y el mismo estilo de "features gateadas sin capa intermedia" que se ve en Clerk ([[2026-1031-clerk-pricing]]).

## Nota de verificación
El "11×" y los importes anuales son lectura literal de las tablas yearly del 2026-11-01; el 8,33 % es un cálculo de este átomo.

---
id: 2026-1031-workos-annual-credits-frente-a-pay-as-you-go
type: atom
certainty: solid
sources: [sources/2026-10-31-workos-pricing.md, sources/2026-11-03-workos-pricing.md]
links: ["[[2026-1031-workos-authkit-primer-millon-de-mau-gratis]]", "[[2026-1031-workos-sso-escalera-de-conexiones-125-100-80-65]]", "[[2026-1101-workos-plan-scale-de-soporte-1000-al-mes]]", "[[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]]"]
---

## Claim
WorkOS ofrece dos planes. **Pay as you go**: precio por uso con descuentos por volumen automáticos, despliegue en minutos, canal de Slack dedicado y pricing transparente. **Annual Credits**: "Everything in Pay as you go, plus..." — descuentos por prepago de créditos, **SLA de 99,99% de uptime**, migración y onboarding guiados, **SLA de soporte garantizado** y canal de Slack dedicado. Su precio es **custom** (no publicado).

## Why It Matters
Annual Credits es el **plan de empresa** y su lista de extras es exactamente la de un contrato enterprise: SLA de uptime del 99,99%, onboarding/migrations guiadas y SLA de soporte garantizado. Para MyOwnClone la lectura es de dos niveles. Primero, en fase beta el plan **Pay as you go basta**: todo lo que el vault necesita (AuthKit, SSO, Directory Sync) tiene precio de lista público y no requiere contrato ni prepago. Segundo, el riesgo estructural es el **prepago de créditos**: es el único punto del modelo WorkOS donde el consumo se paga por adelantado, lo que convierte un error de proyección de tenants en deuda de saldo; para un producto con coste variable de IA por tenant, mezclar créditos prepagados con el coste variable real es exactamente el patrón que hay que evitar en el modelo de costes por categoría ([[2026-1022-costes-por-categoria-tenant]]). Nota: el precio del plan **no está publicado**, así que cualquier comparación cuantitativa entre WorkOS y los planes públicos de Auth0 o Clerk es incompleta mientras no haya una cotización.

## 2026-11-03 — re-verificación
El volcado crudo del 11-03 confirma las dos tarjetas con sus listas completas de bullets. **Pay as you go**: "Automatic volume discounts", "First 1 million active users free", "Deploy in minutes", "Dedicated Slack channel", "Transparent pricing" — CTA "View pricing". **Annual Credits**: "Everything in Pay as you go, plus...", "Pre-pay credit discounts", "99.99% uptime SLA", "Guided migration and onboarding", "Guaranteed support SLA" — CTA "Schedule a call". Matiz nuevo relevante: el CTA de **Pay as you go es "View pricing" (autoservicio)** y el de **Annual Credits es "Schedule a call" (comercial)**, lo que confirma la lectura de este átomo de que Annual Credits es el plan enterprise no publicado y que WorkOS separa deliberadamente el autoservicio del circuito comercial ([[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]]). Se mantiene la conclusión de que el precio de Annual Credits es **custom** y que el prepago de créditos es el único punto del modelo donde el consumo se paga por adelantado.

## Nota de verificación
Secciones "Pay as you go" y "Annual Credits" de la captura del 2026-10-31, verbatim en los bullets ("Pre-pay credit discounts", "99.99% uptime SLA", "Guided migration and onboarding", "Guaranteed support SLA").

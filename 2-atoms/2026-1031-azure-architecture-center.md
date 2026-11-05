---
id: 2026-1031-azure-architecture-center
type: atom
certainty: solid
sources: [sources/2026-10-31-azure-architecture-center.md, sources/2026-11-01-azure-architecture-center.md]
links: ["[[2026-1031-proton-business-vpn-essentials-6-99-minimo-2-usuarios]]", "[[costes-por-categoria-tenant]]", "[[2026-1101-azure-architecture-center-arboles-de-decision-para-elegir-servicios]]", "[[2026-1101-azure-architecture-center-cuatro-puntos-de-entrada]]", "[[2026-1101-azure-architecture-center-landing-zone-y-guias-de-migracion-entre-nubes]]"]
---

## Claim
The Azure Architecture Center provides foundational cloud design patterns and best practices without direct pricing tables, focusing instead on architectural guidance for reliability, security, and cost optimization across Azure services.

## Why It Matters
Architectural guidance without exposed pricing forces cost estimation through indirect means — reviewing documented patterns, reference architectures, and Microsoft's cost-management tools separately. This creates a friction point for teams needing to correlate architectural decisions with budget commitments, especially when comparing against direct-pricing sources like the `costes-por-categoria-tenant` thread which provides explicit per-seat cost models. The absence of embedded pricing in architectural documentation means cost considerations must be extrapolated rather than declared.

## [FRICTION]
> [[2026-1028-proton-business-mail-recommended-y-distincion-por-plan]] differentiates Proton plans by recommended use and features, while the Azure Architecture Center offers no such plan-level recommendations — it provides general patterns applicable across any cloud service. Both cannot simultaneously serve as the primary reference for plan selection: the Azure center's generalism vs. Proton's tiered specificity means teams must supplement architectural guidance with explicit pricing data from direct sources to make informed cost decisions.

## Nota de extensión 2026-11-03
Fuente: `sources/2026-11-01-azure-architecture-center.md` (la captura más completa del lote). La ausencia de precios queda **confirmada por la estructura misma de la navegación**, no solo por inferencia: en la captura completa del 11-01 el footer del sitio de Learn enlaza "Pricing information" (`azure.microsoft.com/pricing`) y "Cost management & billing" (`learn.microsoft.com/en-us/azure/cost-management-billing/`) como recursos **externos y separados** del catálogo de arquitectura, que vive bajo su propia sección "Architecture" junto a "Cloud Adoption Framework" y "Well-Architected Framework". Es decir: Microsoft separa deliberadamente la capa de *cómo construir* de la capa de *cuánto cuesta*, y ninguna de las dos se mezcla.

El center sí publica, en cambio, el **vocabulario de elección** que la nota original daba por ausente: "Make technology choices" con árboles de decisión por servicio (compute, data stores, AI services) y "Apply design patterns" para los patrones de diseño reutilizables. Ver [[2026-1101-azure-architecture-center-arboles-de-decision-para-elegir-servicios]] y [[2026-1101-azure-architecture-center-cuatro-puntos-de-entrada]]. Esto **desplaza** la creeencia original sin refutarla: el center no da precios por plan, pero sí da el marco para *elegir* — que es un input distinto del precio y que, para el eje del vault, es el que convierte "una arquitectura" en "una factura".
El catálogo está además indexado por entrada cruzada Cloud→Cloud ("Azure for AWS professionals", "Azure for Google Cloud professionals") y por "Azure landing zone", lo que confirma que su unidad de trabajo es la equivalencia entre servicios, no el precio: ver [[2026-1101-azure-architecture-center-landing-zone-y-guias-de-migracion-entre-nubes]].
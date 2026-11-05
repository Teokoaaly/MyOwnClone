---
id: 2026-1101-azure-architecture-center-landing-zone-y-guias-de-migracion-entre-nubes
type: atom
certainty: solid
sources: [sources/2026-11-01-azure-architecture-center.md]
links: ["[[2026-1101-azure-architecture-center-cinco-tipos-de-artefacto]]", "[[2026-1022-costes-por-categoria-tenant]]", "[[2026-1023-hetzner-costes-por-categoria-vs-infraestructura-propia]]"]
---

## Claim
El índice del Architecture Center incluye entradas transversales que no son arquitecturas sino **mecanismos de traducción y gobierno**: "Application architecture fundamentals", "Azure landing zone", "Azure categories", "Architecture icons", "Browse all Architectures", "What's new in the Architecture Center", y dos guías de equivalencia Cloud→Cloud: **"Azure for AWS professionals"** y **"Azure for Google Cloud professionals"**.

## Why It Matters
Las dos guías "Azure for X professionals" son la prueba de que Microsoft asume que su audiencia es gente que **ya opera en otro proveedor** y quiere mapear su arquitectura existente, no gente que empieza de cero. Eso es exactamente la postura del vault: MyOwnClone no está eligiendo cloud, está eligiendo **dónde alojar** dentro de un presupuesto de ≤ €4/mes, y el mapa mental por el que se razona es el de VPS + PaaS barato (Hetzner, Neon, Vercel), no el de Azure. El valor de estas guías es el método: **traducir servicios de un proveedor a otro por función, no por producto**.
La entrada "Azure landing zone" es la counterpartia del problema inverso: un *landing zone* es la capa de gobierno (suscripciones, políticas, red) que Azure da por hecha en sus arquitecturas de referencia. Su presencia implícita es una advertencia para el vault: **las arquitecturas de referencia de un hyperscaler asumen un gobierno de cuentas que un proyecto de ≤ €4/mes no tiene**, así que su estructura no es copiable tal cual — solo su forma.

---
id: 2026-1023-live-verify-vocabulario-backoffice-mrr-y-estados-tenant
type: atom
certainty: solid
sources: [0-raw/archive/2026-10-23-2026-10-22-myownclone-live-reverification.md]
links: ["[[2026-1022-platform-admin-tenants-costes-mrr]]", "[[2026-1022-live-verify-fuga-admin-cerrada-pero-queda-i18n]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
El bundle vivo de [[myownclone]] conserva el vocabulario completo del back-office de plataforma, aunque el código de los módulos ya no se sirva: el overview de admin declara `mrrCostsMarginLegend: "MRR / Costs / Margin"`, `costs30d: "Costs (30d)"` y los estados de tenant `tenant`, `trial` y `suspended`; el namespace `tenantDetail` expone `stripeCustomer`, `stripeSubscription` y `subscriptionStatus`, y el vocabulario de planes completo `basic, pro, scale, enterprise, free`. El dashboard del creador enumera nueve secciones: `biblioteca`, `cerebro`, `inbox`, `productos`, `reuniones`, `analiticas`, `facturacion`, `configuracion` y `resumen`.

## Why It Matters
Confirma en la build desplegada que el back-office sigue siendo un producto de plataforma con métricas de negocio (MRR, costes a 30 días, margen) y con gestión de ciclo de vida por tenant —incluido un estado `suspended` que el vault no tenía registrado—, no un simple panel de creador. Como el namespace viaja en el i18n público, esa nomenclatura sigue siendo legible sin sesión (ver [[2026-1022-live-verify-fuga-admin-cerrada-pero-queda-i18n]]): el mapa de negocio interno se puede reconstruir desde el bundle aunque los componentes del panel ya no se sirvan. Es la confirmación más reciente del módulo de plataforma descrito en [[2026-1022-platform-admin-tenants-costes-mrr]] y del desglose de coste por tenant de [[2026-1022-costes-por-categoria-tenant]].

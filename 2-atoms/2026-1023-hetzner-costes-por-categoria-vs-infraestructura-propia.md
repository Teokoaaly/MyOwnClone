---
id: 2026-1023-hetzner-costes-por-categoria-vs-infraestructura-propia
type: atom
certainty: tentative
sources: [sources/2026-10-22-hetzner-cloud.md]
links: ["[[2026-1022-costes-por-categoria-tenant]]", "[[2026-1022-platform-admin-tenants-costes-mrr]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1022-precio-99-mensual]]"]
---

## Claim
El back-office de plataforma de [[myownclone]] desglosa el coste por proveedor (Anthropic + OpenAI + email) y por eje (chat vs. ops) ([[2026-1022-platform-admin-tenants-costes-mrr]]), pero **no existe ninguna categoría de infraestructura**: el hosting es un coste fijo que no aparece en el corte por categorías documentado en [[2026-1022-costes-por-categoria-tenant]], donde solo se distinguen `categoryCloneResponses` y `categoryIngestion` (facturables al tenant) frente a `categoryPlatformOps` (absorbido por la plataforma). Con la referencia de Hetzner, ese coste fijo ausente es cuantificable: **~€5,99/mes** en el plan más barato ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]).

## Why It Matters
Con un plan base de 99/mes ([[2026-1022-precio-99-mensual]]) y un solo tenant, ~€6/mes de hosting es un 6 % del ingreso — visible pero no decisivo; con 10 tenants, cae a 0,6 %, y con 100, a 0,06 %. El punto no es el número sino que **es una categoría ausente del panel**: si el hosting es real (y lo es, el sitio se sirve desde un VPS nginx), es un coste absorbido por la plataforma que no aparece en ninguna de las dos líneas que el founder ve, igual que una parte de `categoryPlatformOps`. La lectura que se infiere (no está en la fuente) es que el MRR real del panel está sobreestimado en esa partida, o que el hosting se computa en otra parte del back-office que la captura de bundles no revela.

## [FRICTION]
> [[2026-1022-costes-por-categoria-tenant]] afirma que el modelo de coste de [[myownclone]] separa el coste facturable al tenant (respuestas del clon, ingestion) del coste de operación interna absorbido por la plataforma, y que el panel lo expone "con un desglose por proveedor (Anthropic + OpenAI + email)".
> Este átomo presiona esa creencia porque ese corte **no tiene línea de infraestructura**: un hosting VPS a ~€5,99/mes es un coste de plataforma que no cabe en ninguna de las tres categorías listadas (Anthropic, OpenAI, email) ni en el eje chat/ops tal como está descrito.
> Ambas no pueden ser completamente correctas: o el hosting se imputa dentro de `categoryPlatformOps` sin desglose visible (imposible de leer en el panel), o el panel de costes no incluye infraestructura porque el hosting se contabiliza aparte. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
El coste de €5,99/mes viene de la página de Hetzner ([[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]); que el VPS vivo de [[2026-1022-live-verify-deployment-migrada-a-vps-nginx]] sea un plan de ese precio es una inferencia no confirmada. La captura de Hetzner no dice nada sobre la contabilidad interna de [[myownclone]].

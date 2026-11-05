---
id: 2026-1103-auth0-entornos-produccion-y-desarrollo-separados-en-essentials
type: atom
certainty: solid
sources: [sources/2026-11-03-auth0-pricing.md]
links: ["[[2026-1101-auth0-b2c-essentials-escala-por-mau]]", "[[2026-1101-workos-staging-gratis-solo-produccion-se-factura]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
El plan **Essentials de Auth0 ($35/mes)** incluye "**Separate Production & Development Environments**", es decir, un tenant de desarrollo separado del de producción. La lista del plan Free no incluye ese feature (Essentials declara "Everything in Free, plus…").

## Why It Matters
Es la línea de coste de un servicio de identidad que suele quedar oculta: **el staging de un proveedor de auth no es gratis** en el sentido de que consume una organization y una factura de $35/mes aunque nunca autentique a un usuario real, y en Auth0 el feature llega a partir de $35/mes, no del Free de $0. Para el vault, que separa costes por categoría y por tenant ([[2026-1022-costes-por-categoria-tenant]]), esto es una diferencia estructural con WorkOS, donde el staging es gratuito y solo se factura la producción ([[2026-1101-workos-staging-gratis-solo-produccion-se-factura]]): en Auth0, un entorno de desarrollo consume una organization. Es también un recordatorio de que en el vault la identidad se paga por **entornos**, no solo por usuarios.

## Nota de verificación
Bullet "Separate Production & Development Environments" y la estructura "Everything in Free, plus…" de la tarjeta Essentials son lectura literal de `sources/2026-11-03-auth0-pricing.md`.

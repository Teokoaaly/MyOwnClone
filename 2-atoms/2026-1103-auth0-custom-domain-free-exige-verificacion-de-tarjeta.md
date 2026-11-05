---
id: 2026-1103-auth0-custom-domain-free-exige-verificacion-de-tarjeta
type: atom
certainty: solid
sources: [sources/2026-11-03-auth0-pricing.md]
links: ["[[2026-1101-auth0-plan-free-25000-mau-sin-tarjeta]]", "[[2026-1022-costes-por-categoria-tenant]]", "[[2026-1103-auth0-organizaciones-5-en-free-y-10-en-essentials]]"]
---

## Claim
La tarjeta del plan Free de Auth0 incluye "**1 Custom Domain***" con la nota al pie "* credit card verification required for custom domains", y "**Unlimited Social Connections**" con la nota "** subject to system limitations". El propio plan declara además "No credit card needed to sign up."

## Why It Matters
Es una contradicción operativa interna de la página que el vault no había registrado: Auth0 dice "no credit card needed to sign up" y, a la vez, **para usar el único dominio personalizado incluido en el plan gratuito hay que verificar una tarjeta**. Para un founder que evita deliberadamente atar una tarjeta a un proveedor —justo la posición que el vault sostiene con ExtraVM, que paga solo con cripto y sin KYC ([[2026-1024-extravm-pago-cripto-sin-kyc-ni-identidad]]) o con los proveedores sin tarjeta como HostBrr— esto significa que la gratuidad del plan Free **no es completa sin tarjeta**. La segunda nota ("Unlimited Social Connections subject to system limitations") es la otra cara: "unlimited" no es ilimitado, y la página no publica cuáles son esas limitaciones. Ambas notas al pie son la prueba de que los bullets de las tarjetas de plan de Auth0 deben leerse **con sus asteriscos**: los números sin asterisco (5 Organizations, 1 Enterprise Connection) no tienen ese tipo de aviso, y este átomo es el que obliga a mirar los que sí lo tienen ([[2026-1103-auth0-organizaciones-5-en-free-y-10-en-essentials]]).

## Nota de verificación
Las dos notas al pie ("* credit card verification required for custom domains." y "** subject to system limitations.") y la frase "No credit card needed to sign up." son lectura literal de `sources/2026-11-03-auth0-pricing.md`. La inferencia sobre el atado a tarjeta es lectura de este átomo.

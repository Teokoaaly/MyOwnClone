---
id: 2026-1101-auth0-sso-scim-en-free-pero-no-en-essentials-b2c
type: atom
certainty: solid
sources: [sources/2026-11-01-auth0-pricing.md, sources/2026-11-03-auth0-pricing.md]
links: ["[[2026-1101-auth0-plan-free-25000-mau-sin-tarjeta]]", "[[2026-1101-auth0-b2b-essentials-escala-por-mau]]", "[[2026-1031-clerk-pricing]]", "[[2026-1027-proton-business-vpn-sso-con-cualquier-saml-2-0-pero-scim-solo-okta-y-entra]]", "[[2026-1103-auth0-organizaciones-5-en-free-y-10-en-essentials]]", "[[2026-1103-auth0-precios-35-y-240-bajo-el-encabezado-b2b-billing]]", "[[2026-1103-auth0-captura-reducida-sin-tablas-ni-feature-matrix]]"]
---

## Claim
El feature matrix de Auth0 es **incomprensible por sí solo** en un punto clave: en la columna **Free**, "Self-Service SSO", "Inbound SCIM" y "Enterprise Connections: 1" figuran como **Included**; pero en las columnas **Essentials y Professional de B2C**, Self-Service SSO pasa a "Not available" y Enterprise Connections a "Not available", mientras que en **B2B** Essentials/Professional Self-Service SSO también es "Not available" y Enterprise Connections son "3 + ADD-ON" / "5 + ADD-ON". Solo la columna Enterprise los da ("Select Enterprise Plans"). La nota al pie de la captura del 2026-10-31 lo dice explícito: "Upgrade to B2B to continue using EC, Self-Service SSO, and SCIM."

## Why It Matters
Traducido a coste para MyOwnClone: **el único escenario en el que se puede tener SSO/SCIM sin pagar es el plan Free (25.000 MAU, $0), y en cuanto se sube a Essentials se pierde el Self-Service SSO en B2C y en B2B**. Es un modelo de gating que se lee al revés respecto a Clerk, donde todas las features están en todos los tiers ([[2026-1031-clerk-pricing]]), y que se aparta del patrón del sector: en Proton Business el SSO con SAML 2.0 viene por plan y el SCIM está limitado a Okta/Entra ([[2026-1027-proton-business-vpn-sso-con-cualquier-saml-2-0-pero-scim-solo-okta-y-entra]]). La consecuencia operativa para el vault es clara: **la decisión Auth0-vs-NextAuth-propio no es "gratis vs de pago" sino "Free y 1 conexión, o de golpe B2B a $150/mes"** — no hay un punto intermedio con SSO. Y para el producto multi-tenant, el SSO por organización es precisamente el requisito que justifica la prima B2B documentada en [[2026-1101-auth0-b2b-essentials-escala-por-mau]].

## Nota de verificación
Las celdas del feature matrix y la nota al pie "Upgrade to B2B to continue using EC, Self-Service SSO, and SCIM" son lectura literal de las capturas del 2026-11-01 y del 2026-10-31 respectivamente. La lectura de "incomprensible" es interpretación de este átomo sobre la tabla, no una frase de la fuente.

## 2026-11-03 — re-verificación
Fuente: `sources/2026-11-03-auth0-pricing.md` (render reducido de 540 palabras de auth0.com/pricing).

Esta captura es la **primera evidencia directa de la nota al pie** en la propia tarjeta de plan (no en el feature matrix): bajo la tarjeta de Essentials aparece literalmente "1 Upgrade to B2B to continue using EC, Self-Service SSO, and SCIM.", y la misma nota se repite bajo la tarjeta de Professional con el superíndice ¹ ("¹ Upgrade to B2B to continue using EC, Self-Service SSO, and SCIM."). En Free, Self-Service SSO y SCIM figuran como incluidos y **marcados como "New"**.

Esto confirma el mecanismo de gating descrito en el Claim de este átomo: Self-Service SSO y SCIM están presentes en el Free, pero el pie de página los condiciona al escalar a B2B. El matiz nuevo es que la captura los etiqueta "New", es decir, Auth0 está **promocionando en el Free features que su propia nota dice que exigen B2B** — marketing y contrato apuntan en direcciones opuestas (ver [[2026-1103-auth0-organizaciones-5-en-free-y-10-en-essentials]] para el mismo patrón de la página). No se puede determinar desde el texto si la nota aplica a los planes B2C o a las columnas B2B de este render; el conflicto con la escalera B2B de $150/$800 se registra en [[2026-1103-auth0-precios-35-y-240-bajo-el-encabezado-b2b-billing]].

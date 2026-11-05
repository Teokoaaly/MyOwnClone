---
id: 2026-1101-auth0-addon-sso-enterprise-100-usd-por-conexion
type: atom
certainty: solid
sources: [sources/2026-11-01-auth0-pricing.md, sources/2026-11-03-auth0-pricing.md]
links: ["[[2026-1101-auth0-b2b-essentials-escala-por-mau]]", "[[2026-1027-proton-business-vpn-sso-con-cualquier-saml-2-0-pero-scim-solo-okta-y-entra]]", "[[2026-1031-workos-pricing]]", "[[2026-1101-auth0-sso-scim-en-free-pero-no-en-essentials-b2c]]", "[[2026-1103-auth0-professional-4-features-de-seguridad-enterprise]]"]
---

## Claim
Las **Enterprise SSO Connections** se cobran como add-on a **$100/mes ($1.100/año) por conexión adicional**, con máximo de 30 conexiones por cuenta. Essentials B2B incluye 3 conexiones; Professional B2B incluye 5. La **Enterprise MFA** cuesta **$100/mes ($1.100/año)** en Essentials y va **incluida** en Professional.

## Why It Matters
Aquí es donde el precio por MAU deja de ser la métrica relevante: el SSO empresarial se factura **por conexión (por cliente IdP), no por usuario**. Para un producto que sirve a empresas (el caso B2B de MyOwnClone), el coste de identidad escala con el **número de clientes corporativos** y con cuántos IdP (Okta, Entra, Google Workspace) hay que integrar, no con los usuarios. Con el presupuesto de ≤ €4/mes del vault, una sola conexión extra de $100/mes (~€92) es 23 veces el presupuesto: si el producto necesita SSO, Auth0 solo es viable dentro de los free tiers de conexiones (3 en Essentials B2B / 1 en Free) o del precio de WorkOS, que es un producto cuyo coste es exactamente por producto/API ([[2026-1031-workos-pricing]]). El contraste con el vault es directo: en Proton Business el SSO es "cualquier SAML 2.0 pero SCIM solo Okta y Entra" ([[2026-1027-proton-business-vpn-sso-con-cualquier-saml-2-0-pero-scim-solo-okta-y-entra]]), es decir, el coste del SSO en el sector está en las capacidades, no en el número de conexiones — en Auth0 el número de conexiones **sí** es un precio.

## Nota de verificación
Precios y topes de conexiones leídos literalmente de la sección "B2B Add-ons" de la captura del 2026-11-01.

## 2026-11-03 — re-verificación
Fuente: `sources/2026-11-03-auth0-pricing.md` (render reducido de 540 palabras de auth0.com/pricing).

Dos puntos: (1) la tarjeta del plan Free vuelve a listar "**1 Enterprise Connection**" y la nota al pie de Essentials/Professional reitera "Upgrade to B2B to continue using EC, Self-Service SSO, and SCIM", confirmando que **EC (Enterprise Connections) es la capacidad que se pierde al subir de plan** (ver [[2026-1101-auth0-sso-scim-en-free-pero-no-en-essentials-b2c]]); (2) la tarjeta de Professional lista "**Enterprise Multi-Factor Authentication**" como feature incluida, lo que confirma el dato de este átomo de que el add-on Enterprise MFA de $100/mes en Essentials **va incluido en Professional** (ver [[2026-1103-auth0-professional-4-features-de-seguridad-enterprise]]).

La captura **no** vuelve a publicar los precios del add-on de conexiones ($100/mes, máx. 30) ni el desglose 3 conexiones en Essentials B2B / 5 en Professional B2B, así que esas cifras quedan sin re-verificar en esta ronda.

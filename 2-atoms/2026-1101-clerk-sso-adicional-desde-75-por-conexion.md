---
id: 2026-1101-clerk-sso-adicional-desde-75-por-conexion
type: atom
certainty: solid
sources: [sources/2026-11-01-clerk-pricing.md]
links: ["[[2026-1031-clerk-pricing]]", "[[2026-1101-auth0-addon-sso-enterprise-100-usd-por-conexion]]", "[[2026-1027-proton-business-vpn-sso-con-cualquier-saml-2-0-pero-scim-solo-okta-y-entra]]"]
---

## Claim
Las **conexiones SSO enterprise** de Clerk (SAML, OIDC, EASIE) están **"Not included" en Hobby**; Pro y Business incluyen **1 conexión por app**, y las adicionales se cobran por tramo de volumen: **2–15 a $75/mes cada una**, **16–100 a $60/mes**, **101–250 a $48/mes**, **251+ "Contact us"**. Business añade además "Enterprise SSO for workspace".

## Why It Matters
Es la línea de coste que decide si MyOwnClone puede vender a **empresas** (clientes con SAML corporativo en varios tenants): el precio de la segunda conexión SSO ya es **$75/mes**, cinco veces el presupuesto de hosting del vault entero. Comparado con Auth0, donde el add-on de SSO enterprise es de $100/conexión ([[2026-1101-auth0-addon-sso-enterprise-100-usd-por-conexion]]), Clerk es más barato por conexión pero con un **suelo de plan** (Pro $20) que Auth0 no tiene en la misma forma; y frente a Proton, donde el SSO con SAML 2.0 viene incluido en el plan y el SCIM es lo que se restringe ([[2026-1027-proton-business-vpn-sso-con-cualquier-saml-2-0-pero-scim-solo-okta-y-entra]]), Clerk cobra **por número de conexiones, no por plan**. Operativamente: **una sola conexión SSO fuerza el plan Pro**; dos o más, el coste mensual de identidad se acerca al 10x la partida de infraestructura.

## Nota de verificación
Tramos verbatim de la fila "SSO connections" de la tabla "Full price breakdown" (captura del 2026-11-01) y bullet "1 SSO connection included / Additional $75/mo each" de la tarjeta Pro.

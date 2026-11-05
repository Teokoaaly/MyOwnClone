---
id: 2026-1031-auth0-catalogo-de-addons-enterprise
type: atom
certainty: solid
sources: [sources/2026-10-31-auth0-pricing.md, sources/2026-11-03-auth0-pricing.md]
links: ["[[2026-1101-auth0-enterprise-contact-us-sla-y-30-dias-de-logs]]", "[[2026-1101-auth0-addon-sso-enterprise-100-usd-por-conexion]]", "[[2026-1029-render-enterprise-compliance]]", "[[2026-1027-proton-business-vpn-sso-con-cualquier-saml-2-0-pero-scim-solo-okta-y-entra]]", "[[2026-1101-auth0-m2m-tokens-5k-incluidos-en-professional]]", "[[2026-1101-auth0-cuotas-de-actions-forms-y-token-vault]]"]
---

## Claim
La página de precios de Auth0 enumera nueve add-on enterprise **sin precio publicado**: AI Identity for B2B & Commerce (conexión de agentes a apps, APIs y servidores MCP, con confirmación humana para acciones críticas), Fine-Grained Authorization, Attack Protection (con Tenant ACL y listas de redes maliciosas), **Private Cloud** (despliegue Auth0 dedicado de baja fricción), Adaptive MFA, Machine-to-Machine Tokens, **Highly Regulated Identity** (Strong Customer Authentication, protocolos FAPI, Customer Managed Keys), Advanced Extensibility (Actions, Forms, Auth0 Marketplace) y **HIPAA BAA & PCI** (Business Associate Agreement y entornos PCI-compliant).

## Why It Matters
Ninguno de estos add-on tiene precio en la página: **la lista completa de capacidades enterprise es una lista de costes no cuantificables**. Para el founder con presupuesto duro de ≤ €4/mes, el dato accionable es el inverso del que se suele leer: la lista de add-on no es una oportunidad, es una **frontera**. Lo único que la página separa del resto es "Private Deployment"/"Private Cloud", que es un despliegue dedicado — una categoría de coste de infraestructura, no de licencia, y por tanto incompatible con un VPS de ≤ €4/mes ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]) y directamente comparable con el eje de cumplimiento que el vault ya separa para Render ([[2026-1029-render-enterprise-compliance]]) y para Proton Business ([[2026-1027-proton-business-vpn-sso-con-cualquier-saml-2-0-pero-scim-solo-okta-y-entra]]). El único add-on que el vault puede descartar por coste sin cotizar es el de AI Identity (+50 % del base, ver [[2026-1101-auth0-addon-agentes-ai-suma-50-por-ciento]]); el resto exigiría pasar por el tier Enterprise "Contact us" ([[2026-1101-auth0-enterprise-contact-us-sla-y-30-dias-de-logs]]).

## Nota de verificación
Los nueve add-on y sus descripciones son lectura literal de la sección "Enterprise add-ons to fit your needs" de la captura del 2026-10-31. La observación de que ninguno publica precio es una observación sobre el contenido de la captura.

## 2026-11-03 — re-verificación
Fuente: `sources/2026-11-03-auth0-pricing.md` (render reducido de 540 palabras de auth0.com/pricing).

Los **nueve add-on** reaparecen, en el mismo orden y con las mismas nueve denominaciones, confirmando que el catálogo sigue sin precios publicados. Descripciones que esta captura desarrolla y que no estaban en el átomo original:
- **AI Identity for B2B & AI Identity for Commerce**: "Connect your AI agents to apps, APIs, and MCP servers in a more secure manner… Enable human confirmation for critical agent actions."
- **Attack Protection**: añade "Tenant ACL, use out-of-the-box blocklists of known malicious networks & anonymizers" y "risk intelligence enhanced with third-party supplemental signals".
- **Private Cloud**: "a low-friction, dedicated Auth0 deployment model for enhanced performance, security, and compliance over our standard public cloud offering".
- **Adaptive MFA**: "designed to only be triggered when a login is suspected to be risky via different risk profiles".
- **Machine-to-Machine Tokens**: precisa que "M2M add-ons are also available on Professional self-service plans" (ver [[2026-1101-auth0-m2m-tokens-5k-incluidos-en-professional]]).
- **Highly Regulated Identity**: "Financial Grade Identity™ controls (Strong Customer Authentication, FAPI protocols) and Customer Managed Keys".
- **Advanced Extensibility**: "leverage the maximum number of Actions and Forms (within platform performance limits)" — el techo de Actions/Forms es del plan, no del add-on (ver [[2026-1101-auth0-cuotas-de-actions-forms-y-token-vault]]).
- **HIPAA BAA & PCI**: sin cambios.

Ninguno de los nueve publica precio: la frontera de coste no cuantificable que describe este átomo se mantiene (ver [[2026-1101-auth0-enterprise-contact-us-sla-y-30-dias-de-logs]]).

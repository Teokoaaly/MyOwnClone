---
id: 2026-1027-proton-business-vpn-sso-con-cualquier-saml-2-0-pero-scim-solo-okta-y-entra
type: atom
certainty: solid
sources: [sources/2026-10-26-proton-business-vpn-overview.md]
links: ["[[2026-1027-proton-business-vpn-professional-anade-sso-scim-ips-dedicadas-y-sentinel]]", "[[2026-1027-proton-business-workspace-standard-no-incluye-sso-ni-scim-en-la-tabla]]", "[[2026-1024-protonvpn-plus-incluye-planes-free-de-mail-drive-y-pass]]"]
---

## Claim
La página de producto B2B separa dos capacidades que la tabla de precios trata como una sola: **SSO** admite "**Okta, Google Workspace, Microsoft Entra ID, or any SAML 2.0 provider** so your team logs in with credentials they already use", mientras que **SCIM** queda limitado a dos proveedores: "Automate provisioning through **Okta or Microsoft Entra ID** so access is granted and revoked automatically". En cambio, el **MDM** sí enumera seis: "**Intune, Jamf, Workspace One, Google Workspace, FleetDM, or Samsung Knox**".

## Why It Matters
La asimetría es el dato: **autenticarse federado es genérico (cualquier SAML 2.0), pero aprovisionar y revocar usuarios automáticamente solo funciona con dos IdP concretos**. Es decir, **el proveedor no da el ciclo completo de identidad en el bundle**: el alta y el login se automatizan para todos, pero el **alta y la baja de las licencias** —la operación que de verdad cuesta dinero y que un producto multi-tenant necesita para revocar el acceso de un tenant que se va— solo está automatizada para Okta y Entra. Google Workspace aparece en SSO y en MDM pero **no en SCIM**. Para el vault esto define qué se puede delegar a un proveedor y qué hay que construir: **el motor de revocación es la pieza que Proton no cubre de forma genérica**, y es la que en un producto multi-tenant con tenants que se van es la que evita pagar licencias muertas ([[2026-1024-protonvpn-plus-incluye-planes-free-de-mail-drive-y-pass]]).

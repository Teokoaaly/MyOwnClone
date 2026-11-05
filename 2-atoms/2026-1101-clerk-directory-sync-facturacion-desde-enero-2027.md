---
id: 2026-1101-clerk-directory-sync-facturacion-desde-enero-2027
type: atom
certainty: solid
sources: [sources/2026-11-01-clerk-pricing.md]
links: ["[[2026-1101-clerk-sso-adicional-desde-75-por-conexion]]", "[[2026-1101-auth0-sso-scim-en-free-pero-no-en-essentials-b2c]]", "[[2026-1102-auth0-precios-sin-cambios-en-48-horas]]"]
---

## Claim
El **Directory Sync** de Clerk (aprovisionamiento/desaprovisionamiento de usuarios vía SCIM o Google Workspace) se factura **por separado de las conexiones SSO**, con la **misma escalera de precios** (1 incluida en Pro/Business; 2–15 a $75/mes; 16–100 a $60; 101–250 a $48; 251+ contacto), y **el cobro de Directory Sync empieza el 1 de enero de 2027** ("Billing for Directory Sync connections starts January 1, 2027").

## Why It Matters
Dos consecuencias practices. Primera, la **fecha de arranque del cobro**: hoy una conexión de Directory Sync es gratis de facto y a partir del 01-01-2027 se factura como el SSO, lo que significa que un presupuesto calculado hoy (noviembre 2026) puede quedar corto en tres meses sin ningún cambio de uso — hay que fechar la decisión con esa fecha en el horizonte. Segunda, el **contaje separado** significa que un cliente que quiere SSO *y* SCIM paga dos veces, exactamente el punto que el vault ya marqué como fricción de proveedor en Proton ([[2026-1027-proton-business-vpn-sso-con-cualquier-saml-2-0-pero-scim-solo-okta-y-entra]]) y que Auth0 resolvió metiendo SSO y SCIM en el Free pero degradándolos al subir de plan ([[2026-1101-auth0-sso-scim-en-free-pero-no-en-essentials-b2c]]). Para MyOwnClone, el SCIM solo se justifica si hay clientes corporativos con varios empleados por tenant; mientras no los haya, es una línea que puede esperar.

## Nota de verificación
Fila "Directory Sync connections" de la tabla "Full price breakdown" y bullet "Additional $75/mo each from January 1, 2027" de la tarjeta Pro, ambos verbatim de la captura del 2026-11-01.

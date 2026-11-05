---
id: 2026-1101-auth0-cuotas-de-actions-forms-y-token-vault
type: atom
certainty: solid
sources: [sources/2026-11-01-auth0-pricing.md]
links: ["[[2026-1101-auth0-numero-de-tenants-por-plan]]", "[[2026-1101-auth0-addon-agentes-ai-suma-50-por-ciento]]", "[[2026-1022-arquitectura-rac-tres-modos-por-clon]]"]
---

## Claim
Auth0 limita por plan la capacidad de personalizar y de emitir credenciales: **Actions + Forms** son 5 (Free), 10 (Essentials), 15 (Professional) y 30 (Enterprise, "30 + ADD-ON"); los **Event Streams** son 1, 3, 4 y 8; y el **Token Vault** —el almacén de tokens para agentes— es 2 (Free), "3 + ADD-ON" (Essentials), "3 + ADD-ON" (Professional) y "4 + ADD-ON" (Enterprise). La CIBA está "Not available" en Free y es ADD-ON en Essentials y Professional.

## Why It Matters
Estos son los límites que se tocan **antes** que los precios: un producto multi-tenant que necesita un flujo de onboarding propio por cliente (Actions/Forms), o que emite tokens para integraciones (Token Vault), tiene un techo de personalización que escala con el plan y no con el número de tenants. En el plan Free de $0 —el único que cabe en el presupuesto de ≤ €4/mes— hay 5 Actions, 1 Event Stream, 2 tokens en Token Vault y ninguna CIBA. Para MyOwnClone, cuyo producto es un clon de IA con memoria por tenant ([[2026-1022-arquitectura-rac-tres-modos-por-clon]]), la lectura es que el plan Free alcanza para autenticar pero no para personalizar por tenant: cualquier lógica de negocio en el flujo de login (por ejemplo, asociar el usuario a su organization) consume Actions, y el vault lo implica en la decisión de qué proveedor de identidad usar.

## Nota de verificación
Filas "Actions + Forms", "[Event Streams]" y "Token Vault" leídas literalmente del feature matrix del 2026-11-01 (idénticas en B2C y B2B).

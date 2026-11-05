---
id: 2026-1103-auth0-workflows-agentes-ai-incluidos-en-plan-free
type: atom
certainty: solid
sources: [sources/2026-11-03-auth0-pricing.md]
links: ["[[2026-1101-auth0-plan-free-25000-mau-sin-tarjeta]]", "[[2026-1101-auth0-addon-agentes-ai-suma-50-por-ciento]]", "[[2026-1101-auth0-cuotas-de-actions-forms-y-token-vault]]", "[[2026-1023-ai-security-tools-agente-como-categoria-dominante]]"]
---

## Claim
El plan **Free de Auth0 ($0/mes)** incluye, según su tarjeta de plan, "**Secure Agentic AI workflows**" como feature incluida, junto a Passwordless Authentication, Unlimited Social Connections, Basic Attack Protection y Brand Customization.

## Why It Matters
Es un matiz que separa dos cosas que el vault tenía mezcladas. Existe un add-on "Auth0 for AI Agents" que cuesta **+50 % del precio base** ([[2026-1101-auth0-addon-agentes-ai-suma-50-por-ciento]]), y a la vez el plan gratuito incluye workflows agénticos. La lectura correcta es que "secure agentic AI workflows" (el flujo de login de un agente: credenciales delegadas, confirmación humana, scopes) **no es lo mismo** que el add-on de AI Agents (Token Vault ilimitado y CIBA, que sí se cobran). Consecuencia práctica para MyOwnClone: permitir que un tenant conecte su agente al producto puede no requerir el add-on de pago, sino solo el hecho de no exceder los límites de Actions/Forms y Token Vault del plan — 5 Actions, 2 tokens de Token Vault y **CIBA no disponible en Free** ([[2026-1101-auth0-cuotas-de-actions-forms-y-token-vault]]). Es decir, el límite real del plan gratuito para agentes no es el precio del add-on, es la ausencia de CIBA. Esto encaja con la lectura del vault de que la capa de identidad de agentes es la que se está pagando ([[2026-1023-ai-security-tools-agente-como-categoria-dominante]]).

## Nota de verificación
"Secure Agentic AI workflows" es lectura literal de la tarjeta del plan Free en `sources/2026-11-03-auth0-pricing.md`. La distinción entre ese feature y el add-on "Auth0 for AI Agents" es interpretación de este átomo: la fuente no enumera qué incluye exactamente cada uno.

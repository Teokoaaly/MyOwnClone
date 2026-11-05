---
id: 2026-1101-clerk-enterprise-precio-custom-y-sla-9999
type: atom
certainty: solid
sources: [sources/2026-11-01-clerk-pricing.md]
links: ["[[2026-1101-clerk-precios-base-hobby-pro-business]]", "[[2026-1101-auth0-enterprise-contact-us-sla-y-30-dias-de-logs]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
El plan **Enterprise de Clerk tiene precio "Custom", se factura solo anualmente** y añade **descuentos por uso comprometido anual, SLA de 99,99% de uptime, soporte premium con account manager técnico dedicado y SLA de tiempo de respuesta, canal de Slack dedicado, retención de logs customizable, destinos de log sink hacia el SIEM, HIPAA con BAA, onboarding y migración "white-glove" y cuestionarios de seguridad custom**. Ninguna cifra de precio es pública; el acceso es por "Talk to sales".

## Why It Matters
Es la misma estructura de precio que el Enterprise de Auth0 ([[2026-1101-auth0-enterprise-contact-us-sla-y-30-dias-de-logs]]) y cierra el patrón de los tres proveedores de identidad del vault: **Clerk y Auth0 tienen tramo gratuito + tramo de pago + tramo "custom" sin publicar; WorkOS es híbrido por producto**. Para MyOwnClone, la lectura práctica es que **la franja Enterprise no es una opción de presupuesto** — es el escenario "un cliente corporativo exige SLA, HIPAA o SSO de workspace y hay que negociarlo" — y por tanto **la decisión de qué proveedor usar no puede posponerse a ese cliente**: hay que elegir Clerk, Auth0 o librería propia antes, porque la configuración que habilita el Enterprise (SSO de workspace, logs a SIEM, BAA) no es retro-compatible con "cambiar de proveedor en el momento del deal". Y en el eje del vault, este tramo es donde el **coste por asiento deja de ser medible** (precio custom) y solo se puede acotar por negotiation.

## Nota de verificación
Tarjeta "Enterprise" de la sección "Plans for every stage" de la captura del 2026-11-01, verbatim. La comparación con el tramo Enterprise de Auth0 y con el presupuesto del vault es lectura operativa de este átomo.

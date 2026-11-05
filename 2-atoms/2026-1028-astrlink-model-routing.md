---
id: 2026-1028-astrlink-model-routing
type: atom
certainty: solid
sources: [sources/2026-10-28-astrlink-github.md]
links: ["[[2026-1028-astrlink-on-device-privacy]]", "[[2026-1028-astrlink-unified-subscriptions]]"]
---

## Claim

AstrLink provides model routing with provider priorities, model name redirects, and configurable retries and failover between providers, selecting providers that support the target model and request protocol.

## Why It Matters

Agents can specify a model name without needing to know which provider supports it. The gateway routes the request to the highest-priority available provider, with automatic retry on failure and failover to secondary providers. This enables model diversity and resilience without agent-level configuration changes.

## [FRICTION]

> [[2026-1023-new-api-escala-adopcion-y-traduccion]] establece que New API tiene 8 canales "New API" en el ranking de PriceAI y que son el camino estándar y no una excentricidad. Este átomo presiona la creencia de que el routing automático entre proveedores siempre selecciona la mejor opción: New API's 8 canales tienen una curva de adopción institucional que el routing automático de AstrLink no contempla —el gateway selecciona por compatibilidad de protocolo y disponibilidad de modelo, no por endorsements institucionales o acuerdos de nivel de servicio. Las dos lecturas pueden coexistir —routing proporciona flexibilidad técnica, mientras que la penetración institucional determina qué proveedores son viables en entornos corporativos— pero la creencia de que el routing solo resuelve el problema técnico ignora la dimensión operativa de compliance y licensing que New API's partners introducen. No hay contradicción técnica, pero sí fricción en la suposición de que routing técnico = viabilidad operativa completa.
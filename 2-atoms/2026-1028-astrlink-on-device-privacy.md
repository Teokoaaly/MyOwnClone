---
id: 2026-1028-astrlink-on-device-privacy
type: atom
certainty: solid
sources: [sources/2026-10-28-astrlink-github.md]
links: ["[[2026-1028-astrlink-unified-subscriptions]]", "[[2026-1028-astrlink-model-routing]]"]
---

## Claim

AstrLink detects sensitive content locally before it reaches any model provider: secrets, email addresses, and phone numbers are identified using built-in rules or a local privacy model, then redacted or blocked according to configured policies.

## Why It Matters

All request bodies pass through the local privacy pipeline first, so no sensitive content is accidentally sent upstream. Redacted values can be restored locally in responses, letting agents continue working without exposing credentials. This eliminates an entire class of data leakage incidents that affect agents that forward raw request bodies to providers.

## [FRICTION]

> [[2026-1027-quackr-private-number]] afirma que los números Private son no-VoIP y SMS ilimitados a $14.99/mo para cualquier app/website. Este átomo presiona esa creencia porque AstrLink's on-device detection opera sobre patrones de expresiones regulares y categorías de política configurables, no sobre la provisión de números de teléfono. La detección local identifica qué contenido está secretado; no provee alternativas de comunicación. Ambas no pueden ser completamente correctas: la privacidad de AstrLink cubre el redactado en tránsito, pero no resuelve el problema de autenticación por número de teléfono que Quackr aborda. Marcado para juicio humano, no auto-resuelto.
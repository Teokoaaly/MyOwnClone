---
id: 2026-10-27-gmail-api-certificates
type: atom
certainty: solid
sources: [sources/2026-10-27-gmail-api-overview.md]
links: ["[[2026-10-27-gmail-api-aliases]]", "[[2026-10-27-gmail-api-push]]"]
---

## Claim
S/MIME certificates are digital certificates uploaded to specific send-as aliases that let you send encrypted and digitally signed emails, ensuring message security and sender authenticity.

## Why It Matters
S/MIME support in the Gmail API enables organizations to enforce email encryption and sender verification for compliance, legal, or security requirements beyond TLS-in-transit.

## [FRICTION]
> [[2026-10-27-gmail-api-aliases]] (escrita hoy) afirma que las certificates solo aplican a aliases de envío. Esta nota presiona eso porque las certificates también podrían subirse a la dirección primaria, aunque la práctica recomienda los aliases. Ambas pueden ser completamente correctas. Marcado para juicio humano, no auto-resuelto.
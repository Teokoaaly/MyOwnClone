---
id: 2026-10-27-gmail-api-aliases
type: atom
certainty: solid
sources: [sources/2026-10-27-gmail-api-overview.md]
links: ["[[2026-10-27-gmail-api-forwarding]]", "[[2026-10-27-gmail-api-certificates]]"]
---

## Claim
Send-as aliases represent the various email addresses from which an account is authorized to send mail; every account has at least one alias representing the primary email address, and aliases correspond to the "Send mail as" feature in the Gmail web interface and are the basis for configuring per-address email signatures.

## Why It Matters
Aliases allow a single Gmail account to send mail from multiple apparent addresses, enabling organizational signature consistency and per-address routing without needing separate accounts.

## [FRICTION]
> [[2026-10-27-gmail-api-forwarding]] (escrita hoy) afirma que las aliases son addresses de reenvío. Esta nota presiona eso porque las aliases son para enviar "como" mientras que el reenvío direcciona copias, pero ambos usan la misma infraestructura de verified addresses. Ambas pueden ser completamente correctas. Marcado para juicio humano, no auto-resuelto.
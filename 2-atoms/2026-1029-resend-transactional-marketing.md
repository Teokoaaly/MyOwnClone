---
id: 2026-1029-resend-transactional-marketing
type: atom
certainty: solid
sources: [sources/2026-10-29-resend-pricing.md]
links: ["[[2026-1029-resend-free-plan]]", "[[2026-1029-resend-pro-plan]]"]
---

## Claim

Resend distinguishes transactional emails (sent via /emails API, triggered by user actions) from marketing emails (sent via /broadcasts API or dashboard, sent to existing contacts only), with different quota implications and unsubscribe handling.

## Why It Matters

The transactional vs marketing distinction affects quota counting and compliance. Transactional emails sent via /emails API count against the plan's monthly quota (3K Free, 50K Pro, 100K Scale), while marketing broadcasts sent via /broadcasts API count against contacts, not email limits — meaning a plan's email quota is irrelevant for broadcast-heavy use cases with large contact lists but low per-contact volume. For newsletters or promotional campaigns, the Broadcasts interface handles unsubscribe links automatically via the {{{RESEND_UNSUBSCRIBE_URL}}} placeholder, whereas /emails API sends require the sender to manage List-Unsubscribe and List-Unsubscribe-Post headers plus a visible unsubscribe link. Teams building newsletters should use Broadcasts to avoid counting emails against their transactional quota; teams sending password resets or order confirmations should use /emails API to keep broadcast counts separate. Misusing the API can lead to unexpected quota exhaustion, especially on lower tiers.

## [FRICTION]

> No conflicting atom found. This is a foundational clarification atom with no direct contradiction in the current vault. No [FRICTION] block added.

## Nota de extensión 2026-11-03
Verificado contra `sources/2026-10-29-resend-pricing.md`: el claim es correcto en sus tres partes —/emails API para transaccionales, /broadcasts o la interfaz Broadcasts para marketing, y los broadcasts solo pueden enviarse a contactos existentes mientras que los transaccionales a cualquier dirección.

Matices de la misma captura que refuerzan el modelo de cuota: los emails enviados por /emails API **sí** cuentan contra la cuota transaccional y cada destinatario cuenta como un email, mientras que los broadcasts cuentan contra los contactos; el envío de newsletters por /emails API es legal pero obliga al remitente a gestionar su propio enlace de baja visible más las cabeceras List-Unsubscribe y List-Unsubscribe-Post, responsabilidad que Broadcasts resuelve con el placeholder {{{RESEND_UNSUBSCRIBE_URL}}}; y "unlimited broadcast sending" significa que los planes de marketing no están limitados por número de emails sino por número de contactos. Detalle del tracking en [[2026-1029-resend-tracking-por-dominio]].
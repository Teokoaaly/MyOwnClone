---
id: 2026-1022-modulo-brain-cerebro-memorias-plantillas
type: atom
certainty: solid
sources: [raw/articles/myownclone-new-findings-may-2026.md]
links: ["[[2026-1022-arquitectura-rac-tres-modos-por-clon]]", "[[2026-1022-email-inbound-contacto-sin-dominio-propio]]", "[[2026-1022-mapa-modulos-internos-desde-bundles-js]]", "[[myownclone]]"]
---
## Claim
El módulo `Brain` de la app del creador de [[myownclone]] es un CRUD de **memorias** más firma de email, plantillas, dominios de spam y dominio inbound: es decir, la superficie donde el creator configura no solo lo que el clon sabe, sino cómo se presenta (firma), cómo reutiliza respuestas (plantillas) y qué mensajes acepta (dominio inbound).

## Why It Matters
Separa dos cosas que en el RAC se confundían: el corpus (lo que se indexa y se retrieve) frente a la **configuración operativa del canal** (firma, plantillas, dominio). Que el dominio inbound esté en el mismo módulo que las memorias sugiere que la capacidad está diseñada aunque no esté activada por tenant — es la diferencia entre "no existe" y "existe en el panel" (ver [[2026-1022-email-inbound-contacto-sin-dominio-propio]]). Además, las memorias editables a mano son la palanca manual sobre el retrieval que describe [[2026-1022-arquitectura-rac-tres-modos-por-clon]]: el creator puede corregir lo que el clon recorda sin reentrenar nada.

## [FRICTION]
> [[2026-1022-email-inbound-contacto-sin-dominio-propio]] (escrita hace ~21 semanas) afirma que el soporte de dominios inbound propios por tenant aparece explícitamente como "Coming soon" y que el único destinatario es `contacto@myownclone.com`.
> Este átomo presiona esa creencia porque el módulo `Brain` incluye el "dominio inbound" entre sus capacidades, es decir, la función está implementada en la app del creador aunque se anuncie como no disponible.
> Ambas no pueden ser completamente correctas: o el control existe en la UI pero la provisión técnica está bloqueada, o la funcionalidad está ya operativa y el estado real es "Coming soon" solo en la web pública. Marcado para juicio humano, no auto-resuelto.

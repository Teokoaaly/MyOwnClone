---
id: 2026-1024-extravm-sin-garantia-legal-de-uptime-solo-creditos
type: atom
certainty: solid
sources: [sources/2026-10-23-extravm-vps-pricing.md]
links: ["[[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]]", "[[2026-1024-evoxt-sla-99-99-y-despliegue-en-2-5-minutos]]", "[[2026-1024-hostbrr-sla-99-9-y-garantia-de-devolucion-30-y-7-dias]]"]
---

## Claim
ExtraVM declara que **no tiene garantía legal de uptime**: "We don't have a legal uptime guarantee, as we believe many provider SLAs are deceiving and for marketing. In the event of excessive downtime due to hardware or network issues, we always credit customers affected." En su lugar afirma que "most offering 99.99% uptime guarantees" — pero se refiere a **las facilities** (Equinix, Digital Realty, Evocative), no a su propio servicio. La página también afirma "Enterprise Uptime: Redundant infrastructure and premium network providers deliver exceptional reliability" como beneficio de marketing.

## Why It Matters
Es la **posición más explícita del vault contra el SLA como categoría de valor**, y por eso mismo es el contrapunto exacto del átomo de Hetzner ([[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]]), donde el SLA con créditos y las certificaciones son la diferencia que el vault identificó como el sobrecoste real de lo barato. ExtraVM **rechaza ese marco de forma declarada**: no da SLA, da créditos discrecionales por downtime, y su 99.99 % viene del proveedor del edificio. Comparado con Evoxt, que vende "99.99% Uptime" sin SLA ([[2026-1024-evoxt-sla-99-99-y-despliegue-en-2-5-minutos]]), y con HostBrr ([[2026-1024-hostbrr-sla-99-9-y-garantia-de-devolucion-30-y-7-dias]]), el patrón del mercado queda claro: **la cifra de uptime es commodity y el SLA auditable es lo que no se publica** — ahora confirmado desde el lado que se niega a tener SLA. Para MyOwnClone, que hoy sirve desde un nginx autoalojado sin SLA (Best Effort), esto define el suelo de garantizability del autoalojado: incluso el proveedor que se posiciona como "enterprise-grade" no lo formaliza.

## [FRICTION]
> [[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]] (escrita hace 1 día) afirma que "la diferencia entre proveedores de hosting en el vault no es la cifra de uptime sino la existencia de un SLA con créditos y certificaciones auditables" y presenta el SLA de Hetzner como el criterio de sustitución de un hosting sin garantía.
> Este átomo presiona esa creencia en un punto: **hay proveedores del mismo rango de precio que rechazan el marco por principio**, no por omisión. ExtraVM no es "SLA no publicado por forgetfulness": declara activamente que los SLAs son "deceiving and for marketing" y sustituye la garantía por créditos discrecionales. Eso significa que el criterio "SLA auditable" no es solo un requisito de compliance, sino una **diferenciación de ideological/provider posture**: se puede querer SLA o querer que no exista.
> Ambas no pueden ser completamente correctas en su lectura fuerte: o el SLA con créditos es siempre un valor para el cliente (y entonces un proveedor que lo niega de forma explícita queda objetivamente peor), o la garantía legal tampoco aporta tanto como la nota sugiere y el criterio real es precio + capacidad de fuss. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
La captura no publica los importes de crédito, el umbral de "excessive downtime", ni qué facilities ofrecen los 99.99 % declarados.

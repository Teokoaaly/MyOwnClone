---
id: 2026-1029-postmark-free-tier
type: atom
certainty: solid
sources: [sources/2026-10-29-postmark-pricing.md]
links: ["[[2026-1022-sin-pagina-precios-ni-docs]]", "[[myownclone]]"]
---

## Claim
El plan Free de Postmark cuesta $0.00/mo e incluye 100 emails/month, pero **no se permiten overages** en este plan — cualquier envío adicional queda bloqueado, no hay vía de pago para excedentes.

## Why It Matters
La ausencia de overages en el plan Free crea un discontinuo extremo: pasar de 100 emails/month a cualquier volumen superior requiere saltar al plan Basic ($15/mo, 10,000 mínimo). Esta barrera de entrada abrupta distingue a Postmark de servicios que permiten pagos por uso desde planes bajos, y refleja la posición de Postmark como producto de "correo transaccional de calidad" más que de utilidad de bajo costo. El efecto es que desarrolladores y proyectoslaterales con volumen variable deben comprometerse a un plan pagado completo desde el inicio, o arriesgarse a que sus emails se silencien sin aviso.

## [FRICTION]
> [[2026-1022-sin-pagina-precios-ni-docs]] (escrita hace ~21 semanas) afirma que [[myownclone]] no publica precios ni documentación pública, y todos los endpoints devuelven 404. Este átomo presiona que Postmark sí publica precios estructurados y transparentes —a diferencia de myownclone, Postmark tiene una página de pricing completa con planes y overages visibles. Ambas pueden ser correctas en sus dominios respectivos: Postmark exhibe precios abiertos mientras myownclone los oculta, pero ambas estrategias refuerzan la necesidad de verificacion contractual antes de comprometerse. Marcado para juicio humano, no auto-resuelto.
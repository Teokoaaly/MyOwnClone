---
id: 2026-1029-resend-rate-limit-por-equipo
type: atom
certainty: solid
sources: [sources/2026-10-29-resend-pricing.md]
links: ["[[2026-1029-resend-pro-plan]]", "[[2026-1029-resend-scale-plan]]", "[[2026-1029-resend-transactional-marketing]]"]
---

## Claim
El límite de API de Resend (requests por segundo) se fija por equipo y es idéntico en todos los planes, incluidos Enterprise: subir de plan no lo aumenta; la Batch Email API envía hasta 100 emails por request y cada request de batch cuenta como uno solo contra el límite, y solo soporte puede revisar un límite superior.

## Why It Matters
Este es el límite que no se compra con dinero: a diferencia del volumen de emails, del número de dominios o de los créditos de IA —todo lo cual mejora al subir de plan (ver [[2026-1029-resend-pro-plan]] y [[2026-1029-resend-scale-plan]])— el techo de requests por segundo es el mismo en Free y en Enterprise. Para MyOwnClone significa que un pico de onboarding (muchos tenants activándose a la vez, cada uno con su email de bienvenida) no se resuelve pagando: se resuelve con batching, y la propia documentación señala el Batch Email API como la palanca, con 100 emails por request. Es un recordatorio del eje del vault: el coste por asiento no es la única restricción — hay capacidades que no escalan con el presupuesto sino con la arquitectura del cliente.

## [FRICTION]
> No conflicting atom found. This is a rate-limit atom with no direct contradiction in the current vault. No [FRICTION] block added.

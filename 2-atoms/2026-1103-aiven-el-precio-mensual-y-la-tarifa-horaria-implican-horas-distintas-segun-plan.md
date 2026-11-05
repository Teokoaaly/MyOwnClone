---
id: 2026-1103-aiven-el-precio-mensual-y-la-tarifa-horaria-implican-horas-distintas-segun-plan
type: atom
certainty: tentative
sources: [sources/2026-11-03-aiven-pricing.md]
links: ["[[2026-1102-aiven-escalera-de-precios-postgresql-de-0-a-270-dolares]]", "[[2026-1102-aiven-factura-por-hora-facturada-al-mes-y-solo-cambia-si-cambias-algo]]", "[[2026-1102-aiven-disponibilidad-de-nube-y-region-por-plan]]"]
---

## Claim
Al dividir el precio mensual "starting from" entre la tarifa horaria publicada, **cada plan implica un número de horas mensual distinto**: Hobbyist $12 / $0,02 = **600 h**, Startup $75 / $0,10 = **750 h**, Business $180 / $0,25 = **720 h**, Premium $270 / $0,37 ≈ **730 h**. El plan Developer ($5/mes) no publica tarifa horaria. Ninguno de los cuatro resultados coincide con un mes natural (730–744 h) y el de Hobbyist se aparta bastante (600 h).

## Why It Matters
La página declara dos precios a la vez sin explicar la relación entre ellos ([[2026-1102-aiven-escalera-de-precios-postgresql-de-0-a-270-dolares]]), y la aritmética sugiere que **el precio mensual es un ancla comercial, no el producto de la tarifa horaria × horas de uso**: el mismo servicio costaría $12/mes o $0,02/h según cómo se mire, y no son equivalentes. Esto matiza el titular de "facturado por la hora, facturado al mes" de [[2026-1102-aiven-factura-por-hora-facturada-al-mes-y-solo-cambia-si-cambias-algo]]: la factura real depende de un número de horas de referencia que Aiven no publica, y ese número varía por plan. Para el modelo de coste del vault la consecuencia práctica es que **el compromiso mensual nunca se puede derivar de la tarifa horaria**, solo al revés; hay que tomar el "starting from" como el número contractual y no hacer conversiones.

## [FRICTION]
> [[2026-1102-aiven-factura-por-hora-facturada-al-mes-y-solo-cambia-si-cambias-algo]] afirma que "Services are billed by the hour and invoiced monthly, so you only pay for what you actually run", lo que sugiere que el coste mensual es derivable de la tarifa horaria. Esta nota presiona esa lectura porque los dos precios publicados no son consistentes entre planes ni con un mes natural (600 h frente a 720–750 h), de modo que "billed by the hour" y "starting from $X/month" no describen la misma magnitud. Ambas no pueden ser completamente correctas: o el mensual es un redondeo comercial de un mismo underlying rate con un mínimo de compromiso distinto por plan, o la facturación por hora usa una base de horas que la página no documenta. Marcado para juicio humano, no auto-resuelto.

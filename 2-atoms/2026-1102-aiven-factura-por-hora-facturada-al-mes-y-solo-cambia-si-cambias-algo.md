---
id: 2026-1102-aiven-factura-por-hora-facturada-al-mes-y-solo-cambia-si-cambias-algo
type: atom
certainty: solid
sources: [sources/2026-11-02-aiven-postgresql-pricing.md, sources/2026-11-03-aiven-pricing.md]
links: ["[[2026-1031-aiven-postgresql-pricing]]", "[[2026-1102-aiven-escalera-de-precios-postgresql-de-0-a-270-dolares]]", "[[2026-1029-upstash-command-billing]]"]
---

## Claim
Aiven factura **por hora** y **factura mensualmente**: "Services are billed by the hour and invoiced monthly, so you only pay for what you actually run". La tarifa horaria incluye el servicio gestionado, la infraestructura cloud subyacente, el aprovisionamiento, el monitorizado, los backups locales, los upgrades de versión, el parcheo de seguridad y las operaciones de fiabilidad 24/7, y **no hay partidas separadas** ni para alta disponibilidad ni para mantenimiento rutinario: "What you see on the plan card is what you pay". La factura solo cambia cuando cambias algo: plan más grande, almacenamiento extra, servicios adicionales, tier de soporte upgraded o BYOC.

## Why It Matters
Es la definición operativa de "coste fijo predecible" que el vault necesita para el modelo multi-tenant: el gasto de infraestructura es una constante mensual que **no escala con los tenants** mientras estos no crezcan de uso — a diferencia del coste por comando o por request que [[2026-1029-upstash-command-billing]] registra para Redis gestionado. La regla práctica que sale de aquí: añadir un tenant a MyOwnClone sobre Aiven no añade euros, y por tanto el margen bruto por asiento es el mismo para el tenant número 1 y para el número 1.000 — la única variable que rompe la previsibilidad es el almacenamiento dinámico (ver [[2026-1102-aiven-disco-dinamico-cuesta-dinero-extra-desde-startup]]).

## 2026-11-03 — re-verificación
La FAQ de la captura del 2026-11-03 repite literalmente la misma formulación: "Services are billed by the hour and invoiced monthly, so you only pay for what you actually run" y "Your bill changes only when you change something", con la misma enumeración de motivos de cambio (plan más grande, almacenamiento extra, servicios adicionales, tier de soporte, BYOC). Matiz nuevo de esta versión: la FAQ **"How does Aiven pricing compare to similar services offered by hyperscalers?"** devuelve **el mismo párrafo completo** que la FAQ de "How does Aiven pricing work?", lo que confirma que la página repite su bloque argumental en dos preguntas distintas. La objeción de que el mensual y la tarifa horaria no encajan entre sí se registra en [[2026-1103-aiven-el-precio-mensual-y-la-tarifa-horaria-implican-horas-distintas-segun-plan]].

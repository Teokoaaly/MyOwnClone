---
id: 2026-1026-heroku-eco-5-dolares-con-pool-de-1000-horas-compartidas
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-dyno-sizes.md]
links: ["[[2026-1026-heroku-suelo-5-dolares-eco-con-sleep-y-7-dolares-basic-always-on]]", "[[2026-1023-hetzner-facturacion-por-hora-0-0096]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]"]
---

## Claim
El plan **Eco** de Cedar cuesta **$5 flat** de suscripción mensual que "**covers a pool of 1000 hours shared by all Eco dynos in an account**", y la tabla lo marca con **0.5 GB de RAM, CPU Share 1x, Compute 1x-4x, "Dyno Units Consumed: N/A", "Dedicated: No"** y **"Sleeps" ✔** — es decir, **el único plan de la tabla con la columna Sleeps marcada** y **el único cuyo precio no se mide en Dyno Units**. Eco además "**are not available for Heroku Enterprise customers**". El resto de la tabla se cobra por uso: "**Heroku charges for dynos based on usage, except for the Eco Dynos Plan**".

## Why It Matters
Es el único punto del catálogo donde el **coste no escala con el runtime**: $5 pagan 1000 horas de *pool compartido por toda la cuenta*, no por dyno. Como un dyno siempre encendido consume ~720 h/mes, el pool cubre **1,39 dynos always-on** y el resto de horas se gasta en dynos adicionales o en picos — el coste marginal de un segundo dyno Eco es $0 hasta agotar el pool, y después es el corte. Es la diferencia estructural con el tramo VPS del vault, donde cada servidor tiene su propia factura ([[2026-1024-lowendbox-2-usd-racknerd-2gb-doble-vcpu-20-98]]) y con la facturación por hora de Hetzner ([[2026-1023-hetzner-facturacion-por-hora-0-0096]]), que es un tercer modelo: ni suscripción ni pool, sino €/hora.
Para el stack vivo ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) la consecuencia es que **"always on" ya no es gratis por dormir**: el eco dormido es el único modo de tener el proceso despierto sin pagar el mes entero, y a cambio se pierde la continuidad — el acceso se hace con la app en reposo, no con un nginx sirviendo.

## [FRICTION]
> [[2026-1026-heroku-suelo-5-dolares-eco-con-sleep-y-7-dolares-basic-always-on]] afirma, transcribiendo la tabla de la página de precios de Heroku, que el plan Eco está limitado a "**Personal accounts only**", y a partir de ahí calcula un "**suelo de un stack PaaS completo**" de **$13/mes** (compute Eco $5 + Postgres Essential $5 + Key-Value Mini $3).
> Este átomo presiona ese cálculo con la redacción de la página de specs: "**Eco dynos are not available for Heroku Enterprise customers**". Las dos restricciones **no son la misma**: "personal accounts only" (captura de precios) dice que **la cuenta debe ser personal**; "not available for Heroku Enterprise customers" (captura de specs) dice que **el cliente Enterprise no puede comprar Eco** — un cliente que usa una cuenta de equipo o de empresa sin ser Enterprise **queda fuera del primer caso y dentro del segundo**.
> Ambas no pueden ser simultáneamente la misma regla: o las dos frases significan lo mismo y la captura de precios está mal transcrita, o son restricciones distintas y entonces **el suelo de $13/mes no es aplicable a una empresa** —el mínimo real para una cuenta de negocio sería **$15/mes** (Basic $7 + Postgres Essential $5 + Key-Value Mini $3), porque el dyno always-on de $7 es el más barato que un cliente no-personal puede comprar. Marcado para juicio humano, no auto-resuelto: la fuente no define "Personal account" ni el alcance de "Heroku Enterprise customers".

## Nota de verificación
El pool de 1000 horas es el texto de la nota al pie de la tabla ("Eco dynos require a $5 flat fee monthly subscription that covers a pool of 1000 hours shared by all Eco dynos in an account"). El cociente 1,39 dynos always-on (1000 h ÷ 720 h) es **cálculo de este átomo**: la fuente no publica horas por dyno ni qué pasa al agotar el pool. El detalle de "sleeps after 30 minutes of inactivity" y el "Personal accounts only" vienen de la captura hermana de precios, no de esta ([[2026-1026-heroku-suelo-5-dolares-eco-con-sleep-y-7-dolares-basic-always-on]]).

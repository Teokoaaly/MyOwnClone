---
id: 2026-1024-alexhost-garantia-de-dinero-devuelto-30-dias
type: atom
certainty: solid
sources: [sources/2026-10-24-alexhost-home.md]
links: ["[[2026-1024-alexhost-dos-cifras-de-ddos-y-dos-de-ancho-de-banda]]", "[[2026-1024-proton-30-dias-de-dinero-devuelto-y-cambio-de-plan-con-credito-prorrateado]]", "[[2026-1024-hostbrr-sla-99-9-y-garantia-de-devolucion-30-y-7-dias]]", "[[2026-1024-alexhost-superficie-legal-dpa-y-terminos-publicados]]", "[[2026-1024-alexhost-dos-metodos-de-pago-cripto-sin-nombre-de-moneda]]"]
---

## Claim
La home de AlexHost publica **cinco claims de garantía y servicio**, todos como texto de marketing y ninguno como documento: **"30-Day Money-Back Guarantee"** (aparece dos veces: como badge con icono `money.svg` y en el párrafo de servicios, con el texto *"AlexHost offers a 30-day money-back guarantee for any of the listed services"*), **"Support tickets 24/7"** (también dos veces: badge y bloque de ventajas), **"Live chat (business hours)"**, **"40000+ Happy Customers"** y **"Founded 2008"**. El detalle fino es que la garantía **cubre "any of the listed services"** —el mismo párrafo enumera "hosting, VPS, dedicated servers, or security certificates" como los productos con soporte post-venta— pero la captura **no publica condiciones**: ni exclusiones, ni si el reembolso es en dinero o en crédito, ni si el pago en criptomoneda queda excluido (que es la regla de HostBrr y ExtraVM en este mismo thread, [[2026-1024-hostbrr-sla-99-9-y-garantia-de-devolucion-30-y-7-dias]] y [[2026-1024-extravm-sin-reembolso-en-pagos-cripto]]), ni si existe periodo de prueba previo en los dedicados de 26 € a 408 €. El bloque de ventajas añade un claim de rendimiento sin metodología: **"High order processing speed — 20% faster than competitors"**.

## Why It Matters
Una **garantía de 30 días sin condiciones publicadas es más fuerte en apariencia y más débil en operación** que una garantía de 7 días con exclusiones explícitas: el vault ya aprendió esto con HostBrr (7 días VPS / 30 días hosting, con el cripto excluido) y con Proton (30 días, con cambio de plan a crédito prorrateado, [[2026-1024-proton-30-dias-de-dinero-devuelto-y-cambio-de-plan-con-credito-prorrateado]]). Lo que hace falta aquí es la tercera condición que esos dos casos tienen y AlexHost no: **a qué se aplica**.

El dato relevante para el vault es la **asimetría de atención**: la página garantiza el reembolso durante 30 días y el uptime durante el 99,99 %, pero no publica **ni SLA con créditos, ni backup, ni política de egreso, ni documentación de panel**. Para el hilo de hosting barato la fila de AlexHost quedaría con la garantía más generosa del mercado y con la columna de cumplimiento completamente vacía — un perfil que, en un producto multi-tenant, es exactamente el que hay que auditar antes de fiarse.

## [FRICTION]
> [[2026-1024-hostbrr-sla-99-9-y-garantia-de-devolucion-30-y-7-dias]] (escrita hace ~1 día) sostiene que la garantía de HostBrr excluye expresamente los pagos en criptomoneda, y que por tanto **la única vía reembolsable de ese proveedor es la que exige identificación bancaria** — una fricción operativa concreta.
> Este átomo dice lo mismo de AlexHost pero **sin la exclusión**: publica "30-day money-back guarantee for any of the listed services" y publica además una sección de criptomoneda con nueve logotipos. Si la garantía cubre "any of the listed services", entonces cubre también los servicios pagados en cripto; si no lo cubre, la página lo oculta.
> Ambas no pueden ser simultáneamente verdaderas como descripción de la política real: o el vault tiene una regla general de "el pago en cripto no se reembolsa" que contradice lo que AlexHost publica, o el caso de HostBrr es una política particular y no un patrón del sector. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
La captura **no** reproduce ni enlaza el texto de la garantía: los enlaces disponibles son a los términos de servicio, al DPA, a la política de cookies y a los términos del programa de afiliados. Tampoco publica SLA, uptime medido, ni el procedimiento de reembolso.

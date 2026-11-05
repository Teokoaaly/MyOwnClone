---
id: 2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes
type: atom
certainty: solid
sources: [sources/2026-10-22-hetzner-cloud.md, sources/2026-11-03-hetzner-cloud.md]
links: ["[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]"]
---

## Claim
La calculadora de coste de Hetzner Cloud (2026-10-22) resuelve la configuración por defecto como **Shared · Regular Performance, plan CPX02, 1 VCPU AMD**, con un precio de **€ 5.99 per month** o **€ 0.0096 per hour**, *excl. VAT*. Esa es la configuración con 1 vCPU, IPv4 primario y 20 TB de tráfico esperado, y es la entrada más barata que la página permite calcular.

## Why It Matters
Es el primer dato de coste de infraestructura **verificable en la fuente** para el vault: el despliegue vivo de [[2026-1022-live-verify-deployment-migrada-a-vps-nginx]] es un VPS autoalojado con nginx cuya IP (212.227.169.99) y cuyo plan no están identificados, así que este precio es la referencia contra la que se puede contrastar cualquier hipótesis de proveedor y plan — y también la vara para decidir si la infraestructura cabe en el presupuesto que la captura fija en ≤ €4/mes ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]). El hecho de que exista facturación por hora (€0.0096/h) además de mensual cambia la granularidad con la que se puede razonar el coste variable de infraestructura frente al coste por uso de los canales SMS ([[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]).

## [FRICTION]
> [[2026-1022-live-verify-deployment-migrada-a-vps-nginx]] (escrita hace ~21 semanas) afirma que [[myownclone]] se sirve desde `Server: nginx/1.28.3 (Ubuntu)` en `212.227.169.99`, pero **no identifica proveedor, plan ni specs** del VPS.
> Este átomo presiona esa laguna porque ofrece el precio exacto del plan compartido más barato de Hetzner; si el VPS vivo fuera un CPX02, su coste sería €5.99/mes (o €0.0096/h si se factura por hora) — pero nada en la fuente permite confirmar que ese servidor sea de Hetzner ni de qué plan se trata.
> Ambas no pueden ser simultáneamente verdaderas en su lectura completa: o el VPS vivo corre en otro proveedor con otro precio, o corre en Hetzner con un plan cuyo precio esta fuente no refleja. Marcado para juicio humano, no auto-resuelto.

## Nota de extensión 2026-11-03
Fuente: `sources/2026-10-31-hetzner-cloud.md`, `sources/2026-11-01-hetzner-cloud.md`, `sources/2026-11-02-hetzner-cloud.md`. La configuración por defecto **CPX02 1 VCPU AMD · € 5.99/mes · € 0.0096/h · IPv4 € 0,00 · 20 TB a € 0,00** se reproduce **sin una sola variación** en las dos capturas que renderizan la calculadora (2026-10-31 y 2026-11-02), y el bloque de planes mantiene "starting from … € 5.99 per month, excl. VAT" en las tres. Es decir: el precio de referencia de infraestructura del vault **no se ha movido en dos semanas** y sigue siendo la entrada más barata que la calculadora permite calcular.

Dos precisiones que las capturas nuevas añaden: (1) el mismo precio de entrada aparece **también como el mínimo de la familia Cost-Optimized**, es decir que el CPX02 es simultáneamente el plan más barato del catálogo y el "starting from" de la familia compartida — no hay un escalón más barato oculto; (2) la captura del 2026-11-01 no renderiza la calculadora, de modo que para esa fecha el dato proviene del bloque de planes, no del widget. Ver [[2026-1102-hetzner-precio-de-entrada-5-99-no-4-67]], que además plantea la fricción con la cifra de € 4,67 afirmada en [[2026-1031-hetzner-cloud]], y [[2026-1023-hetzner-facturacion-por-hora-0-0096]].

## 2026-11-03 — re-verificación
Fuente: `sources/2026-11-03-hetzner-cloud.md`. La configuración por defecto **CPX02 1 VCPU AMD · € 5.99/mes · € 0.0096/hora · IPv4 € 0,00 · 20 TB a € 0,00** se reproduce **sin una sola variación** en la calculadora de esta captura, y el bloque de planes mantiene "starting from … € 5.99 per month, excl. VAT". El precio de referencia de infraestructura del vault **no se ha movido en tres semanas**. La confirmación con cuatro capturas fechadas está en [[2026-1102-hetzner-precio-de-entrada-5-99-no-4-67]] y el marco general en [[2026-1103-hetzner-cinco-capturas-estabilidad-catalogo-vs-widgets-dinamicos]].

---
id: 2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes
type: atom
certainty: solid
sources: [sources/2026-10-22-hetzner-cloud.md]
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

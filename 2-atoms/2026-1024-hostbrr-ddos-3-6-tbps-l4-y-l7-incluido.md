---
id: 2026-1024-hostbrr-ddos-3-6-tbps-l4-y-l7-incluido
type: atom
certainty: solid
sources: [sources/2026-10-23-hostbrr-home.md, sources/2026-10-23-hostbrr-vps-pricing.md]
links: ["[[2026-1023-hetzner-firewalls-estatales-sin-coste-adicional]]", "[[2026-1024-hostbrr-escalera-de-precios-vps-2-00-3-50-y-3-90]]", "[[2026-1024-hostbrr-mitigacion-in-house-sin-scrubbing-externo]]"]
---

## Claim
HostBrr afirma incluir **mitigación DDoS de capa 4 y capa 7 sin coste adicional** en todos sus servicios: "We include robust layer 4 and layer 7 DDoS mitigation automatically at no extra cost", con **hasta 3,6 Tbps de capacidad**, mitigación en línea permanente 24/7/365, **latencia de mitigación < 1 ms** y "Real-Time Detection" (el tráfico se enruta permanentemente por la capa de protección, la mitigación empieza al instante, sin análisis aguas arriba ni retardo de conmutación). La propia página añade la salvedad: "DDoS protection and capacity may vary between services and location", repetida en la FAQ (pregunta 05).

## Why It Matters
Es una de las tres piezas que el vault ya tenía separadas en Hetzner — red troncal redundante, firewalls de estado sin coste adicional ([[2026-1023-hetzner-firewalls-estatales-sin-coste-adicional]]) — pero aquí HostBrr lo empaqueta como **argumento comercial de venta explícito**, con la cifra de capacidad (3,6 Tbps) como métrica de cabecera. Para un SaaS multi-tenant de clones de IA, la mitigación DDoS no es un extra: el relay de inferencia es un objetivo de ataque por naturaleza y su caída se traduce directamente en pérdida de ingresos del tenant ([[2026-1022-platform-admin-tenants-costes-mrr]]). Al estar incluida "automatically at no extra cost" en los VPS de €2,00/mes ([[2026-1024-hostbrr-escalera-de-precios-vps-2-00-3-50-y-3-90]]), es una variable que el vault puede dar por resuelta a coste cero — o, al menos, no por el premium que otros proveedores cobran.

## Nota de verificación
La captura es copy de marketing: no publica el SLA de DDoS, ni el precio de una capacidad superior, ni qué servicios concretos están cubiertos por los 3,6 Tbps completos. La salvedad "may vary between services and location" está transcrita literalmente.

## [NOTA 2026-10-24 — página de precios]
Fuente: `sources/2026-10-23-hostbrr-vps-pricing.md`. La página de precios **reconfirma** la promesa en su FAQ (pregunta 03): "Layer 4 and Layer 7 DDoS mitigation with up to 3.6 Tbps of capacity is included automatically at no extra cost. Protection and capacity may vary between services and locations." Añade dos precisiones que la home no daba: (a) la mitigación es **"Always-On"** y **permanente** — "Traffic is permanently routed through our protection layer. Mitigation begins instantly without any upstream analysis or switchover delay"; (b) la latencia de mitigación se cuantifica en **< 1 ms**, en un panel que muestra **3.6 Tbps Capacity** y **< 1ms Latency**. Y separa explícitamente lo que **sí** es gratis de lo que no: los backups son un **"Optional Add-On"** separado ([[2026-1024-hostbrr-backups-como-addon-opcional-con-gfs]]). La asimetría con el ancho de banda del plan (2.5 TB, ver [[2026-1024-hostbrr-ancho-de-banda-2-5-tb-a-10-gbps]]) se mantiene: la protección es mucho mayor que el tráfico contratado.

---
id: 2026-1024-flokinet-ddos-1tbps-incluido-en-los-siete-planes
type: atom
certainty: solid
sources: [sources/2026-10-24-flokinet-vps-pricing.md]
links: ["[[2026-1024-hostbrr-ddos-3-6-tbps-l4-y-l7-incluido]]", "[[2026-1024-buyvm-ddos-protegido-3-dolares-por-ip-y-cifrado-de-disco-completo]]", "[[2026-1024-skhron-sin-ddos-por-cliente-ni-garantia]]", "[[2026-1024-flokinet-escalera-de-precios-siete-planes]]"]
---

## Claim
FlokiNET incluye **protección DDoS en todos sus planes** — las siete filas de la tabla de precios repiten literalmente **"DDoS Protection (1Tbps+)"** — y la describe en la sección de producto como *"In all locations we provide DDoS filtering with capabilities greater than 1Tbps, giving you one of the best DDoS protections in the market at all (OSI) Layers"*. No es un add-on, no se cobra por IP y no se publica precio aparte. La red se apoya en nodos de virtualización con **conectividad 10/20 Gbit** y en un argumento de coste de peering: *"we do not skimp when it comes to cost of peering and network infrastructure"*.

## Why It Matters
Es el **segundo proveedor del vault con mitigación DDoS incluida de serie en todos sus planes** y el primero que declara la cifra por plan y la cobertura explícita de **todas las capas OSI**. El contraste del thread es instructivo: HostBrr incluye **hasta 3,6 Tbps L4+L7** sin coste ([[2026-1024-hostbrr-ddos-3-6-tbps-l4-y-l7-incluido]]), BuyVM lo cobra a **$3,00/mes por IP** ([[2026-1024-buyvm-ddos-protegido-3-dolares-por-ip-y-cifrado-de-disco-completo]]) y Skhron **no lo ofrece por cliente** y se reserva el derecho a filtrar o null-routar ([[2026-1024-skhron-sin-ddos-por-cliente-ni-garantia]]). FlokiNET se sitúa en el polo de HostBrr —incluido y sin coste— pero con una cifra **3,6 veces menor** (1 Tbps+ frente a 3,6 Tbps) y con un precio base 4 veces más alto. Para el relay autoalojado del vault, cuyo caso de uso es precisamente un endpoint expuesto que reenvía tráfico ([[2026-1023-priceai-sponsors-vps-chinos-para-auto-hospedar-relay]]), la observación operativa es que **la protección DDoS ya no es un discriminante de precio entre proveedores de suscripción**: el que la cobra (BuyVM) y el que la niega (Skhron) quedan fuera por precio y por riesgo, y los dos que la incluyen convergen en "coste cero", con la diferencia puesta solo en la cifra.

## Nota de verificación
"Capacities greater than 1Tbps" y "all (OSI) Layers" son **claims del proveedor**, sin SLA de mitigación, sin ventana de respuesta, sin política de credit y sin indicar si el filtrado es en el datacenter o en scrubbing externo. La captura **no** publica el precio de una capacidad superior ni el detalle por capa.

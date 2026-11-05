---
id: 2026-1027-proton-business-vpn-servidores-dedicados-alquilados-con-ip-fija
type: atom
certainty: solid
sources: [sources/2026-10-26-proton-business-vpn-pricing.md]
links: ["[[2026-1027-proton-business-vpn-enterprise-sin-precio-con-cta-de-contacto-comercial]]", "[[2026-1027-proton-business-vpn-professional-anade-sso-scim-ips-dedicadas-y-sentinel]]", "[[2026-1026-ivpn-despliegue-en-router-y-nas-para-salida-propia]]"]
---

## Claim
La FAQ de precios define el servidor dedicado como **alquiler, no venta**: "Dedicated servers are **reserved exclusively for your team as long as you rent them** from us. Dedicated servers have a **fixed IP address**", y quien intente acceder "must be connected to a special Proton VPN server dedicated solely to your business and available only to your organization members". El flujo de alta a "dedicated VPN servers" y "create a gateway and assign servers to it" queda explícitamente reservado: **"(VPN Professional and Proton Workspace customers only)"**. La página **no publica ningún precio de servidor dedicado, ni número máximo de gateways, ni coste por gateway**.

## Why It Matters
Es la partida **más cara y menos cotizada** de toda la línea, y la captura la describe con precisión de mecanismo: **IP fija, acceso restringido a los miembros de la organización, y alquiler mientras se paga**. Para el producto multi-tenant del vault es exactamente el componente de una "salida dedicada por tenant" —la forma en que un relay puede garantizar que la IP de un tenant no cambia y no se comparte— y **el precio sigue sin existir**: la FAQ describe la mecánica y la tabla de precios la niega, lo que deja la partida como **dato faltante explícito** y no como hipótesis ([[2026-1027-proton-business-vpn-enterprise-sin-precio-con-cta-de-contacto-comercial]]). El detalle de "as long as you rent them" importa: **la exclusividad es una propiedad del contrato de alquiler, no del servidor**, así que termina con el alquiler —el mismo patrón de continuidad que el vault ya registró en el pool de proxies por IP ([[2026-1026-ivpn-despliegue-en-router-y-nas-para-salida-propia]]).

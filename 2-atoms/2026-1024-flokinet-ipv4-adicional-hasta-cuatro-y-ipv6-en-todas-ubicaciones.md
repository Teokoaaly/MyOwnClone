---
id: 2026-1024-flokinet-ipv4-adicional-hasta-cuatro-y-ipv6-en-todas-ubicaciones
type: atom
certainty: solid
sources: [sources/2026-10-24-flokinet-vps-pricing.md]
links: ["[[2026-1024-skhron-ipv6-enrutado-64-y-56-gratis-e-ipv4-addon-0-65]]", "[[2026-1024-flokinet-escalera-de-precios-siete-planes]]", "[[2026-1024-evoxt-ipv6-y-red-privada-sin-cargos]]", "[[2026-1024-flokinet-nombres-servidor-ns1-a-ns4-y-panel-de-dns]]"]
---

## Claim
Todos los planes incluyen de serie **1 IPv4 y un /64 IPv6**, y el IPv4 se puede ampliar **hasta 4 direcciones extra en el momento del pedido**: *"IPs can be added while ordering your new VPS, where you will have the option to order up to 4 extra IPv4. If you wish to add after ordering, or more than 4 IPv4 addresses, please contact us via ticket"*. **IPv6 está soportado en todas las ubicaciones**. El **precio de las IPv4 adicionales no se publica**.

## Why It Matters
Es el mismo punto ciego que el vault ya tiene marcado en Skhron, donde el IPv4 dedicado cuesta **€0,65/mes por dirección** y no está incluido en el plan ([[2026-1024-skhron-ipv6-enrutado-64-y-56-gratis-e-ipv4-addon-0-65]]), y en Evoxt, donde la IP flotante adicional se ofrece **sin precio publicado** ([[2026-1024-evoxt-ipv6-y-red-privada-sin-cargos]]). Aquí el precio base es €7,99 y el extra **no está en la página**, así que un cómputo de "coste real por dirección" es imposible con esta captura: si una IPv4 extra costara lo mismo que en Skhron, cuatro extras serían €2,60/mes — un 33 % del plan de entrada. La diferencia útil con los demás es de **modelo de aprovisionamiento**: FlokiNET solo permite la ampliación **en el checkout** hasta cuatro, y pasado ese punto o después del pedido, **hay que abrir un ticket** — es decir, la ampliación no es self-service, exactamente como la renovación manual de ExtraVM. Para un nodo que puede necesitar varias IPs (varios dominios o servicios en un mismo servidor), la fricción operativa es real aunque el precio sea desconocido.

## Nota de verificación
La captura **no** publica: precio por IPv4 adicional, si hay cargo por IPv6, ni si el /64 se enruta o es solo asignable. El límite de 4 extra en el pedido y la vía de ticket son literales del texto.

---
id: 2026-1024-hostkey-ipv4-e-ipv6-dedicados-por-servidor
type: atom
certainty: solid
sources: [sources/2026-10-23-hostkey-bitcoin-vps.md]
links: ["[[2026-1023-hetzner-ipv4-primario-incluido-o-costo-cero]]", "[[2026-1024-evoxt-ipv6-y-red-privada-sin-cargos]]", "[[2026-1024-hostkey-1gbps-con-trafico-de-entrada-gratuito]]"]
---
## Claim
Cada servidor virtual de HOSTKEY recibe **una subred dedicada IPv4 e IPv6**, con posibilidad de ampliar el pool de direcciones IP si hace falta ("Each virtual server receives a dedicated IPv4 and IPv6 subnet, and HOSTKEY provides the ability to expand the IP address pool if necessary").

## Why It Matters
Es una posicion de generosidad por debajo de la de Hetzner, que incluye un IPv4 primario a coste cero ([[2026-1023-hetzner-ipv4-primario-incluido-o-costo-cero]]) y por encima de la de Evoxt, que publica IPv6 y red privada sin cargos ([[2026-1024-evoxt-ipv6-y-red-privada-sin-cargos]]): aqui lo prometido no es "una IP incluida" sino una **subred completa por VM**. Para el vault eso toca dos cosas concretas. Primera, la infra multi-tenant: una subred dedicada por tenant es exactamente lo que necesita un despliegue de clones que quiera exponer servicios por IP sin compartir espacio de direcciones con otros ([[2026-1022-multi-tenant-slug-unpublished]]). Segunda, el eje de proveedores de proxy y SMS que el vault tambien registra, porque una subred por VM es materia prima de salida por IP en lugar de salida por hostname. Lo que la pagina **no** publica es el precio de ampliar el pool ni el numero maximo de direcciones, de modo que el coste real de la escalabilidad de direcciones queda sin dato.

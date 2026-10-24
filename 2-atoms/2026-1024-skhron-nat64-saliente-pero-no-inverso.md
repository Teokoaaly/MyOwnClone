---
id: 2026-1024-skhron-nat64-saliente-pero-no-inverso
type: atom
certainty: solid
sources: [sources/2026-10-23-skhron-bitcoin-vps.md]
links: ["[[2026-1024-skhron-ipv6-enrutado-64-y-56-gratis-e-ipv4-addon-0-65]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]", "[[2026-1023-hetzner-ipv4-primario-incluido-o-costo-cero]]"]
---

## Claim
Skhron ofrece **NAT64 como puerta de salida**: "Your server can reach IPv4-only services like GitHub through our NAT64 gateway". Pero la conectividad **no es simétrica**: "No, legacy IPv4-only networks can't reach your server without a dedicated IPv4 address. Your connection is legacy IPv4 – you couldn't reach it without adding an IPv4 address."

## Why It Matters
Traducido a operación: un servidor **IPv6-only** de Skhron puede consumir APIs externas en IPv4 (GitHub, registries de paquetes, pasarelas de pago) sin contratar IPv4, pero **no es alcanzable desde clientes IPv4-only**. Para el despliegue nginx autoalojado que el vault ya registra ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) y para un panel web de tenants, esto significa que un plan "sin IPv4" no sirve para el front-end público salvo que los clientes finales usen IPv6; la dirección IPv4 dedicada de €0.65/mes deja de ser opcional en la práctica. La captura no publica límites de uso del NAT64 ni comportamiento de bloqueo por abuso.

---
id: 2026-1026-serverhunter-nat-ipv4-como-restriccion-del-escalon-mas-barato
type: atom
certainty: solid
sources: [sources/2026-10-25-serverhunter-cheap-vps.md]
links: ["[[2026-1024-skhron-ipv6-enrutado-64-y-56-gratis-e-ipv4-addon-0-65]]", "[[2026-1023-hetzner-ipv4-primario-incluido-o-costo-cero]]", "[[2026-1024-skhron-nat64-saliente-pero-no-inverso]]"]
---

## Claim
Todas las ofertas más baratas de la tabla de ServerHunter llevan la etiqueta **"NAT IPv4"**, y esa etiqueta desaparece justo donde empieza el precio alto: los cuatro planes `NAT-128` de Gullo's Hosting (128 MB, **$0.29**, regiones FR/CA/DE/FIN) y los cinco `NAT-256` (256 MB, **$0.33–0.54**) son NAT IPv4; también lo son `NanoVPS-II 384`, `NanoVPS-384`, `NanoVPS-1024 US` de Centerfield Ltd, el `CV-10` de Voyar Cloud ("NAT IPv4" + "IPv6 Only") y el `VPS ServerHunter Offer-3 NAT Only50 Annual` de Priente Cloud ("NAT IPv4" + "NAT Only"). En cambio **`STARDUST1-S - Amsterdam` de Scaleway (1 GB, ≈$0.49) es la única oferta sin esa etiqueta**, y la fila patrocinada de Ignero Corp, que es un dedicado, tampoco la lleva.

## Why It Matters
Es la partida de coste que el thread de hosting ya identificó como **la que se paga dos veces** —la IPv4 dedicada como add-on de Skhron a **€0,65/mes** ([[2026-1024-skhron-ipv6-enrutado-64-y-56-gratis-e-ipv4-addon-0-65]])— y aquí aparece como **la palanca con la que se compra el precio mínimo**: el escalón más barato de todo el mercado documentado se alcanza **renunciando a la IPv4 dedicada** y compartiendo laNAT. La regla de Skhron se invierte: en vez de pagar €0,65 aparte, el servidor de $0,29 **no incluye ninguna IPv4 propia**, y el umbral de $3,48/año solo es alcanzable con la restricción.

Y hay un caso donde la restricción es literalmente un bloqueo de alcance, no solo un ahorro: el `CV-10` de Voyar Cloud combina **"NAT IPv4" + "IPv6 Only"**, es decir un servidor cuya direccionabilidad IPv4 de entrada depende de una NAT compartida. El vault ya registró el caso simétrico en Skhron —NAT64 solo saliente, y "legacy IPv4-only networks can't reach your server without a dedicated IPv4 address" ([[2026-1024-skhron-nat64-saliente-pero-no-inverso]])—: para un producto con dominio público en IPv4, la IPv4 no es una línea de coste sino **una condición de existencia**.

## [FRICTION]
> [[2026-1023-hetzner-ipv4-primario-incluido-o-costo-cero]] registra que la calculadora de Hetzner ofrece el conmutador "IPv6 only / Primary IPv4" con un **€ 0.00** asociado, es decir **IPv4 a coste cero** en la configuración por defecto.
> ServerHunter muestra que **en el tramo de precio real más bajo del mercado la IPv4 no está incluida: no es gratis, es el precio que se paga** (NAT IPv4 en el 90 % de las filas visibles, $0.29–$0.54). Las dos afirmaciones no pueden ser a la vez la regla del vault: o el €0,00 de Hetzner es un dato de configuración y no de precio —lo que el propio átomo marca como lectura tentativa—, o la IPv4 nunca es gratis y el "gratis" de Hetzner es el extremo excepcional de un eje que en el resto del mercado se paga de dos maneras (add-on de €0,65 o renuncia vía NAT).
> Marcado para juicio humano, no auto-resuelto: la captura no publica qué red entrega el IPv4 en las ofertas NAT ni si el NAT es de ports o de direcciones.

## Nota de verificación
La etiqueta "NAT IPv4" y su presencia o ausencia por fila están transcritas literalmente, así como los precios y el nombre de Scaleway como única fila sin la etiqueta. La captura **no publica** cuántas de las 88.559 ofertas son NAT, ni el precio de una IPv4 dedicada equivalente en esos proveedores, ni el número de puertos compartidos.

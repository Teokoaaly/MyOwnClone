---
id: 2026-1026-bitlaunch-ddos-estateful-incluido-y-sin-cifras
type: atom
certainty: tentative
sources: [sources/2026-10-25-bitlaunch-home.md]
links: ["[[2026-1024-hostbrr-ddos-3-6-tbps-l4-y-l7-incluido]]", "[[2026-1024-buyvm-ddos-protegido-3-dolares-por-ip-y-cifrado-de-disco-completo]]", "[[2026-1024-flokinet-ddos-1tbps-incluido-en-los-siete-planes]]"]
---

## Claim
BitLaunch declara "**Advanced DDoS Protection**: BitLaunch provides industry-leading, **stateful**, high capacity DDoS Attack protection. **Included for free with all BitLaunch servers and some of our partner providers.**" La home **no publica ninguna cifra** de capacidad, ni capas (L3/L4/L7), ni latencia de mitigación, ni umbral de saturación — ni siquiera si la protección se extiende a los servidores de DO/Vultr/Linode revendidos o solo a los propios.

## Why It Matters
El thread de hosting barato ya tiene tres regímenes distintos de protección —incluido y por capacidad en HostBrr (3,6 Tbps L4+L7) y FlokiNET (1 Tbps+, todas las capas OSI), extra de $3/IP en BuyVM, y ninguno en Skhron ([[2026-1024-hostbrr-ddos-3-6-tbps-l4-y-l7-incluido]], [[2026-1024-buyvm-ddos-protegido-3-dolares-por-ip-y-cifrado-de-disco-completo]], [[2026-1024-flokinet-ddos-1tbps-incluido-en-los-siete-planes]])— y su regla operativa es que **para un relay expuesto a Internet esta fila pesa más que la de CPU**. BitLaunch aporta una **cuarta variante**: la protección es gratis en sus servidores pero **condicional en los de partners** ("some of our partner providers"), lo que significa que la misma cifra de marketing cubre dos poblaciones de riesgo distintas. Es el mismo problema que el thread ya señaló con ExtraVM, donde la mitigación **varía por ubicación** y Sídney no tiene protección nativa: sin ficha por ubicación, "included for free" no es una garantía operativa sino un rótulo.

## [FRICTION]
> [[2026-1024-buyvm-ddos-protegido-3-dolares-por-ip-y-cifrado-de-disco-completo]] establece, sobre BuyVM, que "DDoS protection is an additional **$3.00/month per IP address**" y que por tanto "es un extra, no un incluido".
> Este átomo presiona esa regla: BitLaunch declara protección **incluida y gratuita** en todos sus servidores, con la única salvedad de que en los de partners lo es "some". Si el coste marginal real de la mitigación en el mercado es distinto de cero —y BuyVM lo publica como $3/IP—, entonces "included for free" no describe una ausencia de coste sino **un coste absorbido en el precio del servidor**, lo que hace incomparables los precios entre proveedores salvo que se documente qué incluye la mitigación. Ambas no pueden ser completamente correctas: o el precio de BitLaunch es más alto porque ya paga la mitigación, o la mitigación en el tramo barato es más barata de lo que BuyVM factura. Marcado para juicio humano, no auto-resuelto: la captura de BitLaunch no publica ningún precio, así que no hay forma de cuantificar el sobrecoste absorbido.

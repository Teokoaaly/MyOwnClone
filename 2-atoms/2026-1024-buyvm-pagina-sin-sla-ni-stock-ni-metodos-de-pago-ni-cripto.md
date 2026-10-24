---
id: 2026-1024-buyvm-pagina-sin-sla-ni-stock-ni-metodos-de-pago-ni-cripto
type: atom
certainty: solid
sources: [sources/2026-10-23-buyvm-kvm-slices.md]
links: ["[[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]]", "[[2026-1024-extravm-sin-garantia-legal-de-uptime-solo-creditos]]", "[[2026-1024-skhron-sla-99-95-y-uptime-medido-99-99]]"]
---
## Claim
La página de planes Dedicated KVM Slice de BuyVM **no publica SLA, ni garantía de uptime, ni créditos por caída, ni número de unidades o stock por plan o por ubicación**, ni **formas de pago** (no hay mención a criptomoneda ni a fiat en toda la captura), ni IVA, ni política de cancelación o reembolso. Los únicos compromisos de servicio con número en la página son: **DDoS protection a $3.00/month por IP** (L4–L7, 500+ Gbps, 700+ M pps), **backups automáticos al 10 % del precio base** con **7 días de retención** y **5 snapshots gratis por ubicación**, y **Block Storage Slabs a $1.25/mes por 256 GB**.

## Why It Matters
Cierra el patrón que el vault ha ido construyendo proveedor a proveedor: **BuyVM es el más barato en precio base y specs, y el más opaco en cumplimiento**. Hetzner publica SLA 99,9 % con créditos, GDPR, ISO/IEC 27001 y BSI C5 ([[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]]); Skhron publica SLA 99,95 % medido y un uptime de 99,99 % ([[2026-1024-skhron-sla-99-95-y-uptime-medido-99-99]]); ExtraVM, en el otro extremo, declara explícitamente que **no tiene garantía legal de uptime**, solo créditos discrecionales ([[2026-1024-extravm-sin-garantia-legal-de-uptime-solo-creditos]]). BuyVM cae en ese segundo extremo pero sin ni siquiera la cortesía de declarar la ausencia. La consecuencia operativa para MyOwnClone es directa: **el hosting sigue siendo una línea de coste fija ausente del corte por categoría del back-office** ([[2026-1023-hetzner-costes-por-categoria-vs-infraestructura-propia]]), y si la plataforma autoaloja tenants de producción sobre slices BuyVM, **no hay contrato que respalde el SLA que el producto necesita prometer**.

## Nota de verificación
Lo que la captura **no** publica es una observación verificable sobre la página, no una afirmación de que BuyVM carezca de esos compromisos en otro documento (ToS, contrato, panel). La captura **no** contiene ninguna mención a BTC, ETH, LTC, USD, EUR, PayPal ni pasarela de pago.

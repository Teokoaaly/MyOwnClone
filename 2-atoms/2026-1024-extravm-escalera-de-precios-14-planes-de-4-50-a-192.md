---
id: 2026-1024-extravm-escalera-de-precios-14-planes-de-4-50-a-192
type: atom
certainty: solid
sources: [sources/2026-10-23-extravm-vps-pricing.md]
links: ["[[2026-1024-extravm-mismo-precio-que-tarjeta-sin-recargo-cripto]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados]]", "[[2026-1024-hostbrr-escalera-de-precios-vps-2-00-3-50-y-3-90]]"]
---

## Claim
La página de precios de ExtraVM publica **14 planes KVM-NVMe** con precios **en USD** ("All prices are in USD (US Dollars)") y una tabla completa de RAM / cores / disco / red: **1 GB $4.50**, 2 GB $8.00, 3 GB $12.00, 4 GB $14.00, 5 GB $17.50, 6 GB $21.00, 8 GB $28.00, 10 GB $35.00, 12 GB $42.00, 16 GB $56.00, 24 GB $84.00, 32 GB $112.00, 48 GB $144.00 y **64 GB $192.00/mes**. El **precio por GB de RAM baja por tramos**: $4.50/GB en 1 GB, $4.00/GB en 2–3 GB, **$3.50/GB en 4–32 GB** y $3.00/GB en 48–64 GB; el rango completo va de 1 GB a 64 GB de RAM, es decir ×64 en RAM por ×42.7 en precio.

## Why It Matters
Es la **ficha de precio completa y verificada** que faltaba en la página de cripto, donde el mismo proveedor solo declaraba "starting at $4.50/month" ([[2026-1024-extravm-mismo-precio-que-tarjeta-sin-recargo-cripto]]). Con la tabla completa, el vault puede comparar ExtraVM con las otras escaleras de precio ya registradas —los tres peldaños de HostBrr ([[2026-1024-hostbrr-escalera-de-precios-vps-2-00-3-50-y-3-90]]), el salto ×6.70 de Hetzner ([[2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados]])— y observar que ExtraVM **no tiene salto de tier**: su curva es continua y sin penalización de escalón, con el mismo $3.50/GB entre 4 y 32 GB. Eso importa para el modelo de coste del vault: el salto de capacidad se paga a precio de lista plano, sin "trampa de escalón" como en el catálogo de Hetzner. La página añade además el argumento de marketing de que "unlike big cloud providers that charge triple, we don't throttle your CPU resources or offer slow burst periods", que debe leerse como claim (no verificado) y no como dato de ficha.

## Nota de verificación
La captura no publica IVA, periodicidad distinta de mensual, descuentos por pago anual ni si el precio incluye algo más. El texto de marketing "we don't throttle your CPU" no está respaldado por specs de CPU asignada en la página.

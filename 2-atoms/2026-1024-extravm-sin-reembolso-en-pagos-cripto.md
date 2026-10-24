---
id: 2026-1024-extravm-sin-reembolso-en-pagos-cripto
type: atom
certainty: solid
sources: [sources/2026-10-23-extravm-crypto-vps.md, sources/2026-10-23-extravm-vps-pricing.md]
links: ["[[2026-1024-hostbrr-sla-99-9-y-garantia-de-devolucion-30-y-7-dias]]", "[[2026-1024-extravm-pago-cripto-sin-kyc-ni-identidad]]", "[[2026-1024-hostbrr-pagos-eur-usd-paypal-cripto-y-provisionamiento-en-minutos]]"]
---

## Claim
ExtraVM **no reembolsa los pagos hechos en criptomoneda**: "we cannot offer refunds for cryptocurrency payments due to the irreversible nature of blockchain transactions and exchange rate volatility. This policy is stated in our terms of service". La página compensa esa ausencia con una recomendación explícita: "We recommend testing with our **5-day money-back guarantee** using traditional payment methods first if you're unsure".

## Why It Matters
El mismo patrón que ya registró el vault en HostBrr, donde "Payments made with cryptocurrency are non-refundable due to how blockchain transactions work" convivía con una garantía de 7 días para VPS ([[2026-1024-hostbrr-sla-99-9-y-garantia-de-devolucion-30-y-7-dias]]): **la garantía de devolución y el pago anónimo son incompatibles**, y el proveedor resuelve el conflicto con una recomendación operativa ("prueba primero con métodos fiat"). Eso tiene un coste para el vault: si el criterio de privacidad es aceptable pero el riesgo de proveedor no, no hay forma de tener ambas cosas — el mismo patrón que HostBrr resuelve con un conmutador EUR/USD y métodos clásicos ([[2026-1024-hostbrr-pagos-eur-usd-paypal-cripto-y-provisionamiento-en-minutos]]). Los 5 días son además una ventana muy corta para validar un autoalojado bajo carga sostenida antes de quedar atado al ciclo de renovación.

## Nota de verificación
La captura **no** publica el texto de los términos de servicio ni el procedimiento para solicitar el reembolso en métodos tradicionales; los "5 días" y la exclusión de cripto son lectura literal de la FAQ.

## [NOTA 2026-10-24]
Fuente: `sources/2026-10-23-extravm-vps-pricing.md` (página de precios). La FAQ de esta segunda captura **confirma y precisa** la garantía: "we offer a 5-day money-back guarantee on **all VPS plans**" —la ventana de 5 días aplica a cualquier plan, no solo a los comprados con métodos fiat— y añade dos condiciones que la página de cripto no detallaba: (1) "We can only provide refunds processed via **fiat payment methods, not cryptocurrency**", confirmando la exclusión; y (2) "We may **deduct transaction/refund fees** from refunds, which is money we lose from processing refunds", es decir, el reembolso no es necesariamente el importe íntegro. Esto refuerza la lectura operativa de la nota original: la garantía existe pero solo es instrumentalmente utilizable por la vía clásica, y aun así tiene un recorte. La misma FAQ añade que "Some payment methods like **bank transfers and cryptocurrency may take time to process**", lo que introduce una cuarta vía de pago lento (no solo la blockchain) y matiza el "instant deployment" con un factor de tesorería. Ver también [[2026-1024-extravm-despliegue-tras-confirmacion-en-15-30-minutos]].

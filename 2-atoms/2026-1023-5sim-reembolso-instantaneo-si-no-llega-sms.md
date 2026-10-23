---
id: 2026-1023-5sim-reembolso-instantaneo-si-no-llega-sms
type: atom
certainty: tentative
sources: [sources/2026-10-22-5sim-home.md, sources/2026-10-22-hero-sms-chatgpt-verification.md]
links: ["[[2026-1023-5sim-smart-buy-y-tasa-entrega-visible]]", "[[2026-1022-stripe-planes-trial-30-dias]]", "[[2026-1023-5sim-catalogo-servicios-precios-y-stock]]", "[[2026-1023-hero-sms-reembolso-si-no-llega-sms-en-20-minutos]]"]
---

## Claim
5sim declara en su home una garantía de **reembolso automático**: "Instant refunds — if no SMS is received, your money is refunded automatically". La compra es por número suelto y prepago sobre saldo ("Add funds to your 5SIM balance"), sin plan mensual: "you will not have to pay for monthly SIM plans too". El proveedor **excluye explícitamente** el envío de SMS salientes y de llamadas: "The service does not support sending outgoing SMS and calls", y remite a unas "Rules of use" y a una "Stop list" (los nombres de los remitentes desde los que no se recibirá SMS).

## Why It Matters
Es el mismo desplazamiento de riesgo que en un SaaS de suscripción: si la unidad no cumple, el proveedor devuelve el dinero y el coste marginal es el reintento, no la pérdida ([[2026-1023-5sim-smart-buy-y-tasa-entrega-visible]]). La contraparte es la Stop list — una lista de remitentes bloqueados que introduce un riesgo de entrega no controlable por el comprador, y que es el límite real de cualquier flujo automatizado que dependa de un SMS concreto.
El patrón de prepago sobre saldo sin suscripción mensual es un modelo distinto al del vault: [[myownclone]] cobra 99 al mes por adelantado ([[2026-1022-precio-99-mensual]]) y ofrece trial ([[2026-1022-stripe-planes-trial-30-dias]]), mientras que aquí no hay plan recurrente en absoluto ([[2026-1023-5sim-catalogo-servicios-precios-y-stock]]).

## Comparación con HeroSMS (2026-10-22)
El competidor **HeroSMS** declara la misma garantía con un dato que 5sim no da: "No SMS received within **20 minutes**? Get an instant automatic refund to your balance", más "loyalty discounts up to 40 %" y soporte 24/7 ([[2026-1023-hero-sms-reembolso-si-no-llega-sms-en-20-minutos]]). Los dos proveedores mueven riesgo al comprador de la misma forma (reembolso si la unidad no cumple), pero solo uno hace auditable el plazo: sin plazo, el reembolso de 5sim no acota el coste temporal de un reintento.

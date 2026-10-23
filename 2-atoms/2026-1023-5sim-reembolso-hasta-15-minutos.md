---
id: 2026-1023-5sim-reembolso-hasta-15-minutos
type: atom
certainty: solid
sources: [sources/2026-10-22-5sim-openai-chatgpt-pricing.md]
links: ["[[2026-1023-5sim-reembolso-instantaneo-si-no-llega-sms]]", "[[2026-1023-5sim-openai-tasa-entrega-techo-56]]", "[[2026-1023-5sim-ventana-5-30-minutos-y-cancelacion-a-5-min]]"]
---

## Claim
La página de producto de OpenAI matiza la promesa de reembolso con un plazo que la home no declara: "If no SMS is received, you can cancel an unused active order and the payment is returned to your 5SIM balance **immediately**", pero también, en el bloque de pasos, "If you didn't receive an SMS, you will be refunded automatically — **rarely it may take up to 15 minutes**", y en el FAQ, "the cost of the number is automatically returned to your 5SIM balance **after the order is completed**". Hay por tanto tres tiempos distintos: cancelación manual de una orden activa sin usar → inmediato; fin del periodo activo → automático; SMS no recibido → automático, pero **hasta 15 minutos**.

## Why It Matters
El reembolso no es instantáneo en el caso que más importa —el SMS que no llegó— y ese caso es la norma con una tasa de entrega del 56% como techo ([[2026-1023-5sim-openai-tasa-entrega-techo-56]]). Eso significa que un flujo automatizado no puede contar con el dinero de vuelta de inmediato para reintentar en el momento: hay una ventana de hasta 15 minutos de caja bloqueada por pedido fallido, o un proceso manual de cancelación por cada orden. El coste de reintento es, por tanto, de **capital circulante y de paciencia**, no solo de saldo.
El matiz encaja además con la ventana de vida de la orden: 5–30 minutos de SMS y cancelación automática a los cinco minutos ([[2026-1023-5sim-ventana-5-30-minutos-y-cancelacion-a-5-min]]), lo que sugiere que "reembolso automático" es en la práctica el resultado de expirar la orden, no de detectar el fallo.

## [FRICTION]
> [[2026-1023-5sim-reembolso-instantaneo-si-no-llega-sms]] (escrita hoy, desde la home) cita la promesa literal "Instant refunds — if no SMS is received, your money is refunded automatically".
> Esta nota, desde la página del servicio OpenAI, dice lo mismo pero añade "rarely it may take up to 15 minutes" y "after the order is completed".
> Ambas no pueden ser exactas: o "instant" describe solo la cancelación manual de una orden sin usar, o la home simplifica un reembolso que la página del producto cuantifica en hasta 15 minutos. Marcado para juicio humano, no auto-resuelto.

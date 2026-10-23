---
id: 2026-1023-5sim-openai-tasa-entrega-65-de-100
type: atom
certainty: solid
sources: [sources/2026-10-22-5sim-openai-chatgpt-pricing.md]
links: ["[[2026-1023-5sim-openai-tasa-entrega-techo-56]]", "[[2026-1023-5sim-smart-buy-y-tasa-entrega-visible]]", "[[2026-1023-5sim-reembolso-hasta-15-minutos]]"]
---

## Claim
La página define explícitamente qué es la "SMS delivery rate": "**the delivery rate shows how often SMS has recently arrived for that exact OpenAI combination**", y da la equivalencia numérica — "a **65%** rate means that SMS was received in about **65 out of 100 recent orders** using the same country and operator for OpenAI". Es una **frecuencia histórica observada sobre pedidos recientes**, calculada por par país-operador **dentro del servicio OpenAI**, no una garantía ni un SLA. La propia página añade la regla de decisión: "when the prices are close, the higher-rate option is usually the stronger choice", y el rango observado en la tabla visible es 39,39%–55,56%.

## Why It Matters
La semántica importa porque fija el contrato implícito del producto: se compra una probabilidad empírica, no una garantía de entrega, y la probabilidad se calcula sobre un histórico reciente de pedidos —es decir, es una métrica que se degrada sola si el proveedor cambia de routing o de proveedor de SMS. Eso convierte a la tasa en un indicador que hay que releer antes de cada compra en lote, igual que un precio que "changes through the day" (como avisa la propia tabla), y explica por qué el proveedor pone la estadística delante del pago ([[2026-1023-5sim-smart-buy-y-tasa-entrega-visible]]). Combinada con el techo del 56% ([[2026-1023-5sim-openai-tasa-entrega-techo-56]]), la consecuencia práctica es que **más de un tercio de los pedidos paga por un SMS que no llega** y entra en la cola de reembolso ([[2026-1023-5sim-reembolso-hasta-15-minutos]]).

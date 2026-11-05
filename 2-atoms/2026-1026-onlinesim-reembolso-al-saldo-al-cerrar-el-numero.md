---
id: 2026-1026-onlinesim-reembolso-al-saldo-al-cerrar-el-numero
type: atom
certainty: solid
sources: [sources/2026-10-25-onlinesim-virtual-sms.md]
links: ["[[2026-1023-5sim-reembolso-instantaneo-si-no-llega-sms]]", "[[2026-1023-hero-sms-reembolso-si-no-llega-sms-en-20-minutos]]", "[[2026-1023-5sim-reembolso-hasta-15-minutos]]"]
---

## Claim
La garantía de OnlineSim **no es automática ni tiene plazo**: se enuncia dos veces, casi con las mismas palabras. "If a message does not arrive at the temporary number you ordered (this can happen for various reasons, for example, the sending site delayed sending or the issued number had a failure), **you can close the phone number and order another**, money from your balance in this case is not debited will be." Y la variante: "If there is no message on the temporary number you have ordered (it may happen for many reasons, for example, the sending website delayed sending or the number has failed), you can **deactivate the phone number and the funds will return to the balance** so that you can order a new virtual mobile number." El reembolso es **a saldo**, y solo se produce si el **usuario** cierra el número.

## Why It Matters
Es un modelo de garantía distinto del de los otros dos operadores y el vault no lo tenía: 5sim promete reembolso automático ("Instant refunds — if no SMS is received, your money is refunded automatically", con el matiz de "hasta 15 minutos" en la página de producto — [[2026-1023-5sim-reembolso-instantaneo-si-no-llega-sms]], [[2026-1023-5sim-reembolso-hasta-15-minutos]]) y HeroSMS fija un umbral explícito de 20 minutos ([[2026-1023-hero-sms-reembolso-si-no-llega-sms-en-20-minutos]]). Aquí el reembolso **depende de una acción del comprador** y no está acotado en el tiempo: si nadie cierra el número, el dinero se queda en el saldo hasta que expire la orden.
Consecuencia operativa: el **tiempo de saldo bloqueado** es la variable de coste real de esta oferta, y es una variable que el proveedor no cuantifica — a diferencia del plazo de 20 minutos de HeroSMS, que sí permite calcular el coste de un reintento. Para un flujo automatizado, esto significa que el cobro del fallo es **tiempo de caja inmovilizada por orden**, no solo el coste nominal del número.

## [FRICTION]
> [[2026-1023-5sim-reembolso-instantaneo-si-no-llega-sms]] (escrita hace tres días) generaliza el patrón del sector como "el desplazamiento de riesgo al comprador de la misma forma (reembolso si la unidad no cumple), pero solo uno hace auditable el plazo" — HeroSMS con 20 minutos, 5sim sin plazo.
> Este átomo presiona esa creencia porque añade un **tercer** régimen, y no es "5sim sin plazo" sino algo más débil: en OnlineSim el reembolso **no es automático en absoluto**, requiere que el comprador cierre la orden, y el dinero vuelve **al saldo**, no al medio de pago.
> Ambas no pueden ser la misma descripción del sector: o el "reembolso automático si la unidad no cumple" es una característica común a los tres proveedores —y entonces el cierre manual de OnlineSim es una excepción que hay que documentar—, o el régimen de garantía varía por proveedor y el vault tiene que tratar el reembolso como un dato **por proveedor**, no como una propiedad del sector. Marcado para juicio humano, no auto-resuelto.

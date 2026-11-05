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


## Nota de extensión 2026-10-26
La captura del 2026-10-25 **confirma la frase exacta** —"Instant refunds — if no SMS is received, your money is refunded automatically"— y añade, en el mismo párrafo de cierre, una cláusula de uso legítimo que el átomo original no transcribía: **"The service does not support sending outgoing SMS and calls. The service is intended for lawful use only. Please read the Rules of use and Stop list (the names of the senders, from which you will not be able to receive SMS)."** ([[2026-1026-5sim-cinco-razones-para-ganar-a-otros-sin-nombrar-a-ninguno]]).

**El detalle nuevo es que el Stop list se define en la propia página como una lista de remitentes bloqueados**, y no como un simple enlace a "Rules of use": "(the names of the senders, from which you will not be able to receive SMS)". Eso convierte la Stop list en un **límite de entrega determinado por un tercero** —el remitente— y no por el proveedor ni por el comprador. Para un flujo automatizado que depende de un SMS concreto, es el mismo límite operacional que la fricción 2 del thread ya señalaba en HeroSMS ("hasta 15 minutos"), y por tanto conviene **anotar el remitente permitido antes de automatizar**, porque un SMS de un remitente bloqueado no es un fallo del flujo sino un no-entregado silencioso con reembolso automático detrás ([[2026-1023-5sim-smart-buy-y-tasa-entrega-visible]]).


## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-onlinesim-virtual-sms.md`. Este átomo describe el régimen de garantía de 5sim ("Instant refunds — if no SMS is received, your money is refunded automatically") y lo generaliza en su §"Comparación con HeroSMS" como: "Los dos proveedores mueven riesgo al comprador de la misma forma (reembolso si la unidad no cumple), pero solo uno hace auditable el plazo".

Con OnlineSim aparece un **tercer régimen, más débil que "5sim sin plazo"**: el reembolso **no es automático en absoluto**. Su FAQ dice "**you can close the phone number and order another**, money from your balance in this case is not debited" y "you can **deactivate the phone number and the funds will return to the balance** so that you can order a new virtual mobile number" ([[2026-1026-onlinesim-reembolso-al-saldo-al-cerrar-el-numero]]).

Tres rasgos que lo distinguen: (1) requiere **una acción del comprador** — cerrar el número — y por tanto no ocurre si nadie interviene; (2) **no tiene plazo** — ni de 20 minutos como HeroSMS, ni de "hasta 15" como la página de producto de 5sim ([[2026-1023-5sim-reembolso-hasta-15-minutos]]); (3) devuelve **al saldo**, no al medio de pago.

Consecuencia para el thread: el reembolso no es una propiedad del sector sino un **dato por proveedor**, y el tiempo de saldo inmovilizado es la variable de coste real en los tres casos. Esta captura añade el extremo más desfavorable de la escala.

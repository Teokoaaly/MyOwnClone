---
id: 2026-1026-onlinesim-numero-solo-entrante-y-exclusivo-de-una-persona
type: atom
certainty: solid
sources: [sources/2026-10-25-onlinesim-virtual-sms.md]
links: ["[[2026-1023-5sim-numero-de-un-solo-uso-una-verificacion]]", "[[2026-1023-5sim-ventana-5-30-minutos-y-cancelacion-a-5-min]]", "[[2026-1022-ia-y-auth-totalmente-servidor]]"]
---

## Claim
El FAQ de OnlineSim define el producto en tres frases: "This is an online mobile number that can be used **without a SIM card**. In our case, it is a mobile number that only belongs to our service **for activation using text messages** and can **only accept incoming messages**"; "The numbers that are purchased through our service are **disposable and cannot be reused** by our clients after the order time has expired"; y "Numbers are issued **exclusively to one person**".

## Why It Matters
Las tres propiedades son las que el vault necesita para modelar una identidad verificada como **recurso de un solo sentido**: sin salida (solo entrante), sin vida más allá de la orden, y de un propietario por orden. Eso cierra por diseño la vía de usar un número temporal como canal de salida o como identidad persistente, y lo confirma en la dirección contraria a la de un proveedor de buzones [[2026-1024-notletters-tres-vias-de-consumo-api-http-imap-y-web]]: aquí no hay lectura, no hay buzón, no hay API de envío — solo un display de códigos dentro de la cuenta.
Comparado con 5sim, que documenta la no reutilización en la página de producto de OpenAI ([[2026-1023-5sim-numero-de-un-solo-uso-una-verificacion]]) y acota la vida de la orden a 5-30 minutos ([[2026-1023-5sim-ventana-5-30-minutos-y-cancelacion-a-5-min]]), OnlineSim hace la misma promesa pero **además** advierte de que el operador puede reemitir la tarjeta SIM ([[2026-1026-onlinesim-reexpedicion-de-sim-a-los-2-3-meses-y-no-vincular-2fa]]), lo que es una restricción que 5sim no declara: la exclusividad es del número durante la orden, no del número para siempre.

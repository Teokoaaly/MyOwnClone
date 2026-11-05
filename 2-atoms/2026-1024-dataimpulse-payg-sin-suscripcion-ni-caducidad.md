---
id: 2026-1024-dataimpulse-payg-sin-suscripcion-ni-caducidad
type: atom
certainty: solid
sources: [sources/2026-10-23-dataimpulse-proxies.md]
links: ["[[2026-1023-hero-sms-modelo-pay-per-use-y-tabla-real-vs-virtual]]", "[[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]", "[[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]", "[[2026-1023-lzt-topup-mastercard-comision-10]]"]
---

## Claim
DataImpulse define su modelo comercial con dos frases que la home repite en cuatro sitios distintos: **"No expiry, no subscription"** y **"Pay-as-you-go"**. El bloque "Key Features" lo formula como **"No extra fees. Pay only for the traffic you use. Credit never expires."**, y la tabla de precios incluye como fila común a los cuatro tipos de proxy: **"Traffic never expires"**. El flujo de compra son tres pasos: registrarse y obtener dashboard → elegir tipo de proxy → **"Top up your balance and activate your proxy"**. La lista de ventajas incluye además **"7-day Refund Policy"** y **"No Time Limits"**.

## Why It Matters
Es el mismo contrato económico prepagado que el vault ya registró para los proveedores de SMS —saldo, pago por uso, sin permanencia ([[2026-1023-hero-sms-modelo-pay-per-use-y-tabla-real-vs-virtual]])—, pero con una diferencia que cambia la gestión de caja: **el crédito no caduca**, igual que en 5sim ([[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]). Para un pipeline de altas automatizadas, "el tráfico no consumido no caduca" y "el saldo no caduca" significan que **no hay coste de oportunidad por literalmente no gastar**: el mínimo de compra ($5) es a la vez el mínimo de exposición al riesgo.
El matiz de la recarga sí tiene precio: si se paga con Mastercard hay un 10 % de comisión sobre el saldo ([[2026-1023-lzt-topup-mastercard-comision-10]]), y DataImpulse no publica ninguna cifra de comisión, así que el coste efectivo del gigabyte es desconocido hasta ver el checkout.

## Nota de verificación
Frases transcritas literalmente. La captura **no** publica: importe mínimo de recarga, si el saldo prepagado es fungible entre los cuatro tipos de proxy, si el reembolso de 7 días aplica solo al primer depósito o a cualquier compra, ni condiciones de ese reembolso.


## Nota de extensión 2026-10-27
La documentación publica una sección **"Auto-recharge"** ("Don't worry about balance") que este átomo no registra, y que **cambia la lectura del flujo de compra** que el átomo transcribe: el paso "Top up your balance and activate your proxy" no es necesariamente manual, porque el saldo puede **rellenarse solo**. Ver [[2026-1027-dataimpulse-auto-recharge-publicado-en-la-documentacion]], que registra el dato y su fricción con este átomo.
El efecto combinado con "Traffic never expires" es el que hay que dejar anotado: **saldo que no caduca + recarga automática = gasto recurrente sin decisión por topping-up ni aviso**, es decir, el control de caja que este átomo daba por estructurado (saldo, prepago, sin permanencia) admite en realidad un **pedido recurrente (standing order)** que el propio producto ofrece. La captura **no** publica umbral, importe ni periodicidad de la recarga, de modo que la cifra que falta es la que decide si esa función es un control o un riesgo.


## Nota de extensión 2026-10-27
La landing móvil **reconfirma** "Pay-as-you-go", "Traffic never expires", "No Time Limits" y "7-day Refund Policy", y **añade una promesa incompatible con la primera**: el badge del bloque de Ad Verification declara **"$2/GB — unused GBs roll over"**. El acarreo entre periodos **solo tiene sentido si existe un periodo**, así que el vault tiene ahora dos descripciones del saldo —"nunca caduca" y "los GB no usados se trasladan"— que **no pueden ser simultáneamente ciertas** sin que "roll over" sea decorado para "no caduca". Es un matiz pequeño de redacción con una consecuencia de caja real (un saldo rotatorio genera una ventana de caducidad implícita) y es la clase de contradicción interna que este thread viene documentando en todo el corpus. Ver [[2026-1027-dataimpulse-gb-sin-caducar-que-igual-rolling-y-son-90-de-satisfaccion]].
Nota: la captura móvil **no** publica el periodo de rollover, las condiciones del reembolso de 7 días, ni si el reembolso aplica al primer depósito o a cualquier compra.


## Nota de extensión 2026-10-27
La página de proxy residencial de 2Captcha **confirma el patrón de saldo prepago sin caducidad con un claim nuevo**, y lo hace en la forma menos obvia posible. Bajo una tabla de **precios por GB** —con nueve tramos de volumen y descuentos explícitos del 0 % al 68,7 %— la lista de inclusiones dice "**Unlimited traffic**", junto a "Flexible rotation options", "API access" y "SOCKS5 supported". Ver [[2026-1027-2captcha-unlimited-traffic-y-socks5-en-un-plan-facturado-por-gb]].

Es decir: **el claim de "sin caducidad" aquí se enuncia con el vocabulario del coste marginal nulo** ("tráfico ilimitado") y **no con el vocabulario del saldo** ("no caduca", "never expires"), en un producto cuyo precio es explícitamente "Price per GB". La conclusión que el thread sostiene con este átomo —que "**el contrato prepago sin caducidad es norma del sector y no una peculiaridad**"— **se refuerza en cuanto al comportamiento** y **se matiza en cuanto a la redacción**: dos de los tres proveedores con saldo prepago medidos (DataImpulse y, por inferencia, 2Captcha) no caducan, pero **solo uno de ellos lo dice con una fórmula no ambigua**.

Lo que 2Captcha **no** publica y este átomo sí necesita: si el saldo caduca, si el tráfico no consumido se factura, si existe recurrencia, y la duración de la sesión sticky. **Es el mismo conjunto de huecos que ya tenía este átomo**, lo que confirma que 2Captcha **no aporta un dato nuevo sobre el ciclo de vida del saldo**, sino un cuarto proveedor con el mismo ciclo.

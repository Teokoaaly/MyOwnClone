---
id: 2026-1024-notletters-precio-005-rubles-por-correo-y-contadores-de-escala
type: atom
certainty: solid
sources: [sources/2026-10-23-notletters-mail.md]
links: ["[[2026-1023-priceai-channels-correo-y-jianma-a-centimos-como-insumo-de-alta]]", "[[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]", "[[2026-1023-lzt-captura-parcial-sin-precios-ni-stock]]"]
---
## Claim
La sección "Statistics of our service" de la home de NotLetters publica cuatro cifras literales: **"0.05 ₽"** como **precio por correo** ("Price per mail"), **"> 5 000 000"** como **correos comprados** ("Mail purchased"), **"> 30 000 000"** como **correos recibidos** ("Emails received") y **"573 Ms"** como **tiempo medio de recepción** ("Average time to receive emails"). Los subtextos de marketing que acompañan a los contadores son: "Thousands of customers have already used our emails", "Most of our customers, get discounts for large volumes", "In just 3 months of operation, customers received 5 million emails" y "On average, our clients receive from 3 to 5 emails per email".

## Why It Matters
El **0.05 ₽ por correo** es la cifra relevante para el vault, porque fija un precio de referencia para el buzón de registro en la moneda en que ese tipo de servicio se cotiza en el este de Europa, y porque cambia el orden de magnitud del coste de un alta: el correo queda por debajo del suelo medido del SMS ($0.1026 en 5sim, [[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]) y por debajo del suelo del correo revendido en el 卡网 (¥0.02, [[2026-1023-priceai-channels-correo-y-jianma-a-centimos-como-insumo-de-alta]]). La lectura hay que hacerla con cuidado: la cifra está en **rubles** y la comparación con los yuanes del 卡网 exige un tipo de cambio que la captura no contiene, de modo que la comparación solo es legítima como **orden de magnitud nominal**, no como precio convertido.
Los contadores, en cambio, son claims sin evidencia adjunta, y el propio texto los mixa: dice a la vez "5 million emails" en tres meses de operación y "> 30 000 000" correos recibidos, sobre un "> 5 000 000" comprados. Con el "3 to 5 emails per email" declarado, la razón implícita entre comprados y recibidos (≈6) queda por encima del rango que la propia página afirma. Es el mismo patrón que el vault ya registró en otros proveedores del sector (contadores que no cuadran entre sí), y por eso el dato defendible es **el precio y el tiempo de recepción**, no los totales.

## [FRICTION]
> [[2026-1023-priceai-channels-correo-y-jianma-a-centimos-como-insumo-de-alta]] fija el suelo de precio del correo como insumo de alta en **¥0.02** (其他邮箱 / iCloud / Outlook), y da por hecho que el correo consumible del sector es esa fila del marketplace.
> Este átomo presiona esa creencia con un precio del mismo orden de magnitud pero distinto: **0.05 ₽ por correo**, en un proveedor dedicado y con su propio canal de venta. Si ambas cifras son comparables, el suelo real del buzón de registro está **por debajo** del que el vault tenía registrado, y la comparación entre proveedor y marketplace —que hasta ahora parecía una diferencia de canal y no de precio— pasa a ser también una diferencia de suelo.
> Ambas no pueden ser completamente correctas: o las dos cifras no son comparables (rubles contra yuanes, buzón contra correo vendido) y entonces el suelo del vault no se move, o sí lo son y el suelo registrado era el de un canal concreto, no el del mercado. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
Los rótulos ("Price per mail", "Mail purchased", "Emails received", "Average time to receive emails") y las cuatro cifras están transcritos literalmente de la captura; el orden de extracción (cifra antes del rótulo) es el del HTML capturado, no una atribución del redactor. La captura **no** publica: formato o lista de dominios, patrón de las direcciones, límites por buzón o por cuenta, plazos de retención, precios por volumen (solo afirma que "la mayoría de los clientes" recibe descuentos), forma de pago, reembolso, condiciones o SLA, ni documentación de la API.

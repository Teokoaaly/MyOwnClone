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


## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-emailondeck-temp-mail.md`. Este átomo fija **0.05 ₽ por correo** como precio de referencia del buzón de registro y, en su §[FRICTION], confronta ese nominal con el suelo de **¥0.02** del 卡网 de PriceAI.

EmailOnDeck añade dos presiones a ese dato, en direcciones opuestas.

**Hacia abajo: el suelo nominal no es el suelo del mercado.** EmailOnDeck se presenta como **gratis** —"EmailOnDeck is always simple and free", "Free & fast temp mail in 2 easy steps"— y no publica ni un precio, ni de la versión gratuita ni del plan PRO enlazado en `pro.emailondeck.com` ([[2026-1026-emailondeck-gratis-con-paso-pro-sin-cifras]]). Si ese "gratis" es real y no tiene límites relevantes, el 0.05 ₽ de NotLetters es el precio de un **canal de pago concreto**, no el suelo del producto. Y como los dos proveedores no son comparables en unidad —NotLetters vende "por correo", PriceAI revende buzones de otros— la fricción 12 del thread sobre la comparabilidad del suelo del correo tiene ahora **un tercer término**: un competidor declarado gratuito sin cifra.

**Hacia arriba: el contador de escala, que es el dato comparable.** NotLetters publica "> 5 000 000" correos comprados y "> 30 000 000" recibidos, y este átomo concluye que el dato defendible es "el precio y el tiempo de recepción, no los totales" porque los contadores no cuadran entre sí (≈6 recibidos por comprado frente a un rango declarado de 3 a 5). EmailOnDeck publica **"Over 215,158,204 temporary emails processed"** con **"© 2015-2026"**, es decir **11 años** de operación ([[2026-1026-emailondeck-contador-215158204-correos-procesados]]). La cifra es **×7 mayor** que la de NotLetters en compras y es, al mismo tiempo, **menos auditable**: no distingue comprados de recibidos ni da periodo ni desglose, de modo que **colapsa en un solo número la distinción que este átomo necesita para poder auditar a NotLetters**.

Nota para el Editor: los dos contadores no son comparables en unidad (uno son unidades compradas y el otro unidades procesadas, sin desglose), así que la conclusión correcta no es "el mayor proveedor es 7 veces más grande" sino "**el vault solo tiene dos contadores de escala del sector de correo y ninguno es auditable**". La regla que este átomo establece —"el dato defendible es el precio y el tiempo, no los totales"— queda reforzada, no matizada.


## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-mail-tm-temp-mail.md`.

Este átomo fija **0.05 ₽ por correo** como precio de referencia del buzón de registro del corpus, con contadores de escala ("> 5 000 000" comprados, "> 30 000 000" recibidos) y tiempo medio de recepción de **573 Ms**. Mail.tm **no publica ningún precio** —el bloque "Free" dice "Every user gets full access to their temporary mailbox and an unlimited number of new ones. **No hidden conditions, no paid extras**"— y **no publica ningún tiempo de recepción**; lo único que ofrece es "Your temporary mailbox is **generated instantly**" y, en el nav, la línea de financiación: "You can support us by **disabling your ad blocker** on our site" ([[2026-1026-mail-tm-gratis-sin-cifras-con-financiacion-por-anuncios]]).

La consecuencia para el Editor es de **unidad de comparación**, no de precio: mail.tm introduce un **cuarto régimen de correo** en el corpus —**gratis, automatizable, y financiado con publicidad**— frente a los tres ya registrados (función de biblioteca del bot, NotLetters pago y automatizable, EmailOnDeck gratuito y manual). Mail.tm es el **único** que combina las dos propiedades que el thread usa para decidir si el correo es una partida cotizable: **coste monetario cero y superficie programable declarada**. Y con eso, el dato de los 573 Ms de NotLetters queda todavía más aislado: es el **único tiempo de recepción medido del corpus**, y la alternativa gratuita no publica ninguno.

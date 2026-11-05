---
id: 2026-1027-2captcha-proxy-acepta-visa-mastercard-airtm-paypal-alipay-btc-y-usdt
type: atom
certainty: solid
sources: [sources/2026-10-26-2captcha-pricing-residential-proxy.md]
links: ["[[2026-1023-lzt-topup-mastercard-comision-10]]", "[[2026-1024-dataimpulse-metodos-de-pago-incluye-cripto]]", "[[2026-1026-decodo-paddle-como-merchant-of-record-y-cripto-excepto-isp-y-datacenter]]"]
---
## Claim
El bloque de compra del proxy residencial de 2Captcha declara: "**We accept these payment methods:**" seguido de un icono con el texto alternativo "**We support Visa, Mastercard, Airtm, PayPal, Alipay, BTC, USDT payment methods**". Son **siete métodos nombrados de forma explícita**: Visa, Mastercard, **Airtm**, PayPal, **Alipay**, **BTC** y **USDT**.

## Why It Matters
Es el **catálogo de métodos de pago más desglosado del corpus de elusión**, porque hasta ahora los proveedores de proxy y captcha declaraban **métodos sin cifra asociada** (DataImpulse: "Alipay, Apple Pay, crypto wallet, Google Pay, Mastercard y Visa", **todos como icono**, y el único indicio de cripto era el genérico "crypto wallet", **sin cadena, ni moneda, ni dirección**, con **ninguna comisión por método de pago** publicada) y las comisiones medidas eran de otros ([[2026-1024-dataimpulse-metodos-de-pago-incluye-cripto]]). La diferencia con 2Captcha no está en que uno use imagen y el otro texto —ambos son iconos con texto alternativo—, sino en que **el de 2Captcha desglosa el cripto en dos instrumentos concretos, BTC y USDT**, frente al "crypto wallet" genérico de DataImpulse. El vault puede **nombrar** el instrumento cripto y distinguir Bitcoin de stablecoin al comparar proveedores.

Las dos inclusiones no triviales son **Airtm** —un agregador de pagos de LatAm— y **Alipay**, que ya aparecía en DataImpulse. La presencia conjunta de **Alipay + BTC + USDT + PayPal** dibuja un perfil de cliente: el mismo comprador puede pagar con métodos de Asia y de LatAm y con stablecoins, lo cual es exactamente el perfil de quien compra capacidad de elusión en volumen. Y es un recordatorio de que el **cripto en este sector es una vía de pago, no una postura de privacidad**: el único dato que el vault tiene de comisión en el sector es el **10 % de lzt.market al recargar con Mastercard** ([[2026-1023-lzt-topup-mastercard-comision-10]]), y 2Captcha **no publica ninguna comisión para ninguno de sus siete métodos**, con lo que el coste efectivo de sus $3.99/GB sigue siendo desconocido hasta el checkout.

Para el modelo de coste del vault, esto importa en un punto concreto: **la tabla de coste por insumo mide el precio de lista, y la lista solo es comparable entre proveedores si se sabe qué métodos aceptan y con qué comisión**. Con cuatro proveedores de proxy medidos antes —DataImpulse, IPRoyal, Bright Data y Decodo— el vault tiene ahora **cinco** declaradores de métodos de pago en la categoría, y solo Decodo (vía Paddle) publica su tratamiento fiscal.

## [FRICTION]
> [[2026-1024-dataimpulse-metodos-de-pago-incluye-cripto]] sostiene que "DataImpulse publica **ninguna comisión por método de pago**, así que el coste efectivo del gigabyte queda abierto hasta ver el checkout — el **10 % de lzt.market** sobre recarga con Mastercard es **la única comisión medida del sector**, y es de otro proveedor".
> Este átomo presiona esa lectura en un punto: **2Captcha también publica cero comisiones**, pero lo hace **desglosando el cripto en dos instrumentos nombrados, BTC y USDT**, mientras que DataImpulse lo deja en un "crypto wallet" genérico. Es decir, **la opacidad de la comisión no es una peculiaridad de DataImpulse: es la norma**, y ahora hay dos confirmaciones. O la ausencia de comisión publicada es un rasgo de los proveedores que **no tienen una entidad de cobro propia** (y entonces el 10 % de lzt —que sí la tiene, con su checkout— es la excepción), o es simplemente que **la mayoría del sector no considera que el coste final del proxy sea un dato de catálogo**. Marcado para juicio humano, no auto-resuelto: 2Captcha **no publica** comisión, ni VAT, ni cambio de divisa, de modo que el coste efectivo de sus $3.99/GB es desconocido con esta captura.

Nota: la captura **no** publica commission rates, VAT, tipo de cambio, ni condiciones de recharge minimum; los siete métodos aparecen **solo como texto alternativo de una imagen**.

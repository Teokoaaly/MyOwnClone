# Extensiones a átomos existentes — captura 2026-10-26-2captcha-pricing-residential-proxy

Fuente: `sources/2026-10-26-2captcha-pricing-residential-proxy.md` (captura `0-raw/2026-10-26-2captcha-pricing-residential-proxy.md`).
Ninguno de los átomos siguientes se ha modificado: las extensiones se proponen para el Editor.

=== EXTEND 2-atoms/2026-1026-decodo-escalera-mensual-de-375-a-275-por-gb.md
## Nota de extensión 2026-10-27
La captura del 2026-10-26 añade una **cuarta escalera de proxy residencial** y, con ella, el dato que faltaba para cerrar la comparación: **2Captcha publica el descuento en porcentaje y el volumen de cada tramo**, y su escalera baja de **$3.99/GB** (1 GB, 0 %) a **$1.25/GB** (10 TB, **−68,7 %**), con tramos intermedios en $3.59 (10 GB, −10 %), $2.99 (30 GB, −25,1 %), $2.25 (100 GB, −43,6 %), $1.99 (200 GB, −50,1 %), $1.8 (1 TB, −54,9 %), $1.49 (3 TB, −62,7 %) y $1.44 (5 TB, −63,9 %). Ver [[2026-1027-2captcha-proxy-residencial-de-399-a-125-por-gb-en-nueve-escalones]].

La comparación con este átomo es doble. **De precio**: la escalera de Decodo va de $3.75 a $2.75 en el tramo mensual y su PAYG está en $4/GB, de modo que **2Captcha tiene un precio de entrada casi idéntico ($3.99 frente a $3.75) y un suelo tres veces más bajo ($1.25 frente a $2.75)**. **De modelo**: Decodo es un plan **mensual** con desembolso recurrente y la columna de descuentos va implícita en los precios; 2Captcha es un **bloque de GB prepagado** con descuento explícito y sin suscripción. Es decir, **el mismo rango de entrada del sector ($3.75–$3.99) se puede comprar con compromiso mensual o sin compromiso, y el vault solo había medido la primera forma**. La conclusión de este átomo —"el precio unitario mejora con el compromiso de capital"— **no se generaliza más allá de los planes mensuales**, y la excepción no es un PAYG sino un cuarto modelo de cobro.

Nota: 2Captcha **no publica** VAT ni total por tramo, de modo que la comparación con la columna "+ VAT" de Decodo sigue siendo incompleta por el lado de 2Captcha.
=== END

=== EXTEND 2-atoms/2026-1024-brightdata-escalera-de-volumen-141-a-798-gb.md
## Nota de extensión 2026-10-27
La escalera de 2Captcha confirma la forma general de la escalera de Bright Data —**precio de entrada alto y descuento fuerte al subir de volumen**— y añade dos magnitudes que el vault no tenía. **Descuento**: −68,7 % en el tramo de 10 TB, contra los **−14 % y −17 %** de Bright Data y el **−26,7 %** de Decodo. **Precio unitario final**: **$1.25/GB**, por debajo del $2.50/GB del tramo de 798 GB de Bright Data.

La diferencia de fondo es el compromiso: **Bright Data exige $499/mes en su primer tramo**, y su "−14 %" es un descuento pequeño **sobre una base de compromiso alto**; 2Captcha alcanza un descuento **4,8 veces mayor** partiendo de un tramo de **1 GB**. Es decir, **la profundidad de la escalera no está correlacionada con la exigencia de capital**: hay una escalera profunda sobre un compromiso bajo y una escalera superficial sobre un compromiso alto. La afirmación de este átomo —que "**el descuento unitario del 14 % en el primer escalón de Bright Data cuesta $499/mes de golpe**"— **se aplica al subconjunto de planes mensuales** y el vault debe corregirla como una generalización, no como una ley del sector.

Nota: Bright Data declara el cupón `RESIGB50` y el *match* del primer depósito; **2Captcha no publica ninguna promoción**, solo precios y descuentos de volumen.
=== END

=== EXTEND 2-atoms/2026-1024-dataimpulse-payg-sin-suscripcion-ni-caducidad.md
## Nota de extensión 2026-10-27
La página de proxy residencial de 2Captcha **confirma el patrón de saldo prepago sin caducidad con un claim nuevo**, y lo hace en la forma menos obvia posible. Bajo una tabla de **precios por GB** —con nueve tramos de volumen y descuentos explícitos del 0 % al 68,7 %— la lista de inclusiones dice "**Unlimited traffic**", junto a "Flexible rotation options", "API access" y "SOCKS5 supported". Ver [[2026-1027-2captcha-unlimited-traffic-y-socks5-en-un-plan-facturado-por-gb]].

Es decir: **el claim de "sin caducidad" aquí se enuncia con el vocabulario del coste marginal nulo** ("tráfico ilimitado") y **no con el vocabulario del saldo** ("no caduca", "never expires"), en un producto cuyo precio es explícitamente "Price per GB". La conclusión que el thread sostiene con este átomo —que "**el contrato prepago sin caducidad es norma del sector y no una peculiaridad**"— **se refuerza en cuanto al comportamiento** y **se matiza en cuanto a la redacción**: dos de los tres proveedores con saldo prepago medidos (DataImpulse y, por inferencia, 2Captcha) no caducan, pero **solo uno de ellos lo dice con una fórmula no ambigua**.

Lo que 2Captcha **no** publica y este átomo sí necesita: si el saldo caduca, si el tráfico no consumido se factura, si existe recurrencia, y la duración de la sesión sticky. **Es el mismo conjunto de huecos que ya tenía este átomo**, lo que confirma que 2Captcha **no aporta un dato nuevo sobre el ciclo de vida del saldo**, sino un cuarto proveedor con el mismo ciclo.
=== END

=== EXTEND 2-atoms/2026-1024-dataimpulse-metodos-de-pago-incluye-cripto.md
## Nota de extensión 2026-10-27
La captura de 2Captcha cierra el hueco que este átomo señalaba: **el corpus ya puede nombrar el instrumento cripto, no solo inferirlo de iconos**. El bloque de compra de `2captcha.com/pricing/proxy` declara "**We accept these payment methods:**" con el texto alternativo "**We support Visa, Mastercard, Airtm, PayPal, Alipay, BTC, USDT payment methods**" — **siete métodos nombrados, con BTC y USDT por separado** — frente a los iconos sin cifra de DataImpulse ("Alipay, Apple Pay, crypto wallet, Google Pay, Mastercard y Visa", sin cadena, sin moneda, sin dirección). Ver [[2026-1027-2captcha-proxy-acepta-visa-mastercard-airtm-paypal-alipay-btc-y-usdt]].

Dos consecuencias. **Primera: "crypto wallet" como categoría era un agrupamiento,** y el desglose de 2Captcha lo sustituye por dos instrumentos concretos, de modo que **el vault puede distinguir Bitcoin de stablecoin** al comparar proveedores. **Segunda: Airtm es el primer agregador de pago de LatAm que aparece en el corpus de elusión**, y su presencia junto a Alipay dibuja un perfil de comprador: métodos de Asia, de LatAm y stablecoins en un mismo checkout. Y **ninguno de los dos publica comisión**, de modo que la conclusión de este átomo —"ninguna comisión por método de pago, el coste efectivo del gigabyte queda abierto hasta el checkout"— **queda confirmada y ampliada**: ya son dos los proveedores del corpus que no declaran comisión, y el único dato de comisión medido sigue siendo el 10 % de lzt.market sobre recarga con Mastercard, de otro sector.

Nota: Airtm, Alipay, BTC y USDT aparecen **solo como nombres en el texto alternativo de una imagen** —igual que los iconos de DataImpulse—; no hay rates, ni mínimos, ni condiciones por método.
=== END

=== EXTEND 2-atoms/2026-1024-iproyal-datacenter-139-por-proxy-y-60-ubicaciones.md
## Nota de extensión 2026-10-27
La captura de proxy residencial de 2Captcha aporta un **contraste de vocabulario que este átomo necesita**: 2Captcha promete "**Unlimited traffic**" en un producto **facturado por GB** ("Price per GB", con nueve tramos), mientras que el "**unlimited bandwidth**" de IPRoyal aparece en un producto **facturado por proxy** ($139/proxy, 60 ubicaciones). Ver [[2026-1027-2captcha-unlimited-traffic-y-socks5-en-un-plan-facturado-por-gb]].

La asimetría importa para el modelo de coste: **"unlimited" solo es un claim coherente cuando la unidad de cobro no es el tráfico**. En el datacenter de IPRoyal el cobro es por proxy y el ancho de banda no tiene coste marginal, de modo que "ilimitado" es exacto. En el proxy residencial de 2Captcha el cobro **es** por gigabyte, de modo que "tráfico ilimitado" solo puede significar **que el tráfico comprado no caduca o no se topa**, no que sea gratis. La conclusión de este átomo —que el "unlimited bandwidth" es **"la primera vez que el vault ve una partida de proxy sin coste marginal por volumen"**— **se convierte en un caso de estudio de dos**: **el mismo adjetivo aplicado a dos modelos de cobro opuestos**, y el vault no puede citarlos como equivalentes sin matizar.

Además, las otras dos inclusiones de 2Captcha ("SOCKS5 supported", "API access") **confirman que el soporte de protocolo y de API ya es estándar en el corpus de proxy**, y que la variable que discrimina entre proveedores ya no es el protocolo sino el precio y la sesión.
=== END

=== EXTEND 2-atoms/2026-1024-dataimpulse-gateway-unico-y-protocolos.md
## Nota de extensión 2026-10-27
La captura de proxy residencial de 2Captcha añade **una segunda vía de integración de proxy que no es el gateway HTTP**: la lista de inclusiones declara "**API access**" y "**SOCKS5 supported**", junto a "Flexible rotation options" y "Unlimited traffic". Ver [[2026-1027-2captcha-unlimited-traffic-y-socks5-en-un-plan-facturado-por-gb]].

El contraste es útil porque este átomo registraba, para DataImpulse, **un único gateway con ocho carpetas de targeting y credenciales generadas desde la API**, con SOCKS5 como una de las opciones de protocolo del gateway. En 2Captcha, **SOCKS5 y el acceso por API aparecen como dos inclusiones independientes del plan**, sin gateway único declarado. Es decir, **el corpus tiene ya dos arquitecturas de integración distintas** —gateway con credenciales por carpeta (DataImpulse) frente a acceso por API y SOCKS5 en paralelo (2Captcha)— y el vault no puede asumir que **"usar la API del proveedor" significa "usar su gateway"**.

Nota: la captura **no** publica el formato de las credenciales, la duración de la sesión sticky, ni el número máximo de conexiones simultáneas.
=== END

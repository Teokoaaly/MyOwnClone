---
id: 2026-1027-2captcha-unlimited-traffic-y-socks5-en-un-plan-facturado-por-gb
type: atom
certainty: solid
sources: [sources/2026-10-26-2captcha-pricing-residential-proxy.md]
links: ["[[2026-1024-dataimpulse-payg-sin-suscripcion-ni-caducidad]]", "[[2026-1024-iproyal-datacenter-139-por-proxy-y-60-ubicaciones]]", "[[2026-1024-dataimpulse-gateway-unico-y-protocolos]]"]
---
## Claim
Bajo la tabla de nueve planes, la página de proxy residencial de 2Captcha enumera cuatro inclusiones: "**Flexible rotation options**", "**API access**", "**SOCKS5 supported**" y "**Unlimited traffic**". Es decir, el producto se factura **por gigabyte comprado** ("Price per GB", con descuento por volumen) y, a la vez, promete **tráfico ilimitado** en su lista de características.

## Why It Matters
Es la **primera vez que el vault ve "unlimited traffic" en un producto que se factura por GB**. El único "unlimited" que tenía registrado era el "**unlimited bandwidth**" del datacenter de IPRoyal, y aquel era **precisamente** el caso cómodo: ahí se cobra **por proxy** y el ancho de banda no tiene coste marginal, con lo que "ilimitado" es coherente ([[2026-1024-iproyal-datacenter-139-por-proxy-y-60-ubicaciones]]). Aquí el modelo es el contrario: **se compra GB por adelantado y se promete que el tráfico no tiene límite** — lo que solo tiene una lectura consistente: **una vez comprados los GB, no hay tope de consumo ni caducidad**, es decir, el claim sustituye al límite por "no caduca" y no significa "gratis".

La diferencia importa porque el thread tiene un modelo explícito del saldo prepago: DataImpulse publica "**No expiry, no subscription**" y "**Traffic never expires**", con "pay only for the traffic you use" en el FAQ ([[2026-1024-dataimpulse-payg-sin-suscripcion-ni-caducidad]]). Si "Unlimited traffic" significa lo mismo, **el vault ya tiene una segunda confirmación del patrón** — y una fuente que además es más escueta, porque no dice "never expires" sino "unlimited". Si significa otra cosa (tráfico adicional sin límite dentro de los GB comprados, o ausencia de throttling por ancho de banda), el claim es distinto y el modelo de saldo se queda sin definir.

Las otras tres inclusiones completan el cuadro de integración: **rotación flexible sin duración de sesión publicada** (el thread ya sabe que la sesión sticky es la unidad que decide el coste, §8.2, y aquí no hay cifra), **acceso por API** (el mismo modo de integración que ya usa el captcha con su flujo de cinco pasos y `captcha ID`) y **SOCKS5**, el mismo protocolo que DataImpulse ya soportaba junto a HTTP/HTTPS y "Authorization by IP" ([[2026-1024-dataimpulse-gateway-unico-y-protocolos]]). Ninguna de las tres es nueva; lo nuevo es que **un proveedor de captcha publica ahora también proxy, con los mismos requisitos de integración**.

## [FRICTION]
> [[2026-1024-dataimpulse-payg-sin-suscripcion-ni-caducidad]] aporta la fórmula literal del contrato de saldo prepago sin caducidad —"**No expiry, no subscription**" y "**Traffic never expires**"—, y el thread lo eleva a norma: "**el contrato prepago sin caducidad es norma del sector y no una peculiaridad**" (§7), apoyado en el segundo proveedor independiente ([[2026-1024-iproyal-residencial-175-por-gb-y-pool-de-64m]]).
> Este átomo presiona esa normalización en un punto: **2Captcha dice "Unlimited traffic" en un producto cuyo precio es explícitamente "Price per GB"**, es decir, usa un vocabulario de coste marginal nulo en un producto cuyo precio es explícitamente marginal. Las dos lecturas son incompatibles en su consecuencia: o "unlimited" es sinónimo de "el tráfico comprado no caduca" (y entonces hay una **segunda** norma, pero el claim del vault sigue siendo válido porque significa lo mismo), o "unlimited" describe una garantía distinta —por ejemplo, ancho de banda sin throttling o un tier que no se agota— (y entonces **el claim es más fuerte que el de DataImpulse y hasta más fuerte que el "unlimited bandwidth" de IPRoyal**, que al menos se cobraba por proxy y no por GB). Marcado para juicio humano, no auto-resuelto: la captura **no** aclara el alcance de "Unlimited traffic" ni publica condiciones de saldo.

Nota: la captura **no** publica duración de sesión sticky, número de IPs o países, ni el formato de las credenciales, ni throughput o ancho de banda máximo.

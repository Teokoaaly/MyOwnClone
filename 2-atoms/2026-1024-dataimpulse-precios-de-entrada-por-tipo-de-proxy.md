---
id: 2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy
type: atom
certainty: solid
sources: [sources/2026-10-23-dataimpulse-proxies.md]
links: ["[[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]", "[[2026-1023-lzt-topup-mastercard-comision-10]]", "[[2026-1022-costes-por-categoria-tenant]]", "[[2026-1024-dataimpulse-escalera-de-volumen-por-tipo]]"]
---

## Claim
La home de DataImpulse fija el precio de entrada por gigabyte de cada uno de sus cuatro pools: **residencial $1/GB, datacenter $0.50/GB, móvil $2/GB y premium residencial $5/GB**, con un plan "Intro" de **$5** ("For New Users") en los cuatro tipos de proxy. El FAQ lo repite en su forma más directa: *"Residential starts from $1 per GB without a subscription. You pay only for the traffic you use. Mobile proxies start from $2/GB, and datacenter ones are the cheapest – just $0.50 per GB."*

## Why It Matters
El precio es el eje de posicionamiento del proveedor, no un detalle: dentro del mismo catálogo, el datacenter cuesta **la mitad** que el residencial, el móvil cuesta **el doble** y el premium residencial **cinco veces más**. Es una escala explícita de riesgo de bloqueo — datacenter = rápido y barato pero "best for sites that don't aggressively block server IPs"; móvil = "not the cheapest but still the strongest option" para verificación publicitaria y plataformas sociales.
Para el modelo de coste del vault esto cambia la jerarquía de insumos: el proxy **no** es un coste marginal pequeño al lado del SMS (que va de $0.1026 a $8.8897 por número en [[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]). A $1/GB, el tráfico de proxy puede dominar el coste de un alta si el flujo consume MB por sesión, y además es el único insumo cuyo coste depende de un volumen que el proveedor controla (tráfico no consumido = no facturado, ver [[2026-1024-dataimpulse-payg-sin-suscripcion-ni-caducidad]]).
El matiz de la comisión sigue vigente: si se recarga con Mastercard hay un 10 % de comisión sobre el saldo ([[2026-1023-lzt-topup-mastercard-comision-10]]), aunque DataImpulse no publica comisiones: su lista de métodos de pago es solo una fila de iconos, sin cifras.

## [FRICTION]
> [[2026-1022-costes-por-categoria-tenant]] afirma que el coste del producto se reparte en tres categorías — `categoryCloneResponses` y `categoryIngestion` (facturables al tenant) frente a `categoryPlatformOps` (memoria, embeddings, clasificadores internos, absorbidos por la plataforma) — y que "el consumo del tenant escala linealmente pero la operación interna no se traslada".
> Este átomo presiona ese corte porque el tráfico de proxy es un **tercer insumo variable con coste marginal explícito** (hasta $5/GB en premium residencial) que no encaja en ninguna de las tres categorías: no es respuesta de clon, ni ingesta, ni operación interna. En un pipeline de altas automatizadas con IP por cuenta, ese tráfico escala linealmente con el tenant, exactamente como las categorías facturables.
> Ambas no pueden ser completamente correctas: o el proxy entra como coste variable por tenant facturable (rompiendo la asunción de que las operativas internas no se trasladan), o se asume absorbido por la plataforma, con lo que su crecimiento lineal erosiona el margen de forma invisible en el panel de [[2026-1022-platform-admin-tenants-costes-mrr]]. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
Números transcritos literalmente de la home y del FAQ. La captura **no** publica: número máximo de conexiones simultáneas, ancho de banda por conexión, ni comisiones o cambio de divisa.

## Nota fechada — 2026-10-24 (captura IPRoyal, no modifica lo anterior)
Un segundo proveedor confirma que **el $/GB no es la unidad del sector**, solo la de DataImpulse. IPRoyal publica cinco líneas con **cinco unidades distintas**: residencial $1.75/GB (pool 64M+), ISP $1.80/proxy (500K+ IPs), datacenter $1.39/proxy (60+ ubicaciones, "unlimited bandwidth"), móvil $117/mes (4.5M+ IPs) y Web Unblocker $1.00/1000 requests. Es decir: el residencial de IPRoyal es **×1,75** del de DataImpulse, y el móvil pasa de coste marginal por GB a **coste fijo recurrente** ([[2026-1024-iproyal-cinco-lineas-y-cinco-unidades-de-precio]], [[2026-1024-iproyal-movil-117-al-mes-y-45m-de-ips]], [[2026-1024-iproyal-datacenter-139-por-proxy-y-60-ubicaciones]]). La escala de precios de este átomo sigue siendo válida **para el catálogo de DataImpulse**, pero no puede generalizarse al sector.


## Nota de extensión 2026-10-27
Este átomo construye una **escala explícita de riesgo de bloqueo** dentro de un mismo proveedor (datacenter $0.50/GB, residencial $1/GB, móvil $2/GB, premium residencial $5/GB) y concluye que "el proxy **no** es un coste marginal pequeño al lado del SMS" y que es "el único insumo cuyo coste depende de un volumen que el proveedor controla".

Con la captura del Browser API de 2Captcha del 2026-10-26, la segunda de esas dos afirmaciones **se acota**: hay ya un proveedor del corpus que **separa** el tráfico de navegación del tráfico de proxy y lo publica por separado —"$0.10/GB" de browser traffic, con "**Proxy traffic is billed separately**" ([[2026-1027-2captcha-browser-api-010-por-gb-con-el-proxy-facturado-a-parte]])—. Es decir, **el proxy deja de ser el único insumo con coste dependiente de volumen que nadie controla**: el GB de tráfico de navegador es exactamente eso, y además **con un precio unitario ($0,10) cinco veces por debajo del datacenter más barato del corpus**. La jerarquía "correo ≪ captcha ≪ proxy ≪ SMS" del thread **necesita una línea más**: hay ahora una partida —**tráfico de navegador**— que es más barata que el captcha y que se factura por volumen de red no controlado, pero **sin la IP dentro**.

**La consecuencia metodológica es más fuerte que el dato de precio**: la escala de riesgo de bloqueo que este átomo construye **no es transferible**, porque depende de qué se compra con el GB. El datacenter barato de DataImpulse es "rápido y barato pero no para sitios que bloquean IPs de servidor"; el GB de 2Captcha **no compra ninguna IP**. La misma magnitud nominal —GB— cubre en un caso el acceso con una IP de riesgo conocido y en el otro solo el cómputo del navegador, con lo que cualquier comparación entre los dos $/GB está comparando paquetes distintos.

Nota de verificación: la captura de 2Captcha **no** publica el precio de sus proxies ni el precio de los proxies de terceros que el cliente puede traer; el "0,10/GB" es literal y es solo tráfico de navegador.


## Nota de extensión 2026-10-27
La landing móvil **añade el benchmark de sector que el vault no tenía para el pool móvil**, y además lo publica en dos formas que no coinciden. En la prosa: **"$2/GB for DataImpulse mobile proxies vs $3/GB for industry average mobile proxies"**. En la tabla "DataImpulse vs Average Mobile Proxy Provider": el precio del promedio del sector figura como **"~$3-$8 per GB, Monthly fees"**. La diferencia entre "$3/GB" y "~$3-$8 per GB" **no es una discrepancia de redondeo**: es la diferencia entre una cifra puntual y un rango, y ambas conviven en la misma página. Es además la **primera cifra de "media del sector" que el vault tiene para el móvil**, y sitúa el precio de DataImpulse en el **extremo bajo del rango**, no en el medio.
El FAQ "What is the cheapest mobile proxy provider?" añade la **unidad que faltaba**: **"Some providers charge per port per day ($2–7/day), others per gigabyte."** Es decir, en el móvil hay **tres unidades en juego** —GB, puerto-día y mes (este último con el móvil de IPRoyal a $117/mes, [[2026-1024-iproyal-movil-117-al-mes-y-45m-de-ips]])— y el vault solo tenía medidas dos. Átomos nuevos: [[2026-1027-dataimpulse-movil-2-a-7-dolares-por-puerto-y-dia]] y [[2026-1027-dataimpulse-tabla-comparativa-con-el-promedio-movil]].
La confirmación del precio de entrada móvil ($2/GB, plan Intro de $5 por 2,5 GB) también **ratifica la lectura del vault de que el $/GB es un parámetro de proveedor y no de mercado**: el mismo producto aparece en este corpus a $2/GB, a $117/mes y a $0,50/GB en datacenter, y ahora con un "promedio de sector" declarado entre $3 y $8/GB.

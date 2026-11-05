---
id: 2026-1026-decodo-pool-de-115m-en-el-cuerpo-y-125m-en-el-pie
type: atom
certainty: solid
sources: [sources/2026-10-25-decodo-residential-pricing.md]
links: ["[[2026-1024-brightdata-400m-de-ips-en-195-paises-con-targeting-gratis]]", "[[2026-1024-iproyal-pool-de-64m-sin-desglose-geografico]]", "[[2026-1026-decodo-targeting-a-nivel-de-asn-y-zip-incluido-gratis]]"]
---

## Claim
La página de precios de Decodo declara **dos cifras distintas de pool en el mismo documento**. El cuerpo del producto dice **"115M+ ethically-sourced IPs in 195+ locations"** (repetido en "Premium quality": "an extensive 115M+ IPs from 195+ locations"), y el pie de página cierra con **"125M+ IPs from 195+ locations"**. Los 195+ países coinciden en ambas; **el número de IPs no**.

## Why It Matters
Es el mismo patrón que el vault ya registró en Anubiz (doce declaradas frente a diez enumeradas) y en BitLaunch (27 declaradas frente a 25 entradas): **el pool de un proveedor es un claim, no un inventario**, y aquí además es **un claim contradictorio dentro de una misma página**.
El efecto directo es sobre la comparabilidad con lo ya medido: Bright Data declara **400M+** ([[2026-1024-brightdata-400m-de-ips-en-195-paises-con-targeting-gratis]]), IPRoyal **64M+** ([[2026-1024-iproyal-pool-de-64m-sin-desglose-geografico]]), DataImpulse **90M+**. Con Decodo, la tabla de pools del vault queda **115M+ o 125M+** — un intervalo del 8,7 % sin resolver dentro de una sola fuente. En la práctica, la cifra que decide para un flujo de verificación no es el pool bruto sino **la granularidad por país**, y Decodo **no publica ni un solo desglose por país, ciudad o ASN**: solo el agregado y los 195+ países.
El matiz que sí publica Decodo, y que ningún otro del corpus publica, es **"ethically-sourced"** con "115M+ ethically-sourced IPs" — que es el mismo argumento de origen que DataImpulse usa ("first-party, no third-party resellers") pero aquí **sin ninguna cifra de consentidores ni auditoría adjunta**.

## [FRICTION]
> [[2026-1024-brightdata-400m-de-ips-en-195-paises-con-targeting-gratis]] compara pools por magnitud ("400M+ frente a 90M+ de IPs") y usa la coincidencia de **195+ países** como prueba de que la escala de país es alike sectorial.
> Este átomo presiona esa comparación en el punto de la granularidad: **con Decodo, el número de IPs publicados es internamente inconsistente (115M+ y 125M+ en la misma página)**, de modo que ordenar proveedores por pool exige elegir una de las dos cifras de una fuente que ella misma se contradice. Y el desglose geográfico que sí tenía DataImpulse (India 2.374.712, Brasil 1.252.375) **no aparece en Decodo**: no hay ni una fila por país.
> Ambas no pueden ser completamente correctas: o el tamaño del pool es una magnitud comparable entre proveedores, o es un claim publicitario que cada proveedor emite con su propio redondeo —y en ese caso el criterio operativo del vault (país real de la IP == país de la identidad) **no se puede auditar en Decodo con esta captura**. Marcado para juicio humano, no auto-resuelto: la contradicción es de la propia página y el desglose no existe.

## Nota de verificación
Ambas cifras transcritas literalmente, cada una de su punto de la página. La captura **no** publica: qué cuenta cada cifra (IPs únicas, proxies o rotaciones), el desglose por país, ni el número de consentidores.


## Nota de extensión 2026-10-27
La home **añade el desglose por país** que este átomo declaraba ausente ("Decodo **no publica ni un solo desglose por país, ciudad o ASN**"), y **mantiene la contradicción del pool**: el FAQ dice *"Decodo's residential proxy network includes **115M+ ethically-sourced IPs across 195+ locations**"* y el pie cierra con **"125M+ IPs from 195+ locations"**.

El desglose publicado es de **diez países**, cada uno con recuento y enlace a su propia página de proxies: **United States 16M+**, **India 11M+**, **Germany 5.6M+**, **United Kingdom 5M+**, **France 4.6M+**, **Spain 3.7M+**, **Canada 3M+**, **Italy 2M+**, **Australia 1M+**, **Netherlands 870K+**. La suma es **52,77M**, es decir **42,2 %** del pool declarado de 125M o **45,9 %** del de 115M.

Dos precisiones que el vault necesita para no sobreinterpretar: (1) el desglose es **agregado y no está atribuido por producto** —la página es la home de proxies, no un desglose de la API—, y (2) **la captura no publica la metodología de los recuentos ni si estos diez países son los diez mayores**. La contradicción 115M+/125M+ **sigue viva y ahora convive con un desglose que no reconcilia ninguna de las dos cifras**. Ver [[2026-1027-decodo-home-publica-diez-paises-con-conteo-de-ips-que-contradice-el-atom-del-pool]].

---
id: 2026-1026-decodo-targeting-a-nivel-de-asn-y-zip-incluido-gratis
type: atom
certainty: solid
sources: [sources/2026-10-25-decodo-residential-pricing.md]
links: ["[[2026-1024-brightdata-400m-de-ips-en-195-paises-con-targeting-gratis]]", "[[2026-1024-dataimpulse-cobertura-195-paises-y-targeting-gratis-por-pais]]", "[[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]]"]
---

## Claim
La lista de lo que incluye cada plan de Decodo incluye **"Continent, country, state, city, ZIP code, and ASN-level targeting"**, y el párrafo introductorio lo declara **gratis**: "Every plan includes the full access to 115M+ IP pool and **free advanced targeting**". Se suman **HTTP(S) & SOCKS5**, **"Rotating and sticky session options"**, **"<0.5s avg. response time"**, **"99.92% success rate"** y **"99.99% uptime"**.

## Why It Matters
El **targeting a nivel de ASN** es la granularidad más fina que el vault ha visto publicada en un proveedor de proxy, y es exactamente la que el criterio operativo del vault exige: que el país real de la IP coincida con el país de la identidad usada ([[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]]). El ASN identifica el bloque de enrutamiento real, no una etiqueta geográfica declarada: es el dato que permite descartar una IP "de España" que en realidad sale por un ASN de otro país.
Y como en Bright Data ([[2026-1024-brightdata-400m-de-ips-en-195-paises-con-targeting-gratis]]), **el targeting granular viene gratis en todos los planes**, incluido el de 3 GB a $11.25 — mientras que DataImpulse solo lo hace gratis en el Premium Residencial y lo cobra por país en los demás ([[2026-1024-dataimpulse-cobertura-195-paises-y-targeting-gratis-por-pais]]). Eso significa que **el coste de cumplir el criterio de coincidencia país-IP es cero en Decodo y en Bright Data, y distinto de cero en DataImpulse**: la partida se elimina del modelo de coste en dos de los tres proveedores medidos.
El resto de la lista son **cifras de marketing de página**: <0,5 s, 99,92 % de éxito y 99,99 % de uptime, sin methodology adjunta en la lista de features (el FAQ sí declara que las métricas proceden de la investigación de Proxyway 2024, ver [[2026-1026-decodo-metricas-de-proxyway-2024-como-fuente-de-las-cifras-de-exito-y-uptime]]).

## Nota de verificación
Transcripción literal. La captura **no** publica: cuántos ASN son seleccionables, si el targeting por ASN aplica a todos los países o solo a los que tienen ASN propio, ni el desglose de IPs por ASN.


## Nota de extensión 2026-10-27
La home amplía **el alcance del targeting** que este átomo documenta para la línea residencial: *"Targeting by **state, city, or ASN** is now available for **datacenter and ISP proxies**."* Es decir, el targeting granular que este átomo registraba como **exclusivo y gratuito del residencial** se extiende ahora —con la misma marca de "now available", es decir, **novedad**— a las dos redes estáticas, que son justo las que el vault cotiza **por IP** en la tabla de coste por insumo ([[2026-1024-iproyal-isp-180-por-proxy-y-500k-ips]], [[2026-1024-iproyal-datacenter-139-por-proxy-y-60-ubicaciones]]).

El bloque de geolocalización añade dos niveles que este átomo no recogía: **"195+ locations"** con **"City-level targeting"**, y el texto *"Access public web data across the globe with **continent-, country-, state-, city-, and ASN-level targeting**"* — es decir, **targeting a nivel de continente**, el más fino publicado en el corpus de proxy, y por encima del ZIP que este átomo Thought máximo.

Consecuencia para el modelo de coste: **la partida de "elegir la ubicación correcta" tiene precio cero en Decodo también en las redes estáticas**, lo que refuerza la regla ya registrada —el coste de cumplir el criterio país-real-de-la-IP == país-de-la-identidad **es cero en Decodo** ([[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]])— y hace más Comparable la comparación de $0,27/IP y $0,02/IP con los $1,80/IP y $1,39/IP de IPRoyal.

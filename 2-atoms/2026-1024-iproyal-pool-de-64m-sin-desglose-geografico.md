---
id: 2026-1024-iproyal-pool-de-64m-sin-desglose-geografico
type: atom
certainty: solid
sources: [sources/2026-10-24-iproyal-pricing.md]
links: ["[[2026-1024-iproyal-residencial-175-por-gb-y-pool-de-64m]]", "[[2026-1024-dataimpulse-cobertura-195-paises-y-targeting-gratis-por-pais]]", "[[2026-1024-iproyal-cinco-lineas-y-cinco-unidades-de-precio]]", "[[2026-1024-2captcha-hcaptcha-y-geetest-ausentes-del-catalogo-publicado]]"]
---

## Claim
Las cifras de escala de IPRoyal son **claims con signo "+" y sin ningún desglose**: **"64M+ proxy pool"** (residencial), **"500K+ unique IPs"** (ISP), **"4.5M+ IPs"** (móvil) y **"60+ locations"** (datacenter). No hay ni un solo país, ciudad ni ASN enumerado, ni un desglose de IPs por ubicación, ni un contador visible. La única "geografía" publicada es el recuento de ubicaciones del datacenter.

## Why It Matters
Es el mismo patrón que el vault ya registró con 5sim, HeroSMS y NoOnes: **el proveedor publica un agregado sin inventario** ([[2026-1024-dataimpulse-cobertura-195-paises-y-targeting-gratis-por-pais]] es el contraejemplo — DataImpulse sí tabula IPs por país, con India 2.374.712 y EE.UU. 533.615). La diferencia con DataImpulse no es de honestidad sino de **granularidad**: 64M+ frente a 90M+ son dos números agregados incomparables, y el "64M+" **no dice de dónde son las IPs**, que es exactamente la variable que decide si un pool sirve para el pipeline del vault (país de la IP == país de la identidad usada).
Y el "64M+" tiene además una ambigüedad de unidad no resuelta: "proxy pool" puede contar proxies, IPs únicas o rotaciones posibles, mientras el móvil dice "4.5M+ IPs" y el ISP "500K+ **unique** IPs". El vault no puede sumar ni comparar esas tres cifras sin saber qué cuenta cada una.

## Nota de verificación
Cifras transcritas literalmente de las cinco tarjetas. La captura **no** publica: ningún nombre de país, ni la lista de las 60+ ubicaciones del datacenter, ni el número de IPs por ubicación, ni definición de "unique" para el pool ISP. Todos los "+" son claims sin verificación adjunta.

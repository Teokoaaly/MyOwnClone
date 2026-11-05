---
id: 2026-1027-decodo-tablero-de-precios-de-la-home-con-ocho-lineas-y-cinco-unidades
type: atom
certainty: solid
sources: [sources/2026-10-26-decodo-smartproxy-home.md]
links: ["[[2026-1024-iproyal-cinco-lineas-y-cinco-unidades-de-precio]]", "[[2026-1026-decodo-escalera-mensual-de-375-a-275-por-gb]]", "[[2026-1024-iproyal-movil-117-al-mes-y-45m-de-ips]]", "[[2026-1026-decodo-integraciones-de-navegador-y-agentes-como-gratis-con-cada-plan]]"]
---

## Claim
La home de Decodo publica un **tablero de precios de ocho líneas con cinco unidades distintas**, todas en formato "From": **Web Data API — From $0.15/1K**, **Video Downloader — From $0.08/GB**, **Residential Proxies — From $2/GB**, **ISP Proxies — From $0.27/IP**, **Mobile Proxies — From $2.25/GB**, **Datacenter Proxies — From $0.02/IP**, **Site Unblocker — From $0.95/1K req** y **High-Speed Proxies — Price on request**. Debajo, una tercera sección lista **Free tools**: **Chrome Proxy Extension**, **Firefox Add-on** y **Proxy Checker**, los tres con "Free" y "Try now" propio.

Cuatro de estas cifras **no existían en el vault**: **Video Downloader a $0,08/GB** (línea de producto nueva, sin equivalente en ningún otro proveedor medido), **ISP a $0,27/IP**, **Mobile a $2,25/GB** y **Datacenter a $0,02/IP**. Y una más es relevante para el modelo de coste: **High-Speed Proxies no tiene precio**, solo "Contact sales".

## Why It Matters
El tablero de la home es **la segunda tabla de precios completa del vault con unidades mezcladas**, y por eso remata el problema que el átomo de IPRoyal dejó abierto ([[2026-1024-iproyal-cinco-lineas-y-cinco-unidades-de-precio]]): la diferencia es que **aquí hay ocho líneas y cinco unidades, y las unidades no coinciden con las de ningún otro proveedor**. En el mismo pantallazo conviven $/1K, $/GB, $/IP y "precio a consultar" — con lo que **la mitad del catálogo de Decodo no es comparable con la mitad del de nadie**.

Las tres cifras nuevas cambian la tabla de coste por insumo del thread en tres puntos:

- **Datacenter a $0,02/IP**: es **×25 más barato** que el $1,39/proxy de datacenter de IPRoyal ([[2026-1024-iproyal-datacenter-139-por-proxy-y-60-ubicaciones]]) y **×70 más barato** que el $1,40–$1,80/IP de Bright Data. Con eso, la partida de proxy barato del vault **deja de estar en el rango de $1+/IP** y entra en una zona de céntimos: **el datacenter de Decodo cuesta lo que cuesta un GB de DataImpulse ($0,50/GB) dividido por 25**.
- **ISP a $0,27/IP**: **×6,7 más barato** que el $1,80/proxy de ISP de IPRoyal. Es la primera vez que el vault ve una **IP estática de proveedor a precio de céntimos**, lo que replantea la partida de "identidad estable" del modelo de coste ([[2026-1024-iproyal-isp-180-por-proxy-y-500k-ips]]).
- **Mobile a $2,25/GB**: **por debajo de los $5/GB del Premium Residencial de DataImpulse** y por encima del $2/GB móvil de DataImpulse, y **con la particularidad de estar cotizada en la misma unidad que el residencial** —lo que hace comparables las dos líneas internas de Decodo, cosa que en IPRoyal no ocurría (el móvil allí era $/mes fijo, [[2026-1024-iproyal-movil-117-al-mes-y-45m-de-ips]]).

El punto que hay que no perder de vista es **la línea sin precio**: "High-Speed Proxies — Price on request" es la **segunda partida no cotizable** que la home de Decodo deja abierta (la primera es el Enterprise de la API, que va a "Contact sales"). Es decir, **en el catálogo más amplio del proveedor, dos de las líneas más relevantes —alta velocidad y enterprise— no se pueden cotizar desde el catálogo público**, y esa es exactamente la forma que la thread ya registró en Bright Data: la línea de empresa es la única partida cuyo precio no existe en ninguna captura ([[2026-1024-proton-ofrece-vpn-para-empresas-sin-precio-publicado]]).

Y el **Video Downloader a $0,08/GB** es, aritméticamente, **el precio por gigabyte más bajo de todo el corpus**: por debajo del $0,50/GB de datacenter de DataImpulse ([[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]). No es comparable como insumo de proxy —es descarga de vídeo, presumably sin residential ni rotación— pero su existencia es la prueba de que **el $/GB de Decodo no tiene un suelo de mercado**: es el mismo byte con precio distinto según para qué se use.

## Nota de verificación
Ocho líneas y tres herramientas transcritas literalmente. La captura **no** publica: qué incluyen los $2,25/GB de móvil (¿direcciones rotativas? ¿sticky?), si los $0,02/IP de datacenter son por IP y por cuánto tiempo, ni la definición de "High-Speed" ni sus condiciones. La equivalencia "Video Downloader = descarga de vídeo" es una lectura del nombre del producto, no una descripción de la fuente.

## Nota relacionada
El precio **residencial** de este mismo tablero ($2/GB) es el titular cuyo análisis ya está en [[2026-1026-decodo-titular-de-2-por-gb-y-entrada-real-de-375]] y [[2026-1026-decodo-escalera-mensual-de-375-a-275-por-gb]]; aquí lo que es nuevo es el **resto del tablero** y, sobre todo, el hecho de que la home lo presente **junto a la API de scraping** en la misma pantalla, lo que hace que el vault tenga que elegir **qué línea** está cotizando antes de comparar con nadie.

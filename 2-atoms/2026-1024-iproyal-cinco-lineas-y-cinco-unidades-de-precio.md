---
id: 2026-1024-iproyal-cinco-lineas-y-cinco-unidades-de-precio
type: atom
certainty: solid
sources: [sources/2026-10-24-iproyal-pricing.md]
links: ["[[2026-1024-iproyal-residencial-175-por-gb-y-pool-de-64m]]", "[[2026-1024-iproyal-isp-180-por-proxy-y-500k-ips]]", "[[2026-1024-iproyal-datacenter-139-por-proxy-y-60-ubicaciones]]", "[[2026-1024-iproyal-movil-117-al-mes-y-45m-de-ips]]", "[[2026-1024-iproyal-web-unblocker-ia-a-1-dolar-por-1000-solicitudes]]", "[[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]", "[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]"]
---

## Claim
La página de precios de IPRoyal publica **cinco líneas de producto con cinco unidades de precio distintas**, y ninguna de las cinco coincide con la unidad de las otras cuatro: **Residencial desde $1.75/GB** (pool de 64M+ proxies), **ISP desde $1.80/proxy** (500K+ IPs únicas), **Datacenter desde $1.39/proxy** (60+ ubicaciones), **Mobile desde $117/mes** (4.5M+ IPs) y **Web Unblocker desde $1.00/1000 requests** (IA). La página no publica una tabla única: es un carrusel de cinco tarjetas, cada una con su precio "from", su cifra de escala y su párrafo de posicionamiento.

## Why It Matters
La consecuencia no es el precio: es que **IPRoyal no es comparable con el otro proveedor de proxy del vault sin una tabla de conversión**. DataImpulse publica sus cuatro pools íntegramente **por GB** ([[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]), así que su tabla se puede leer de un vistazo; IPRoyal mezcla **por GB, por proxy, por mes y por mil de solicitudes** en la misma pantalla. Cualquier comparación "IPRoyal vs DataImpulse" tiene que empezar por declarar en qué unidad se compara, y tres de las cinco unidades de IPRoyal **no tienen equivalente publicado** en DataImpulse.
La quinta unidad es la más importante: el Web Unblocker se factura **por 1000 solicitudes**, que es exactamente la unidad de 2Captcha ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]) y la de ningún otro insumo del vault. Es la señal de que el mercado está convergiendo hacia **cobrar por el resultado (peticiones desbloqueadas) en vez de por el recurso (bytes)**.

## Nota de verificación
Precios y cifras transcritos literalmente de las cinco tarjetas de `iproyal.com/pricing/`. La captura **no** publica: duración o ancho de banda incluidos en un "proxy" de ISP o datacenter, qué cubre exactamente el mes de $117 en móvil, ni el tipo de cambio, IVA o comisiones por método de pago. La captura es un **render plano**: el orden literal del texto intercala el precio, la cifra de escala y el nombre del producto en una secuencia que se repite cinco veces, de modo que la correspondencia precio↔producto está confirmada por esa repetición y no por una tabla.


## Nota de extensión 2026-10-27
Decodo publica en su home un tablero de **ocho líneas con cinco unidades de precio** —Web Data API **$0.15/1K**, Video Downloader **$0.08/GB**, Residential **$2/GB**, ISP **$0.27/IP**, Mobile **$2.25/GB**, Datacenter **$0.02/IP**, Site Unblocker **$0.95/1K req** y High-Speed **"Price on request"**—, más **tres herramientas gratuitas** (Chrome Proxy Extension, Firefox Add-on, Proxy Checker). Es el **segundo tablero del corpus con unidades mezcladas**, y el que más unidades añade por línea.

Tres datos que este átomo deja ahora disponibles para la tabla de coste por insumo, y que **no aparecen en ningún otro proveedor medido**: **datacenter a $0,02/IP** (×25 más barato que el $1,39/IP de IPRoyal), **ISP a $0,27/IP** (×6,7 más barato que el $1,80/IP de IPRoyal) y **móvil a $2,25/GB** (la primera vez que el móvil de un proveedor se cotiza **en la misma unidad que el residencial**, lo que hace comparables las dos líneas internas de Decodo; en IPRoyal el móvil era $/mes fijo, [[2026-1024-iproyal-movil-117-al-mes-y-45m-de-ips]]).

Y un patrón que el tablero hace explícito: **la línea de empresa vuelve a quedar fuera del catálogo**. "High-Speed Proxies — Price on request" es la segunda partida no cotizable de Decodo, después del Enterprise de la API — el mismo hueco que este átomo ya detectara en Proton ([[2026-1024-proton-ofrece-vpn-para-empresas-sin-precio-publicado]]). Ver [[2026-1027-decodo-tablero-de-precios-de-la-home-con-ocho-lineas-y-cinco-unidades]].

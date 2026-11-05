# Extensiones a átomos existentes — captura 2026-10-26-decodo-smartproxy-home

Fuente: `sources/2026-10-26-decodo-smartproxy-home.md` (captura `0-raw/2026-10-26-decodo-smartproxy-home.md`).
Ninguno de los átomos siguientes se ha modificado: las extensiones se proponen para el Editor.

=== EXTEND 2-atoms/2026-1026-decodo-rebranding-desde-smartproxy-con-url-y-pie-en-la-misma-pagina
## Nota de extensión 2026-10-27
La home **cierra dos huecos** que este átomo declaraba abiertos ("la captura **no** publica: la fecha del rebranding…").

Primero, **la fecha**: el FAQ responde *"Is Decodo the same company as Smartproxy?"* con **"Yes… Smartproxy officially became Decodo in April 2025. It's the same company, team, infrastructure, and proxy network, now under a new name that reflects our broader web data platform."** Es decir, **el rebranding es de abril de 2025**, y no de 2026: la marca lleva más de un año publicada con el nombre nuevo mientras el vault seguía capturando `smartproxy.com`. La sección de la home se titula literalmente **"Smartproxy is now Decodo"** y el FAQ añade **"the same trusted team and solutions you've relied on since 2018"** — el rango de antigüedad declarado es 2018, no 2025.

Segundo, **el aviso de suplantación**: *"Just be careful with the old name: **Smartproxy.org isn't us. It's an impersonator** and has no connection to Decodo, our team, or our infrastructure. **The only official Decodo website is Decodo.com.**"* Es el mismo patrón de persistencia de dominio que el vault ya registró con SMS-Activate ([[2026-1024-sms-activate-ru-sirve-el-mismo-aviso-que-el-dominio-org]]), pero aquí invertido: **no es un negocio que desaparece dejando vivo su dominio**, es una marca que **avisa activamente** del impostor.

Tercero, **una captura más de la doble identidad**: el pie de esta home —capturada en `smartproxy.com`— dice **"© 2018-2026decodo.com (formerly smartproxy.com). All Rights Reserved"**, igual que la página de precios del 2026-10-25. Dos capturas distintas, dos dominios distintos de marca, **un mismo actor**, y una fecha de cambio de nombre que ahora el vault conoce. Ver [[2026-1027-decodo-smartproxy-org-es-un-impostor-y-el-mismo-equipo-desde-2018]].
=== END

=== EXTEND 2-atoms/2026-1026-decodo-pool-de-115m-en-el-cuerpo-y-125m-en-el-pie
## Nota de extensión 2026-10-27
La home **añade el desglose por país** que este átomo declaraba ausente ("Decodo **no publica ni un solo desglose por país, ciudad o ASN**"), y **mantiene la contradicción del pool**: el FAQ dice *"Decodo's residential proxy network includes **115M+ ethically-sourced IPs across 195+ locations**"* y el pie cierra con **"125M+ IPs from 195+ locations"**.

El desglose publicado es de **diez países**, cada uno con recuento y enlace a su propia página de proxies: **United States 16M+**, **India 11M+**, **Germany 5.6M+**, **United Kingdom 5M+**, **France 4.6M+**, **Spain 3.7M+**, **Canada 3M+**, **Italy 2M+**, **Australia 1M+**, **Netherlands 870K+**. La suma es **52,77M**, es decir **42,2 %** del pool declarado de 125M o **45,9 %** del de 115M.

Dos precisiones que el vault necesita para no sobreinterpretar: (1) el desglose es **agregado y no está atribuido por producto** —la página es la home de proxies, no un desglose de la API—, y (2) **la captura no publica la metodología de los recuentos ni si estos diez países son los diez mayores**. La contradicción 115M+/125M+ **sigue viva y ahora convive con un desglose que no reconcilia ninguna de las dos cifras**. Ver [[2026-1027-decodo-home-publica-diez-paises-con-conteo-de-ips-que-contradice-el-atom-del-pool]].
=== END

=== EXTEND 2-atoms/2026-1026-decodo-metricas-de-proxyway-2024-como-fuente-de-las-cifras-de-exito-y-uptime
## Nota de extensión 2026-10-27
La home **añade una tercera cifra de éxito, más alta y más específica** que la de este átomo: *"**99.99% success** on the hard, anti-bot-protected targets such as **Amazon and Cloudflare-protected sites** – that trip up most AI-native scraping tools."* El hero añade además **"<0.2s response time"** y **"99.99% uptime"**.

El contraste con este átomo es el que importa: la cifra de **99,92 %** es una **medición de tercero con método publicado** (500 peticiones por endpoint contra `ipinfo.io/ip`, sesión rotativa, VPN del mismo país, Proxyway 2024), y su propio límite —documentado aquí— es que **mide conectividad, no supervivencia ante un sitio que bloquea**. La cifra de la home de **99,99 %** es exactamente la que mide esa segunda cosa, **pero sin método**: no dice cuántas peticiones, contra qué URLs, en qué ventana ni qué cuenta como éxito. Y la latencia **se duplica** entre el hero (**<0,2 s**) y la página de precios (**<0,5 s**).

Consecuencia práctica para el vault: **ninguna de las dos cifras puede usarse como parámetro de reintentos**. Con 99,92 % medido, el número de fallos es acotable; con 99,99 % sin método, es desconocido — y en un producto facturado por mil de requests, **cada reintento es cuota consumida**, así que el coste del fallo es idéntico al del éxito. Ver [[2026-1027-decodo-9999-de-exito-en-destinos-anti-bot-como-amazon-y-cloudflare]].
=== END

=== EXTEND 2-atoms/2026-1026-decodo-135k-clientes-y-cinco-años-de-premio-proxyway-como-escala
## Nota de extensión 2026-10-27
Este átomo declaraba como hueco que la captura "**no publica: número de reseñas, puntuación**". La home **publica las tres**, con denominador: **Trustpilot 4,2/5 con 2.116 reseñas**, **G2 4,6/5 con 700+ reseñas** y **Proxyway 9,3/10**, esta última con la precisión de que sus pruebas incluyen "independent tests of its **Web Scraping API, residential, mobile, ISP, and datacenter proxies**".

El dato que hay que registrar no es la puntuación sino **la dispersión entre plataformas**: **0,4 puntos de diferencia** entre el canal de Consumidores finales (Trustpilot, 4,2) y el de compradores enterprise (G2, 4,6), con denominadores del mismo orden (2.116 frente a 700+). Es un patrón de canal, no de proveedor: **el mismo producto puntúa peor donde lo compra el usuario final que donde lo compra la empresa**. Y la escala de clientes de este átomo (**135 000+**) queda ahora **corroborada por dos fuentes de reseñas independientes**, que es el tipo de triangulación que el vault no tenía en ningún otro proveedor de proxy.

El matiz que sigue abierto: la marca **también usa los premios como sustituto de SLA** (Proxyway "Best Value 2025" por quinto año, G2 "Best Usability 2025"), y las reseñas no son un compromiso contractual. Ver [[2026-1024-iproyal-premios-y-distintivos-como-sustituto-de-sla]].
=== END

=== EXTEND 2-atoms/2026-1026-decodo-targeting-a-nivel-de-asn-y-zip-incluido-gratis
## Nota de extensión 2026-10-27
La home amplía **el alcance del targeting** que este átomo documenta para la línea residencial: *"Targeting by **state, city, or ASN** is now available for **datacenter and ISP proxies**."* Es decir, el targeting granular que este átomo registraba como **exclusivo y gratuito del residencial** se extiende ahora —con la misma marca de "now available", es decir, **novedad**— a las dos redes estáticas, que son justo las que el vault cotiza **por IP** en la tabla de coste por insumo ([[2026-1024-iproyal-isp-180-por-proxy-y-500k-ips]], [[2026-1024-iproyal-datacenter-139-por-proxy-y-60-ubicaciones]]).

El bloque de geolocalización añade dos niveles que este átomo no recogía: **"195+ locations"** con **"City-level targeting"**, y el texto *"Access public web data across the globe with **continent-, country-, state-, city-, and ASN-level targeting**"* — es decir, **targeting a nivel de continente**, el más fino publicado en el corpus de proxy, y por encima del ZIP que este átomo Thought máximo.

Consecuencia para el modelo de coste: **la partida de "elegir la ubicación correcta" tiene precio cero en Decodo también en las redes estáticas**, lo que refuerza la regla ya registrada —el coste de cumplir el criterio país-real-de-la-IP == país-de-la-identidad **es cero en Decodo** ([[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]])— y hace más Comparable la comparación de $0,27/IP y $0,02/IP con los $1,80/IP y $1,39/IP de IPRoyal.
=== END

=== EXTEND 2-atoms/2026-1026-decodo-prueba-de-3-dias-con-100-mb-y-autoactivacion-del-plan
## Nota de extensión 2026-10-27
La home confirma la existencia de **dos free tiers distintos** en la misma marca, y el FAQ los separa con precisión: *"Decodo offers a **3-day free trial for proxies**, as well as a **free starter plan for its Web Data API** that includes **$5 in testing credits (up to 10k requests) with no credit card required** to get started."*

Lo que este átomo establece —que la prueba de proxies **auto-activa el plan de pago** al terminar y por tanto **anula la garantía de 14 días**— **se mantiene sin cambio**, pero ahora hay que leerlo junto a un dato nuevo: **la Web Data API no tiene trial sino plan gratuito permanente**, y el banner de cierre de la home dice **"up to 10K free monthly requests"**. Es decir: **la línea de scraping tiene una entrada recurrente y sin tarjeta**, y la línea de proxy tiene una prueba de tres días que **convierte sola en commitment**. El vault debe cotizar **dos mecanismos de entrada distintos** para el mismo actor, con_semántica de riesgo opuesta. Ver [[2026-1027-decodo-plan-gratuito-de-la-web-data-api-con-5-de-credito-y-10k-solicitudes-sin-tarjeta]].
=== END

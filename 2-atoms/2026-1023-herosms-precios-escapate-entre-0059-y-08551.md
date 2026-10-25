---
id: 2026-1023-herosms-precios-escapate-entre-0059-y-08551
type: atom
certainty: solid
sources: [sources/2026-10-22-hero-sms-home.md]
links: ["[[2026-1023-herosms-catalogo-cinco-servicios-visibles]]", "[[2026-1023-5sim-piso-de-precio-telegram-01026-usd]]", "[[2026-1023-5sim-claim-500k-numeros-y-piso-0008]]"]
---

## Claim
El rango de precios de escaparate de HeroSMS (captura del 2026-10-22) va de **`from $0.0059`** (TikTok/Douyin) a **`from $0.8551`** (Full rent), con `Whatsapp` en `from $0.0625`, `Instagram+Threads` en `from $0.0075` y `Ticketmaster` en `from $0.0195`. Son precios "from" por servicio, sin desglose por país ni por operador, sobre las cinco tarjetas del selector ([[2026-1023-herosms-catalogo-cinco-servicios-visibles]]). El mínimo del vault baja así de $0.1026 (5sim, servicio `telegram`, mínimo medido en CSV) a **$0.0059**, por debajo del propio claim de 5sim de **$0.008** de suelo ([[2026-1023-5sim-claim-500k-numeros-y-piso-0008]]).

## Why It Matters
El "coste de una identidad verificada" que el vault usa como referencia de margen ([[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]) era un número **de proveedor**, no de mercado: con dos proveedores comparados, el suelo publicado cae de $0.1026 a $0.0059, es decir **17,4× más barato**. Eso no significa que una activación cueste $0.0059 —los precios "from" son de la combinación más barata, y en 5sim las cifras observadas quedaron muy por encima del claim— pero sí significa que cualquier plan que fije margen sobre un coste unitario de un céntimo está calculando sobre el peor de los casos, no sobre el mercado.
La comparación solo es legítima servicio a servicio y con la misma granularidad (precio mínimo real de un par país-operador), no entre un `from` publicitario y un mínimo medido.

## [FRICTION]
> [[2026-1023-5sim-piso-de-precio-telegram-01026-usd]] (escrita hoy, a partir del CSV de precios de `telegram` de 5sim) fija **$0.1026** como el suelo real observado de una activación y lo usa como referencia de escala frente al coste de inferencia.
> Este átomo presiona esa creencia porque el precio de escaparate más bajo de HeroSMS es **$0.0059**, 17,4 veces por debajo de ese suelo medido: el vault no tiene un suelo de mercado, tiene un suelo por proveedor, y el mínimo real puede estar una orden de magnitud más abajo.
> Ambas no pueden ser simultáneamente correctas como afirmación general sobre "el coste de una verificación": o $0.1026 es una propiedad de 5sim/`telegram` (y no del mercado), o el `from $0.0059` de HeroSMS es un ancla publicitaria que ningún comprador alcanza.
> Marcado para juicio humano, no auto-resuelto.

## Extensión (captura `/pricing`, 2026-10-24)
La captura del 2026-10-24 de `hero-sms.com/pricing` (que en realidad termina en un 404 y re-renderiza el selector de la home, ver [[2026-1024-herosms-url-de-precios-devuelve-404-y-no-publica-precios-propio]]) confirma tres de los cinco "from" de esta nota —`Full rent` $0.8551, `Ticketmaster` $0.0195, `TikTok/Douyin` $0.0059— pero **contradice el de `Whatsapp`, que pasa de `from $0.0625` a `from $0.075` (+20 % en dos días)**; la quinta tarjeta ya no es `Instagram+Threads` sino `facebook`, al mismo `from $0.0075`. Ver [[2026-1024-herosms-precio-de-whatsapp-sube-de-00625-a-0075]] y [[2026-1024-herosms-el-quinto-servicio-del-selector-cambia-en-dos-dias]]. Esta nota conserva su tabla original sin modificar: queda fechada como foto del 2026-10-22, no como precio vigente.

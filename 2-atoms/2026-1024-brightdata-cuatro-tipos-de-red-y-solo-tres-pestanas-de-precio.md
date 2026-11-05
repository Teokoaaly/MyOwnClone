---
id: 2026-1024-brightdata-cuatro-tipos-de-red-y-solo-tres-pestanas-de-precio
type: atom
certainty: solid
sources: [sources/2026-10-24-brightdata-proxy-pricing.md]
links: ["[[2026-1024-dataimpulse-cuatro-tipos-y-que-cada-uno-resuelve]]", "[[2026-1024-brightdata-precios-por-ip-dos-tablas-sin-etiquetar]]", "[[2026-1024-brightdata-web-unlocker-resuelve-captcha-y-no-requiere-kyc]]"]
---

## Claim
El FAQ declara **cuatro redes de IP**: **Datacenter** ("the most cost-effective", para "mass crawling of non-sophisticated target websites"), **ISP Network** (IPs residenciales reales proporcionados directamente por ISPs, "most suitable for use cases that require permanent, non-rotating IPs, or for whoever needs a small amount of residential IPs"), **Residential Network** (rotativas, para "the most sophisticated websites", permiten emular un usuario real) y **Mobile Network** (conexión móvil real rotativa 3G/4G/5G, para "highly sophisticated websites"). En paralelo, la página ofrece **cuatro soluciones** de proxy —anonymous, rotating, shared y dedicated— y solo **tres pestañas de precio**: *Residential proxies | ISP proxies | Datacenter proxies*.

## Why It Matters
Es la taxonomía de tipos de proxy más limpia que tiene el vault, y coincide en la estructura con la de DataImpulse ([[2026-1024-dataimpulse-cuatro-tipos-y-que-cada-uno-resuelve]]): cuatro redes con cuatro posicionamientos de coste y de riesgo de bloqueo. Pero aquí aparece una asimetría que el otro proveedor no tenía: **la red móvil se describe y no tiene pestaña de precio**. Es decir, el tipo que el vault ha identificado como el más caro por gigabyte y el más resistente a bloqueo **no es cotizable con esta fuente**, lo que deja la tabla de coste por insumo incompleta en su tramo superior.
Y el solapamiento de dos taxonomías en la misma página —tipos de red (4) frente a tipos de solución (4: anonymous, rotating, shared, dedicated)— es una fuente real de confusión al comparar proveedores: son ejes distintos y mezclarlos produce comparaciones falsas, como la que hace esta captura al presentar dos tablas de $ por IP sin decir a qué red pertenecen ([[2026-1024-brightdata-precios-por-ip-dos-tablas-sin-etiquetar]]).

## Nota de verificación
Descripciones transcritas literalmente. La captura **no** publica el $/GB de la red móvil, ni el precio de las soluciones "shared" frente a "dedicated" más allá de las dos tablas por IP, ni si "Static Residential" del FAQ (término distinto del "ISP Network" de la misma respuesta) es un quinto producto o un sinónimo.


## Nota de extensión 2026-10-26
La página de introducción de la documentación (`docs.brightdata.com/introduction`) reinforce la inconsistencia que este átomo ya registraba, y la desplaza un eje. Su bloque **"Proxy networks"** declara **"Five network types for routing traffic at scale"** y lista **cinco** entradas: *Residential* ("400M+ real-user IPs"), *Datacenter* ("Fast, low-cost IPs"), *ISP* ("Static residential-grade IPs"), *Proxy Manager* ("Open-source proxy routing") y *Browser Extension* ("Proxies in Chrome").

Las dos últimas no son redes de IP sino **herramientas de cliente**, y **Mobile** —que sí es una red de IP según el FAQ registrado en este átomo— no aparece en la lista. De ahí la lectura que propone [[2026-1026-brightdata-cinco-tipos-de-red-en-docs-contra-cuatro-en-faq]]: el «5» no es un quinto tipo de red, es un conteo de **entidades de catálogo** (3 redes + 2 herramientas) mientras el FAQ cuenta **redes** (4, con móvil). La cifra "400M+ real-user IPs" que aparece aquí es además la que ya figura en [[2026-1024-brightdata-400m-de-ips-en-195-paises-con-targeting-gratis]], y esta página no añade ni el desglose por 195 países ni el targeting gratuito, es decir, la landing no sustituye a la ficha de producto.

Valor para el átomo: la taxonomía de 4 redes del FAQ sigue siendo la correcta para el modelo de coste; el "cinco" de la docs es un artefacto de navegación y no una quinta red cotizable. El recuento de 3 pestañas de precio sin móvil continúa sin resolver con esta fuente.

## Nota de extensión 2026-11-03
Las capturas del hub de precios (`sources/2026-10-31-`, `sources/2026-11-01-` y `sources/2026-11-02-brightdata-pricing.md`) añaden una **tercera taxonomía de redes**, distinta de las dos ya registradas: el widget de chat de venta ("Sophie") responde a *"I want to scrape LinkedIn profiles by URL"* con **"Target your traffic by geolocation with residential, ISP, or mobile proxies"** — **tres redes (Residential, ISP, Mobile)**, con **Datacenter ausente** de la respuesta. Es decir, la página que **vende** el producto nombra tres redes y deja fuera precisamente la más barata de cotizar. El detalle y la comparación con el «4 del FAQ» y el «5 de las docs» están en [[2026-1101-brightdata-el-chat-de-precios-nombra-tres-redes-y-omite-datacenter]].

Lo que **no** cambia con esta fuente es el hueco central de este átomo: **la red móvil sigue sin pestaña de precio**, y ahora hay además una tercera superficie (el chat) que la menciona sin cotizar, y una cuarta (la ficha de Proxy Networks del hub) que es la única que publica el volumen del pool residencial ("400M+ monthly Residential IPs"). Ninguna de las tres capturas del hub publica un $/GB.

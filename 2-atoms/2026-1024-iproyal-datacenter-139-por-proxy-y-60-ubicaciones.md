---
id: 2026-1024-iproyal-datacenter-139-por-proxy-y-60-ubicaciones
type: atom
certainty: solid
sources: [sources/2026-10-24-iproyal-pricing.md]
links: ["[[2026-1024-iproyal-cinco-lineas-y-cinco-unidades-de-precio]]", "[[2026-1024-iproyal-isp-180-por-proxy-y-500k-ips]]", "[[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]", "[[2026-1024-dataimpulse-cobertura-195-paises-y-targeting-gratis-por-pais]]"]
---

## Claim
El datacenter de IPRoyal se anuncia a **"from $1.39/proxy"** con **"60+ locations"** y un párrafo que promete **ancho de banda ilimitado**: *"Access **unlimited bandwidth** with maximum performance. From scraping and streaming to software-driven monitoring—get high-speed reliability at a price that's nice."*

## Why It Matters
El "unlimited bandwidth" es la primera vez que el vault ve **una partida de proxy sin coste marginal por volumen**, en un sector donde todo se medía por GB. Es exactamente lo contrario del diagnóstico del thread: el proxy era "la única partida cuyo coste depende de un volumen que nadie controla" ([[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]); aquí el datacenter cobra **por proxy y promete el tráfico sin límite**, con lo que el coste marginal de un scraping de volumen alto cae a **cero por el lado del proveedor**. El límite vuelve a ser el número de proxies, no los bytes.
La cifra geográfica también es un contrapunto: **"60+ locations"** es un número de localizaciones, no de países. DataImpulse publica 195+ países con el recuento de IPs de cada uno ([[2026-1024-dataimpulse-cobertura-195-paises-y-targeting-gratis-por-pais]]), que es un inventario; "60+ locations" con un "+" no es enumerable ni auditable, y la captura no muestra ni una lista.

## [FRICTION]
> [[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]] establece que el datacenter es "el más barato del catálogo" a $0.50/GB y lo sitúa como la opción para scraping simple de páginas estáticas; [[2026-1024-dataimpulse-cuatro-tipos-y-que-cada-uno-resuelve]] lo define con "Sub-100 ms latency" y "99.9% uptime".
> Este átomo presiona esa lectura en el criterio de selección: si el datacenter de IPRoyal se factura por proxy con ancho de banda ilimitado, **entonces "el más barato por GB" no es el criterio correcto** — un flujo de scraping pesado que genera mucho tráfico puede ser más barato con un pool de proxies de ancho de banda ilimitado que con GB medidos, aunque el $/GB nominal sea mayor. Y "60+ locations" es un claim de escala claramente menor que las 195+ países del otro proveedor.
> Ambas no pueden ser completamente correctas: o el $/GB es la unidad que decide el coste total del scraping, o la unidad real es "proxies usados × tráfico incluido" y el vault no tiene forma de cuantificarlo con esta fuente. Marcado para juicio humano, no auto-resuelto: la captura no publica ni qué volumen de tráfico incluye un proxy ni si el "unlimited bandwidth" es real o un claim.

## Nota de verificación
Precios y frases transcritos literalmente. "Unlimited bandwidth" y "60+ locations" son **claims del propio proveedor**. La captura **no** publica: cities o países enumerables, límite de concurrencia, ancho de banda por proxy, ni SLA de uptime.


## Nota de extensión 2026-10-27
La captura de proxy residencial de 2Captcha aporta un **contraste de vocabulario que este átomo necesita**: 2Captcha promete "**Unlimited traffic**" en un producto **facturado por GB** ("Price per GB", con nueve tramos), mientras que el "**unlimited bandwidth**" de IPRoyal aparece en un producto **facturado por proxy** ($139/proxy, 60 ubicaciones). Ver [[2026-1027-2captcha-unlimited-traffic-y-socks5-en-un-plan-facturado-por-gb]].

La asimetría importa para el modelo de coste: **"unlimited" solo es un claim coherente cuando la unidad de cobro no es el tráfico**. En el datacenter de IPRoyal el cobro es por proxy y el ancho de banda no tiene coste marginal, de modo que "ilimitado" es exacto. En el proxy residencial de 2Captcha el cobro **es** por gigabyte, de modo que "tráfico ilimitado" solo puede significar **que el tráfico comprado no caduca o no se topa**, no que sea gratis. La conclusión de este átomo —que el "unlimited bandwidth" es **"la primera vez que el vault ve una partida de proxy sin coste marginal por volumen"**— **se convierte en un caso de estudio de dos**: **el mismo adjetivo aplicado a dos modelos de cobro opuestos**, y el vault no puede citarlos como equivalentes sin matizar.

Además, las otras dos inclusiones de 2Captcha ("SOCKS5 supported", "API access") **confirman que el soporte de protocolo y de API ya es estándar en el corpus de proxy**, y que la variable que discrimina entre proveedores ya no es el protocolo sino el precio y la sesión.

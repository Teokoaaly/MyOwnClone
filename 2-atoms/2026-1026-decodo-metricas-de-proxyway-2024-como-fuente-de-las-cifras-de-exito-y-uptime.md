---
id: 2026-1026-decodo-metricas-de-proxyway-2024-como-fuente-de-las-cifras-de-exito-y-uptime
type: atom
certainty: solid
sources: [sources/2026-10-25-decodo-residential-pricing.md]
links: ["[[2026-1026-decodo-fraud-score-32-72-contra-45-57-del-pool-global]]", "[[2026-1024-iproyal-premios-y-distintivos-como-sustituto-de-sla]]", "[[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]]"]
---

## Claim
Decodo declara en su lista de features **"<0.5s avg. response time", "99.92% success rate" y "99.99% uptime"**, y el FAQ declara **de dónde salen**: "Residential proxies' average response time and success rate provided on our website are based on **Proxyway's research** (proxy-market-research-2024)". La metodología se publica: **500 peticiones por endpoint** a `http://ipinfo.io/ip`, dividiendo el tiempo total entre 500, con **sesión rotativa**, **Python 3.9.6** y peticiones enviadas desde **la VPN del mismo país que el endpoint**.

## Why It Matters
Es el **único caso del corpus donde la página de precios de un proxy hace públicos el método de medición de sus propias métricas de calidad** —número de peticiones, objetivo, modo de sesión, versión de Python y—even el origen de la IP de prueba. La comparación es: 2Captcha publica un SLA ("99.9% uptime") sin método ([[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]]); IPRoyal sustituye el contrato por distintivos de terceros sin metadatos ([[2026-1024-iproyal-premios-y-distintivos-como-sustituto-de-sla]]); Decodo publica **la cifra y el método, y ambos son de un tercero y de 2024**.
Dos consecuencias operarias. La primera: **el 99,92 % de éxito no es una promesa contractual, es una medición de tercero con fecha**, y su valor real es un **0,08 % de fallo por petición** — que en un lote de 100 000 peticiones de scraping son 80 fallos, y en un flujo de alta con reintentos es un multiplicador del coste.
La segunda, y más relevante para el vault: **la prueba se hace contra `ipinfo.io/ip`**, un endpoint de consulta de IP que casi nadie bloquea. Es decir: **el 99,92 % mide conectividad, no supervivencia ante un sitio que bloquea** — y el criterio que decide un alta real es el segundo. El método honesto y la cifra que no sirve para lo que el proveedor sugiere.

## Nota de verificación
Método y cifras transcritos literalmente. La captura **no** publica: fecha de la medición dentro de 2024, número de endpoints, ni si el resultado se extrapoló a otros tipos de proxy distintos de los residenciales.


## Nota de extensión 2026-10-27
La home **añade una tercera cifra de éxito, más alta y más específica** que la de este átomo: *"**99.99% success** on the hard, anti-bot-protected targets such as **Amazon and Cloudflare-protected sites** – that trip up most AI-native scraping tools."* El hero añade además **"<0.2s response time"** y **"99.99% uptime"**.

El contraste con este átomo es el que importa: la cifra de **99,92 %** es una **medición de tercero con método publicado** (500 peticiones por endpoint contra `ipinfo.io/ip`, sesión rotativa, VPN del mismo país, Proxyway 2024), y su propio límite —documentado aquí— es que **mide conectividad, no supervivencia ante un sitio que bloquea**. La cifra de la home de **99,99 %** es exactamente la que mide esa segunda cosa, **pero sin método**: no dice cuántas peticiones, contra qué URLs, en qué ventana ni qué cuenta como éxito. Y la latencia **se duplica** entre el hero (**<0,2 s**) y la página de precios (**<0,5 s**).

Consecuencia práctica para el vault: **ninguna de las dos cifras puede usarse como parámetro de reintentos**. Con 99,92 % medido, el número de fallos es acotable; con 99,99 % sin método, es desconocido — y en un producto facturado por mil de requests, **cada reintento es cuota consumida**, así que el coste del fallo es idéntico al del éxito. Ver [[2026-1027-decodo-9999-de-exito-en-destinos-anti-bot-como-amazon-y-cloudflare]].

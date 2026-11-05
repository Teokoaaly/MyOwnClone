---
id: 2026-1027-decodo-home-publica-diez-paises-con-conteo-de-ips-que-contradice-el-atom-del-pool
type: atom
certainty: solid
sources: [sources/2026-10-26-decodo-smartproxy-home.md]
links: ["[[2026-1026-decodo-pool-de-115m-en-el-cuerpo-y-125m-en-el-pie]]", "[[2026-1024-dataimpulse-cobertura-195-paises-y-targeting-gratis-por-pais]]", "[[2026-1024-brightdata-400m-de-ips-en-195-paises-con-targeting-gratis]]", "[[2026-1024-iproyal-pool-de-64m-sin-desglose-geografico]]"]
---

## Claim
La home de Decodo publica un **desglose de IPs por país para diez países**, cada uno con su propio enlace a la página de proxies del país: **United States 16M+ IPs, United Kingdom 5M+, Netherlands 870K+, Germany 5.6M+, India 11M+, Canada 3M+, France 4.6M+, Australia 1M+, Italy 2M+, Spain 3.7M+**. La suma de los diez es **52,77M**, es decir el **42,2 %** del "125M+ IPs worldwide" que la misma página declara en el pie.

El desglose es por pool agregado (residencial, ISP, móvil y datacenter juntos), no por tipo: la sección se titula "Discover ethically-sourced IPs worldwide" y la frase de targeting es "Access public web data across the globe with continent-, country-, state-, city-, and ASN-level targeting". La home también da la cifra del pool residencial por separado en el FAQ: "Decodo's **residential** proxy network includes **115M+** ethically-sourced IPs across 195+ locations".

## Why It Matters
Es el **único proveedor del corpus que publica el pool con desglose numérico por país sin adjuntar el CSV**: Bright Data da el agregado de 400M+ y el número de países ([[2026-1024-brightdata-400m-de-ips-en-195-paises-con-targeting-gratis]]), IPRoyal da 64M+ y ni una fila por país ([[2026-1024-iproyal-pool-de-64m-sin-desglose-geografico]]), y DataImpulse sí publica filas por país pero con recuentos exactos ([[2026-1024-dataimpulse-cobertura-195-paises-y-targeting-gratis-por-pais]]). Decodo publica diez filas con **redondeo en "M+"** — 16M+, 11M+, 5,6M+, 870K+ — es decir, un inventario **aproximado** por diez de 195+ países.

Lo que hace útil el dato es que **ordena el mercado de los destinos**. India (11M+) y EE.UU. (16M+) concentran el grueso; España, que es el país del vault, declara **3,7M+ IPs** — comparable a Francia (4,6M+) y por encima de Italia (2M+) o Australia (1M+). Eso convierte la pregunta "¿de dónde saco la IP?" en una pregunta **con respuesta numérica publicada** para los diez países que más importan, y sin respuesta publicada para los 185 restantes.

El límite hay que decirlo: **diez de 195+ países** y en números redondeados hacia arriba. La suma de lo publicado (52,77M) deja fuera el 57,8 % del pool declarado, así que la tabla **no permite auditar** el "125M+" ni el "115M+" residencial: es un extracto, no un inventario.

## [FRICTION]
> [[2026-1026-decodo-pool-de-115m-en-el-cuerpo-y-125m-en-el-pie]] afirma, en su "Nota de verificación", que la captura de precios de Decodo "**no publica: ... el desglose por país**", y sostiene en su "Why It Matters" que "Decodo **no publica ni un solo desglose por país, ciudad o ASN**: solo el agregado y los 195+ países".
> Este átomo presiona esa afirmación desde una captura distinta de la **misma marca y el mismo día**: la home de `smartproxy.com` publica diez países con recuento de IPs y enlaza a la página de proxies de cada uno. La diferencia entre capturas es real (página de precios vs home), pero **la afirmación del átomo viejo se lee hoy como una propiedad del proveedor, y el proveedor sí publica desglose**.
> Ambas no pueden ser completamente correctas: o Decodo no publica desglose por país —y entonces el vault tiene que tratar la home como una excepción no capturada por la página de precios—, o sí lo publica —y entonces la comparabilidad de pools por granularidad que el átomo viejo daba por rota en Decodo **se reabre**, porque ahora existe una fila por país para diez destinos. Marcado para juicio humano, no auto-resuelto: la captura no publica la metodología de los recuentos ni si los diez países son los diez mayores.

## Nota de verificación
Cifras por país transcritas literalmente, con su redondeo "M+"/"K+" original. La suma (52,77M) y el porcentaje sobre 125M+ son **cálculos del vault**. La captura **no** publica: la fecha de los recuentos, el reparto por tipo de proxy dentro de cada país, ni el número de IPs de los otros 185+ países.

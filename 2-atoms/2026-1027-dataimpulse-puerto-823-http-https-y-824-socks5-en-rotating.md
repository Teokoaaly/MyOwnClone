---
id: 2026-1027-dataimpulse-puerto-823-http-https-y-824-socks5-en-rotating
type: atom
certainty: solid
sources: [sources/2026-10-26-dataimpulse-docs-types-of-connections.md]
links: ["[[2026-1024-dataimpulse-gateway-unico-y-protocolos]]", "[[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]", "[[2026-1027-dataimpulse-sticky-por-puerto-en-rango-10000-20000]]", "[[2026-1024-dataimpulse-cuatro-tipos-y-que-cada-uno-resuelve]]"]
---

## Claim
La página *Types of connections* de la documentación de DataImpulse publica la tabla de puertos del modo **rotating**: para HTTP/HTTPS, "**823** PORT"; para SOCKS5, "**824** PORT", con la definición del modo transcrita literalmente — "The IP address changes automatically with each new request." Es decir, **el puerto no es una constante del producto: es una función del protocolo**.

## Why It Matters
El átomo del gateway único ([[2026-1024-dataimpulse-gateway-unico-y-protocolos]]) dejó escrito que "todos los tipos de proxy comparten el mismo endpoint y el mismo par de credenciales, así que cambiar de datacenter a residencial premium no obliga a tocar el código — solo el usuario", y su Nota de verificación confessaba que la captura **no** publicaba "si el puerto 823 es el mismo para los cuatro tipos de proxy". La documentación responde a esa pregunta en la dirección contraria a lo que el átomo asumía: el **hostname** (`gw.dataimpulse.com`) y las **credenciales** sí son únicos, pero el **puerto cambia con el protocolo** (823 HTTP/HTTPS, 824 SOCKS5) y además cambia del todo al pasar a sticky ([[2026-1027-dataimpulse-sticky-por-puerto-en-rango-10000-20000]]).
Para el vault esto tiene una consecuencia de cableado directo: un cliente que cablea `http://login:password@gw.dataimpulse.com:823` y más tarde quiere SOCKS5 **tiene que cambiar una constante más**, no solo la constante de "usuario". Y para el modelo de coste por sesión ([[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]), el hecho de que la rotación sea "IP nueva en cada request" fija el **peor caso de tráfico por request**: cada unidad de trabajo del pipeline de altas consume el mínimo teórico de una conexión sin estado de IP, lo que hace que la granularidad de cobro por gigabyte ([[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]) se mida en requests cuando el flujo usa rotating.

## [FRICTION]
> [[2026-1024-dataimpulse-gateway-unico-y-protocolos]] afirma que "El acceso técnico es un **gateway único** con los mismos parámetros en los siete lenguajes que muestra la home (Python, Node.js, PHP, C#, Go, Ruby, curl): `hostname = 'gw.dataimpulse.com'`, `port = 823`" y que "Protocolos soportados: **HTTP / HTTPS / SOCKS5**".
> Este átomo presiona ese dato: la documentación técnica publica **dos puertos distintos para el mismo modo rotating según el protocolo** (823 HTTP/HTTPS, 824 SOCKS5), de modo que el ejemplo `port = 823` del átomo viejo solo es válido para HTTP/HTTPS, y el mismo patrón de "gateway único" se rompe en el puerto cuando además se elige sticky ([[2026-1027-dataimpulse-sticky-por-puerto-en-rango-10000-20000]]). La lectura "un único endpoint" sobrevive para hostname y credenciales, pero no para el puerto.
> Ambas no pueden ser completamente correctas: o el puerto es una propiedad fija del gateway y el 824 de SOCKS5 es un alias del mismo backend, o el endpoint único solo es único en las credenciales y el puerto forma parte del contrato de sesión. Marcado para juicio humano, no auto-resuelto: la captura no publica si el 824 sirve el mismo pool que el 823 ni si sticky exige además otro tipo de proxy.

## Nota de verificación
Cifras y frases transcritas literalmente de la página. La captura **no** publica: si los puertos 823/824 son los mismos para residencial, móvil y datacenter, si sticky exige además otro tipo de proxy, ni si existe un límite de puertos sticky por cuenta.

# Extensiones a átomos existentes — captura 2026-10-26-dataimpulse-docs-proxies-index (2026-10-27)

Fuente: `sources/2026-10-26-dataimpulse-docs-proxies-index.md` (captura `0-raw/2026-10-26-dataimpulse-docs-proxies-index.md`).
Ninguno de los átomos siguientes se ha modificado: las extensiones se proponen para el Editor.

=== EXTEND 2-atoms/2026-1024-dataimpulse-cuatro-tipos-y-que-cada-uno-resuelve
## Nota de extensión 2026-10-27
El índice de la documentación de proxies confirma la **taxonomía de cuatro pools** desde una página distinta a la home, con los mismos cuatro nombres y cada uno enlazado a su propia landing de producto: **Residential Proxies**, **Mobile Proxies**, **Datacenter Proxies** y **Premium Residential Proxies** ("We provide:"). La confirmación no es trivial por un motivo de nomenclatura: la home llama al cuarto pool "**premium residencial**" y este átomo lo transcribe como "Premium residencial: high-quality IP addresses"; la documentación lo nombra como **producto propio con landing propia** (`dataimpulse.com/premium-residential-proxies/`), no como una variante del residencial.
La consecuencia de catálogo es que el **cuarto pool sigue siendo el único con landing y nombre propios** y, por tanto, el único cuya especificación técnica (targeting fino incluido, Proxy Manager dedicado, API extra) se puede esperar que difiera —lo que refuerza el criterio de este átomo: el salto de precio del premium residencial ($5/GB frente a $1/GB del residencial, [[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]) no es un recargo de marketing sino el precio de un producto con superficie de control propia.
La captura **no** publica: ni una sola especificación técnica (el índice es un índice de navegación de 60 palabras), ni el orden de la taxonomía como jerarquía, ni si existen pools que no figuren en este índice.
=== END

=== EXTEND 2-atoms/2026-1024-dataimpulse-gateway-unico-y-protocolos
## Nota de extensión 2026-10-27
La documentación confirma que el árbol de páginas de proxies está ordenado como **Proxies → Types of connections → Protocols** (piedes "Previous Welcome / Next Types of connections" y "Previous Proxies / Next Protocols"). Es decir, el proveedor **documenta los protocolos en una página propia y separada**, después de las conexiones — lo que convierte "Use any protocol depending on your setup" (la fila común de las cuatro tablas de precios que este átomo transcribe) en un **capítulo propio de la documentación** y no en una nota de marketing.
Eso importa para este átomo porque separa dos cosas que aquí estaban fundidas: **el endpoint** (`gw.dataimpulse.com`, credenciales, puertos) y **los protocolos** (HTTP/HTTPS vs SOCKS5). La página de *Types of connections* muestra que el **puerto cambia con el protocolo** —823 para HTTP/HTTPS, 824 para SOCKS5— y que el modo sticky usa un rango de puertos propio (10000–20000), de modo que la URL completa no es `login:password@gw.dataimpulse.com:823` sino una función de (modo de sesión, protocolo). Ver [[2026-1027-dataimpulse-puerto-823-http-https-y-824-socks5-en-rotating]] y [[2026-1027-dataimpulse-sticky-por-puerto-en-rango-10000-20000]].
La captura **no** publica: el contenido de la página "Protocols", ni si los puertos 823/824 difieren por pool.
=== END

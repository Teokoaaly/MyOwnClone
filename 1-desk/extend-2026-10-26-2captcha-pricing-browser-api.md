# Extensiones a átomos existentes — captura 2026-10-26-2captcha-pricing-browser-api (2026-10-26)

Fuente: `sources/2026-10-26-2captcha-pricing-browser-api.md` (captura `0-raw/2026-10-26-2captcha-pricing-browser-api.md`).
Ninguno de los átomos siguientes se ha modificado: las extensiones se proponen para el Editor.

=== EXTEND 2-atoms/2026-1026-brightdata-un-credito-por-request-y-cinco-por-mb-en-browser-api
## Nota de extensión 2026-10-27
Este átomo calcula el **coste marginal de la elusión en una unidad común** a partir del valor declarado de los créditos de Bright Data y concluye que el **Browser API es "5 veces más caro que la petición simple por el mismo dinero"** (5 créditos por MB frente a 1 crédito por request). La captura del Browser API de 2Captcha del 2026-10-26 **ofrece el contraejemplo de un competidor que no usa créditos y publica el $/GB directamente**: una única fila —"**Browser API | 1 GB Traffic | $0.1 / GB | 0% off | Top up**"— con el texto "**Browser API costs $0.10/GB. Proxy traffic is billed separately. With your own proxies, you pay only for browser traffic.**" ([[2026-1027-2captcha-browser-api-010-por-gb-con-el-proxy-facturado-a-parte]]).

**El punto que esta extensión añade es que en 2Captcha el navegador y el proxy son dos partidas independientes, mientras que en Bright Data son un solo crédito.** En Bright Data el Browser API consume 5 créditos por MB de tráfico, y esos créditos salen del mismo pool que el Web Unblocker y la SERP API, de modo que la navegación es una **sub-partida del mismo presupuesto** que la extracción; en 2Captcha, el tráfico de navegador se factura **aparte del proxy**, de modo que el coste total es la suma de dos líneas elegibles por separado y **el proveedor incluso invita a traer proxies propios** ("With your own proxies, you pay only for browser traffic"). La consecuencia para el modelo de coste del vault: **la "navegación real" ya no es una línea única en el corpus**, es un Browser API que puede venir incluido en otro producto (Bright Data) o separado de la red (2Captcha).

**Y hay una diferencia de orden de magnitud que el vault no debe leer sin matizar.** $0,10/GB es 5 veces más barato que el **datacenter de DataImpulse** a $0,50/GB ([[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]) y 40 veces más barato que el **PAYG de Bright Data a $4/GB** ([[2026-1024-brightdata-payg-a-4-por-gb-sin-compromiso]]). Pero la comparación no es homogénea: **$0,10/GB no incluye la IP**, mientras que los $/GB del corpus proxy normalmente **sí**. La comparación correcta es $0,10/GB **más** un proxy, contra un $/GB **con** proxy dentro. El vault solo puede afirmar el 5–40× si ya tiene un proxy barato, y esa es precisamente la conclusión operativa: **la línea de navegador es casi gratis y la partida cara es la red**.

Nota de verificación: la captura **no** publica qué es un "GB" (¿tráfico de red total? ¿payload?), ni el número de navegadores concurrentes, ni el precio de los proxies de 2Captcha, ni SLA. El "0% off" es literal y no implica que exista un descuento mayor.
=== END

=== EXTEND 2-atoms/2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy
## Nota de extensión 2026-10-27
Este átomo construye una **escala explícita de riesgo de bloqueo** dentro de un mismo proveedor (datacenter $0.50/GB, residencial $1/GB, móvil $2/GB, premium residencial $5/GB) y concluye que "el proxy **no** es un coste marginal pequeño al lado del SMS" y que es "el único insumo cuyo coste depende de un volumen que el proveedor controla".

Con la captura del Browser API de 2Captcha del 2026-10-26, la segunda de esas dos afirmaciones **se acota**: hay ya un proveedor del corpus que **separa** el tráfico de navegación del tráfico de proxy y lo publica por separado —"$0.10/GB" de browser traffic, con "**Proxy traffic is billed separately**" ([[2026-1027-2captcha-browser-api-010-por-gb-con-el-proxy-facturado-a-parte]])—. Es decir, **el proxy deja de ser el único insumo con coste dependiente de volumen que nadie controla**: el GB de tráfico de navegador es exactamente eso, y además **con un precio unitario ($0,10) cinco veces por debajo del datacenter más barato del corpus**. La jerarquía "correo ≪ captcha ≪ proxy ≪ SMS" del thread **necesita una línea más**: hay ahora una partida —**tráfico de navegador**— que es más barata que el captcha y que se factura por volumen de red no controlado, pero **sin la IP dentro**.

**La consecuencia metodológica es más fuerte que el dato de precio**: la escala de riesgo de bloqueo que este átomo construye **no es transferible**, porque depende de qué se compra con el GB. El datacenter barato de DataImpulse es "rápido y barato pero no para sitios que bloquean IPs de servidor"; el GB de 2Captcha **no compra ninguna IP**. La misma magnitud nominal —GB— cubre en un caso el acceso con una IP de riesgo conocido y en el otro solo el cómputo del navegador, con lo que cualquier comparación entre los dos $/GB está comparando paquetes distintos.

Nota de verificación: la captura de 2Captcha **no** publica el precio de sus proxies ni el precio de los proxies de terceros que el cliente puede traer; el "0,10/GB" es literal y es solo tráfico de navegador.
=== END

=== EXTEND 2-atoms/2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes
## Nota de extensión 2026-10-27
Esta extensión se solapa con la propuesta homónima del bloque de la captura MCP y añade el dato específico del Browser API: **la primera cifra publicada de esta línea es $0.10/GB**, con el proxy facturado aparte y con la opción explícita de traer proxies propios ([[2026-1027-2captcha-browser-api-010-por-gb-con-el-proxy-facturado-a-parte]]).

**Lo que el dato añade al argumento del giro es la composición de la cadena.** El átomo sostenía que 2Captcha "cobra por el **resultado útil** (extracción exitosa) y no por el recurso"; el Browser API publica lo contrario en su propia línea: **un precio de recurso** ($0,10 por GB de tráfico, facturándose el tráfico consumido y no el dato obtenido). Sumado al Scraper API (por request, [[2026-1027-2captcha-scraper-api-030-por-mil-de-requests-en-los-cinco-planes]]) y al MCP (por llamada, [[2026-1027-2captcha-mcp-seis-modos-con-precios-por-llamada]]), el resultado es que **tres de las líneas nuevas del giro se cobran por unidad de recurso o de entrada, y solo la más antigua —el captcha— se cobra por resultado**. El principio "pagar por el resultado" queda, con estas cifras, **acotado al captcha** y demonstrado como decisión de línea de producto dentro de un mismo proveedor.
=== END

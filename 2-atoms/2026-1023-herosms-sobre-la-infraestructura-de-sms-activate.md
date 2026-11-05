---
id: 2026-1023-herosms-sobre-la-infraestructura-de-sms-activate
type: atom
certainty: solid
sources: [sources/2026-10-22-hero-sms-home.md, sources/2026-10-22-sms-activate-closed.md]
links: ["[[2026-1023-herosms-catalogo-cinco-servicios-visibles]]", "[[2026-1023-herosms-claims-700-servicios-180-paises-500k-numeros]]", "[[2026-1023-5sim-catalogo-servicios-precios-y-stock]]", "[[2026-1023-sms-activate-cierra-total-el-22-de-diciembre]]"]
---

## Claim
HeroSMS **no es un proveedor de infraestructura propio**: su propia página lo declara dos veces. En las bullet points de la home: "Market-leading activation software (powered by **SMS-Activate** technical infrastructure)". Y en el FAQ, respondiendo a "Why is choosing HeroSMS a great option?": "**HeroSMS is a new service built on the foundation of SMS-Activate**, widely known market leader. The project is based on the best technical features of SMS-Activate, but stands out with more modern technologies and more profitable terms." Es decir, es una **fachada comercial (white-label) sobre SMS-Activate**, que aporta la interfaz, el catálogo y la tabla de stock. La inferencia razonable (no declarada por el proveedor) es que el pool de números y la cobertura de país **heredan** del operador de origen. Las cinco tarjetas del selector y sus precios quedan igualmente determinados por el proveedor de infraestructura ([[2026-1023-herosms-catalogo-cinco-servicios-visibles]], [[2026-1023-herosms-claims-700-servicios-180-paises-500k-numeros]]), igual que el selector de 5sim publica sus propias cifras ([[2026-1023-5sim-catalogo-servicios-precios-y-stock]]).

## Why It Matters
Cambia cómo se lee todo el resto de la captura: los `from $…` y los contadores de stock de las tarjetas son **datos de un proveedor presentados en la web de otro**. HeroSMS es el mismo tipo de actor que 5sim pero con el respaldo de un operador mayor, lo que explica por qué puede declarar cosas que 5sim no puede (700+ servicios, 180+ países) sin que su catálogo visible las respalde: el inventario es heredado.
Consecuencia práctica para el vault: **dos de los proveedores que se comparan no son independientes**. Si un plan de aprovisionamiento de SMS compara "oferta de HeroSMS" contra "oferta de 5sim" como dos mercados, está comparando una fachada y un operador autónomo, no dos proveedores. La comparación de precio y stock solo es informativa si se sabe cuál de los dos es el dueño del número.

## [FRICTION]
> [[2026-1023-5sim-catalogo-servicios-precios-y-stock]] (escrita hoy, desde la home de 5sim) trata las cifras del selector de 5sim como **datos propios del proveedor** y discute su consistencia interna (mismo bloque replicado en tres URL, precios distintos para el mismo servicio en selector y ficha de producto) como un problema de renderizado y de sincronización de catálogo.
> Este átomo presiona esa creencia porque ofrece una **explicación alternativa y más simple** para el mismo tipo de anomalía: si HeroSMS es una fachada sobre SMS-Activate, es plausible que sectorialmente varios sitios de números publiciten las mismas cifras de marketing heredadas de un mismo operador ("500.000 números", "180+ países"), y que los contadores por servicio de cada web se calculen sobre inventarios agregados distintos. Es decir, la inconsistencia observada en 5sim podría no ser un fallo de su catálogo sino una propiedad del sector.
> Ambas no pueden ser completamente correctas como explicación: o las cifras de 5sim son propias y la coincidencia con HeroSMS es casual, o ambas son marketing heredado de un operador común. Marcado para juicio humano, no auto-resuelto.

## Extensión (aviso de cierre de SMS-Activate, 2026-10-22)
La fuente del **propio operador cerrado** confirma el traspaso desde el lado de SMS-Activate: "Свои технологии мы передали команде сервиса HeroSMS. Это мощный новичок на рынке, который уже получает отличный фидбэк. Рекомендуем попробовать его" — *transferimos nuestras tecnologías al equipo del servicio HeroSMS; es un novato potente en el mercado que ya recibe feedback excelente; recomendamos probarlo*. Esto **confirma** que la relación es de traspaso de tecnología al cierre del operador, no solo marketing white-label, y añade dos datos propios del emisor: HeroSMS es **"un novato potente"** (es decir, no es un proveedor maduro de 10 años como lo era SMS-Activate) y **recibe feedback excelente** según el operador saliente. El cierre total y la cronología completa están en [[2026-1023-sms-activate-cierra-total-el-22-de-diciembre]].

## Nota de verificación
Ambas citas están transcritas literalmente de la captura del 2026-10-22. Lo que **no** puede verificarse desde esta fuente es la relación societaria real ni si el stock mostrado en las tarjetas es stock propio de HeroSMS o inventario agregado de SMS-Activate; la página no lo distingue. El aviso de cierre añade que el traspaso fue de **tecnologías** —no dice explícitamente "números", "stock" ni "catálogo"—, por lo que la herencia del pool queda inferida, no declarada.


## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-onlinesim-virtual-sms.md`. Este átomo afirma que HeroSMS es una fachada white-label sobre SMS-Activate e infiere que "el pool de números y la cobertura de país **heredan** del operador de origen", dejando la herencia como inferencia no declarada.

La captura de OnlineSim añade un **segundo candidato de infraestructura independiente**: su FAQ declara "We have our own **equipment that holds the SIM cards** and our own **software**" ([[2026-1026-onlinesim-equipo-propio-de-sim-y-software-propio]]). Si eso es cierto, el corpus deja de tener un único linaje de hardware con varios escaparates: habría al menos dos operadores con SIM cards propias, y el stock no sería un recurso único heredado de SMS-Activate.

Refuerza el punto desde el lado de la geografía: el selector de pago de OnlineSim sirve **Bielorrusia +375, Ucrania +380, Kazajistán +77, Kirguistán +996 y Uzbekistán +998** pero **no Rusia ni China**, mientras el módulo de números gratuitos sí incluye China ([[2026-1026-onlinesim-sin-rusia-ni-china-en-el-selector-de-pago]]). Un proveedor que hereda el pool de un operador ruso y **excluye precisamente el mercado doméstico de ese operador** no puede ser simplemente su fachada: o son dos pools distintos, o la herencia no es el mecanismo.

Nota de alcance: es una declaración de marketing del propio OnlineSim, sin verificación de hardware. La inferencia que queda abierta es si "own equipment" es un hecho o parte del mismo patrón de claims sin evidencia que el vault ya registró en 5sim y HeroSMS.


## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-hero-sms-api-docs.md`.

Este átomo sostiene que HeroSMS es una **fachada white-label sobre SMS-Activate** y que "la inferencia razonable (no declarada por el proveedor) es que el pool de números y la cobertura de país **heredan** del operador de origen". La página de API **publica la compatibilidad de protocolo de forma literal**: "HeroSMS is compatible with **former** SMS-Activate partners", con el paso 3 del procedimiento escrito como "**Replace the host from `https://api.sms-activate.ae` to `https://hero-sms.com`**" y el paso 4 "Enter the API key from your HeroSMS account" ([[2026-1027-hero-sms-compatibilidad-de-wire-con-los-clientes-de-sms-activate]]).

Consecuencia para el Editor: la compatibilidad **wire** es un dato mucho más fuerte que la fórmula de marketing "built on the foundation of SMS-Activate" —dos hosts, una clave, y un procedimiento de cambio publicado. Pero hay que **mantener la distinción** que el átomo ya establece: lo que el proveedor declara es **compatibilidad de protocolo**, no **herencia de pool**. Es decir, la línea "el pool y la cobertura heredan del operador de origen" **sigue siendo inferencia**; lo que ha dejado de ser inferencia es que la API de HeroSMS es **intercambiable con la del operador cerrado**. Esa distinción es la que sostiene la fricción 7 del thread (cierre de SMS-Activate contra "fachada sobre operador vivo"): ahora se puede decir que el receptor **hereda la interfaz** de un operador que cerró, lo cual no prueba que herede su inventario.

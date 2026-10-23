---
id: economia-de-la-verificacion-y-reventa-de-cuentas
type: thread
updated: 2026-10-23
sources: [sources/2026-10-22-5sim-home.md, sources/2026-10-22-5sim-prices.md, sources/2026-10-22-5sim-products-catalog.md, sources/2026-10-22-5sim-openai-chatgpt-pricing.md, sources/2026-10-22-hero-sms-home.md, sources/2026-10-22-hero-sms-chatgpt-verification.md, sources/2026-10-22-sms-activate-closed.md, sources/2026-10-22-lzt-market-home.md, sources/2026-10-22-priceai-home.md, sources/2026-10-22-priceai-channels.md, sources/2026-10-22-priceai-official-prices.md, sources/2026-10-22-hetzner-cloud.md]
links: ["[[myownclone]]", "[[myownclone-gtm-monetization-roadmap]]", "[[myownclone-platform-architecture]]", "[[2026-1022-costes-por-categoria-tenant]]", "[[2026-1022-mvp-salir-al-mercado-pronto]]"]
---

# Thread — La economía de la verificación: números SMS, cuentas de IA revendidas y el coste real de un alta

> **Este thread REGISTRA un mercado; no lo recomienda.** Todo lo que sigue son precios, cifras y avisos leídos de páginas públicas el 2026-10-22 y atomizados el 2026-10-23. Buena parte de ese mercado consiste en cosas que se rompen: cuentas que caducan en tres días, números que no aceptan el SMS, marcas retiradas por fraude y saldos atrapados. El vault documenta ese mercado porque alguien va a preguntar por él; la decisión de participar —o no— es de una persona.

El corpus de esta thread atomiza tres capas que se confunden entre sí y que conviene separar antes de sacar ninguna conclusión de coste.

## 1. La forma del mercado: tres capas, no un mercado

| Capa | Qué se vende | Cómo se mide | Dónde está |
|---|---|---|---|
| **(a) Activación de número SMS** | Un número virtual de un solo uso, por el que llega un código | Por unidad, precio por par (país, operador) | 5sim, HeroSMS |
| **(b) Cuentas y suscripciones de IA ya hechas** | La cuenta creada y verificada, o la suscripción reenvendida | Por unidad o por pack, en yuanes | lzt.market `LLM Accounts`, PriceAI 卡网 |
| **(c) Reley 中转 de acceso a API** | Cuota de modelos revendida con multiplicador | Por multiplicador y disponibilidad | PriceAI 中转 — vive en [[myownclone-platform-architecture]], aquí no se duplica |

La distinción que decide todo lo demás: **verificar un número y comprar una cuenta no son la misma operación**. La primera es un insumo: pagas un código de un solo uso, creas la cuenta tú, y asumes el riesgo de que te la rechacen. La segunda es un producto terminado: pagas por una cuenta que otro ya verificó, con un estado de entrega que el vendedor declara en el título (成品号, 速刷, CDK, 官方充值) y con una columna de precio con garantía que va de ×1,1 a ×1.659 sobre el precio de lista ([[2026-1023-priceai-channels-doble-columna-minimo-y-minimo-con-garantia]]).

La diferencia en el perfil de riesgo es la que hay que retener: comprar capacidad de verificación es una compra de instrumento; comprar cuentas es **account-farming**, con exposición a ToS y a baneo de plataforma, y con un modo de entrega que el propio canal declara —"封号不保（母号被封/被退也不保）", "无售后", "平均存活3天", "日产300"— dentro del texto del título ([[2026-1023-priceai-channels-modos-de-entrega-declarados-en-los-titulos]]). Es la diferencia entre pagar por una herramienta y pagar por un inventario que se degrada solo.

La cadena de valor completa está documentada de punta a punta en los átomos: **proveedor de números → API para integradores y revendedores de registro masivo → mercado de cuentas por lotes**. HeroSMS publica una API sin documentación y cinco socios cuyo producto es el registro automatizado ("Register thousands of accounts daily with our partners"; "Create accounts in bulk, combine them into a network, sell them on an exchange"), y su propia copy dice que sus soluciones "help you bypass restrictions" ([[2026-1023-herosms-api-y-partners-de-registro-masivo]]). lzt.market es el destino de ese output: `LLM Accounts` es categoría de primera clase con vía individual (`/llm/item/add`) y carga masiva (`/mass-upload/llm/start`) ([[2026-1023-lzt-categoria-llm-accounts-para-reventa]], [[2026-1023-lzt-venta-individual-y-masiva-por-categoria]]). El vault no comparte esa línea: compite por el tramo de conversación con IA, no por la fábrica de identidades.

Dos detalles de esa taxonomía que conviene no perder: la navegación de **compra** de lzt.market solo muestra 22 categorías (Gaming 17, Social network 5) y **no incluye `LLM Accounts`**, que solo aparece en el lado vendedor — con 23 categorías individuales frente a 19 con carga masiva, y cuatro (Epic Games, Valorant/LoL, Social Club, Battle.net) deliberadamente fuera del canal masivo, probablemente por riesgo de bloqueo o volumen de soporte ([[2026-1023-lzt-categorias-gaming-y-social-network]]). Es decir, la reventa de cuentas de IA es un mercado **del lado del vendedor**, con su propia superficie de tickets de disputa y no un escaparate de consumo ([[2026-1023-lzt-superficie-de-avisos-faq-y-tickets]]). Y el único número económico que la captura de lzt publica es una comisión: recargar saldo con MasterCard cuesta **10 %** ([[2026-1023-lzt-topup-mastercard-comision-10]]) — un multiplicador que se aplica a todo lo comprado con ese saldo, incluidos los céntimos de una activación.

## 2. La aritmética del número: lo medido contra lo declarado

Aquí es donde el mercado se rompe a sí mismo, porque **casi todas las cifras que se citan de este sector son claims de marketing del propio vendedor**, y las pocas medidas contradicen a los claims o a sí mismas.

### 5sim: auditable, y por eso mismo el que más contradicciones tiene

Lo medible de 5sim es el CSV de precios del servicio `telegram`: **175 combinaciones país-operador en 111 países, 16 operadores**. Es el único proveedor de la captura donde el precio real es decodificable ([[2026-1023-5sim-piso-de-precio-telegram-01026-usd]]).

| Magnitud | Cifra | Naturaleza |
|---|---|---|
| Precio mínimo | **$0.1026** (Colombia, `virtual34`, 273.971 uds.) | **Medición** (CSV) |
| Precio máximo | **$8.8897** (Italia, `virtual60`/`virtual59`) | **Medición** |
| Dispersión min→max | **86,6×** | **Medición** |
| Mediana / media de las 175 filas | **$0.8942** / **$1.297** | **Medición** |
| Stock agregado | **128.999.730** unidades; 20 filas por encima del millón | **Medición** |
| Claim de la home | "starts at **$0.008**", "Over 500,000 numbers", "more than 180 countries" | **Claim** |
| Stock declarado para `OpenAI/ChatGPT` | **13.724.093** unidades — el más bajo de las ocho categorías del selector, frente a 64–162 M en las demás | Claim de contador |

El claim de $0.008 está **12,8× por debajo** del suelo medido del mismo proveedor ([[2026-1023-5sim-claim-500k-numeros-y-piso-0008]]). Y la misma home que dice "500.000 números" renderiza contadores por servicio de **128.999.934 (Telegram)** y **162.638.240 (Google/YouTube)**: dos órdenes de magnitud por encima de su propia cifra global. El contador de `OpenAI/ChatGPT` es el más bajo de los ocho —**13.724.093**— y el proveedor **no lo desglosa por país u operador** en la home ([[2026-1023-5sim-chatgpt-verificacion-stock-13-7-millones]]).

Dos avisos metodológicos que hay que aplicar al leer cualquier precio de esta fuente:
- **La tabla visible no está ordenada por precio.** Las 20 filas que renderiza el HTML están ordenadas por la columna `rate` descendente, no por coste, y las 41 filas con `rate = -1.0` quedan fuera de la vista: quien lee la pantalla concluye que el precio empieza en $0.5769 (Lituania) cuando el CSV trae Colombia a $0.1026, **5,6× más barato** ([[2026-1023-5sim-tabla-visible-ordenada-por-descuento-no-por-precio]]).
- **El stock no correlaciona con el precio.** Letonia tiene 7,9 M unidades a $4.0; Países Bajos 8,6 M a $3.2051; Angola 5 M a $0.2218 ([[2026-1023-5sim-stock-abundante-no-implica-precio-bajo]]). Y el 98,3 % de las unidades del catálogo pertenece a **un solo operador**, `virtual34`, que aparece en 107 de las 175 filas y es el más barato en 95 de los 111 países ([[2026-1023-5sim-virtual34-domina-el-catalogo]]).

Y la dispersión no es solo entre países: dentro de Italia el precio va de $4.0 a $8.8897 (122 %) y 83 de los 111 países tienen **un único operador** ([[2026-1023-5sim-dispersion-intra-pais-y-pocos-operadores]]). El precio real de la verificación es "precio por par país-operador", y en tres de cada cuatro países ese par no se puede elegir.

Y el ranking del precio es contraintuitivo: los diez suelos más caros son Italia $4.0, Alemania $3.5, Argelia $3.4551, Australia $3.2225, Francia $2.5, España $2.0513, Irlanda $1.9231… mientras **EEUU está en $0.6545** y Canadá entre $0.359 y $0.75. La variable que explica el precio no es el PIB del país sino la oferta concreta de operadores ([[2026-1023-5sim-europa-occidental-paga-la-factura]]). Cualquier plan de verificación que pida "número occidental" tiene que comparar país por país, no aplicar una regla regional.

Y la verificación de cuentas de IA es, en el catálogo del proveedor, **una línea larga de cola y no su centro de gravedad**: de los 1221 nombres enumerables solo **28 son de IA o herramientas de IA** (2,3 %), y dentro del catálogo hay 50 servicios de apuestas y un bloque de plataformas de microtareas y datasets ([[2026-1023-5sim-catalogo-28-servicios-ia]], [[2026-1023-5sim-catalogo-50-servicios-de-apuestas]], [[2026-1023-5sim-catalogo-plataformas-de-microtareas-y-datasets]]). El catálogo además no es una sola lista: son **dos listas con plantillas distintas y sin un nombre en común** — 245 entradas curadas (`Temporary Phone Number for X`, donde están los ocho servicios del selector) y 975 de cola alfabética (`Get a Temporary Phone Number for X`), de las cuales solo 5 de las 28 de IA caen en el bloque curado ([[2026-1023-5sim-dos-listas-una-curada-y-una-cola-alphabetica]]). Es decir: el proveedor tiene un producto de volumen —retail, delivery, apuestas— y la verificación de IA es un caso de uso más.

### HeroSMS: más barato en escaparate, opaco por diseño

| Magnitud | Cifra | Naturaleza |
|---|---|---|
| Precio "from" más bajo visible | **$0.0059** (TikTok/Douyin) | Claim ("from") |
| Precio "from" más alto visible | **$0.8551** (Full rent) | Claim ("from") |
| Precio de un número de ChatGPT | **no publicado** | — |
| Cobertura declarada | "180+ countries", "700+ sites", "500K+ numbers daily" | Claim |
| Cobertura enumerada en la página | **20 países, 45 servicios**, `Show more` sin contador | **Medición** |
| Reembolso | "No SMS received within **20 minutes**? Get an instant automatic refund" | Claim con plazo |

El suelo publicado del vault baja así de $0.1026 a $0.0059, **17,4×** — pero son magnitudes distintas (mínimo medido vs. "from" publicitario), así que el vault no tiene un suelo de mercado: tiene un suelo por proveedor ([[2026-1023-herosms-precios-escapate-entre-0059-y-08551]]). La diferencia estructural con 5sim es que **HeroSMS no publica ni precio ni stock del servicio que vende para ChatGPT**: la landing de ChatGPT es una guía SEO de 5 pasos con FAQ, y los cinco precios visibles (Full rent, Ticketmaster, TikTok, Instagram, Whatsapp) son de otros servicios ([[2026-1023-hero-sms-pagina-de-chatgpt-sin-precio-ni-stock-propio]], [[2026-1023-hero-sms-marketing-seo-por-servicio-en-vez-de-catalogo]]). Cualquier comparación de coste entre los dos proveedores hecha sobre páginas públicas es **asimétrica por construcción**: 5sim es auditable, HeroSMS no.

Y hay un dato que desmonta la comparación misma: **HeroSMS declara ser una fachada sobre SMS-Activate** ("powered by SMS-Activate technical infrastructure"; "HeroSMS is a new service built on the foundation of SMS-Activate") ([[2026-1023-herosms-sobre-la-infraestructura-de-sms-activate]]). Dos de los tres actores medidos no son independientes. Por eso es tan relevante que el tercero haya dejado de existir (§6).

Dos detalles más de HeroSMS que cambian la lectura de su catálogo. El primero es el **reparto físico/virtual**, que ningún precio delataría: en los cinco servicios visibles el stock virtual supera al físico entre 103× y 537× —Ticketmaster 98.850 físicos frente a 10.162.287 virtuales, Instagram+Threads 84.493 frente a 45.397.143, Whatsapp 104.283 frente a 25.319.129, TikTok/Douyin 133.403 frente a 21.064.192, y Full rent 1948 físicos con **0** virtuales— ([[2026-1023-hero-sms-stock-fisico-y-virtual-por-servicio]]). El segundo es el **contrato económico**: prepago sobre saldo, pago por uso, sin permanencia, con periodo de uso "temporary, from 20 min" y "Codes are exclusively available to buyers", es decir, no existe modo de prueba ([[2026-1023-hero-sms-modelo-pay-per-use-y-tabla-real-vs-virtual]]).

Y una asimetría más: de los **45 servicios enumerados** en HeroSMS, **solo uno es de IA** —`OpenAI`, enlazado a `/service/chatgpt`— frente a los 28 de 1221 de 5sim. La proporción es casi idéntica (2,2 % frente a 2,3 %), pero la diferencia operativa es total: en 5sim la verificación de IA es una categoría de primer nivel con precio y contador de stock; en HeroSMS es **una línea más de un bloque de enlaces SEO, sin tarjeta, sin precio y sin stock consultable** ([[2026-1023-herosms-solo-openai-como-servicio-de-ia]], [[2026-1023-hero-sms-marketing-seo-por-servicio-en-vez-de-catalogo]]). Para 5sim, además, el canal de confirmación no es solo SMS: una entrada del catálogo (`Virtual Number for Dropped-Call & Flash Call Verification`) ofrece **verificación por llamada** ([[2026-1023-5sim-una-entrada-de-verificacion-por-llamada]]).

### El precio del insumo en la capa (b): yuanes y céntimos

La tabla 卡网 de PriceAI es la única fuente de la captura donde el insumo de verificación aparece con **precio de mercado, stock y número de canales**: 接码 (códigos de verificación) a **¥0.20–¥0.57** y correo a **¥0.02–¥1.24** ([[2026-1023-priceai-channels-correo-y-jianma-a-centimos-como-insumo-de-alta]]).

| Fila | Precio | Con stock | Canales |
|---|---|---|---|
| **OpenAI / ChatGPT 接码** | **¥0.37** | **723** | **789** |
| Google / Gemini 接码 | ¥0.20 | 105 | 125 |
| PayPal 接码 | ¥0.49 | 11 | 12 |
| 通用接码 | ¥0.57 | 195 | 229 |
| Gmail / Google 邮箱 | ¥0.30 | 298 | 425 |
| 其他邮箱 / iCloud / Outlook | ¥0.02 | 71 / 56 / 259 | 93 / 123 / 295 |
| 真人 / KYC 验证 | **¥10.28** | **1** | 3 |

Dos lecturas. La primera: existe una capa que **compra el número en algún sitio y lo revende como código**, a un precio muy por debajo del suelo de 5sim — con un control de calidad explícito en el propio título ("没有售后", "售出不退"). La segunda, y más incómoda: el cuello de botella del alta con identidad real **no es el SMS, es el KYC humano**, que cuesta tres órdenes de magnitud más y tiene una unidad en stock.

La tabla completa son 53 productos en 7 plataformas (其他 17, ChatGPT 10, Claude 7, Grok 5, 邮箱 5, 接码 5, Gemini 4), con **9.147 unidades con stock, 2.727 agotadas y 11.874 canales** repartidos en **39 tiendas distintas** ([[2026-1023-priceai-channels-composicion-53-productos-en-7-plataformas]], [[2026-1023-priceai-channels-stock-por-fila-y-seis-productos-muertos]], [[2026-1023-priceai-channels-39-tiendas-y-una-larga-cola-de-revendedores]]). El precio abarca **cuatro órdenes de magnitud**, de ¥0 a ¥1.027.94 ([[2026-1023-priceai-channels-dispersion-de-precios-cuatro-ordenes]]), y en la familia ChatGPT: ChatGPT 普号 **¥0.05**, Codex周边 ¥0.18, ChatGPT Team ¥5.14, ChatGPT Plus 试用订阅 **¥11.85**, ChatGPT Go ¥29.87, Codex 额度充值 ¥75, ChatGPT Plus 正价代充 **¥112.04**, **ChatGPT Pro 100刀档 ¥123.60**, Pro 200刀档 ¥204.57, Pro 500刀档 ¥604.46 ([[2026-1023-priceai-channels-escalera-de-reventa-chatgpt-y-codex]]).

Y un detalle que invalida cualquier lectura ingenua de esa columna: **el nombre del plan no ordena el precio**. En Grok, "Ultra (200刀)" cuesta ¥71.75 y "Premium (30刀)" ¥118.22, porque Ultra se sirve por 速刷 (cuenta generada en serie) y Premium por 卡冲官方充值 ([[2026-1023-priceai-channels-grok-escalera-incoherente-ultra-mas-barato-que-premium]]). Lo que se compra no es "Plus" o "Ultra": es **Plus con recharge oficial a cuenta propia y 30 días de garantía**, y el mismo nombre de marca vale ¥11.85 o ¥112.04 según el modo de entrega (**×9,45**).

### El arbitraje de suscripción, que es otra capa del mismo negocio

Aparte de la reventa, PriceAI registra los precios **oficiales por región** de 17 paquetes, y ahí el margen se mide en porcentaje de descuento ([[2026-1023-priceai-17-paquetes-y-frescura-desigual]]):

| Producto | Precio de referencia | Mínimo regional | Descuento |
|---|---|---|---|
| ChatGPT Go | $8 ≈ ¥53.51 | **¥23.74 (Egipto)** | **−56 %** |
| ChatGPT Plus | $20 ≈ ¥133.79 | **¥103.65 (Filipinas)** | **−23 %** |
| ChatGPT Pro 100刀档 / 500刀档 | $100 / $500 | ¥582.63 / ¥2.913.14 (Egipto) | −13 % |
| ChatGPT Pro 200刀档 | $200 | ¥941.33 (Filipinas) | −30 % |
| Google AI Plus / Pro / Ultra 20x | $4.99 / $19.99 / $199.99 | **Bolivia**: ¥19.96 / ¥79.84 / ¥798.43 | **−40 %** |
| Google AI Ultra 5x | $99.99 | **¥199.43 (Turquía)** | **−70 %** |
| Claude Pro | $20 | ¥118.33 (Pakistán, canal iOS Store) | −12 % |
| Claude Pro Annual | $200/año | ¥1.229.99 (Egipto) | −8 % |
| Claude Max 5x / 20x | $100 / $200 | Nueva Zelanda | **−1 %** |
| Grok Plus / Super / Ultra | $8 / $100 / $200 | **Estados Unidos** | **sin brecha** |

Dos conclusiones. Una: **cada familia de producto tiene su propia geografía de precio**, y no hay un país "barato" genérico — el 70 % de Turkey es del escalón 5x de Google y el 40 % de Bolivia no toca ese mismo plan ([[2026-1023-priceai-gemini-ultra-5x-turquia-70-menos]], [[2026-1023-priceai-gemini-bolivia-40-menos]]). Y otra: **Grok no regionaliza**, lo que lo convierte en la referencia "sin arbitraje" contra la que se leen las demás ([[2026-1023-priceai-grok-sin-descuento-regional]]). En el tramo alto de Claude, el 1 % es ruido de redondeo: no hay geoarbitraje que capturar ([[2026-1023-priceai-claude-max-nueva-zelandia-1-menos]]).

Dos precisiones que evitan leer mal la tabla. La primera: hay **dos escaleras distintas de ChatGPT** y no deben mezclarse. La de cuotas de suscripción son tres pasos con el consumo valorado en dólares de uso —Plus $20/mes ($25 por 5 h, $450 al mes), Pro 5x $100/mes ($3.200 al mes) y Pro 20x $200/mes ($8.000 al mes)—, con la advertencia explícita de que **la API va aparte, aunque tengas la suscripción** ([[2026-1023-priceai-chatgpt-plus-y-pro-precios-y-ventanas]]). La de precios regionales es otra: tres tramos de $100, $200 y $500, cada uno con su país mínimo distinto —Egipto (¥582.63, −13 %), Filipinas (¥941.33, −30 %) y Egipto (¥2.913.14, −13 %) ([[2026-1023-priceai-chatgpt-pro-tres-tiers-de-precio]]). Es el mismo tipo de acoplamiento (plan, país, canal) que ya se vio en el stock de SMS: el precio nominal es una referencia del agregador y lo que se compra es un par. Y un tercer plano: el "−56 %" del ChatGPT Go es de la página de precios oficiales por región, y ese Go **no aparece** en la tabla de ventanas de cuota, así que el catálogo de OpenAI no es idéntico entre las dos páginas ([[2026-1023-priceai-chatgpt-go-egipto-56-menos]]). La segunda: la muestra regional varía mucho —de 235 regiones en ChatGPT Go a 48 en Grok Plus—, así que un "mínimo" sobre 48 regiones es una afirmación mucho más frágil que uno sobre 235 ([[2026-1023-priceai-17-paquetes-y-frescura-desigual]]). Y el plan anual es un caso único: solo Claude Pro Annual, $200/año con un 8 % de brecha en Egipto y canal iOS Store; los otros 16 paquetes de la tabla son mensuales ([[2026-1023-priceai-claude-pro-anual-egipto]]).

Todo esto tiene una pieza operativa que solo aparece en la home: el **支付门槛 (umbral de pago)** es una variable de comparación de primera clase —junto con 官网正价, 地区价 y 资格价—, y el instrumento que resuelve ese umbral es un producto aparte: el patrocinador **zovocard**, tarjetas virtuales de pago transfronterizo que cubren "ChatGPT/Claude 订阅、AWS 与 Google Cloud 云服务、跨境电商与建站等场景"; junto a él, **Spaceship** vende dominios `.xyz` numéricos de 6 a 9 dígitos desde **¥4.55/año** ([[2026-1023-priceai-oficial-precios-regionales-y-umbral-de-pago]], [[2026-1023-priceai-zovocard-y-spaceship-patrocinios-de-pago-y-dominio]], [[2026-1023-priceai-zovocard-tarjetas-virtuales-para-suscripciones]]). El agregador monetiza la necesidad que su propia tabla expone. El coste real de comprar una suscripción de IA en el mercado chino no es el precio: es **precio + medio de pago + fiabilidad del medio de pago**.

## 3. La fiabilidad: la tasa de entrega no es la disponibilidad

Este es el punto donde el mercado se revela como lo que es: un producto que vende una **probabilidad empírica**, no una garantía.

La página de OpenAI de 5sim define la "SMS delivery rate" con una precisión que conviene citar: es "how often SMS has recently arrived for that exact OpenAI combination", y **"a 65% rate means that SMS was received in about 65 out of 100 recent orders"** — una frecuencia histórica sobre pedidos recientes, calculada por par país-operador. **No es un SLA** ([[2026-1023-5sim-openai-tasa-entrega-65-de-100]]).

El reparto de responsabilidad entre las dos páginas es desigual y define el modelo: 5sim publica la tasa **antes** del pago, ofrece **Smart Buy** ("automatically picks the number with the highest SMS delivery success rate") y **no exige registrarse para navegar** el catálogo; HeroSMS sustituye esa transparencia por un **criterio de selección no auditable** —"specifically selected to pass ChatGPT's verification checks"—, sin publicar tasa, sin precio unitario y con reembolso a 20 minutos ([[2026-1023-5sim-smart-buy-y-tasa-entrega-visible]], [[2026-1023-hero-sms-openai-bloquea-numeros-voip-y-reintento-en-un-minuto]]). En los dos casos, el dato que decide el resultado —la tasa de aceptación de OpenAI— no lo publica ninguno: 5sim publica la de entrega del SMS, no la del alta.

| Dato | Cifra | Fuente |
|---|---|---|
| Techo de entrega declarado para OpenAI | **56 %** | Página del producto, 5sim |
| Mejor tasa visible en la tabla | **55.56 %** (Czechia `virtual26`, **43 pcs**) | Medición |
| Peor tasa visible | **39.39 %** (Slovakia `virtual34`, 95.841 pcs) | Medición |
| Mejor tasa **con stock de volumen** | 54.17 % (Poland `virtual34`, **110.468 pcs**) | Medición |
| Precio "from" del selector vs. ficha de producto | **$0.01 vs. $0.05**, mismo día | Conflicto declarado |
| Ventana de vida del número | **5–30 min**, auto-cancelación a los **5 min** | Claim |
| Reutilización | "Can I reuse the number? **No**" / "one OpenAI account verification" | Claim |

De aquí sale la aritmética honesta del coste: en el mejor caso visible, **casi uno de cada dos números comprados para verificar una cuenta OpenAI no recibe el SMS**, y el coste esperado por verificación *exitosa* es entre **1,8× y 2,5×** el precio nominal ([[2026-1023-5sim-openai-tasa-entrega-techo-56]]). Y no es amortizable: un número sirve para **una** verificación y no se reutiliza ([[2026-1023-5sim-numero-de-un-solo-uso-una-verificacion]]).

La otra mitad del problema es que **stock y tasa están desalineados**: las filas con mejor tasa tienen inventario residual —Estonia 24 pcs al 47,62 %, Czechia 43 al 55,56 %, Netherlands 63 al 42,5 %, France 224 al 43,48 %— mientras las dos filas con stock de cinco cifras (Polonia `virtual34` 110.468 al 54,17 % y Eslovaquia `virtual34` 95.841 al 39,39 %) tienen tasas menores o intermedias; Inglaterra `virtual66` comparte el 54,17 % con 930 unidades ([[2026-1023-5sim-openai-mejor-tasa-poco-stock]]). La única combinación que aguanta volumen es un `virtual34` con ~110.000 unidades al 54,17 %; todo lo demás es muestra de escaparate. Y esa tabla muestra **8 de 76 países, todas filas europeas**, con precios visibles de $0.12 a $0.5179, en un catálogo cuyo sesgo real es India y el sudeste ([[2026-1023-5sim-openai-tabla-visible-8-filas]], [[2026-1023-5sim-openai-76-paises-y-130-operadores]], [[2026-1023-5sim-catalogo-desviado-hacia-india-y-asia]]).

**Las tres promesas de reembolso son mutuamente inconsistentes**, y esta es la fricción más concreta del sector:

| Proveedor / página | Promesa |
|---|---|
| 5sim, home | "**Instant** refunds — if no SMS is received, your money is refunded automatically" |
| 5sim, página del producto OpenAI | "the payment is returned to your 5SIM balance **immediately**" (cancelación manual de orden sin usar) / "you will be refunded automatically — **rarely it may take up to 15 minutes**" / "returned to your 5SIM balance **after the order is completed**" |
| HeroSMS | "No SMS received within **20 minutes**? Get an **instant** automatic refund to your balance" |

Tres plazos y tres fórmulas sobre la misma operación. "Instantáneo" solo es cierto para la cancelación manual de una orden activa sin usar; **el caso que domina —el SMS que no llegó— es el que 5sim cuantifica en hasta 15 minutos** y HeroSMS en 20 ([[2026-1023-5sim-reembolso-instantaneo-si-no-llega-sms]], [[2026-1023-5sim-reembolso-hasta-15-minutos]], [[2026-1023-hero-sms-reembolso-si-no-llega-sms-en-20-minutos]]). Para un flujo automatizado la diferencia no es de texto: es una ventana de caja bloqueada por pedido fallido. Y ojo al matiz de HeroSMS: en su panel **no existe vía de retirada de fondos**; el reembolso automático solo es exigible mientras la empresa exista.

El resto de la capa de fiabilidad, resumido: **seis productos muertos** en la tabla de PriceAI (Claude Team Standard sin precio, Windsurf y Suno con "未记录" — nunca registrados—, 多邻国 Super de hace 15 días, Telegram con fecha 09/01, 礼品卡 de hace 9 horas); el timestamp discrimina casi exactamente el subconjunto sin precio — **las cinco filas fuera de la ventana de minutos son las cinco más rotten**, y todas las filas con precio están en minutos —, porque un canal que lleva horas sin actualizar es un canal sin oferta vigente ([[2026-1023-priceai-channels-stock-por-fila-y-seis-productos-muertos]], [[2026-1023-priceai-channels-frescura-minutos-y-cinco-restas]]); y OpenAI **bloquea números VoIP**, con lo que el reintento real es "comprar otro, de otro país" en menos de un minuto, según el proveedor ([[2026-1023-hero-sms-openai-bloquea-numeros-voip-y-reintento-en-un-minuto]]).

## 4. Qué significa para MyOwnClone

Aquí es donde el thread tiene que ser honesto, y la respuesta corta es: **hoy, casi nada**.

**(a) Ningún paso de SMS está vivo en el producto.** El alta verificada en `/registro` es self-service con **magic link + código de 6 dígitos por email + Google OAuth**; el onboarding son cuatro campos (`name`, `personality`, `language`, `confirm`) ([[2026-1022-live-verify-alta-y-precios-ya-publicos]], [[2026-1022-onboarding-cuatro-pasos-encuestas]]). No hay teléfono en ninguna parte del flujo. Este mercado es, hoy, **adyacente y no producto**: no toca el funnel actual, solo el de terceros ([[2026-1023-5sim-chatgpt-verificacion-stock-13-7-millones]]).

**(b) Si se añadiera verificación por SMS, aparecería una cuarta categoría de coste.** El modelo de [[2026-1022-costes-por-categoria-tenant]] separa `categoryCloneResponses` y `categoryIngestion` (facturables al tenant) de `categoryPlatformOps` (absorbido por la plataforma), con la asunción de que "el consumo del tenant escala linealmente pero la operación interna no se traslada". Un SMS de alta escala **una vez por alta de tenant**, y no es ni respuestas ni ingestion: es una categoría que el corte actual no contempla, y cuya asunción de "absorción" se erosiona en silencio ([[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]). Y el cálculo no es solo el precio del número: la verificación por SMS de HeroSMS exige **VPN o proxy cuya geolocalización coincida con el país del número y una IP distinta por cuenta**, porque "no registrar varias cuentas desde una misma IP" está "prohibido por OpenAI" ([[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]]). Una IP fija de servidor —el patrón del nginx autoalojado vivo en `212.227.169.99`— es exactamente el patrón que ese proveedor dice que dispara el bloqueo. El coste marginal por alta, tal como está calculado en el vault, excluye tres partidas: la IP geolocalizada, la comisión de recarga (10 % en lzt.market) y la continuidad de identidad, porque el número desechable **verifica el alta pero no sostiene la cuenta** — OpenAI ofrece alternativas por email para la recuperación ([[2026-1023-hero-sms-numeros-de-un-solo-uso-y-recuperacion-por-email]]).

**(c) Comprar cuentas pre-made no es comprar capacidad de verificación.** lzt.market y la tabla 卡网 venden la cuenta terminada, con modos de entrega declarados en prosa de marketplace, advertencias de baneo escritas en el título y una columna de garantía que multiplica el precio hasta ×1.659. Es **account-farming**, con exposición de ToS y de baneo de plataforma, y la propia página de HeroSMS lo dice sin rodeos: "bypass restrictions", "sell them on an exchange". El vault no recomienda esto ni lo propone como opción; lo registra porque el coste de entrada de esa alternativa es casi cero y alguien acabará probándolo ([[2026-1023-lzt-categoria-llm-accounts-para-reventa]]).

**(d) El borde regulatorio y ético es real y está documentado.** Los átomos registran tres cosas que no son interpretación: un proveedor **retirando su marca porque cualquier servicio que se llame como él es una estafa** ("Наше имя уходит вместе с нами" (Nuestro nombre se va con nosotros); "Si usted encontró un servicio que se llama SMS-Activate, esté seguro: esto son estafadores") (§6); OpenAI bloqueando VoIP; y la exigencia de que IP/VPN coincidan con el país del número.

Y hay un cuarto punto que no es un hecho del sector sino del proveedor: la guía de 5sim para OpenAI afirma, sin citar ninguna norma ni política de OpenAI, que "Is it allowed to use a virtual number for OpenAI / ChatGPT? **Yes**", y cierra con un descargo en sentido contrario —"this website is an independent publication and is **not affiliated with, sponsored, authorized, or otherwise endorsed by OpenAI**" ([[2026-1023-5sim-guia-openai-marketing-sin-vinculo-con-openai]]). Es una declaración comercial del vendedor, no una autorización. La página es contenido SEO con las mismas cifras de la tabla (precio, países, operadores, tasa) repetidas en cada guía de servicio —Claude, Manus, Cursor, DeepSeek, NVIDIA, Apple— lo que confirma que la verificación de cuentas de IA es una **vertical con estrategia de contenido propia**, no un caso suelto ([[2026-1023-5sim-catalogo-28-servicios-ia]]). Es un mercado lleno de cosas que se rompen, y el vault **lo registra, no lo recomienda**.

## 5. Hetzner: el único ancla limpia de toda la captura

Frente a todo lo anterior hay una línea de coste del vault que sí es un proveedor con precio verificable y relato de cumplimiento: **el hosting**. Y la comparación es instructiva precisamente porque es el mismo tipo de partida —infraestructura del producto— y el estándar de calidad es radicalmente otro.

| Magnitud | Cifra | Naturaleza |
|---|---|---|
| Plan más barato calculable (Shared · **Regular Performance**, plan **CPX02**, 1 vCPU AMD) | **€ 5.99/mes** *excl. VAT* | **Medición** (calculadora) |
| Facturación por hora equivalente | **€ 0.0096/h** | **Medición** |
| Familias del catálogo ("starting from") | Cost-Optimized (Shared) desde **€ 5.99**; Regular Performance (Shared) desde **€ 6.49** (+€ 0.50, ×1.08) | Claim de catálogo |
| Salto a vCPU dedicadas | General Purpose desde **€ 43.49/mes** (+€ 37.00, ×6.70; **×7.26** del más barato) | Claim de catálogo |
| Tráfico de salida incluido | **20 TB**, coste estimado **€ 0.00** | Medición |
| Recargo | **€ 1.00 por TB adicional en la UE** | Claim de página |
| IPv4 primario | **€ 0.00** (conmutador en la configuración por defecto; lectura tentativa) | Lectura de captura |
| SLA | **99,9 %** de uptime con créditos, soporte 24/7 por email | Claim de página |
| Cumplimiento | **GDPR**, **ISO/IEC 27001** (parques de Alemania y Finlandia), **BSI C5** | Claim de página |
| Firewalls stateful y redes privadas | "sin costes adicionales", asignables a tantos servidores | Claim de página |
| Apps de un clic | Coolify, Docker CE, GitLab CE, Grafana, Prometheus, Jitsi, Nextcloud… | Claim de página |
| API/CLI e IaC | REST API, CLI, integraciones Python/Go, Ansible, Terraform, Kubernetes | Claim de página |
| Regiones | Alemania, Finlandia, Singapore y USA; zonas disponibles **FSN1, NBG1, HEL1, SIN**; parques en Falkenstein, Nuremberg, Helsinki, Hillsboro, Ashburn y Singapore (desde 2024) | Medición |

Dos cosas se pueden decir de esto. La primera, y incómoda: **el plan más barato de Hetzner no cabe en el presupuesto de ≤ €4/mes que la captura fijaba** — es un 50 % por encima sin IVA, y el suelo de lista es €5.99 sin IVA con el siguiente escalón en €6.49, de modo que la conclusión "no hay ningún plan por debajo de €5.99" es una inferencia del átomo, no una frase de la página ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]). La palanca real es la facturación por hora: €0.0096/h significa que un servidor encendido unas pocas horas cuesta céntimos, no €5.99 ([[2026-1023-hetzner-facturacion-por-hora-0-0096]]).

La segunda: **el hosting tampoco aparece en el corte de costes del back-office**. No existe categoría de infraestructura en el desglose documentado: con un plan base de 99/mes y un solo tenant, ~€6/mes es el 6 % del ingreso; con 100 tenants, el 0,06 % ([[2026-1023-hetzner-costes-por-categoria-vs-infraestructura-propia]]). Es una tercera línea de coste fijo de plataforma que el panel no muestra.

El contraste que cierra el thread: **el hosting tiene precio verificable, SLA, cumplimiento auditable y un contrato que dice qué pasa cuando el servidor se cae; el mercado de la verificación no tiene ninguna de esas cosas**. Ni SLA, ni SLA de entrega (la "tasa" es un histórico observado que se degrada solo), ni cumplimiento, ni continuidad de contraparte (§6). Por eso el vault tiene un anchor y no dos: Hetzner es el único sitio de la captura donde el número y el contrato son la misma cosa.

El argumento de venta de Hetzner también merece la nota de cautela que corresponde: el comparador de tráfico da AWS €1.560,41/mes, Azure €1.287,11, Google €1.326,61 y Hetzner €0.00 a 20 TB, pero la cifra de "ahorro medio" que la página muestra (€ −4.785,64/mes) es mayor que cualquiera de las diferencias individuales que ella misma enseña, y los datos se atribuyen a sparecores.com, sin metodología verificable en la captura ([[2026-1023-hetzner-comparativa-trafico-20tb-contra-hyperscalers]]).

## 6. El cierre: SMS-Activate, y lo que significa para el sector

El aviso de cierre de SMS-Activate es el hecho más duro de esta thread, y no por lo que dice del sector en abstracto sino por lo que dice de su calendario de contacto. El proveedor **cesó toda su actividad** el 22 de diciembre, tras 10 años ("С 22 декабря мы полностью прекратили свою деятельность"), sin dar el año ni la razón ([[2026-1023-sms-activate-cierra-total-el-22-de-diciembre]]). El calendario de la liquidación es la parte legible:

- **22 de diciembre** — cesa la actividad.
- **5 de febrero** — se cierra la retirada de fondos ("вывод средств"). La razón que da el propio proveedor: "больше некому обрабатывать ваши запросы" — después de esa fecha ya no hay nadie que gestione las solicitudes. El saldo retenido pasó de ser crédito exigible a dinero atrapado ([[2026-1023-sms-activate-retiradas-hasta-el-5-de-febrero]]).
- **Hasta el 30 de abril** — única vía de contacto: un email, `info@sms-activate.org`, "по самым важным вопросам", con un SLA declarado de **hasta 7 días** de respuesta ([[2026-1023-sms-activate-contacto-hasta-el-30-de-abril-con-plazo-de-7-dias]]).
- **La marca se retira** y el proveedor advierte literalmente que cualquier servicio que se llame SMS-Activate **es una estafa** ([[2026-1023-sms-activate-nombre-retirado-cualquier-servicio-igual-es-fraude]]).
- Y lo más relevante para el resto del thread: **el propio cierre confirma el traspaso a HeroSMS** — "Свои технологии мы передали команде сервиса HeroSMS... Рекомендуем попробовать его" ([[2026-1023-herosms-sobre-la-infraestructura-de-sms-activate]]).

Tres lecturas que el vault no puede cerrar. (i) Si SMS-Activate dejó de existir como empresa, HeroSMS no puede ser una fachada sobre un operador vivo: es **sucesor único por traspaso de tecnología**, y en ese caso sus cifras de marketing ("180+", "700+", "500K+") son herencia de un origen que ya no publica nada que las respalde. (ii) El precedente del saldo atrapado es una advertencia estructural sobre el modelo prepago: la garantía de reembolso protege contra la unidad que no cumple, **no contra la desaparición del proveedor**. (iii) El mismo hecho convierte la comparación "5sim vs HeroSMS" en algo más pequeño de lo que parecía: no son dos mercados, son un operador autónomo y el último superviviente de un linaje que ya se apagó.

## 7. Fricciones para juicio humano

Las que los átomos levantaron y el vault no puede resolver. Están aquí para decisión de una persona.

1. **Tres recuentos de países para 5sim y uno más para HeroSMS.** La home dice "more than 180", el catálogo muestra `Show all 153`, el CSV de `telegram` contiene 111 países y la ficha de OpenAI declara 76 países con 130 operadores. HeroSMS declara "180+" con una lista visible de 20 países y sin contador de exhaustividad. Ninguno de estos cuatro recuentos es un inventario ([[2026-1023-5sim-catalogo-153-paises-contra-180-de-la-home]], [[2026-1023-herosms-20-paises-enumerados-contra-180-declarados]]).
2. **Tres promesas de reembolso incompatibles** ("instant" / "hasta 15 minutos" / "20 minutos") sobre la misma operación, con "instant" solo cierto en el caso menos frecuente (§3).
3. **El suelo de $0.008 contra el de $0.1026**, ambos atribuidos a 5sim el mismo día, y contra el de $0.0059 de HeroSMS, que no es un mínimo medido sino un "from" publicitario de otro servicio. El vault no tiene un suelo de mercado: tiene tres cifras de proveedor que no se comparan entre sí ([[2026-1023-5sim-claim-500k-numeros-y-piso-0008]]).
4. **"500.000 números" contra contadores por servicio de cientos de millones**, en la misma home. Y el "500K+/500.000 números" de HeroSMS reproduce las dos cifras exactas de 5sim — lo que apunta a una constante publicitaria del sector o a un origen común, no a dos inventarios ([[2026-1023-herosms-claims-700-servicios-180-paises-500k-numeros]]).
5. **1329 contra 1221 servicios**: el botón dice `Show all 1329` y el cuerpo de la página solo hace enumerable 1221 nombres únicos sin un solo duplicado. 108 servicios quedan fuera de lo legible ([[2026-1023-5sim-catalogo-1221-servicios-nombres-unicos]]).
6. **El suelo de OpenAI: $0.01 en el selector y $0.05 en la ficha de producto**, el mismo día, y en un bloque de cifras que es idéntico byte a byte entre la home y `/en/products` — es decir, la misma cifra replicada en dos URL, no dos corroboraciones ([[2026-1023-5sim-openai-76-paises-y-130-operadores]], [[2026-1023-5sim-catalogo-servicios-precios-y-stock]]).
7. **El cierre de SMS-Activate contra la lectura "HeroSMS es una fachada sobre un operador vivo"**. El aviso del propio operador saliente —"transferimos nuestras tecnologías al equipo del servicio HeroSMS"— y su calendario de liquidación no pueden ser compatible con un "fachada sobre operador activo" ([[2026-1023-herosms-sobre-la-infraestructura-de-sms-activate]]).
8. **Y la grande, que no es de este mercado sino del producto:** ¿de dónde saldría una verificación de identidad en MyOwnClone, si algún día hiciera falta? El correo con magic link y código de 6 dígitos funciona y es el que ya sostiene las cuentas ([[2026-1022-auth-magic-link-codigo-seis-digitos]]). Todo lo de esta thread sugiere que el margen de mejora del alta es cero y el coste de cambio no lo es.

## Nota de método

Todas las cifras de este thread proceden de átomos del 2026-10-23 leídos de capturas del 2026-10-22. La distinción entre **medición** y **claim** se ha mantenido explícita en cada tabla: "medición" = dato que el lector calculó sobre la captura (CSV de precios de 5sim, tabla de 53 filas de PriceAI, lista de países de HeroSMS, calculadora de Hetzner); "claim" = declaración del propio proveedor en su página, sin evidencia adjunta. Las fuentes principales son `sources/2026-10-22-5sim-*.md`, `sources/2026-10-22-hero-sms-*.md`, `sources/2026-10-22-sms-activate-closed.md`, `sources/2026-10-22-lzt-market-home.md`, `sources/2026-10-22-priceai-channels.md` y `sources/2026-10-22-hetzner-cloud.md`. La captura de lzt.market es un **render parcial de SPA** sin un solo precio, así que de ese mercado solo puede afirmarse la forma del catálogo, nunca el precio ([[2026-1023-lzt-captura-parcial-sin-precios-ni-stock]]).

Ver también: [[myownclone-estado-live-2026-10]] (estado vivo del producto), [[myownclone-platform-architecture]] (la capa de inferencia y los 中转), [[myownclone-gtm-monetization-roadmap]] (dónde encajaría una decisión de este tipo), [[2026-1022-mvp-salir-al-mercado-pronto]] y [[2026-1022-beta-activo-trafico-real]].

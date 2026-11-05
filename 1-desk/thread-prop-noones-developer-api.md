# Propuesta de hilo — captura `2026-10-25-noones-developer-api.md`

Fuente: `sources/2026-10-25-noones-developer-api.md` (`https://dev.noones.com/`, capturada 2026-10-25, 547 palabras).
Átomos nuevos de esta captura: 13 (todos en `2-atoms/`, prefijo `2026-1026-noones-`).
Extensiones a átomos existentes: 2 (en `1-desk/extend-noones-developer-api.md`). Fricciones planteadas: 3.

---

## Propuesta A — `economia-de-la-verificacion-y-reventa-de-cuentas`

```markdown
### La capa institucional del mismo mercado: operar cuentas ajenas con API y consentimiento

La §7 de este thread llegó a una conclusión sobre NoOnes que era, hasta ahora, una afirmación sin contraparte: **la identidad verificada no es un riesgo legal que se minimiza, es el producto** — el peldaño L1→L3 no da precio, da **techo** ([[2026-1024-noones-escalera-de-verificacion-l1-l1plus-l2-l3]], [[2026-1024-noones-tabla-de-limites-por-nivel]]). Y la §7.5 dejó la pregunta abierta: **qué hay en código abierto para automatizar el alta**.

La captura del 2026-10-25 de `https://dev.noones.com/` (547 palabras) añade la pieza que faltaba: **el proveedor no solo permite operar cuentas propias; ofrece formalmente operar las cuentas de terceros**, y lo hace con un mecanismo de consentimiento explícito, no con credenciales compartidas.

**Los dos formatos, y por qué la bifurcación es el dato.** La página ofrece exactamente dos puertas —"Choose Your Format" ([[2026-1026-noones-api-dos-formatos-directo-y-delegado]]):

| Formato | Texto literal | Techo |
|---|---|---|
| **Direct Access** | "create an app that can only access and automate **your own** NoOnes account" | Solo la cuenta del que instala ([[2026-1026-noones-acceso-directo-limitado-a-tu-propia-cuenta]]) |
| **Delegated Access** | "create an app that **other users can install and grant permission** to manage their account—from automating trading on their behalf to keeping track of accounting" | Cuentas de terceros, con permiso concedido por cada titular ([[2026-1026-noones-acceso-delegado-app-instalada-por-el-usuario]]) |

Lo relevante para esta thread es que **el modelo institucionalizado no es "reventa de cuentas" sino "gestión de cuentas con permiso"** — y por eso merece un sitio al lado del bot de registro masivo ([[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]) y de la categoría `LLM Accounts` de lzt.market ([[2026-1023-lzt-categoria-llm-accounts-para-reventa]]), no dentro de ellos. En la reventa, el vendedor entrega un inventario y asume el baneo ("封号不保", "平均存活3天"); en Delegated Access, **el usuario conserva la cuenta, la verifica y concede el permiso**, y la app opera dentro de una plataforma que publica el techo de volumen de cada nivel. Es la versión con contrato del negocio que el corpus documenta en su versión artesanal.

**El dato duro, y por qué es una fricción con la escalera de verificación.** El único caso de uso que cruza la frontera entre cuentas es el del historial: *"This API allows to retrieve analytics data for you own account and other users of your app"*, con fines declarados *reporting* y *audit* ([[2026-1026-noones-api-de-analitica-del-historial-para-cuentas-propias-y-de-usuarios-de-tu-app]]). Y los cuatro badges de la página **revelan la distribución de permisos mejor que cualquier documento**: los tres casos operativos —bank transfer, buying bot, greeting app— llevan "Direct Access", y **solo el de historial lleva "Direct Access Delegated Access"** ([[2026-1026-noones-cuatro-casos-de-uso-como-catalogo-de-integracion]]). Es decir: **la superficie que cruza cuentas es estrecha y específica** (leer y reportar), no un "haz lo que quieras con mi cuenta".

Pero hay un punto que la captura deja abierto y que hay que dejar escrito sin resolver: uno de los cuatro bullets de cabecera es **"Trade on behalf of your clients"** y otro **"Automatically update offer margins"** ([[2026-1026-noones-trade-en-nombre-de-tus-clientes-como-modelo-de-negocio]], [[2026-1026-noones-actualizacion-automatica-de-margenes-de-oferta]]) — es decir, el proveedor **invita al tercero a ser market maker del lado vendedor**, y el lado vendedor es exactamente el que §7 ya gobierna por identidad: **Publish Offers = No en L1, Yes desde L1+**, y la **Visa virtual exige ID completo** ([[2026-1024-noones-publicar-ofertas-y-visa-virtual-exigen-id]]). La captura **no publica los scopes delegables** ni si esa capacidad hereda el nivel del usuario delegante o el de la app. Marcado para juicio humano: o la identidad verificada del usuario es la que abre la capacidad y la app es un ejecutor, o existe capacidad de operar por terceros sin verificación individual del titular —y eso cambiaría el significado de toda la escalera L1→L3.

**Lo que la captura no da, y es importante decirlo con precisión.** `dev.noones.com` **no es un repositorio de documentación**: cero endpoints, cero esquema de autenticación, cero rate limits, cero precios, cero SLA; el botón "Get Started" apunta a un ancla de la misma página ([[2026-1026-noones-dev-noones-sin-precios-ni-limites-ni-documentacion-publica]]). Las promesas son todas cualitativas —"grow your business, automate trades, decrease trade times", "hands-free", "discounted"— y **no hay una sola cifra en las 547 palabras** ([[2026-1026-noones-promesas-de-la-dev-home-sin-una-sola-cifra]]). El único dato duro de toda la página es **la estructura de permisos**, no el rendimiento. Esto corrige, sin reescribirlo, la lectura que el thread hacía de la superficie pública de NoOnes: el enlace "API documentation" que el pie expone apunta a `dev.noones.com`, pero lo que hay ahí es el escaparate de dos formatos de acceso, y lo técnico vive detrás de dos dashboards autenticados.

**Y un detalle de superficie que hay que registrar porque separa dos lecturas de "el proveedor bloquea".** La captura de `dev.noones.com` del 2026-10-25 devuelve **contenido completo**, sin mensaje de jurisdicción restringida, mientras que la home `noones.com` del 2026-10-23 devolvía exclusivamente *"You are accessing NoOnes from a restricted jurisdiction"* con detección de IP en EE.UU. ([[2026-1026-noones-dev-noones-devuelve-contenido-mientras-la-home-bloquea-por-ip]]). La captura no registra la IP de origen de ninguna de las dos, así que **no se puede distinguir "el subdominio de developers no está filtrado" de "las dos capturas se hicieron desde IPs distintas"**. Marcado para juicio humano, no auto-resuelto: la §"La geografía como tercera capa" de este thread trata el filtro de NoOnes como uniforme, y esta captura lo pone a prueba sin cerrarlo.

**El punto de método para el resto del thread.** El caso de uso más pequeño de la API es el más revelador: un bot que **saluda al contraparte** cuando empieza un trade —*"the bot will greet your trade partner and let them know you'll be there shortly"* ([[2026-1026-noones-bot-de-saludo-al-iniciar-el-trade]]). No mueve fondos, no toca precios: **cubre el hueco de latencia de respuesta con un contraparte anónimo**. Y el caso de gift cards deja claro el patrón de "API de marketplace sin capa de ejecución": *"build your bot, connect it to a gift card processor"* — el procesamiento lo pone el integrador ([[2026-1026-noones-bot-de-compra-de-gift-cards-con-procesador-externo]]). En los dos extremos, la automatización que la plataforma **no** incluye es exactamente la que el proveedor considera suyas; lo que ofrece es el andamiaje de permisos. Para una thread que documenta markets de fricción, esto es una categoría nueva: **fricción de permisos**, que no es la de verificación, ni la de precio, ni la de geolocalización.
```

THREAD: economia-de-la-verificacion-y-reventa-de-cuentas

---

## Propuesta B — `el-agregador-de-precios-como-producto`

```markdown
### La otra mitad del mercado: el proveedor que publica un market maker en lugar de un agregador

Este thread documenta cómo se construye un agregador de precios de terceros sin SLA, y su tesis de fondo es que **el negocio real de un agregador es mantener el dato fresco** (§5: el canal de corrección es un grupo de QQ, sin SLA ni auditoría; la promesa de "更新时间" verificable se vuelve falsa sin que nadie lo note). La captura del 2026-10-25 de `https://dev.noones.com/` no es un agregador, pero es **el caso limite del mismo problema**: un proveedor de marketplace que no publica precios de insumo, sino que **invita al integrador a mantener su propio libro de ofertas**.

**Los cuatro bullets de cabecera de `dev.noones.com`**, textuales ([[2026-1026-noones-api-dos-formatos-directo-y-delegado]]):

- "Automate your trading"
- "Receive trade activity notifications"
- "**Trade on behalf of your clients**"
- "**Automatically update offer margins**"

El último es el que importa aquí. **"Automatically update offer margins"** es la función de un agregador de precios aplicada al lado vendedor del marketplace: el bot recalcula el margen de sus ofertas y lo escribe en la plataforma ([[2026-1026-noones-actualizacion-automatica-de-margenes-de-oferta]]). La diferencia estructural con PriceAI y VeriDrop es total y vale la pena explicitarla: PriceAI **no vende** ("不卖货、不收款、不参与交易") y VeriDrop **no publica precio** sino detección; los dos son índices. El integrador que usa esta API de NoOnes no es un índice — **es un market maker que escribe en el libro de un tercero**.

**Por qué esto importa para la arquitectura del producto del vault.** Este thread ya registró la lección de PriceAI: una cifra sin criterio es ruido, y lo que hace un agregador defendible es **declarar la unidad, el denominador y el criterio de frescura** (§2, §7.3). La API de NoOnes es el ejemplo simétrico: **no publica ninguna de esas tres cosas**. La captura son **547 palabras sin un solo número** —ni precios, ni límites, ni SLA, ni endpoints, ni esquema de autenticación ([[2026-1026-noones-dev-noones-sin-precios-ni-limites-ni-documentacion-publica]], [[2026-1026-noones-promesas-de-la-dev-home-sin-una-sola-cifra]]). Lo único auditable es **la estructura de permisos**: Direct Access (solo la cuenta propia) frente a Delegated Access (cuentas de terceros con permiso concedido por cada titular) ([[2026-1026-noones-acceso-directo-limitado-a-tu-propia-cuenta]], [[2026-1026-noones-acceso-delegado-app-instalada-por-el-usuario]]), con el único caso de uso que cruza cuentas siendo **historial de trading para reporting y audit** ([[2026-1026-noones-api-de-analitica-del-historial-para-cuentas-propias-y-de-usuarios-de-tu-app]]).

**La lección de diseño, que es transferible.** Un market maker necesita tres cosas que esta captura demuestra que **no están en la API**: (1) un **feed de precios de referencia** —de dónde sale el margen objetivo—; (2) un **criterio de freshness** —cuándo se recalcula—; (3) una **unidad de volumen** —sobre qué se mide el margen. La API de NoOnes no publica ninguna de las tres, y su propio caso de uso de gift cards lo dice con claridad: *"build your bot, connect it to a gift card processor"* — la capa de ejecución y de liquidación la pone el integrador, no el proveedor ([[2026-1026-noones-bot-de-compra-de-gift-cards-con-procesador-externo]]). Para un producto como el del vault, que ya tiene un modelo de negocio centrado en manage + pricing ([[myownclone-gtm-monetization-roadmap]]), la lección es incómoda: **delegar el margen a la API del proveedor no elimina el trabajo del agregador, solo le quita la oportunidad de que ese trabajo sea medible y auditable por el usuario**. El bot de saludo automático, que "solo" cubre la latencia de respuesta con el contraparte ([[2026-1026-noones-bot-de-saludo-al-iniciar-el-trade]]), es el recordatorio de que **en un mercado entre pares la fricción que se automatiza primero es la de confianza, no la de precio** — y que automatizar el margen sin automatizar la confianza produce un libro que la contraparte no quiere atender.
```

THREAD: el-agregador-de-precios-como-producto

---

## Nota para el editor

- No se ha modificado ningún fichero en `3-threads/` ni en `2-atoms/`.
- Las dos propuestas son texto para insertar; cada bloque lleva su línea `THREAD:` con el hilo al que corresponde.
- Átomos de esta captura: `2026-1026-noones-api-dos-formatos-directo-y-delegado`, `2026-1026-noones-acceso-directo-limitado-a-tu-propia-cuenta`, `2026-1026-noones-acceso-delegado-app-instalada-por-el-usuario`, `2026-1026-noones-api-de-analitica-del-historial-para-cuentas-propias-y-de-usuarios-de-tu-app`, `2026-1026-noones-bot-de-saludo-al-iniciar-el-trade`, `2026-1026-noones-bot-de-compra-de-gift-cards-con-procesador-externo`, `2026-1026-noones-dev-noones-sin-precios-ni-limites-ni-documentacion-publica`, `2026-1026-noones-actualizacion-automatica-de-margenes-de-oferta`, `2026-1026-noones-cuatro-casos-de-uso-como-catalogo-de-integracion`, `2026-1026-noones-trade-en-nombre-de-tus-clientes-como-modelo-de-negocio`, `2026-1026-noones-notificaciones-de-actividad-de-trade-como-capacidad-de-la-api`, `2026-1026-noones-promesas-de-la-dev-home-sin-una-sola-cifra`, `2026-1026-noones-dev-noones-devuelve-contenido-mientras-la-home-bloquea-por-ip`.
- Extensiones propuestas en `1-desk/extend-noones-developer-api.md`: `2-atoms/2026-1024-noones-superficie-publica-productos-y-dominios-espejo`, `2-atoms/2026-1024-noones-publicar-ofertas-y-visa-virtual-exigen-id`.
- Fricciones: (1) `2026-1026-noones-dev-noones-sin-precios-ni-limites-ni-documentacion-publica` vs `2026-1024-noones-superficie-publica-productos-y-dominios-espejo` ("API documentada"); (2) `2026-1026-noones-trade-en-nombre-de-tus-clientes-como-modelo-de-negocio` vs `2026-1024-noones-publicar-ofertas-y-visa-virtual-exigen-id` (nivel heredado en permisos delegados); (3) `2026-1026-noones-dev-noones-devuelve-contenido-mientras-la-home-bloquea-por-ip` vs `2026-1024-noones-bloquea-ip-estadounidense-con-mensaje-explicito` (uniformidad del filtro de jurisdicción).
- Cifras verificadas literalmente contra `sources/2026-10-25-noones-developer-api.md` (líneas 10-13 bullets, 21 promesa de cabecera, 25 iconos de caso de uso, 31-35 bank transfer, 41-45 buying bot, 51-55 greeting app, 57 y 59-63 historial/SIWP, 67-83 los dos formatos con sus dos URLs de dashboard).

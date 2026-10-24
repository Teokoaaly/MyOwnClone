---
id: thread-myownclone-platform-architecture
type: thread
updated: 2026-10-23
sources: [raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md, raw/articles/myownclone-frontend-recon.md, raw/articles/myownclone-technical-deep-dive-2026-06-23.md, sources/2026-10-22-midjourney-proxy-github.md, sources/2026-10-22-new-api-github.md]
links: ["[[myownclone]]", "[[myownclone-vs-myclone-is]]", "[[myownclone-security-surface]]"]
---

# Thread — Arquitectura real de MyOwnClone

Qué hace el producto por dentro, verificado contra bundles y código. Este thread es el contrapeso de [[myownclone-strategy-and-vision]]: allí está lo que el founder quiere que sea; aquí está lo que el código hace. La distancia entre ambos threads es, en gran parte, el backlog del producto.

> **⚠️ Actualizado 2026-10-22 — este thread describe la generación anterior del despliegue.**
> La re-verificación en vivo (`0-raw/2026-10-22-myownclone-live-reverification.md`) encuentra que el sitio ya no está en Vercel, ya no tiene nueve subdominios, ya no expone cero endpoints REST y ya no usa Poppins ni PostHog. Lo que sobrevive intacto es la parte derivada del **checkout local del código** — la arquitectura de dos repos, el drift de schemas, el pipeline de chat — porque esa evidencia no depende del hosting. La parte de **superficie desplegada** (hosting, API, stack, instrumentación, diseño) es histórica. Ver [[myownclone-estado-live-2026-10]].

## Estado vivo (2026-10-22) — lo que se sabe del despliegue actual

Tres secciones de este thread quedaron desactualizadas y se sustituyen aquí:

- **Hosting** — ya no Vercel. `Server: nginx/1.28.3 (Ubuntu)` desde `212.227.169.99`, sin `x-vercel-id`. Certificado Let's Encrypt emitido el 2026-10-14. El Aviso Legal sigue diciendo "Vercel Inc." — ver [[2026-1022-live-verify-deployment-migrada-a-vps-nginx]].
- **API** — ya no cero endpoints. `GET /api/clones`, `/api/inbox` y `/api/clones/x/prompts` devuelven `401 {"error":"Unauthorized"}`; `/api/auth/session` devuelve `200`. El chat público sigue en 404 (bug `myownclone_public_bp`). Ver [[2026-1022-live-verify-superficie-rest-api-inexistente-antes]].
- **Stack de diseño e instrumentación** — Poppins pasa a DM Sans; la clave de tema `myownclone-theme` pasa a `localStorage["theme"]`; las variables CSS son un set nuevo; no hay identificadores de Sentry ni PostHog en el HTML ni en los chunks. Ver [[2026-1022-live-verify-identidad-legal-y-diseno-reconstruidos]].

Lo que no se puede determinar desde fuera: la versión de Next.js (`/_next/version.json` devuelve 404 porque el catch-all sirve HTML) y si el backend Flask de `api/` sigue siendo el que sirve el sitio, o si el despliegue nuevo es solo el front.

## La capa de inferencia: entre API propia, gateway y relay

Esta sección añade a lo anterior la pieza que faltaba: **de dónde sale la inferencia y con qué abstracción**. Todo lo de 2026-10-22 describe un producto que consume inferencia como un backend opaco; el material del 2026-10-23 permite ver el **mercado de esa capa** por dentro —el software que la implementa (new-api), el mercado que la revende (los 中转站 de PriceAI) y el patrón que se repite cuando no hay API oficial (midjourney-proxy).

### Lo que hay hoy: un puntero, no una capa

El estado actual es el de un **proveedor único detrás de una variable de entorno**: el `README.md` del repo declara *LLM: DeepSeek (configurable via `OPENAI_API_BASE`)*, y `AGENTS.md` lo repite como dependencia crítica (`OPENAI_API_BASE` — proveedor LLM, DeepSeek por defecto). No hay router, no hay grupos, no hay precios por uso, no hay failover. Encima de ese puntero, Dify actúa como capa de prompts y recuperación ([[2026-1022-gap-dify-como-capa-inferencia-prompts]]), y el consumo se factura al tenant por categorías sobre un desglose **por proveedor** (Anthropic + OpenAI) ([[2026-1022-costes-por-categoria-tenant]]). Los embeddings, en cambio, están partidos: Voyage en el competidor ([[2026-1022-myclone-viaje-embeddings-voyage]]) y `text-embedding-3` inferido aquí ([[2026-1022-pgvector-embeddings-openai-inferidos]]).

Es decir: **la inferencia es una dependencia, no una arquitectura**. Y el propio thread ya sabe que dos de las tres piezas que un producto serio necesita de esa capa —API de consumo y precios públicos— **no existen todavía** (fricciones 3 y 4).

### Qué es un gateway: la anatomía de new-api

El caso canónico de esa capa ausente es **New API** (`QuantumNous/new-api`), un gateway de IA autoalojado, fork AGPLv3 de One API (MIT), que se describe como un *"unified AI model hub for aggregation & distribution"* y **convierte varios LLM a formato OpenAI-, Claude- o Gemini-compatible** ([[2026-1023-new-api-gateway-unificado-de-modelos]]). Los upstreams declarados son OpenAI, Anthropic, Gemini, Azure OpenAI, AWS Bedrock, Vertex AI, DeepSeek y Qwen.

Lo que el README documenta, pieza por pieza:

- **Una sola API, varios protocolos** — `/v1/chat/completions`, `/v1/responses`, `/v1/messages`, `/v1beta/models/{model}:generateContent`, más imágenes, audio, `/v1/embeddings`, `/v1/rerank` y plugins de tareas ([[2026-1023-new-api-una-sola-api-multiproto]]). El embedding y el rerank bajo la misma clave es exactamente la pieza que hoy está partida entre Voyage y `text-embedding-3`.
- **Canales, grupos y routing** — un canal es una clave upstream con modelos y **asignación de grupo**; el routing se decide por grupo, prioridad, peso, afinidad y *channel-pin*; la key del cliente debe compartir grupo y modelos con el canal ([[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]). El **grupo** es la palanca comercial: es la unidad a la que se asigna el precio ([[2026-1023-new-api-grupos-como-eje-de-precio-del-relay]]).
- **Dos motores de precio** — precios por *ratio* (倍率) por modelo y por nivel de uso, y un sistema de **expresiones** con precios propios de caché (`cc`, `cc1h`, `cc12h`), pico/valle y precios por número de peticiones ([[2026-1023-new-api-precios-por-ratio-y-expresion]]).
- **Contabilidad de tokens** — `tokenkit` existe porque las estimaciones nativas subcontaban el tráfico de agentes (definiciones de tools, function calls y sus salidas) **31–93 %** frente a 54 ventanas reales de Claude Code y Codex; el arreglo deja ≤1 % de sesgo ([[2026-1023-new-api-tokenkit-conteo-de-tokens-calibrado]]). Es decir: **la normalización por tokens es en sí misma un producto**, con su propio modelo de error.
- **Conversión con pérdida declarada** — `relaykit` es el módulo que convierte entre los cuatro protocolos de texto y el README avisa de que *"protocol-specific tools and fields may not map exactly"* ([[2026-1023-new-api-relaykit-conversion-perdida-de-campos]]). "Compatible con OpenAI" no es "idéntico a OpenAI", y el propio proyecto lo dice.
- **Extensibilidad** — las tareas asíncronas (imagen, vídeo) son **plugins JavaScript en sandbox**; cada plugin valida su request y declara sus propios hechos de uso, y el gateway solo los acota ([[2026-1023-new-api-plugins-de-tareas-js-en-sandbox]]). El soporte de un proveedor no está en el core: cambiar de proveedor en una capacidad no toca el núcleo.
- **Despliegue** — local con un contenedor y SQLite; en producción, `docker-compose.yml` levanta **New API + PostgreSQL + Redis**, con ClickHouse opcional para el log de consumo ([[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]). Sobre eso, una advertencia operativa de manual: sin Redis compartido, *"rate limiters count limits independently per node"* ([[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]).
- **Licencia** — AGPLv3 con Sección 7: **enlace visible al proyecto original y aviso de atribución en la interfaz**, visible para el cliente final ([[2026-1023-new-api-licencia-agplv3-y-atribucion-en-ui]]). Choca de frente con una marca propia sin filiación y con la ausencia de código público en el vault.
- **Aviso legal** — el README condiciona explícitamente el uso a claves upstream legítimas, cumplimiento de ToS, y para operación pública: registro, licencias, seguridad de contenido, **verificación de identidad real, retención de logs, impuestos** y autorización upstream ([[2026-1023-new-api-aviso-legal-para-reventa-publica]]).
- **Escala** — 50,5k stars, 6.608 commits, actividad el mismo día de la captura, 7 idiomas en consola; la advertencia operativa es que `latest` se mueve y hay que fijar versión ([[2026-1023-new-api-escala-adopcion-y-traduccion]]).
- **Stack** — monolito **Go + Gin** con el front **React 19 / Rsbuild / Tailwind 4** embebido (`web/dist`), Bun como runner, y un wrapper Electron; el backend es el producto, no una capa aparte ([[2026-1023-new-api-stack-go-gin-react19-y-electron]]).

El dato estructural que cierra el círculo: **Midjourney-Proxy es un upstream declarado de new-api** ("Midjourney interface support"), y a la vez el README de Midjourney-Proxy lista `new-api` entre las aplicaciones que lo consumen ([[2026-1023-midjourney-proxy-ecosistema-de-aplicaciones-que-lo-consumen]]). Dos proyectos que se citan mutuamente y se montan uno sobre otro.

### El mercado: qué se compra cuando no hay contrato

PriceAI es un agregador, no un vendedor: su home se define como *"AI 低价卡网订阅与中转 API 比价雷达"* y su FAQ dice *"PriceAI 不卖货、不收款、不参与交易"* ([[2026-1023-priceai-home-como-radar-y-no-como-vendedor]]). Estructura en cuatro módulos con ejes distintos:

| Módulo | Qué compara | Átomo |
|---|---|---|
| 卡网订阅 | cuentas, membresías, correo, 卡密, CDK, Kiro — precio con stock y modo de entrega | [[2026-1023-priceai-modulo-kanet-marcas-y-modos-de-entrega]] |
| 官方订阅 | precio oficial, precio regional, elegibilidad y umbral de pago | [[2026-1023-priceai-catalogo-ocho-canales-y-fecha-de-tipo-de-cambio]] |
| 官方 API | cuota gratuita, Token Plan y límites de los proveedores chinos | [[2026-1023-priceai-sin-cuotas-gratis-tabuladas]] |
| 中转 API | multiplicador (倍率), estabilidad e información declarada | [[2026-1023-priceai-modulo-api-transit-tres-ejes-de-comparacion]] |

La tabla de reventa usa **fuente de canal** como campo estructural: **22 de las 30 filas son Sub2API y 8 son New API** ([[2026-1023-priceai-transit-canal-tipo-sub2api-vs-new-api]]). Comparar 30 relays es comparar, en su mayor parte, despliegues del mismo stack con distinto 号池 y distinto multiplicador.

El precio se expresa como **综合倍率 = 充值系数 × 模型倍率** ([[2026-1023-priceai-transit-formula-del-multiplicador-compuesto]]) y la dispersión es real: de **0.04x–0.10x** en 悠米AI中转 (New API) y 0.01x–0.20x en 皓悦 APISub2API, hasta **7.00x** en 合聚API para ChatGPT ([[2026-1023-priceai-transit-dispersion-de-multiplicadores]]). Tres límites que el multiplicador no cubre:

- **Cobertura parcial por diseño** — la cabecera declara *"排名只用有直连监测的分组"*: solo entran los grupos con monitorización directa. "No收录" en la columna Gemini (6 filas) y en Claude (3) significa "no observable", no "no existe" ([[2026-1023-priceai-transit-cobertura-parcial-y-criterio-de-ranking]]).
- **El precio no predice la estabilidad** — 悠米AI中转 es el más barato (0.04–0.10x) y tiene 85,1 % de disponibilidad; HubCore llega a 99,8 % con techo de 2,00x; 贝贝 tiene la disponibilidad mínima (73,9 %) con Claude a 0,05–1,60x ([[2026-1023-priceai-transit-precio-y-estabilidad-desacoplados]]). Y la columna de disponibilidad mezcla denominadores heterogéneos (60–1320 muestras, o volumen 24 h), así que **es observación pública, no SLA** ([[2026-1023-priceai-transit-disponibilidad-7d-con-denominadores-heterogeneos]]).
- **La verificación de modelo está pendiente** — la función 模型检测 aparece como *"即将开放"*: hoy el agregador no puede confirmar qué modelo hay detrás de un multiplicador ([[2026-1023-priceai-transit-guia-previa-y-verificacion-de-modelo-pendiente]]).

Y el factor político: los patrocinadores **son canales de reventa y están dentro del propio ranking** (Dragon API, 合聚API, 灵绘AI), con copy de 0,2× o 0,05× que no coincide con el rango tabulado ([[2026-1023-priceai-transit-patrocinadores-y-ranking-en-la-misma-pagina]], [[2026-1023-priceai-patrocinadores-y-canales-de-reventa-con-multiplicador]]). El agregador lo declara: *"不售卖 API，不替商家担保"* y solo sobrevive lo revisable — nombre original, enlace, stock y fecha ([[2026-1023-priceai-limite-de-verificacion-y-responsabilidad]]).

Debajo del mismo eje está el mercado de **cuentas**: 39 tiendas con cola larga en el catálogo de 卡网, con "招代理" y "分销" en los propios títulos ([[2026-1023-priceai-channels-39-tiendas-y-una-larga-cola-de-revendedores]]), y el mismo nombre de plan revendido a precios que difieren ×9,45 según el modo de entrega —"ChatGPT Plus 试用订阅" a ¥11,85 frente a "ChatGPT Plus 正价代充" a ¥112,04 ([[2026-1023-priceai-channels-escalera-de-reventa-chatgpt-y-codex]]). lzt.market tiene la categoría `LLM Accounts` como vertical de primera clase, con alta individual y carga masiva ([[2026-1023-lzt-categoria-llm-accounts-para-reventa]]), y un 10 % de comisión al recargar con MasterCard ([[2026-1023-lzt-topup-mastercard-comision-10]]) — su captura, eso sí, no publica ni un precio ([[2026-1023-lzt-captura-parcial-sin-precios-ni-stock]]).

El límite estructural que el vault hereda si compra inferencia así: **una suscripción de producto no es un paquete de tokens de API** —*"ChatGPT、Claude、Gemini 的官方月订阅多是产品内额度，不等同 API token 包"* ([[2026-1023-priceai-suscripcion-no-es-api-token]]). El panel de costes de este producto desglosa por proveedor (Anthropic + OpenAI), es decir, consumo medido por token: cualquier oferta de suscripción es techo de referencia, no presupuesto de inferencia. Y los planes oficiales que se comparan entre sí no son comparables entre sí: la tabla mezcla **requests, prompts, credits y dólares de uso** sin columna de conversión ([[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]]), en un mundo donde "Coding Plan" y "Token Plan" son categorías de producto con cuota por ventana, no por token ([[2026-1023-priceai-token-plan-como-categoria-producto]]).

### El arquetipo: cuando no hay API oficial, alguien construye el puente

`novicezk/midjourney-proxy` (Apache-2.0) **convierte el canal de Discord de Midjourney en una llamada por API** — *"代理 MidJourney 的discord频道，实现api形式调用AI绘图"* ([[2026-1023-midjourney-proxy-convierte-discord-en-api-rest]]). El patrón es exactamente el mismo que el de Dify en este producto: un puente HTTP entre una interfaz que no es API y el consumidor que sí necesita API.

La anatomía del acoplamiento es lo que hay que mirar: el proxy **no se autentica contra Midjourney, sino contra Discord**, con token de usuario, ID de servidor e ID de canal; el WebSocket con token de usuario es lo que da los mensajes de error y la funcionalidad completa ([[2026-1023-midjourney-proxy-arquitectura-token-discord-y-wss]]). De ahí vienen sus dos dinámicas: multi-cuenta con cola por cuenta ([[2026-1023-midjourney-proxy-funcion-multicuenta-con-cola-por-cuenta]]) y riesgo de aviso o baneo por frecuencia de dibujo ([[2026-1023-midjourney-proxy-riesgo-de-cuenta-por-frecuencia-de-dibujo]]). Y sus defaults son la mitad del aviso: `mj.task-store.type` en memoria por defecto (se pierde al reiniciar) y **`mj.api-secret` vacío = autenticación desactivada** ([[2026-1023-midjourney-proxy-config-tareas-y-autenticacion]]).

Aquí está el paralelismo estructural con el bug `myownclone_public_bp`: **un endpoint que debería existir y no existe**. El chat público devuelve 404 porque la ruta no está registrada ([[2026-1022-live-verify-superficie-rest-api-inexistente-antes]]), y en el otro lado del mercado el mismo hueco —proveedor sin API— se llena con un puente no oficial, frágil y con el default abierto. La lección de los dos lados es la misma: **la capa de acceso a inferencia es la decisión de arquitectura que más caro sale cuando se pospone**. Si el proveedor no da API, alguien va a construir el puente; la elección es si lo construyes tú, con su tríada de degradación (cuenta, sesión, rate limit) asumida, o si compras acceso a un puente ajeno.

Y en el ecosistema de estos proxies el valor no está en el proxy: hay siete aplicaciones de terceros construidas encima —integración en otros chats, plataformas de agregación, empaquetado móvil— y también una herramienta para **eludir el captcha del proveedor** ([[2026-1023-midjourney-proxy-ecosistema-de-aplicaciones-que-lo-consumen]]). Es decir: demanda real servida sin SLA y sin superficie legal ([[2026-1023-midjourney-proxy-relevancia-para-clones-con-imagen]]).

### El arquetipo tiene dos ediciones, y eso es el dato de negocio

La edición abierta de `midjourney-proxy` documenta exactamente **siete capacidades** en "主要功能" ([[2026-1023-midjourney-proxy-funciones-imagen-base64-y-describe]]): la instrucción Imagine con sus acciones, **imagen en base64 como垫图 (imagen de referencia)**, **Blend** (mezcla) y **Describe** (imagen a texto), **progreso de tarea en tiempo real**, **traducción de prompt chino→inglés configurable (Baidu Translate o GPT)**, **predetección de palabras sensibles con override manual** y la conexión `user-token` por WSS para obtener errores y funcionalidad completa.

Eso define qué significa "API" para un generador de imágenes: no prompt→PNG, sino **reproducir el vocabulario de botones del bot de Discord**. Pero dos de esas siete funciones no son de imagen sino de producto: la traducción **delega** su trabajo a Baidu o a GPT según `mj.translate-way`, y el filtrado de palabras sensibles es un override manual. Es exactamente el patrón de "capa de inferencia externa" que este producto ya usa con Dify ([[2026-1022-gap-dify-como-capa-inferencia-prompts]]): **el núcleo del proxy no es el modelo, es el orquestador de capacidades ajenas**.

La lectura de negocio está en el reparto entre ediciones. El README de la edición abierta remite a `midjourney-proxy-plus` ([[2026-1023-midjourney-proxy-edicion-plus-ampliada]]), y el reparto es quirúrgico: **todo lo que es "uso del modelo"** (Imagine, Blend, Describe, traducción, sensible) queda en la edición abierta; **todo lo que es "operación sobre el proveedor"** vive en la de pago — pool de cuentas persistente y mantenido dinámicamente, consulta y ajuste de `settings`, **verificación automática de popups**, **apelación automática de "Action needed to continue"**, resolución de caída frecuente de token, panel de administración embebido, configuración dinámica en backend, además de funciones de imagen (Pan, Zoom, Vary, Remix, seed) y generación de vídeo con soporte V7 Alpha.

Es decir: **el core público es "llamar al dibujo por API" y lo premium es "que no te baneen"**. Eso mapea casi exactamente contra el eje del producto propio: el core público es el clon; lo que se cobra aparte es la operación. Es un precedente de pricing del sector que el vault no tenía, y también una advertencia: la edición plus declara perseguir las versiones del proveedor (V7 Alpha, vídeo) mientras la edición abierta tiene **229 commits con el último cambio de código en `src/main` de junio de 2024** — el único movimiento posterior fue el README, en agosto de 2025 ([[2026-1023-midjourney-proxy-popularidad-y-actividad-del-repo]]). La curva es instructiva: **5,4k stars y 2,4k forks, pero el código congelado desde hace más de un año**; la popularidad no se convirtió en mantenimiento porque el esfuerzo se mudó a la edición de pago. Es un precedente de que el propio sector financia la continuidad con una edición separada, no con el código abierto — y el contraste con el producto propio es directo: aquí el código abierto es el activo comercial principal, allí no hay repositorios públicos ([[2026-1022-sin-repos-publicos-github]]).

Y hay una lectura operativa de coste que conecta con el thread de costes: el apartado "快速启动" ofrece **tres vías de despliegue, dos sin servidor propio** — Railway (*"基于Railway平台，不需要自己的服务器"*), con Zeabur como alternativa, y Docker en servidor o local ([[2026-1023-midjourney-proxy-despliegue-java17-y-paas-sin-servidor]]). El stack es **Java 17 + Maven + `application.yml`**, con `ProxyApplication` como entrypoint y `docker build . -t midjourney-proxy`. Es decir: **levantar este puente puede costar 0 € de servidor** si se acepta un PaaS, contra el suelo de €5,99/mes de Hetzner que no cabe en el presupuesto de ≤ €4/mes ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]). Y el stack mainstream es una señal: una integración con un proveedor sin API oficial **no exige un lenguaje exótico** — el trabajo real está en el estado, las cuentas y la resiliencia, no en la implementación. Detalle operativo que importa: la persistencia de tareas en Redis es un requisito adicional que en un PaaS puede implicar un servicio de backing aparte.

### Qué significa para el build-vs-buy

Lo que la evidencia deja es una posición, no un plan:

1. **El `OPENAI_API_BASE` es un límite de arquitectura disfrazado de variable de entorno.** Un gateway convierte "proveedor" en "canal + grupo + precio"; aquí el proveedor es una constante. Mezclar proveedores, o caer a un relay cuando el upstream falla, requiere hoy tocar configuración y redeploy. Un gateway es **la abstracción que falta** — no un lujo de escala.
2. **Lo que un gateway compra, en orden de valor para este producto:** (a) un solo endpoint y una sola credencial para proveedor y embeddings; (b) coste medido por token con contabilidad honesta, en lugar de la atribución por proveedor que hoy infiere el panel; (c) failover entre canales, imposible con un puntero único; (d) la capacidad de vender a un tenant el mismo modelo con márgenes distintos sin duplicar el stack.
3. **Lo que cuesta, con nombres:** AGPLv3 con atribución visible en la interfaz ([[2026-1023-new-api-licencia-agplv3-y-atribucion-en-ui]]), que choca con la marca propia y con la ausencia de repos públicos; **app + Postgres + Redis** sobre una infraestructura hoy stateless en nginx ([[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]); y el coste real de la conversión multi-protocolo, que el propio proyecto declara con pérdida de campos ([[2026-1023-new-api-relaykit-conversion-perdida-de-campos]]). El suelo de self-hosting del sector lo ponen los patrocinadores chinos de VPS (Aliyun 2核2G "desde 68 元/año", Tencent 2核4G "desde 199 元/año", ambos con copy que menciona montar un relay propio) — son declaraciones de sponsor, sin SLA ni verificación, no un precio confirmado ([[2026-1023-priceai-sponsors-vps-chinos-para-auto-hospedar-relay]]).
4. **Lo que no hay que hacer:** comprar inferencia en el 中转 sin asumir que es una caja negra. Sin SLA ([[2026-1023-priceai-descargo-de-responsabilidad-sin-sla]]), con verificación de modelo pendiente, con 号池 compartido y con dispersión de multiplicador de casi dos órdenes de magnitud —es decir, con un multiplicador que puede ser margen, error de conteo o ambas cosas ([[2026-1023-new-api-tokenkit-conteo-de-tokens-calibrado]]). Para un producto que factura al tenant por uso, un canal sin SLA es un coste que se paga en incertidumbre.
5. **Y la capa que no se compra:** el control de acceso. El vault hoy sirve `/api/clones`, `/api/inbox` y `/api/clones/x/prompts` con `401` pero expone `/api/auth/session` en 200, sin rate limiting ([[2026-1022-sin-rate-limiting]]), en un nginx sin cookies seguras ([[2026-1022-cookie-next-locale-sin-httponly-ni-secure]]) y con toda la IA y la autenticación en servidor ([[2026-1022-ia-y-auth-totalmente-servidor]]). El gateway resuelve el lado del consumo, no el del borde.

## El hallazgo estructural: dos productos, no uno

[[2026-1022-myownclone-dos-repos-flask-nextjs]] — MyOwnClone no es un monorepo. Son **dos bases de código con procesos de arranque separados**:

| Capa | Ubicación | Arranque | Acceso a datos |
|---|---|---|---|
| Backend Flask/SQLAlchemy | `api/` (`controllers/myownclone_public.py`, `controllers/console/myownclone/*`, `models/{clone,analytics}.py`, `core/retrieval.py`, `core/myownclone/{email_ai,silos}.py`) | `python -m api.app_factory`, puerto 5001 | SQLAlchemy |
| Frontend Next.js/Drizzle | `src/app/(dashboard)/*`, `src/lib/db/schema/*` | `npm run dev`, puerto 3000 | **Drizzle directo** |

El frontend tiene su propia ruta `src/app/api/clone/memories/route.ts` que **no pasa por Flask**. De ahí sale el segundo hallazgo: [[2026-1022-auth-flask-nextauth-desconectados]] — dos sistemas de identidad conviviendo sobre el mismo modelo de datos. Flask usa `@login_required`, `@account_initialization_required`, `@setup_required`; el frontend usa `auth()` de NextAuth. Ninguno gobierna al otro. La fricción con [[2026-1022-myownclone-jwt-token-required]] (que exige `@token_required` como patrón) sugiere que existen tres decoradores y dos o tres mecanismos coexistiendo en la misma base de datos.

## La superficie real del producto

[[2026-1022-mapa-modulos-internos-desde-bundles-js]] reconstruye el mapa completo desde 15 bundles (~1,2 MB) en dos capas:

- **Admin Platform** — `AdminPlatformResumen` (MRR, costes por proveedor y por eje, gráficos), `AdminPlatformTenants` (CRUD, invitaciones, cortesías, trials, impersonación), `AdminPlatformInbox` (bandea global `*@` con labels y estados), `AdminPlatformSpam` (blacklist de dominios), `AdminPlatformFeedback`, `AdminPlatformFaqs`, `AdminImpersonationBanner`.
- **Tenant App** — `Onboarding`, `Brain`, `Triage`, `PublicBooking`, `MyBooking`, `PublicRecording`, `FeedbackWidget`, `PublicFooter`, `CookieBanner`.

Sobre esa capa, [[2026-1022-modulo-brain-cerebro-memorias-plantillas]] precisa qué es "Brain": CRUD de memorias + firma de email + plantillas + dominios de spam + dominio inbound. Es la superficie donde el creator configura no solo qué sabe el clon sino cómo se presenta y qué mensajes acepta.

[[2026-1022-tres-silos-opt-in-publico]] confirma que los tres silos (pedagogía / soporte / recomendaciones) son estructura de configuración real, no solo marketing: la superficie de chat se parametriza con knowledge/terms/personality y `/admin/brain` asigna a cada silo su corpus (`/knowledge`, `/products`, `/support`, `/terms`).

[[2026-1022-modulo-reuniones-booking-video]] documenta el módulo de reuniones: booking público con calendario y detección automática de timezone, videollamada "on myownclone", grabación con transcripción, descarga ICS compatible con Google/Outlook/Office 365/Apple, y burbuja de chat incrustada en las páginas de grabación. Es un módulo completo, no un placeholder.

## El pipeline de chat, paso a paso

[[2026-1022-pipeline-chat-actual-myownclone]] — el camino real de `POST /api/myownclone/public/clones/{slug}/chat`:

1. `CloneConfig` por slug
2. `CloneModePrompt` por `clone_id` + modo activo
3. `_add_memories_to_prompt()` — concatena memorias al system prompt
4. `retrieve_from_silo()` — RAG sobre el dataset de Dify
5. `full_prompt = system_prompt + CONTEXT + user_message`
6. `model_instance.invoke_llm_stream()` → SSE `data: {content: chunk}` hasta `data: [DONE]`

Dos consecuencias: el prompt se almacena **sin historial** (cada `PUT` sobrescribe), y la recuperación es contra **Dify como capa de inferencia** ([[2026-1022-gap-dify-como-capa-inferencia-prompts]]) — lo que implica que todo cambio de prompt pasa por Dify y que la compilación de variables (`{name}`, `{role}`) tiene que ocurrir antes de enviar al modelo, con sintaxis `{{variable}}` como MyClone.is.

## Por qué no hay API (y por qué no es solo una decisión)

[[2026-1022-ia-y-auth-totalmente-servidor]] — ningún bundle contiene claves ni endpoints de OpenAI, Anthropic, Cohere, Supabase, Auth0, Clerk o NextAuth. Las únicas salidas a terceros son PostHog (`eu.i.posthog.com/i/v1/logs`) y Sentry (`sentry.io`). No hay tRPC, WebSocket ni SSE de negocio en el cliente.

[[2026-1022-mutaciones-rsc-sin-api-rest]] y [[2026-1022-api-privada-sin-documentacion]] llevan esa opacidad a su consecuencia: las mutaciones viajan por Server Actions (protocolo RSC) contra el mismo servidor Next.js, `api.myownclone.com` sirve el mismo HTML de la app, y no hay docs funcionales. No es que exista una API privada: es que **no hay API**. La fricción con [[2026-1022-myclone-api-rest]] (que decía que MyOwnClone expone OpenAPI) queda sin resolver — el checkout local de Dify en el vault no es la API pública del producto.

[[2026-1022-neon-postgres-serverless]] da la capa de datos: Neon (PostgreSQL serverless), con la corrección de que `api.` no es un host de API Routes sino un alias del mismo deployment. [[2026-1022-pgvector-embeddings-openai-inferidos]] infiere PGvector + `text-embedding-3` de OpenAI por extensión de Neon, y marca los LLM como Anthropic Claude + OpenAI por strings de tracking de coste — en tensión directa con la opacidad total de arriba.

## El stack, verificado

[[2026-1022-frontend-nextjs-vercel-sentry-posthog]] — Next.js **16.2.4** (Turbopack) con React 19, SSR + RSC, en Vercel Edge `cdg1::iad1` (París). Sentry (`org 4511315838173184`, env `vercel-production`, sample rate 0.1), PostHog SDK 1.373.4 en `eu.i.posthog.com`, i18n `next-intl` con español por defecto e inglés en `/en`. Tipografías Poppins (variable) y JetBrains Mono (variable).

[[2026-1022-posthog-integracion-pesada-sentry]] — la instrumentación es más pesada de lo que sugiere la lista: el chunk principal (187 KB) está dominado por el SDK de PostHog, con feature flags, session recording con detección de rageclick, surveys, product tours, conversations, web vitals, autocapture, error tracking envolviendo `onerror`/`unhandledrejection`/`console.error`, toolbar/editor, e integraciones configuradas de Intercom y Crisp Chat. La superficie legal es pequeña y no está documentada: [[2026-1022-superficie-legal-publica-dpa-clon-terms]] (seis documentos, cinco con versión `/en/legal/*`), [[2026-1022-tema-oscuro-css-variables]] (12 variables CSS, `localStorage` key `myownclone-theme`, clase `dark` + `prefers-color-scheme`, timezone Europe/Madrid).

## Multi-tenant

[[2026-1022-multi-tenant-slug-unpublished]] — cada creador tiene un slug `[slug].myownclone.com` que queda unpublished por defecto hasta que publica; dominio personalizado soportado pero no obligatorio; aislamiento entre tenants mencionado explícitamente en el aviso legal. Ese "aislamiento" es de datos, no de superficie HTTP — ver [[myownclone-security-surface]].

## Fricciones abiertas

1. **Dos repos, dos schemas** — [[2026-1022-drift-schema-drizzle-sqlalchemy]] documenta cuatro bugs de drift concretos: enum `teach`/`pedagogy` (ver también [[2026-1022-bug-enum-modos-teach-vs-pedagogy]]), `cloneModePrompts.updatedAt` ausente en Drizzle, `title` de memorias que **se pierde en el pipeline**, y `memories.updatedAt` ausente en SQLAlchemy. El drift no es teórico: hay pérdida de datos documentada.
2. **Auth** — [[2026-1022-auth-flask-nextauth-desconectados]] vs [[2026-1022-myownclone-jwt-token-required]]: ¿tres decoradores coexistiendo o dos mecanismos mal nombrados?
3. **Proveedor de IA** — [[2026-1022-pgvector-embeddings-openai-inferidos]] vs [[2026-1022-ia-y-auth-totalmente-servidor]]. Con el `OPENAI_API_BASE` como único puntero, falta la abstracción de gateway que permitiría mezclar proveedores o caer a un relay — ver «La capa de inferencia».
4. **API** — [[2026-1022-api-privada-sin-documentacion]] vs [[2026-1022-myclone-api-rest]].
5. **Backend real** — [[2026-1022-neon-postgres-serverless]] vs [[2026-1022-myownclone-dos-repos-flask-nextjs]]: el aviso legal dice "Vercel serverless functions"; el código dice Flask en 5001. Conviven ambos, o el aviso legal describe un despliegue que ya no es el de producción.

Ver también: [[myownclone-vs-myclone-is]] (comparativa de superficie) y [[myownclone-security-surface]] (endurecimiento HTTP).

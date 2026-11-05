# Extensiones a átomos existentes — captura 2026-10-26-veridrop-faq

Fuente: `sources/2026-10-26-veridrop-faq.md` (captura `0-raw/2026-10-26-veridrop-faq.md`).
Ninguno de los átomos siguientes se ha modificado: las extensiones se proponen para el Editor.

=== EXTEND 2-atoms/2026-1024-veridrop-metodo-de-la-puntuacion-mediana-publica
## Nota de extensión 2026-10-27
La FAQ aporta la **tabla de pesos completa** que esta nota decía faltar: **11 项常规检测** más **1 项** de contexto largo pagada aparte, con los pesos nominales **thinking signature (25%) > behavioral signature (15%) > structured output (12%) > consistency / knowledge / token usage (各 10%) > pdf (8%) > identity / protocol / integrity / message_id (各 5%)**, y los umbrales de veredicto **≥85 优秀(绿) / 70-84 通过(浅绿) / 50-69 marginal(黄) / <50 未达标(红)**. La misma FAQ afirma **"评分公式公开,可逐行审计"** bajo AGPL-3.0, lo que **presiona** la afirmación de esta nota de que el score se publica sin definir cómo se agrega: el caso abierto pasa a ser la **agregación a mediana de informes públicos**, no la tabla de pesos. Véase [[2026-1027-veridrop-pesos-de-los-11-detectores-y-el-contexto-largo-de-pago]] y [[2026-1027-veridrop-los-pesos-de-la-deteccion-suman-110-y-no-100]] (la suma de los once pesos nominales es 110, no 100).
=== END

=== EXTEND 2-atoms/2026-1024-veridrop-tercer-estado-edge-y-su-dispersion
## Nota de extensión 2026-10-27
La FAQ documenta la **semántica de los umbrales** que faltaba para leer el estado intermedio: **50-69 = marginal(黄)**, y sobre todo la **regla de veto** — **"任意 detector 报严重问题,verdict 会被砍到 marginal(圆圈变黄)— 即使分数够 70 也不绿"**. Es decir, el "边缘/marginal" que esta nota registraba como tercer estado agregado **tiene una regla de producción explícita**: no es una zona de puntuación intermedia, es el resultado de un detector grave. Y el color del veredicto (verde / amarillo) es una dimensión **distinta** del recuento 通过/边缘/失败 por test. Véanse [[2026-1027-veridrop-una-desviacion-grave-baja-el-veredicto-a-amarillo]] y [[2026-1027-veridrop-tres-senos-de-deteccion-protocolo-capacidad-y-uso]].
=== END

=== EXTEND 2-atoms/2026-1024-veridrop-cobertura-de-protocolos-por-relay
## Nota de extensión 2026-10-27
La FAQ añade **por qué la cobertura de Gemini es tan baja en el directorio (18 de 50)**: no es que falten relays, es que **el 99 % de los relays de Gemini de terceros solo expone protocolo OpenAI-compatible** y **Google 官方 también ofrece endpoint OpenAI-compatible** (`/v1beta/openai`), de modo que **"维护两套独立的检测逻辑成本高且容易引入翻译层导致结果失真"** y la detección de Gemini se hace **"只走 OpenAI 兼容路径(POST /chat/completions)"**. La etiqueta "Gemini" del directorio, por tanto, **no implica que el relay exponga la API nativa de Google**. Véanse [[2026-1027-veridrop-gemini-solo-se-detecta-por-la-ruta-openai-compatible]] y [[2026-1023-new-api-una-sola-api-multiproto]].
=== END

=== EXTEND 2-atoms/2026-1024-veridrop-home-12292-relays-y-cuatro-modelos-con-doble-nivel-de-evidencia
## Nota de extensión 2026-10-27
La FAQ aporta los **identificadores de modelo verbatim** que faltaban: la detección cubre **nueve** modelos OpenAI — `gpt-5.6-sol`, `gpt-6-astra`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5.5`, `gpt-5.4`, `gpt-5.3-codex`, `gpt-5.4-nano`, `gpt-5.4-mini` — y la home **GPT 5.6** es el tablero de OpenAI. La misma FAQ aclara el dato de los "4 模型组" de esta nota: son **grupos de modelo** y cada uno tiene su propio **escalón de patrocinio S1–S10**, es decir, **la CNC publicitaria de VeriDrop es multidimensional, con un eje por grupo de modelos**. Véanse [[2026-1027-veridrop-gpt-6-astra-exige-chat-completions-y-responses-api]] y [[2026-1027-veridrop-tres-flujos-de-ingreso-y-el-aislamiento-de-la-comision]].
=== END

=== EXTEND 2-atoms/2026-1024-veridrop-leaderboard-home-paga-la-posicion-pero-no-el-verdict
## Nota de extensión 2026-10-27
La FAQ añade el **inventario completo de los tres flujos de ingreso** del sitio: **① 联盟合作** (comisión del relay por registro, **"不影响用户实际支付价格"**), **② 基础收录与站长后台套餐**, **③ 模型级 S 赞助位(4 个模型组均为 S1–S10) y Top1–Top10 精选位(均明确标识为付费展示)**, con la detección **"本身永久免费、无需注册"**. Y añade la garantía más fuerte que esta nota tenía: **"联盟收入与评分严格隔离"**, **"即使是付费 Featured 客户,被检出严重问题 仍标严重问题"** y **"代码完全开源(AGPL-3.0),评分公式公开,可逐行审计"**. Es decir, la separación commerce/métrica que el vault registró en PriceAI como excepción (patrocinadores fusionados en la tabla) aparece aquí como **norma declarada y auditable**. Véanse [[2026-1027-veridrop-tres-flujos-de-ingreso-y-el-aislamiento-de-la-comision]] y [[2026-1023-priceai-patrocinadores-y-canales-de-reventa-con-multiplicador]].
=== END

=== EXTEND 2-atoms/2026-1024-veridrop-ventana-de-actividad-y-frescura-de-deteccion
## Nota de extensión 2026-10-27
La FAQ añade una **causa de "cero" que no es caída**: un resultado de **"0 个 GPT 模型可用"** es casi siempre **falta de permiso GPT en la key** — **"很多综合中转站把模型按厂家分组卖,有的客户买的是 Claude 卡、有的是 Gemini 卡,没买就调不出对应模型"** — y VeriDrop lo resuelve con un **preflight** que lista los modelos que la key sí puede usar, con redirección automática a la página del otro protocolo. Con ello, la disponibilidad del modelo deja de ser un atributo del par (sitio, modelo) y pasa a tener **una tercera dimensión: el tipo de tarjeta/grupo del cliente**. Véanse [[2026-1027-veridrop-cero-modelos-gpt-suele-ser-permiso-de-key-y-no-relay-caido]] y [[2026-1027-veridrop-preflight-y-el-0-que-no-significa-relay-malo]].
=== END

=== EXTEND 2-atoms/2026-1024-veridrop-relays-con-dominios-efimeros-y-riesgo-de-contraparte
## Nota de extensión 2026-10-27
La FAQ añade el **lado del comprador** del riesgo de contraparte, con tres riesgos prácticos declarados: **① 跑路风险** — el relay puede dejar de servir, subir precios o **desaparecer con el saldo** (**"大额充值要慎重"**); **② 模型响应跟官方不一致** — cambio de modelo, retirada de capacidades o **falsificación del recuento de tokens**; **③ prompt 内容被记录** — **"涉及商业机密 / 用户数据的对话最好避开来路不明的中转站"**. Y un quinto punto de la lista de trampas: **"规则说变就变"**, con la misma key pasando de funcionar a **"升级套餐"**, **"分组失效"** o **直接封号** sin previo aviso. Es la confirmación textual de que **el contrato implícito con un relay no es un contrato**, sino una configuración que el otro puede editar. Véanse [[2026-1027-veridrop-riesgo-legal-gris-y-tres-peligros-practicos-del-relay]] y [[2026-1027-veridrop-cinco-indicadores-duros-para-elegir-relay]].
=== END

=== EXTEND 2-atoms/2026-1023-priceai-transit-formula-del-multiplicador-compuesto
## Nota de extensión 2026-10-27
La FAQ de VeriDrop impone una **precondición que PriceAI no exige** sobre la fórmula `综合倍率 = 充值系数 × 模型倍率`: **"倍率只有在 token 数真实时才有意义。同样标 0.5 倍,如果输入 token 被多算了三成,实际花的并不少"**, y enumera las tres comprobaciones previas — **① si los tokens son creíbles**, **② si lo entregado es el modelo anunciado**, **③ cómo se factura la caché**. La cifra de contexto que la FAQ sí da es la del rango de descuento del sector: los relays existen porque **"部分中转站把多家厂商的批发额度打包零售,价格比官方低 30-70%"**. Véanse [[2026-1027-veridrop-el-multiplicador-solo-significa-algo-con-tokens-fieles]] y [[2026-1027-veridrop-tres-formas-de-dilucion-o-concubamiento]].
=== END

=== EXTEND 2-atoms/2026-1023-priceai-transit-guia-previa-y-verificacion-de-modelo-pendiente
## Nota de extensión 2026-10-27
La función **"模型检测"** que PriceAI marcaba como **"即将开放"** **tiene ya un sustituto operativo y ajeno**: el **desplegable de modelos** de VeriDrop **"自动列出该 key 在该中转站可用的模型"**, es decir, la comprobación de qué modelos puede invocar una key concreta ya es gratis y automática, y la FAQ prescribe un **protocolo de prueba de pureza en tres pasos** — **① 验模型** (firma de servidor en Claude; campos foráneos `claude_*` en `usage` en GPT), **② 验 token** (crecimiento del contador y coherencia stream/no-stream), **③ 验 capacidad** (tres datos enterrados en texto largo + tool calling + salida estructurada). Véanse [[2026-1027-veridrop-la-prueba-de-pureza-en-tres-pasos]] y [[2026-1027-veridrop-el-usage-de-la-respuesta-delata-el-trasvase-de-protocolo]].
=== END

=== EXTEND 2-atoms/2026-1023-priceai-faq-antifraude-y-prueba-pequena
## Nota de extensión 2026-10-27
La FAQ de VeriDrop explica **por qué una prueba pequeña no basta para detectar calidad**: **"掺水的站照样能正常回复,所以发一句话测试看不出来,要用针对性的检测"**, y define las tres formas de dilución — **换模型**, **多算 token**, **砍能力** (truncado de contexto o eliminación de thinking/tool calling/multimodal). Es el mismo motivo por el que el protocolo antifraude de PriceAI (comprobar contacto, postventa, grupo activo, historial) es un control de **que el canal exista**, no de **que entregue lo que dice**. La aporta complementaria es que la verificación de calidad tiene **instrumentos públicos y gratuitos** (detección gratuit con clave propia, informe público reproducible). Véanse [[2026-1027-veridrop-tres-formas-de-dilucion-o-concubamiento]] y [[2026-1027-veridrop-cinco-indicadores-duros-para-elegir-relay]].
=== END

=== EXTEND 2-atoms/2026-1023-new-api-una-sola-api-multiproto
## Nota de extensión 2026-10-27
La FAQ de VeriDrop documenta el **coste de auditar una capa de traducción**, y es un argumento directo contra la estrategia de normalizar a un único formato: **"维护两套独立的检测逻辑成本高且容易引入翻译层导致结果失真"**, y **"Veridrop 集中在 OpenAI 兼容路径上做透"** precisamente porque el 99 % de los relays de Gemini de terceros solo exponen esa ruta. La lección para el gateway del vault es que **normalizar destruye la evidencia**: una capa que convierte Claude y Gemini a OpenAI-compatible **elimina por diseño los campos `claude_*` y la nomenclatura Anthropic del `usage` que son la única huella de conversión detectable** ([[2026-1027-veridrop-el-usage-de-la-respuesta-delata-el-trasvase-de-protocolo]]). Véase también [[2026-1023-new-api-relaykit-conversion-perdida-de-campos]].
=== END

=== EXTEND 2-atoms/2026-1023-new-api-relaykit-conversion-perdida-de-campos
## Nota de extensión 2026-10-27
La FAQ de VeriDrop da el **nombre exacto de los campos que delatan la conversión**, que es la cara operativa de esta nota: un OpenAI nativo solo devuelve **prompt_tokens / completion_tokens / total_tokens**, mientras que la presencia de **`claude_cache_creation_5m_tokens`**, **`usage_source: anthropic`** o **`input_tokens` / `output_tokens`** (nomenclatura Anthropic) delata que el relay **tradujo la petición a un backend Claude y reenvió la respuesta como OpenAI**. VeriDrop marca eso como **严重问题** y **rechaza el detector entero**. Es decir: **la pérdida de campos de la conversión no es silenciosa, deja un residuo legible**, y un detector lo busca explícitamente. Véanse [[2026-1027-veridrop-el-usage-de-la-respuesta-delata-el-trasvase-de-protocolo]] y [[2026-1027-veridrop-openai-deteccion-nivel-comportamiento-protocolo-sin-prueba-criptografica]].
=== END

=== EXTEND 2-atoms/2026-1023-new-api-licencia-agplv3-y-atribucion-en-ui
## Nota de extensión 2026-10-27
Aparece un **segundo proyecto AGPL-3.0 del corpus** con el mismo perfil: **VeriDrop** declara **"代码完全开源(AGPL-3.0),评分公式公开,可逐行审计"** y es autoalojable (**`pip install -e .[web\]` → `uvicorn web.server:app`**, más un CLI `relay-detector detect --base-url ... --api-key ... --mode full`). La comparación con el competidor del sector es explícita en la FAQ: **"cctest.ai 也声称不上传 key,但代码闭源无法验证"**. Es un patrón que el vault puede reusar: **la apertura del código es la única prueba verificable de la promesa de custodia de credenciales** ([[2026-1027-veridrop-autoalojable-con-cli-y-codigo-abierto-para-auditar]] y [[2026-1027-veridrop-informe-publico-anonimo-y-la-key-cifrada-en-la-cola]]).
=== END

=== EXTEND 2-atoms/2026-1023-new-api-grupos-como-eje-de-precio-del-relay
## Nota de extensión 2026-10-27
La FAQ de VeriDrop describe la **misma segmentación por grupos** aplicada al acceso a modelos, no solo al precio: **"很多综合中转站把模型按厂家分组卖,有的客户买的是 Claude 卡、有的是 Gemini 卡,没买就调不出对应模型"**. Es decir, el **grupo del canal no solo fija el multiplicador sino qué modelos puede invocar la key del cliente** — y por tanto **el catálogo y el precio de un relay son propiedades del par (relay, grupo del cliente)**, no del relay. Es la razón operativa de por qué un mismo relay presenta un catálogo distinto a cada cliente. Véanse [[2026-1027-veridrop-cero-modelos-gpt-suele-ser-permiso-de-key-y-no-relay-caido]] y [[2026-1026-new-api-consulta-de-saldo-upstream-y-prioridad-arrastrable]].
=== END

=== EXTEND 2-atoms/2026-1023-hetzner-presupuesto-4-euros-no-alcanza
## Nota de extensión 2026-10-27
La FAQ de VeriDrop ofrece un **activo autoalojable y sin coste de licencia** para el presupuesto de infraestructura del vault: el detector es **AGPL-3.0**, se instala con `pip install -e .[web\]` + `uvicorn web.server:app` y tiene un **CLI autónomo** (`relay-detector detect --base-url ... --api-key ... --mode full`), de modo que **la medición de calidad de proveedores puede alojarse en el VPS de ≤ €4/mes** en lugar de depender de un tercero. El coste que sí escala es **el de la prueba**: **~12 llamadas API y 3000-5000 tokens** en modo standard (**Haiku ~$0.012, Sonnet ~$0.05, Opus ~$0.20**), y **~$3.32** (sonda de profundidad) a **~$27.06** (sonda máxima de 875.9k tokens) en GPT-6 Astra. Es decir, **la partida de verificación tiene coste variable de token del usuario, no de infraestructura**. Véanse [[2026-1027-veridrop-el-coste-de-la-sonda-larga-paga-el-usuario]] y [[2026-1027-veridrop-autoalojable-con-cli-y-codigo-abierto-para-auditar]].
=== END

=== EXTEND 2-atoms/2026-1026-new-api-cache-12h-openai-2-5x-y-precios-gpt-6-astra
## Nota de extensión 2026-10-27
La página de detección de VeriDrop da **la capacidad declarada de gpt-6-astra** y su coste de medición: **máximo de entrada 922k**, con sondas **32k → 461k → 875.9k** en modo extremo (**"官方标准输入价估算约 $27.06,不含输出和中转站加价"**) y **32k → 100k → 200k** en modo profundidad (**"约 $3.32"**). La cifra de $25/M de este átomo, aplicada a 875.9k, daría **~$21.90**: hay **~24 % de diferencia** con la estimación publicada, y la captura no publica la fórmula de la estimación. Véanse [[2026-1027-veridrop-la-sonda-de-contexto-largo-y-la-maxima-por-modelo]] y [[2026-1027-veridrop-el-coste-de-la-sonda-larga-paga-el-usuario]].
=== END

---
id: 2026-1023-new-api-grupos-como-eje-de-precio-del-relay
type: atom
certainty: tentative
sources: [sources/2026-10-22-new-api-github.md]
links: ["[[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]", "[[2026-1023-new-api-precios-por-ratio-y-expresion]]", "[[2026-1023-priceai-transit-canal-tipo-sub2api-vs-new-api]]"]
---

## Claim
**Inferencia** (no afirmada literalmente por el README): el **grupo** de New API es el eje sobre el que un operador de relay aplica su **decisión comercial de precio**. Lo que la fuente sí sostiene, literalmente, es que (a) el canal se crea con una **asignación de grupo**, (b) la **API key del cliente debe compartir grupo y modelos** con el canal, (c) el routing se decide por *group, priority, weight, affinity, channel-pin*, (d) el precio se define por modelo y por nivel de uso, y (e) el propio commit de i18n confirma que **existen "descripciones de grupo built-in"** traducibles (*"The built-in group descriptions are translated; descriptions an administrator saved are shown as written"*), es decir, hay grupos predefinidos de fábrica con nombre y descripción, como los que el ranking de PriceAI llama **分组**.

## Why It Matters
Si el grupo es la unidad de precio, entonces la fórmula de PriceAI — *综合倍率 = 充值系数 × 模型倍率* ([[2026-1023-priceai-transit-formula-del-multiplicador-compuesto]]) tiene un correlato técnico: **el multiplicador es la configuración del grupo**, y por eso puede variar por canal aunque el modelo y el upstream sean los mismos. Eso explica por qué 8 filas de distintos operadores pueden llevar la etiqueta New API con multiplicadores tan distintos (0.04x a 7.00x, [[2026-1023-priceai-transit-dispersion-de-multiplicadores]]).
La lectura para el vault es de **coste de cambio de proveedor**: cambiar de proveedor upstream no es un cambio de una variable, es reasignar canales, pesos y grupos y reconfigurar la key de cada cliente. Un gateway con esta estructura no es intercambiable de la noche a la mañana aunque la API sea "compatible" ([[2026-1023-new-api-relaykit-conversion-perdida-de-campos]]).
Marcado `tentative`: la atribución del precio al grupo es una inferencia a partir de la existencia de grupos con descripción built-in y de la regla grupo↔canal↔key; el README no publica un campo "precio por grupo".

## [FRICTION]
> [[2026-1023-priceai-transit-cobertura-parcial-y-criterio-de-ranking]] usa "分组" con un significado **de PriceAI**: *"排名只用有直连监测的分组"* — solo entran los grupos **con monitorización directa**, es decir, un **agrupamiento de monitorización del propio agregador**, con su función de filtrado junto al modelo, el canal y el 号池.
> Este átomo presiona esa creencia en un punto de vocabulario: **"分组" significa en New API otra cosa** — un grupo de asignación que liga canales, keys, permisos y precios dentro del gateway. Son homónimos con semántica distinta, y el riesgo real es que el vault lea "grupo" en la tabla de PriceAI y lo confunda con el grupo de un despliegue New API, concluyendo que el ranking agrupa por el mecanismo de routing del software.
> Ambas no pueden ser completamente correctas en su lectura general: o "分组" es un término único con dos implementaciones distintas, o PriceAI usa un término con un agrupamiento distinto y no el grupo del gateway. Marcado para juicio humano, no auto-resuelto: la fuente de PriceAI no define "分组" más allá de la regla de selección, y el README de New API no menciona ningún ranking externo.


## Nota de extensión 2026-10-27
La FAQ de VeriDrop describe la **misma segmentación por grupos** aplicada al acceso a modelos, no solo al precio: **"很多综合中转站把模型按厂家分组卖,有的客户买的是 Claude 卡、有的是 Gemini 卡,没买就调不出对应模型"**. Es decir, el **grupo del canal no solo fija el multiplicador sino qué modelos puede invocar la key del cliente** — y por tanto **el catálogo y el precio de un relay son propiedades del par (relay, grupo del cliente)**, no del relay. Es la razón operativa de por qué un mismo relay presenta un catálogo distinto a cada cliente. Véanse [[2026-1027-veridrop-cero-modelos-gpt-suele-ser-permiso-de-key-y-no-relay-caido]] y [[2026-1026-new-api-consulta-de-saldo-upstream-y-prioridad-arrastrable]].

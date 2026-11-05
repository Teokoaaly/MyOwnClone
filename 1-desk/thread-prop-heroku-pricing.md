# Propuesta de hilo — captura `2026-10-25-heroku-pricing.md`

Fuente: `sources/2026-10-25-heroku-pricing.md` (`https://www.heroku.com/pricing`, capturada 2026-10-25, 89.764 caracteres).
Átomos nuevos de esta captura: 22 (todos en `2-atoms/`, prefijo `2026-1026-heroku-`).
Extensiones a átomos existentes: 4. Fricciones planteadas: 4.

---

## Propuesta A — `escala-de-hosting-barato-y-el-limite-de-4-euros`

```markdown
### El PaaS con precios verificables: qué cuesta una pila gestionada cuando nada se publica por debajo

La captura de `sources/2026-10-25-heroku-pricing.md` (`https://www.heroku.com/pricing`, 2026-10-25) es **el único catálogo de plataforma gestionada del vault con precios de lista por producto y por unidad**. No es un precio de VPS: es una tabla con cuatro capas —cómputo, datos, inferencia y servicios— que este thread no tenía medidas. Y su valor aquí no es comparativo, porque **ningún plan de Heroku entra en el tramo de ≤ €4/mes**: el suelo es **Cedar Eco a $5/mes**. Su valor es que **fija el precio de lo que "gestionado" significa cuando se paga la gestión**.

**El suelo de cómputo: $5 con una condición que cambia la arquitectura.** Cedar Eco cuesta **$5/mes** con **0,5 GB de RAM**, escalado **1x–4x**, **sin Private Space**, **2 process types** y dos condiciones que no aparecen en la tabla de precios de ningún VPS: *"Personal accounts only"* y *"Sleeps after 30 minutes of inactivity"* ([[2026-1026-heroku-suelo-5-dolares-eco-con-sleep-y-7-dolares-basic-always-on]]). Cedar Basic cuesta **$7/mes** con los mismos 0,5 GB, **Free SSL**, **10 process types**, **"Always on"** y **0,28 Dyno Units / Month** ([[2026-1026-heroku-suelo-5-dolares-eco-con-sleep-y-7-dolares-basic-always-on]]). El salto de $2 entre ambos es exactamente la compra de **no dormir**: es el precio más barato documentado en el vault por un dyno *siempre encendido*.

| Plan | $/mes | RAM | Escalado | Private Space | Condición publicada |
|---|---|---|---|---|---|
| Cedar Eco | $5 | 0,5 GB | 1x–4x | No | Solo cuentas personales; duerme tras 30 min de inactividad |
| Cedar Basic | $7 | 0,5 GB | 1x–4x | No | Always on; Free SSL; 10 process types; 0,28 Dyno Units/mes |
| Standard-1X | $25 | 0,5 GB | 1x–4x | No | 1 Dyno Unit/mes |
| Standard-2X | $50 | 1 GB | 2x–8x | No | 2 Dyno Units/mes |
| Performance-M | $250 | 2,5 GB | 12x | No | 8 Dyno Units/mes; Autoscaling |
| Performance-2XL | $1,500 | 126 GB | 100x | No | 60 Dyno Units/mes; Autoscaling |

**La unidad que este thread no tenía: el Dyno Unit.** Toda la familia Basic, Standard, Private y Shield se priced a **$25 por Dyno Unit y mes** —"1 Dyno Units / Month" en Standard-1X, "5" en Private-S, "6" en Shield-S —lo que convierte al Dyno Unit en **una moneda interna de cómputo** ([[2026-1026-heroku-dyno-units-25-dolares-por-unidad-excepto-performance]]). Pero **la familia Performance rompe la regla**: Performance-M cuesta $250 con 8 Dyno Units, Performance-L $500 con 16, Performance-XL $750 con 30 y Performance-2XL $1,500 con 60. Es decir, **los dynos dedicados no se cobran como múltiplo del Dyno Unit sino por una relación propia** que solo se lee comparando filas ([[2026-1026-heroku-performance-de-250-a-1500-dolares-con-autoscaling]]). Para un thread que ordena planes por precio, esto es una advertencia metodológica: **la "unidad" de un catálogo puede ser una convención interna, no un denominador común**.

**El segundo eje, que ningún VPS tiene: el coste de la capa de datos.** Aquí es donde la comparación con el stack vivo ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) se vuelve aritmética y no retórica:

| Servicio | Plan | $/mes | Condición publicada |
|---|---|---|---|
| Heroku Postgres | Essential-0 | $5 | RAM compartida; máx. 4 h de parada/mes; 4.000 tablas |
| Heroku Postgres | Standard-0 | $50 | Servidor dedicado; máx. 1 h de parada/mes; rollback 4 días |
| Heroku Postgres | Premium-0 | $200 | High Availability; máx. 15 min de parada/mes; rollback 7 días |
| Heroku Postgres | Advanced 4G | $150 / $180 Private / $210 Shield | 2 vCPU; cómputo y storage desacoplados |
| Key-Value Store | Mini | $3 | 25 MB; multi-tenant |
| Key-Value Store | Premium 7 | $750 | 7 GB; single-tenant; 10.000 conexiones |
| Apache Kafka | Basic 0 | $100 | 3,73 GB; retención 1 semana; cluster compartido |
| Apache Kafka | Extended | desde $4,000 | 400 GB; 8 brokers; 6 semanas |

([[2026-1026-heroku-postgres-essential-5-a-20-dolares-con-4-horas-de-parada]], [[2026-1026-heroku-postgres-standard-50-a-12000-con-dedicado-y-1-hora-de-parada]], [[2026-1026-heroku-postgres-premium-200-con-ha-y-15-minutos-de-parada]], [[2026-1026-heroku-postgres-advanced-150-a-40000-con-precios-privados-y-shield]], [[2026-1026-heroku-key-value-store-mini-3-dolares-hasta-12500]], [[2026-1026-heroku-kafka-desde-100-dolares-con-1-semana-de-retencion]])

**La suma que desmonta el "PaaS a coste cero".** La composición exacta del stack vivo del producto —nginx + Postgres + Redis autoalojado— en la opción más barata de cada capa gestionada de Heroku es **Cedar Eco $5 + Postgres Essential-0 $5 + Key-Value Mini $3 = $13/mes**, con dos salvedades que la tabla de precios no esconde pero tampoco destaca: **Eco duerme a los 30 minutos de inactividad** y **el Postgres Essential es un plan compartido con 4.000 tablas de límite**. Es la primera vez que el vault puede poner un número de "coste de la gestión" al lado de su **suelo de ≤ €4/mes**: **gestionar cuesta unos 3× el techo**, y ese 3× compra **sleep gestionado, backups, failover y certificates** en lugar de potencia ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]).

**La confirmación de que ese coste tiene un suelo, no un degradado.** El Atlas del thread ya establecía en su §2 que "el suelo de hosting del vault es un roundup editorial, no un precio de contrato", y la §3 trataban la caída de precio como una serie continua. El catálogo de Heroku muestra el otro comportamiento posible: **el precio de la gestión sube por saltos de configuración, no por décimas**. Postgres Standard-0 a $50 compra un servidor dedicado, y **Premium-0 a $200 compra exactamente las mismas specs que Standard-0 —4 GB de RAM, 64 GB de disco, 120 conexiones— y solo añade High Availability y un techo de parada de 15 minutos en lugar de 1 hora** ([[2026-1026-heroku-postgres-premium-200-con-ha-y-15-minutos-de-parada]]). Es **×4 de precio por una garantía de disponibilidad**, no por capacidad. El ratio se mantiene en toda la escalera: Standard-10 a $12,000 frente a Premium-10 a $24,000 ([[2026-1026-heroku-postgres-standard-50-a-12000-con-dedicado-y-1-hora-de-parada]]). Para un producto que factura por tenant, **ese es el salto que decide si la base de datos es un coste o una factura variable**.

**El eje que este thread sí tiene y Heroku publica: el cumplimiento como tramo de precio.** La familia Private arranca en **Private-S a $125** y Shield en **Shield-S a $150** — **+20 % sobre las mismas specs** ([[2026-1026-heroku-private-y-shield-desde-125-y-150-dolares]], [[2026-1026-heroku-shield-un-20-por-ciento-mas-que-private-con-las-mismas-specs]]). Shield añade **"Ability to sign BAAs for HIPAA compliance"**, **"PCI compliance"**, keystroke logging, space level log drains y **strict TLS enforcement**. Esto **presiona la fricción 37** de este thread: la §6 afirmaba que el eje de cumplimiento auditable tenía **un único representante, Hetzner**. Heroku **no publica ISO 27001 ni GDPR**, pero publica **PCI y BAA HIPAA como producto de precio** — con la diferencia estructural de que **todos los planes Private y Shield exigen un Private Space cuyo precio no aparece en esta tabla** ([[2026-1026-heroku-fir-dynos-kubernetes-todos-requieren-private-space-desde-25]]). Es decir: **el cumplimiento se compra por suscripción y con un complemento no cuantificado**, que es exactamente el patrón que la §6 criticaba en el extremo "onion" del mercado, aparecerá ahora en el extremo enterprise.

**Y la fricción estructural que este thread debe registrar.** La fila "General Purpose 2CPU-4GB" de los dynos Fir cuesta **$80** y se anuncia como 2 CPU, pero **la propia fila declara 1 vCPU y el plan `dyno-1c-4gb`** ([[2026-1026-heroku-fir-general-purpose-2cpu-4gb-dice-1-vcpu]]). Es la contradicción más limpia que ha salido del corpus para el patrón "el nombre del plan y su ficha técnica no son la misma cifra" que la §8.12.4 ya había aislado en AlexHost. Marcado para juicio humano: **o la etiqueta "2CPU" describe la instancia y el `dyno-1c-4gb` el recurso reservado**, o el catálogo tiene un error. Y a escala, **todos los planes Fir de la tabla, desde Classic 1CPU-0,5GB a $25, requieren Private Space** ([[2026-1026-heroku-fir-dynos-kubernetes-todos-requieren-private-space-desde-25]]).

**La lectura que cierra la sección.** Heroku **no entra en la §1** —su suelo es $5, por encima del techo de ≤ €4/mes— y **no aporta una fila de precio al tramo que este thread ha medido**. Aporta tres cosas que el corpus no tenía: **un suelo de gestión cuantificado ($13/mes para la pila mínima)**, **una moneda de cómputo propia (el Dyno Unit, que el Performance no respeta)**, y **el cumplimiento como tramo de precio con sobrecoste uniforme del 20 %**. La pregunta que el hilo puede llevarse es la de la §2 reformulada: **si gestionar cuesta 3× el techo, ¿qué parte del coste del producto es en realidad el precio de no operar?** — con el dato nuevo de que **ese 3× no se puede comprar a medias**: el único tramo donde la garantía de disponibilidad sube sin specs es ×4.
```

THREAD: escala-de-hosting-barato-y-el-limite-de-4-euros

---

## Propuesta B — `myownclone-platform-architecture`

```markdown
### La capa de inferencia, cotizada: un catálogo de precios por token frente a los multiplicadores sin base de referencia

La §"La capa de inferencia: entre API propia, gateway y relay" del thread llegó a una conclusión Negative y una Positiva. La negativa: **la inferencia hoy es una dependencia, no una arquitectura** —un `OPENAI_API_BASE` a DeepSeek, sin router, sin precios por uso y sin failover ([[2026-1022-gap-dify-como-capa-inferencia-prompts]]). La positiva: **el mercado de esa capa tiene su propia arquitectura medible**, el gateway New API, con grupos como eje de precio y multiplicadores de 0,04x a 7,00x ([[2026-1023-new-api-grupos-como-eje-de-precio-del-relay]], [[2026-1023-priceai-transit-dispersion-de-multiplicadores]]).

La captura de `sources/2026-10-25-heroku-pricing.md` añade el dato que faltaba: **una tabla de precios de inferencia por modelo, en una unidad estable —el millón de tokens— publicada por un proveedor con SLA comercial**, que sirve de **base de referencia** para el debate del multiplicador. Y no la añade como un argumento: la añade como **el lugar donde se puede ver que el multiplicador, tal como el vault lo tiene registrado, no es interpretable**.

**Lo que la tabla publica.** Heroku Managed Inference lista, por **1M de tokens de entrada y de salida**, con columna de **"Region Provisioned"**:

| Modelo | Entrada $/1M | Salida $/1M | Región |
|---|---|---|---|
| claude-3-haiku | $0.25 | $1.25 | EU |
| claude-4-5-haiku | $1.10 | $5.50 | US \| EU |
| claude-4-sonnet | $3.00 | $15.00 | US \| EU |
| claude-sonnet-4-6 | $3.30 | $16.50 | US \| EU |
| claude-opus-4-5 | $5.00 | $25.00 | US \| EU |
| claude-opus-4-8 | $5.50 | $27.50 | US \| EU |
| glm-4-7-flash | $0.07 | $0.40 | US |
| gpt-oss-120b | $0.15 | $0.60 | US \| EU |
| minimax-m2 | $0.30 | $1.20 | US |
| qwen3-235b | $0.22 | $0.88 | US |
| deepseek-v3-2 | $0.62 | $1.85 | US |
| nova-pro | $0.80 | $3.20 | US \| EU |

([[2026-1026-heroku-inference-claude-opus-4-8-a-5-50-y-27-50-por-millon]], [[2026-1026-heroku-inference-modelos-abiertos-0-07-a-0-62-por-millon-de-entrada]], [[2026-1026-heroku-inference-region-provisioned-eu-y-us-por-modelo]])

**La primera corrección, de método: la columna "Model Source" existe, y el multiplicador del vault no la tiene.** La tabla nombra el origen de cada modelo —Anthropic, OpenAI, Z.ai, Moonshot AI, DeepSeek, MiniMax, Qwen, Amazon, Cohere, Stability AI— y ese campo es **el que le falta al sistema de multiplicadores**. El vault tiene "modelo de referencia" implícito en el nombre del canal, pero no publicado. Con esta tabla, un multiplicador de 0,05x aplicado a claude-opus-4-8 significa **$0.275 por 1M de tokens de entrada**, y aplicado a glm-4-7-flash significa **$0.0035**: **el mismo multiplicador significa cosas distintas en un factor de 79 según el modelo**. Y un multiplicador de 1,00x **no significa un precio de lista**: significa $5.50 en Opus 4.8 y $0.07 en GLM 4.7 Flash. La dispersión 0,04x–7,00x que la §"El mercado" registra es real, pero **está medida contra un eje que el vault todavía no ha fijado** ([[2026-1023-priceai-transit-dispersion-de-multiplicadores]]). Marcado para juicio humano, no auto-resuelto.

**La segunda corrección, de la fragilidad del multiplicador: el precio por token de Heroku es una reventa, no una API oficial.** La tabla nombra a Anthropic como *Model Source* de Claude, pero **los precios de Heroku no son los precios de la API de Anthropic**: son los de un intermediario que compra capacidad y la revende. Esto es exactamente lo que el §"El mercado" llama el riesgo estructural del corpus, pero ahora con la contrapartida: **una reventa puede publicar sus precios, un multiplicador no**. Para el producto propio, esto significa que **el catálogo de Heroku es una base de referencia más sólida que cualquier multiplicador**, porque declara la unidad, el modelo y la dirección del tráfico —tres cosas que el eje de los ratios no declara ([[2026-1026-heroku-inference-claude-opus-4-8-a-5-50-y-27-50-por-millon]]).

**La tercera corrección, de la sección que más necesita el thread: la región es una columna de precio, no un metadato.** La tabla separa "Region Provisioned" en **"US | EU"** y **"US"**, y **solo claude-3-haiku aparece con "EU" en solitario**. Todo el resto de Claude y gpt-oss-120b admiten ambas; **Qwen, DeepSeek, GLM, Kimi, MiniMax y el rerank de Amazon son US-only** ([[2026-1026-heroku-inference-region-provisioned-eu-y-us-por-modelo]]). La consecuencia para este producto es directa e incómoda: **los modelos open-weight que el vault ha considerado por precio no están disponibles en la UE**, y **la imagen es US-only sin excepción** — Stable Image Core a **$0.04/imagen** y Stable Image Ultra a **$0.14/imagen** ([[2026-1026-heroku-imagen-0-04-y-0-14-dolares-por-imagen-solo-us]]). Para un producto con Aviso Legal y DPA propios ([[2026-1022-superficie-legal-publica-dpa-clon-terms]]), **generar imagen sale de la UE sí o sí**; y el único modelo claude que se queda en la UE es **el más barato de la frontera Claude**. Esto es el eje de residencia de datos convertido en tabla de precios, que es exactamente el argumento que la §"El stack, verificado" del thread no tenía.

**La cuarta corrección, de las unidades que el thread ya sabía que no se comparaban.** La tabla de inferencia de Heroku usa **cuatro unidades incompatibles** en la misma página: **por 1M de tokens de entrada y salida** (texto), **por 1M de tokens de entrada** (embeddings: cohere-embed-v4 a $0.12 y cohere-embed-multilingual a $0.10), **por 1.000 consultas** (rerank: Amazon Rerank 1.0 a $1 y Cohere Rerank 3.5 a $2) y **por imagen** ([[2026-1026-heroku-embeddings-0-10-y-0-12-por-millon-de-tokens-de-entrada]], [[2026-1026-heroku-rerank-1-y-2-dolares-por-1000-consultas]]). El thread ya registró el problema equivalente en el otro extremo —la tabla oficial que mezcla **requests, prompts, credits y dólares de uso** sin columna de conversión ([[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]])— y ahora tiene **el mismo problema con la unidad resuelta en un extremo**: Heroku publica las unidades una por tabla y sin convertirlas. La diferencia es que **aquí el vault puede compararlas con las suyas**: el embeddings del producto es `text-embedding-3` de OpenAI ([[2026-1022-pgvector-embeddings-openai-inferidos]]) y el de Voyage en el competidor ([[2026-1022-myclone-viaje-embeddings-voyage]]); el rerank es la pieza que New API expone como endpoint (`/v1/rerank`) y que hoy no existe en el producto ([[2026-1023-new-api-gateway-unificado-de-modelos]]).

**Y una quinta corrección, que es la que más pesa para el negocio: hay un precio de lista para el consumo de inferencia de un competidor con el mismo modelo base.** El producto factura por tenant con un desglose **por proveedor (Anthropic + OpenAI)** ([[2026-1022-costes-por-categoria-tenant]]). Con esta tabla, el vault puede por primera vez **auditar si un relay es más barato que comprar el token**: si la columna de proveedor del panel dice Anthropic y el multiplicador efectivo del canal es 1,0x–2,0x, **el margen del relay es directamente el sobrecoste frente a una lista de $5.50/$27.50 por 1M en Opus 4.8**; y si es 0,05x, **el relay vende el mismo token por debajo de la lista y solo es explicable por capacidad o por riesgo de cumplimiento**. Ese es el dato que decide si construir gateway propio es una decisión de arquitectura o una decisión de margen.

**Lo que queda abierto, y es lo que el hilo debe dejar escrito.** La tabla **no publica SLA, no publica throughput, no publica límites de tasa y no publica qué región se factura cuando el modelo es "US | EU"**; y el bloque de soporte publica **Basic gratis** y remite Standard, Premier y Signature a "contact sales" sin importes ([[2026-1026-heroku-soporte-basico-gratis-y-success-plans-enterprise]]). Los MCP sí tienen un modelo declarado —**dynos one-off con pay-as-you-go**— pero **sin tabla de precios** ([[2026-1026-heroku-mcp-servers-con-dynos-one-off-pay-as-you-go]]), y los add-ons de Elements solo se cotizan en el Marketplace, con **1 crédito = $1** para clientes Enterprise ([[2026-1026-heroku-elements-1-credito-igual-a-1-dolar-solo-enterprise]]). Es decir: **la parte de cómputo de datos y la de inferencia están cotizadas al centavo; la de soporte, integración y agentes no lo está**. Para un producto que necesita facturación al tenant, esa es la frontera exacta entre lo que puede presupuestarse y lo que no.
```

THREAD: myownclone-platform-architecture

---

## Nota para el editor

- No se ha modificado ningún fichero en `3-threads/`.
- Las dos propuestas son texto para insertar en los hilos indicados; los `THREAD:` de arriba identifican a cuál corresponde cada bloque.
- Átomos de esta captura: `2026-1026-heroku-suelo-5-dolares-eco-con-sleep-y-7-dolares-basic-always-on`, `2026-1026-heroku-dyno-units-25-dolares-por-unidad-excepto-performance`, `2026-1026-heroku-performance-de-250-a-1500-dolares-con-autoscaling`, `2026-1026-heroku-fir-dynos-kubernetes-todos-requieren-private-space-desde-25`, `2026-1026-heroku-fir-general-purpose-2cpu-4gb-dice-1-vcpu`, `2026-1026-heroku-postgres-essential-5-a-20-dolares-con-4-horas-de-parada`, `2026-1026-heroku-postgres-standard-50-a-12000-con-dedicado-y-1-hora-de-parada`, `2026-1026-heroku-postgres-premium-200-con-ha-y-15-minutos-de-parada`, `2026-1026-heroku-postgres-advanced-150-a-40000-con-precios-privados-y-shield`, `2026-1026-heroku-private-y-shield-desde-125-y-150-dolares`, `2026-1026-heroku-key-value-store-mini-3-dolares-hasta-12500`, `2026-1026-heroku-kafka-desde-100-dolares-con-1-semana-de-retencion`, `2026-1026-heroku-inference-claude-opus-4-8-a-5-50-y-27-50-por-millon`, `2026-1026-heroku-inference-modelos-abiertos-0-07-a-0-62-por-millon-de-entrada`, `2026-1026-heroku-inference-region-provisioned-eu-y-us-por-modelo`, `2026-1026-heroku-embeddings-0-10-y-0-12-por-millon-de-tokens-de-entrada`, `2026-1026-heroku-rerank-1-y-2-dolares-por-1000-consultas`, `2026-1026-heroku-imagen-0-04-y-0-14-dolares-por-imagen-solo-us`, `2026-1026-heroku-mcp-servers-con-dynos-one-off-pay-as-you-go`, `2026-1026-heroku-elements-1-credito-igual-a-1-dolar-solo-enterprise`, `2026-1026-heroku-connect-demo-gratis-y-ediciones-enterprise-exclusivas`, `2026-1026-heroku-soporte-basico-gratis-y-success-plans-enterprise`.
- Átomos de la captura anterior (`heroku-signup`) que ya existen y no se duplican aquí: `2026-1026-heroku-alta-*`, `2026-1026-heroku-claims-de-escala-*`, `2026-1026-heroku-metodos-de-despliegue-*`, `2026-1026-heroku-paises-seleccionables-*`, `2026-1026-heroku-tres-variantes-de-privacy-*`, `2026-1026-heroku-recaptcha-enterprise-*`.
- Cifras de la tabla de precios del hilo: comprobadas literalmente contra `sources/2026-10-25-heroku-pricing.md` (líneas 59–79 para Cedar y Private/Shield, 104–119 para Fir, 159–200 para Postgres Essential/Standard/Premium, 266–276 para Advanced, 301–311 para Key-Value, 350–352 y siguientes para Kafka, 393–421 para Text-to-Text, 464–466 para Embeddings, 476–478 para Rerank, 480–483 para imagen).

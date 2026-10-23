---
id: 2026-1023-new-api-gateway-unificado-de-modelos
type: atom
certainty: solid
sources: [sources/2026-10-22-new-api-github.md]
links: ["[[2026-1023-priceai-transit-canal-tipo-sub2api-vs-new-api]]", "[[2026-1023-new-api-una-sola-api-multiproto]]", "[[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]"]
---

## Claim
**New API** (`QuantumNous/new-api`) se describe en su propio README como un **gateway de IA autoalojado** para aplicaciones, agentes y equipos: se conectan servicios de modelo upstream, se expone una API consistente a los clientes y se gestionan en un solo sitio **routing, acceso, uso y costes**. La sección *About* lo resume como un **"unified AI model hub for aggregation & distribution"** que **convierte varios LLM a formato OpenAI-compatible, Claude-compatible o Gemini-compatible**. Upstreams declarados: **OpenAI, Anthropic, Google Gemini, Azure OpenAI, AWS Bedrock, Vertex AI, DeepSeek, Qwen** y otros servicios compatibles. Es un fork de **One API** (`songquanpeng/one-api`, licencia MIT).

## Why It Matters
Es la definición canónica del software que el vault ya había encontrado **por el reverso**: 8 de las 30 filas del ranking de relays de PriceAI se autoidentifican como "New API" ([[2026-1023-priceai-transit-canal-tipo-sub2api-vs-new-api]]). Esta fuente es la del propio proyecto y explica qué significa esa etiqueta: un motor de agregación autoalojado que **normaliza protocolos y centraliza la facturación**, es decir, la infraestructura típica de un relay.
Para el vault importa la diferencia con un simple proxy: New API no solo reenvía, **convierte** entre los cuatro protocolos de texto ([[2026-1023-new-api-una-sola-api-multiproto]]) y **gestiona cuotas y grupos** ([[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]). Eso lo convierte en la pieza que hace posible el negocio de reventa con multiplicador, no en un simple relay de una sola clave.
Y fija una limitación de licencia para cualquier plan de auto-hospedaje del vault: **AGPLv3 con obligaciones de atribución en la interfaz** ([[2026-1023-new-api-licencia-agplv3-y-atribucion-en-ui]]).

## Extensión (posición en el ecosistema)
El README declara su linaje y su entorno: **"Upstream Projects"** lista **One API** (*"Original project base"*, MIT) y **Midjourney-Proxy** (*"Midjourney interface support"*); **"Supporting Tools"** lista **new-api-key-tool** (*"Key quota query tool"*) y **new-api-horizon** (*"New API high-performance optimized version"*). Los upstreams declarados son **OpenAI, Anthropic, Google Gemini, Azure OpenAI, AWS Bedrock, Vertex AI, DeepSeek, Qwen** y otros compatibles, y la fila de capacidades añade **OAuth/OIDC, passkeys y 2FA** para el acceso de usuarios.
La cadena de valor queda visible en una tabla: un proyecto base (One API, MIT) → un fork AGPL con más capacidades → **variantes y herramientas derivadas** (una versión "high-performance" y una herramienta de consulta de quota de key). Es el patrón de una plataforma open source con economía alrededor: el gateway es el núcleo y el margen vive en la operación, el rendimiento y las herramientas.
El dato de **Midjourney-Proxy como proyecto upstream** cierra un círculo que el vault tenía abierto desde el otro lado: el README de Midjourney-Proxy listaba a `new-api` como aplicación que lo consume ("接入MidJourney Proxy的接口管理 & 分发系统", [[2026-1023-midjourney-proxy-ecosistema-de-aplicaciones-que-lo-consumen]]). Ahora está confirmado en dirección contraria: New API es **el agregador que se apoya en Midjourney-Proxy** para la interfaz de Midjourney. Dos proyectos que se citan mutuamente y se montan uno sobre otro. Y para el vault esto importa por la **reversibilidad**: el soporte de un proveedor no está en el core, es un plugin o un adaptador ([[2026-1023-new-api-plugins-de-tareas-js-en-sandbox]]), así que cambiar de proveedor en una capacidad concreta no toca el núcleo.

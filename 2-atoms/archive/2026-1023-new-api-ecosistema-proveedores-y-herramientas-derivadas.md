---
id: 2026-1023-new-api-ecosistema-proveedores-y-herramientas-derivadas
type: atom
certainty: retired
sources: [sources/2026-10-22-new-api-github.md]
links: ["[[2026-1023-new-api-gateway-unificado-de-modelos]]", "[[2026-1023-midjourney-proxy-ecosistema-de-aplicaciones-que-lo-consumen]]", "[[2026-1023-new-api-plugins-de-tareas-js-en-sandbox]]"]
---

## Claim
El README declara la **posición de New API en su propio ecosistema**: **"Upstream Projects"** lista **One API** (*"Original project base"*, MIT) y **Midjourney-Proxy** (*"Midjourney interface support"*). **"Supporting Tools"** lista **new-api-key-tool** (*"Key quota query tool"*) y **new-api-horizon** (*"New API high-performance optimized version"*). Los upstreams declarados en la descripción del producto son **OpenAI, Anthropic, Google Gemini, Azure OpenAI, AWS Bedrock, Vertex AI, DeepSeek, Qwen** y otros servicios compatibles, y la fila de capacidades añade **OAuth/OIDC, passkeys y autenticación de dos factores** para el acceso de usuarios.

## Why It Matters
La cadena de valor queda visible en una tabla: un proyecto base (One API, MIT) → un fork AGPL con más capacidades → **variantes y herramientas derivadas** (una versión "high-performance" y una herramienta de consulta de quota de key). Es el patrón clásico de una plataforma open source con economía alrededor: el gateway es el núcleo, y el margen vive en la operación, el rendimiento y las herramientas.
El dato de **Midjourney-Proxy como proyecto upstream** cierra un círculo que el vault ya tenía abierto desde el otro lado: el README de Midjourney-Proxy listaba a `new-api` como aplicación que lo consume ("接入MidJourney Proxy的接口管理 & 分发系统", [[2026-1023-midjourney-proxy-ecosistema-de-aplicaciones-que-lo-consumen]]). Ahora está confirmado en la dirección contraria: New API es **el agregador que se apoya en Midjourney-Proxy para la interfaz de Midjourney**. Son dos proyectos que se citan mutuamente y se montan uno sobre otro.
Para el vault, esto importa por la **reversibilidad**: el soporte de un proveedor no es código propio del gateway, es un plugin o un adaptador ([[2026-1023-new-api-plugins-de-tareas-js-en-sandbox]]), lo que significa que el coste de cambiar de proveedor de una capacidad concreta no está en el core.


## [RETIRED]
Contenido fusionado dentro de [[2026-1023-new-api-gateway-unificado-de-modelos]] por regla de una idea por átomo. Fuente: [[2026-1023-new-api-gateway-unificado-de-modelos]].

---
id: 2026-1026-heroku-inference-region-provisioned-eu-y-us-por-modelo
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-pricing.md]
links: ["[[2026-1026-heroku-inference-modelos-abiertos-0-07-a-0-62-por-millon-de-entrada]]", "[[2026-1024-1984-hosting-politica-de-sin-logs-e-imagenes-de-privacidad]]", "[[2026-1022-superficie-legal-publica-dpa-clon-terms]]"]
---

## Claim
La tabla Text-to-Text de Heroku Managed Inference incluye una columna **"Region Provisioned"** con dos valores, **"US | EU"** y **"US"**, y solo un modelo aparece con **"EU"** en solitario: **claude-3-haiku**, priced **$0.25 / $1.25**. Con "US | EU" están los ocho modelos Anthropic restantes (claude-4-5-haiku, claude-4-sonnet, claude-4-5-sonnet, claude-sonnet-4-6, claude-opus-4-5, claude-opus-4-6, claude-opus-4-7, claude-opus-4-8), más **gpt-oss-120b**, **nova-lite** y **nova-pro**. Con **"US" únicamente**: **qwen3-235b**, **qwen3-coder-480b**, **deepseek-v3-2**, **glm-4-7**, **glm-4-7-flash**, **kimi-k2-thinking**, **kimi-k2-5**, **minimax-m2**, **minimax-m2-1** y **nova-2-lite**. Los modelos **Text-to-Score** (Amazon Rerank 1.0, Cohere Rerank 3.5) y los **Embedding** (cohere-embed-v4, cohere-embed-multilingual) son **"US | EU"**; los dos **Image Models** (Stable-image-core, Stable-image-ultra) son **"US"** únicamente.

## Why It Matters
Es el **eje de residencia de datos** que el vault había tratado como un argumento de marketing de proveedor y que aquí aparece como **columna de precio**. La consecuencia práctica es dura: **casi todos los modelos de pesos abiertos que el vault ha considerado —Qwen, DeepSeek, GLM, Kimi, MiniMax— no están disponibles en la UE**, solo en US. Para un producto con clientes europeos y datos de terceros ([[2026-1022-superficie-legal-publica-dpa-clon-terms]]), **elegir un open-weight por precio implica que la inferencia sale de la UE**, o aceptar una transferencia internacional de datos.
Y el reverso también es información: **claude-3-haiku es el único modelo con región EU exclusiva**, a $0.25/$1.25 — es decir, el más barato de la frontera Claude **y** el único que se queda en la UE. Eso lo convierte, por precio y por residencia, en el candidato obvio para el tráfico europeo que no pueda ir a US, y explica por qué un proveedor pondría la marca "EU" en una fila de catálogo.
El detalle final cierra el patrón de una línea por proveedor: **la imagen es US-only** (Stable Image Core y Ultra), lo que significa que **generar imagen para un clon europeo sale de la UE sí o sí** — un punto que une esta captura con el debate de imagen del vault ([[2026-1024-1984-hosting-politica-de-sin-logs-e-imagenes-de-privacidad]]) y con la pieza de Midjourney que es precisamente un puente no oficial ([[2026-1023-midjourney-proxy-relevancia-para-clones-con-imagen]]).

## Nota de verificación
La tabla **no explica qué implica "Region Provisioned"** — si es el lugar del cómputo, el del almacenamiento de prompts o el del facturado. La asignación US/US|EU/EU es lectura literal de la columna.

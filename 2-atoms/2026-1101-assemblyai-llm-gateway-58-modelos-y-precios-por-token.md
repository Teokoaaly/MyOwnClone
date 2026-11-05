---
id: 2026-1101-assemblyai-llm-gateway-58-modelos-y-precios-por-token
type: atom
certainty: solid
sources: [sources/2026-11-01-assemblyai-pricing.md]
links: ["[[2026-1101-assemblyai-tarifas-por-hora-no-por-minuto]]", "[[2026-1022-costes-por-categoria-tenant]]", "[[2026-1022-myclone-viaje-embeddings-voyage]]"]
---

## Claim
El LLM Gateway de AssemblyAI muestra **58 modelos** con precios por millón de tokens de entrada y salida (de GPT-5 Nano a $0,05/$0,40 hasta GPT-6 Astra a $10/$50), con un matiz de routing explícito: "Prices shown are for global routing. **In-region (US/EU) pricing is 10% higher** due to provider cost increases. Add `"model_region": "global"` to your API requests to get the rates shown." La FAQ define la unidad: "one English word equals about 1.3 tokens".

## Why It Matters
El vault ya tiene un patrón de coste por tokens resuelto —el viaje de embeddings con Voyage ([[2026-1022-myclone-viaje-embeddings-voyage]]) y el corte por categoría de [[2026-1022-costes-por-categoria-tenant]])— y el LLM Gateway de AssemblyAI es exactamente el tipo de relay que el vault ya ha documentado como categoría rentable en otras notas. El dato accionable para el vault es el **+10 % por procesar in-region US/EU**: es un recargo escondido sobre el mismo modelo por un requisito de residencia de datos, y para un producto con base de clientes en España ([[2026-1022-i18n-es-first-jurisdiccion-es]]) ese recargo es un coste real, no hipotético. La conversión "1 palabra inglesa ≈ 1,3 tokens" es la pieza que permite cotizar el coste del LLM en términos de palabras (una respuesta de 500 palabras ≈ 650 tokens) sin hacer aritmética de tokens cruda: es la misma operación de normalización de unidades que el vault ya plantea en Deepgram (precio por minuto, [[2026-1031-deepgram-pricing]]) y en Gemini (25 tokens por segundo de audio).

## Actualización 2026-11-04 — re-verificación y desglose por proveedor
La captura del 2026-11-04 (`sources/2026-11-04-assemblyai-pricing.md`, render completo, idéntico al del 11-02) reproduce sin variación el bloque LLM Gateway: **"Showing 58 of 58 models"**, los mismos 58 pares input/output, el recargo **"+10 %" por routing in-region US/EU**, la definición de token ("one English word equals about 1.3 tokens") y los mismos filtros de proveedor y de banda de precio. Lo que esta captura añade es la lectura del desglose de los 58 modelos por proveedor —**AWS Bedrock 26, Open AI 11, Vertex 10, Digital Ocean 4, Fireworks 4, Inception Labs 2 y AssemblyAI 1**— y por banda de precio de entrada (**29** por debajo de $1/1M, **22** entre $1 y $5, **7** por encima de $5), que se documenta en [[2026-1104-assemblyai-llm-gateway-58-modelos-de-7-proveedores-y-56-de-terceros]].

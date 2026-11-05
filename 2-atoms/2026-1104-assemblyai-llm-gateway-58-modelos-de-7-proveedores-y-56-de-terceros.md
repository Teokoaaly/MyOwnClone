---
id: 2026-1104-assemblyai-llm-gateway-58-modelos-de-7-proveedores-y-56-de-terceros
type: atom
certainty: solid
sources: [sources/2026-11-04-assemblyai-pricing.md, sources/2026-11-02-assemblyai-pricing.md, sources/2026-11-01-assemblyai-pricing.md]
links: ["[[2026-1101-assemblyai-llm-gateway-58-modelos-y-precios-por-token]]", "[[2026-1022-myclone-viaje-embeddings-voyage]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
Los "58 de 58 modelos" del LLM Gateway de AssemblyAI se reparten entre **siete proveedores** según el filtro de la propia tabla: **AWS Bedrock 26, Open AI 11, Vertex 10, Digital Ocean 4, Fireworks 4, Inception Labs 2 y AssemblyAI 1**. Es decir, **56 de los 58 modelos son de terceros y solo uno es propio de AssemblyAI**. El mismo filtro de precio de entrada agrupa los 58 en tres bandas: **"Under $1 / 1M in" → 29 modelos**, **"$1–$5 / 1M in" → 22** y **"$5+ / 1M in" → 7**. La captura del 11-04 reproduce estas cifras exactamente igual que las del 11-01 y del 11-02.

## Why It Matters
Cambia la lectura de qué es el LLM Gateway para el vault: **no es un catálogo de modelos propios, es un relay multi-proveedor** — el mismo tipo de pieza que el vault ya modela como relay de embeddings ([[2026-1022-myclone-viaje-embeddings-voyage]]). Dos consecuencias operativas. Primera: latarifa publicada es la tarifa *de salida* de AssemblyAI sobre la de origen, y el recargo de **+10 % por routing in-region US/EU** ("due to provider cost increases", ver [[2026-1101-assemblyai-llm-gateway-58-modelos-y-precios-por-token]]) tiene sentido precisamente porque el mayorista es Amazon y Google: el recargo no es un margen de AssemblyAI sobre sí mismo, es el coste de proveedor pasado más un 10 %. Segunda: la **concentración en Bedrock (26 de 58, el 45 %)** es una dependencia operativa —un cambio de condiciones en AWS afectaría a casi la mitad del catálogo—, mientras que la dispersión de los tres modelos más baratos (GPT-5 Nano, Nemotron Lightning 3.5 30B A3B y Nemotron 3 Nano 30B A3B) apunta a proveedores de modelos abiertos. Y para el corte de costes del vault ([[2026-1022-costes-por-categoria-tenant]]) la conclusión práctica es que **el Gateway no crea una partida de coste nueva**: si el clon ya paga tokens a un proveedor, migrar al relay solo cambia quién factura y con qué recargo de región.

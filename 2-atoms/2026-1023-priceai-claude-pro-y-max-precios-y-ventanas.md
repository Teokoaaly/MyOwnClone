---
id: 2026-1023-priceai-claude-pro-y-max-precios-y-ventanas
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-official-api.md]
links: ["[[2026-1023-priceai-chatgpt-plus-y-pro-precios-y-ventanas]]", "[[2026-1023-priceai-suscripcion-no-es-api-token]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
Las suscripciones oficiales de Claude se tabulan con la misma estructura de ventanas que ChatGPT, pero con cuotas **más bajas** a igual precio:

| Plan | Precio | 5h | Semana | Mes |
| --- | --- | --- | --- | --- |
| Pro | $20/mes | $5 | $30 | $130 |
| Max 5x | $100/mes | $60 | $400 | $1300 |
| Max 20x | $200/mes | $150 | $800 | $3200 |

Cobertura (7 ítems): **Claude Fable 5, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 5, Claude Sonnet 4.6**. El descriptor del canal advierte que la cuota se calcula dinámicamente por **uso dentro del producto, longitud de mensaje, adjuntos y ventana de 5 horas**, y que la página de cobertura añade: **"Claude Code 或 Console API 需要单独看限制和计费"**.

## Why It Matters
A $20/mes, Claude Pro entrega $130 de cuota mensual frente a los $450 de ChatGPT Plus — **3,5× menos**. A $200/mes, Max 20x ($3200) iguala exactamente a ChatGPT Pro 20x ($8000/mes → no: la mitad). Es decir: **a mismo precio, Claude da la mitad de cuota de ChatGPT en el plan alto** (1.300 vs. 4.500 en el tramo de $20; 3.200 vs. 8.000 en el tramo de $200). La comparación entre modelos de frontera del vault depende de cuál cuota se mira: no son equivalentes.
Y el límite "Console API aparte" es exactamente la línea que separa el precio de producto del precio de API ([[2026-1023-priceai-suscripcion-no-es-api-token]]), que es donde entra [[2026-1022-costes-por-categoria-tenant]] como el panel donde un producto multi-tenant registra su consumo real de Anthropic.

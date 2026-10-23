---
id: 2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos
type: atom
certainty: tentative
sources: [sources/2026-10-22-priceai-official-api.md]
links: ["[[2026-1023-priceai-stepfun-step-plan-prompts-y-llamadas]]", "[[2026-1023-priceai-alibaba-coding-plan-50-usd]]", "[[2026-1023-priceai-qwen-token-plan-credits-5h-y-7d]]"]
---

## Claim
La tabla de la captura usa **cuatro unidades de cuota distintas**, sin columna que las iguale:

- **requests** — Tencent TokenHub (1.200/9.000/18.000 y 6.000/45.000/90.000) y Alibaba Model Studio (6.000/45.000/90.000) ([[2026-1023-priceai-tencent-tokenhub-coding-plan-lite-y-pro]], [[2026-1023-priceai-alibaba-coding-plan-50-usd]]).
- **prompts** — StepFun, con conversión oficial ~15 llamadas de modelo por prompt ([[2026-1023-priceai-stepfun-step-plan-prompts-y-llamadas]]).
- **credits** — Alibaba Bailian Token Plan, 700/5h y 2.500/7d ([[2026-1023-priceai-qwen-token-plan-credits-5h-y-7d]]).
- **dólares de uso** — ChatGPT, Claude, Grok y OpenCode Go, con ventanas 5h/semana/mes ([[2026-1023-priceai-chatgpt-plus-y-pro-precios-y-ventanas]]).

La lectura transversal es que **el request es la unidad común entre nubes chinas** (mismas cifras en Tencent y Alibaba) y que **el dólar de uso es la unidad común entre proveedores occidentales**; prompts y credits son unidades propietarias sin equivalencia publicada fuera de su propio plan.

## Why It Matters
Sin una columna de conversión, esta tabla **no permite construir un ranking de coste por capacidad**: comparar "6.000 requests/5h a $50" con "$12/5h" exige saber cuánto consume un request promedio en tokens, y la captura no lo publica. Por eso este átomo es *tentative* en su lectura comparativa aunque las cifras sean tabuladas.
Es también la razón por la que el vault no debería modelar el gasto de inferencia con esta fuente: sirve para saber qué planes existen y a qué precio de lista, no para derivar un coste por token. Para el coste real por token el vault necesita los precios estándar de la otra vista de PriceAI (input/output/cache token), que esta captura no tabula.

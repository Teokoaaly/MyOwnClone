---
id: 2026-1026-heroku-inference-modelos-abiertos-0-07-a-0-62-por-millon-de-entrada
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-pricing.md]
links: ["[[2026-1026-heroku-inference-claude-opus-4-8-a-5-50-y-27-50-por-millon]]", "[[2026-1022-gap-dify-como-capa-inferencia-prompts]]", "[[2026-1023-new-api-precios-por-ratio-y-expresion]]"]
---

## Claim
En la misma tabla Text-to-Text de Heroku, los **modelos de pesos abiertos y los de tamaño medio** cotizan muy por debajo de la frontera Claude. Precio de entrada por 1M tokens: **nova-lite $0.06** (salida $0.24), **glm-4-7-flash $0.07** (salida $0.40), **gpt-oss-120b $0.15** (salida $0.60), **qwen3-235b $0.22** (salida $0.88), **minimax-m2 $0.30** (salida $1.20), **minimax-m2-1 $0.30** (salida $1.20), **nova-2-lite $0.33** (salida $2.75), **qwen3-coder-480b $0.45** (salida $1.80), **glm-4-7 $0.60** (salida $2.20), **kimi-k2-thinking $0.60** (salida $2.50), **kimi-k2-5 $0.60** (salida $3.00), **deepseek-v3-2 $0.62** (salida $1.85), **nova-pro $0.80** (salida $3.20). El cociente salida/entrada **no es fijo**: va de **×3,0** (deepseek-v3-2: $1.85/$0.62) a **×8,3** (nova-2-lite: $2.75/$0.33).

## Why It Matters
Da al vault el **suelo y techo de precio de token con lista pública verificada**, que es lo que faltaba para calibrar el multiplicador de los relays: **$0.06** (nova-lite) frente a **$5.50** (claude-opus-4-8) es un factor **×92** en la misma columna y en la misma página. Cuando un canal de reventa declara "0,05× del oficial", la pregunta que el vault puede ahora responder es **de qué oficial**: si es Claude, $0.165/1M; si es un open-weight como glm-4-7-flash, $0.0035/1M. Son dos órdenes de magnitud y el mismo multiplicador.
El hallazgo fino es el **cociente salida/entrada variable**: Anthropic lo fija en ×5 en las ocho filas, pero en los modelos abiertos va de ×3 a ×8,3. Es decir, **el "precio de salida" no es un recargo uniforme del sector**, y un producto que asuma ×5 para todos los proveedores está subestimando a los modelos con output caro (nova-2-lite) y sobreestimando a los baratos (deepseek). Como el vault ya sabe que **Dify es la capa de inferencia por prompts** ([[2026-1022-gap-dify-como-capa-inferencia-prompts]]), y que el gateway reparte por modelo y grupo ([[2026-1023-new-api-precios-por-ratio-y-expresion]]), este es el tipo de tabla que debería entrar en el modelo de coste como **precio de referencia por par (modelo, sentido)**, no como un único precio por token.
Y para el producto del vault, el dato accionable es que **minimax-m2 y minimax-m2-1 se cotizan a $0.30/$1.20** — el mismo par de precios para las dos versiones, o sea **sin prima por la generación más reciente**.

## [FRICTION]
> [[2026-1023-new-api-grupos-como-eje-de-precio-del-relay]] sostiene, como hipótesis, que "el grupo es la unidad de precio" y que "el multiplicador es la configuración del grupo", y lo apoya con la dispersión 0.04x–7.00x de los canales ([[2026-1023-priceai-transit-dispersion-de-multiplicadores]]).
> Este átomo presiona esa creencia en un punto concreto: **el multiplicador no se aplica a un "precio oficial" único, porque el precio de lista verificado del mismo sector está en un rango de ×92 dentro de la misma columna de la misma página**. Con precios de referencia que van de $0.06 (nova-lite) a $5.50 (claude-opus-4-8) por 1M de tokens de entrada, **un multiplicador de 0,05× significa $0.003 o $0.275 según el modelo de referencia**, y un multiplicador de 1,00× significa $0.06 o $5.50. Es decir: **el multiplicador solo es interpretable si se declara el par (modelo, upstream) al que se aplica**, y si el producto reenvíaClaude sin distinguir el modelo de referencia, su contabilidad por ratio no es comparable entre filas.
> Ambas no pueden ser completamente correctas: o el grupo fija el precio por modelo (y entonces el multiplicador es un parámetro derivado, no la palanca primaria), o el multiplicador es la palanca y entonces la tabla de ratios necesita columna de modelo de referencia, que el vault todavía no tiene publicada. Marcado para juicio humano, no auto-resuelto: el README de New API no publica una columna de precio de referencia.

## Nota de verificación
Los cocientes salida/entrada y el factor ×92 son cálculo de este átomo sobre las dos columnas de la tabla. Todos estos modelos salvo nova-lite, gpt-oss-120b, nova-pro y qwen3-coder-480b figuran con "Region Provisioned: US" únicamente.

---
id: 2026-1024-noones-limite-diario-suma-de-todas-las-operaciones-en-24h
type: atom
certainty: solid
sources: [sources/2026-10-23-noones-limits-and-verification.md]
links: ["[[2026-1024-noones-tabla-de-limites-por-nivel]]", "[[2026-1024-noones-nivel-2-sin-limites-diarios-y-100k-por-operacion]]", "[[2026-1024-noones-limites-vitalicios-trade-y-wallet-seguros-por-separado]]"]
---
## Claim
La KB define el límite diario como un **agregado temporal, no por operación**: *"the daily limit applies to the _sum_ of all operations performed by user over the last 24 hours"*. Las operaciones que se suman son cuatro familias: **trade** (initiated via marketplace **y** via messenger), **internal and external send-out**, **receiving internal deposit**, y **convert (aka swap, hedging)**. Aparte, los vitalicios se contabilizan **por separado**: *"Lifetime trade limits and wallet send-out limits are tracked separately. For example, you can have $500 remaining for trading, and $4,000 left for wallet send outs."*

## Why It Matters
El límite diario de NoOnes es una **ventana deslizante de 24h sobre todo el flujo de valor**, no un cupón por acción: por eso la misma cifra ($5K en L1) no equivale a $5K por operación sino a $5K repartidos entre trade, envío, recepción y conversión. Para un phone farm esto importa porque **el mismo dinero cuenta varias veces por rutas distintas** (convertir, enviar internamente, mover por messenger) — el diseño del contador es el mecanismo por el que un operador que rota rutas no evade el techo, solo lo consume más rápido. Y la separación de vitalicios (trade vs. send-out de wallet) es una segunda contabilidad independiente: los $20K de cada lado en L1 **no son un único presupuesto de $20K**, sino dos presupuestos de $20K que se consumen en flujos distintos (comprar/vender vs. retirar).


## Nota de extensión 2026-10-27
A partir de `sources/2026-10-26-hero-sms-api-docs.md`.

Este átomo documenta que NoOnes impone un **techo diario agregado de operaciones** y un control de saldo que el vault tiene registrado como "el único control granular de gasto del sector". HeroSMS no publica ningún techo, pero su API publica **la herramienta para que el cliente lo construya**: `get/activations/history` con `from`/`to` obligatorios, `countries[]`, `services[]`, `statuses[]`, `size`, `page`, `sort[id]` y `search` ([[2026-1027-hero-sms-el-historial-de-activaciones-exige-ventana-temporal-y-filtros]]), más `get/activations/stats` y `get/activations/offers/{verificationType}` ([[2026-1027-hero-sms-trece-operaciones-de-activacion]]).

Consecuencia para el Editor: el thread puede **reformular el reparto de responsabilidades** en el control de gasto de SMS. NoOnes **centraliza** el límite y lo oculta detrás de un techo; HeroSMS **externaliza** el control y publica el histórico para que el cliente lo audite. Y hay un matiz que el átomo debe conservar: **HeroSMS no publica ningún techo**, de modo que externalizar el control **transfiere al pipeline una responsabilidad que NoOnes asume** —con un modelo prepago sobre saldo ([[2026-1023-hero-sms-modelo-pay-per-use-y-tabla-real-vs-virtual]]), lo que se quiere vigilar no es el número de operaciones sino **el saldo retenido**.

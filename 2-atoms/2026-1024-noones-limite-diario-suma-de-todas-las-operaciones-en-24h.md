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

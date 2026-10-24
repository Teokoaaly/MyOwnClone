---
id: 2026-1024-noones-limites-vitalicios-trade-y-wallet-seguros-por-separado
type: atom
certainty: solid
sources: [sources/2026-10-23-noones-limits-and-verification.md]
links: ["[[2026-1024-noones-limite-diario-suma-de-todas-las-operaciones-en-24h]]", "[[2026-1024-noones-tabla-de-limites-por-nivel]]", "[[2026-1024-noones-nivel-2-sin-limites-diarios-y-100k-por-operacion]]"]
---
## Claim
NoOnes mantiene **tres contadores vitalicios independientes**, no un único saldo histórico: en la tabla, **Lifetime Trade Limit** ($20K en L1, ∞ en L1+/L2/L3), **Lifetime Send-out Limit** ($20K en L1, ∞ en el resto) y **Send-out Tx Limit** ($1K en L1, ∞ en el resto). La nota lo hace explícito: *"Lifetime trade limits and wallet send-out limits are tracked separately. For example, you can have $500 remaining for trading, and $4,000 left for wallet send outs."* La prosa de L1 confirma el par **$20,000** para trading y **$20,000** para send-out, y su viñeta *"Daily limit of $5,000"* replica el valor de la tabla sin añadir un cuarto contador: los contadores son tres (Lifetime Trade, Lifetime Send-out, Send-out Tx).

## Why It Matters
La existencia de **tres** contadores (y no dos) significa que el límite efectivo es el mínimo de todos: en L1 el límite real no es "$20K vitalicios" sino **$1K por envío** — el límite por transacción es 20 veces más restrictivo que el vitalicio. Esto importa en el diseño de caja: un operador que quiera drenar los $20K vitalicios de send-out necesita **al menos 20 transacciones** y, en el caso de Lightning, con el techo de $1k por tx que **no escala con el nivel de verificación** ( Lightning send-out Tx Limit = $1k en L1, L1+, L2 y L3). La lección transferible al vault: cuando un proveedor publica varias cifras de límite, hay que leer **cuál es el más pequeño**, no el más grande, porque el más grande es el que aparece en la prosa de marketing.

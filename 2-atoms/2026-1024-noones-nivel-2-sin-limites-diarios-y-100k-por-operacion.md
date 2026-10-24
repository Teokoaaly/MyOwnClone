---
id: 2026-1024-noones-nivel-2-sin-limites-diarios-y-100k-por-operacion
type: atom
certainty: tentative
sources: [sources/2026-10-23-noones-limits-and-verification.md]
links: ["[[2026-1024-noones-tabla-de-limites-por-nivel]]", "[[2026-1024-noones-escalera-de-verificacion-l1-l1plus-l2-l3]]", "[[2026-1024-noones-verificacion-basica-l1plus-revision-manual-hasta-72h]]"]
---
## Claim
La sección "Why should I verify my account?" describe los niveles en prosa, y para **L2** dice literalmente: *"Verify your identity and get rid of all limits. There are no daily or lifetime limits whatsoever. The only limit is the maximum amount per trade, which is $100,000. But you can have as many trades as you want."*, con el añadido *"Access to more payment methods"*. Para **L3**: *"Enhanced due diligence checks require verification of address. Level 3 users can trade up to $1,000,000 in a single trade."* La misma prosa asegura que L1 da *"a daily limit of $5,000"* y un límite vitalicio de **$20,000** para trading y **$20,000** para send-out de wallet.

## Why It Matters
La prosa es la que explica el **modelo de negocio** del proveedor: el cliente no paga un fee de verificación, paga con **capacidad**. En L2 no hay cupón diario ni vitalicio —solo un **techo por operación de $100,000** y "as many trades as you want"— y en L3 el techo sube a **$1,000,000** en una sola operación a cambio de verificar dirección (enhanced due diligence). Para una operación que mueve cripto entre pares, la pregunta operativa no es "cuánto cuesta verificar" sino "cuántas operaciones de $100K hace falta para extraer el volumen que necesito" — y esa pregunta tiene respuesta distinta en L2 (muchas operaciones) que en L3 (una sola). En el vault esto se separa del caso de los proveedores de SMS, donde la verificación es un coste marginal por alta y no una capacidade ([[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]).

## [FRICTION]
> [[2026-1024-noones-tabla-de-limites-por-nivel]] recoge la tabla "P2P Trade limits" de la misma KB, donde la fila **Daily Limit** para L2 aparece como **$100K** (y 1 million para L3), mientras que esta prosa de L2 afirma *"There are no daily or lifetime limits whatsoever"*.
> Ambas afirmaciones no pueden ser ciertas a la vez: o la tabla (columna *Daily Limit*) refleja en realidad el **per-trade limit** repetido —impresión que apoyaría la prosa—, o la prosa exagera y L2 sí arrastra un tope agregado diario de $100K, lo que limitaría el "as many trades as you want" a $100K por día en total.
> La captura no contiene ninguna de las dos páginas de la KB, así que el vault solo puede registrar el conflicto, no resolverlo. Impacto real para el phone farm: la capacidad diaria garantizada en L2 es **$100K** en el peor caso de lectura y **ilimitada** en el mejor; un plan de capacidad basado en L2 debe asumir el techo conservador.
> Marcado para juicio humano, no auto-resuelto.

---
id: 2026-1103-aiven-se-vende-como-all-inclusive-pero-dos-partidas-contradicen-el-titular
type: atom
certainty: solid
sources: [sources/2026-11-03-aiven-pricing.md]
links: ["[[2026-1102-aiven-disco-dinamico-cuesta-dinero-extra-desde-startup]]", "[[2026-1101-aiven-runtime-pasa-a-facturacion-por-uso-con-egreso-de-red]]", "[[2026-1031-aiven-postgresql-pricing]]"]
---

## Claim
El titular con el que Aiven abre su página de precios es: **"Aiven's pricing is all-inclusive and transparent, providing you with the confidence and ease to forecast monthly expenses without any surprises from variable costs."** Pero **dos partidas de la misma página contradicen ese titular**: el **dynamic disk sizing** es "Available at an additional cost" desde Startup ($75/mes), y la FAQ de Runtime anuncia que **"Billing will move to usage-based, including active app runtime, plus applicable storage and network egress costs"**. La propia FAQ de billing cierra con "What you see on the plan card is what you pay" y "Your bill changes only when you change something: choose a larger plan, **add extra storage**, ... or **enable BYOC**" — es decir, la lista de cambios que sí mueven la factura incluye precisamente las dos partidas que rompen el "todo incluido".

## Why It Matters
Fija la lectura correcta del posicionamiento de Aiven: **"all-inclusive" es cierto en la capa de servicios gestionados e infraestructura base, y falso en la capa de almacenamiento y de la capa de aplicación**. Para el vault esto importa porque el titular es exactamente el argumento que usaría un cliente al comparar "coste fijo predecible" ([[2026-1031-aiven-postgresql-pricing]]) frente a la alternativa de VPS barato: si se cita sin matiz, se está citando la frase del vendor. Con el matiz correcto, la comparación de coste total queda así: el plan base es un coste fijo real y con networking incluido ([[2026-1102-aiven-todo-el-coste-de-red-incluido-en-todos-los-planes]]), pero el almacenamiento —la partida que crece con los datos de cada tenant— se factura aparte, y la capa de aplicación es la que se abrirá a coste variable.

## [FRICTION]
> [[2026-1102-aiven-disco-dinamico-cuesta-dinero-extra-desde-startup]] ya registra que el almacenamiento dinámico es una línea de coste separada desde Startup. Esta nota no lo contradice: lo que añade es que **esa línea contradice el titular "all-inclusive ... without any surprises from variable costs" de la propia página**. La fricción real es entre la promesa de la página y su propia tabla, y queda marcada para juicio humano: o "all-inclusive" se lee como "sin cargos ocultos de infraestructura y servicios" (y el almacenamiento dinámico es una ampliación explícita de capacidad, no una sorpresa), o la página vende una previsibilidad que su tabla no entrega. Marcado para juicio humano, no auto-resuelto.

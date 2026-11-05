---
id: 2026-1026-new-api-consulta-de-saldo-upstream-y-prioridad-arrastrable
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]", "[[2026-1023-new-api-precios-por-ratio-y-expresion]]", "[[2026-1026-new-api-dos-carteras-y-fallback-al-cny]]"]
---

## Claim
**v1.0.0-rc.45** añade dos cosas al panel de canales:

1. **Prioridad de canal arrastrable**: se activa el **"modo arrastre"** en la lista de canales y se reordena la prioridad a pulso.
2. **Consulta de saldo upstream**: se puede consultar el saldo del upstream en **canales de tipo New API**, y esos canales pueden **enlazar Hailuo, Vidu y Veo**; además se añade la consulta de saldo para **canales Sub2API** (PR #7749).

## Why It Matters
La consulta de saldo upstream convierte al gateway en un **gestor de capacidad multi-proveedor**: el operador ve, desde su consola, cuánto le queda a cada proveedor y puede enrutar en consecuencia. Eso es exactamente la pieza que falta en el modelo de coste del vault, donde hoy el precio de un relay es una **tabla de terceros** ([[2026-1023-new-api-precios-por-ratio-y-expresion]]) y no una relación viva con el upstream.
La aparición de **Hailuo, Vidu y Veo** como upstreams enlazables — junto al soporte ya existente de **New API** y **Sub2API** — confirma el mapa de eslabones que el vault viene trazando: **New API y Sub2API son gateways que se pueden anidar el uno en el otro** ([[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]). Un relay puede ser cliente de otro relay, y eso multiplica el margen posible y el riesgo de contraparte en la misma cadena.
El arrastre de prioridad, por su parte, es la confirmación de que **la prioridad de canal es un parámetro operativo de primer orden**: se modifica con el mouse, no con un archivo, porque se cambia en caliente cuando un proveedor falla. Es un detalle de UX que revela la frecuencia con la que ese parámetro se toca en la práctica.

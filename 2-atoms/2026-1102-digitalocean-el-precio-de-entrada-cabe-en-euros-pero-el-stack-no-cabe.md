---
id: 2026-1102-digitalocean-el-precio-de-entrada-cabe-en-euros-pero-el-stack-no-cabe
type: atom
certainty: tentative
sources: [sources/2026-11-02-digitalocean-droplets-pricing.md, sources/2026-11-03-digitalocean-droplets-pricing.md]
links: ["[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1031-digitalocean-entrada-basic-512-mib-4-dolares-al-mes]]", "[[2026-1024-hostbrr-value-2gb-1-vcpu-2gb-ram-25-gb-storage]]"]
---

## Claim
El precio de entrada de DigitalOcean es **$4.00/mes**, una cifra **en dólares** que, convertida al tipo de cambio habitual de ~1,10 USD/EUR, equivale a **≈ €3,64/mes — por debajo del techo de ≤ €4/mes** del vault. Pero el primer plan que puede alojar el stack (2 GiB / 1 vCPU, [[2026-1024-hostbrr-value-2gb-1-vcpu-2gb-ram-25-gb-storage]] como referencia de "suelo real del stack") cuesta **$12.00/mes ≈ €10,91**, casi **tres veces** el presupuesto. El umbral que decide es por tanto **$6.00** (1 GiB), que es cuando el plan deja de ser decorativo.

## Why It Matters
Es el punto donde el encuadre "DigitalOcean es el proveedor caro" del vault tiene que matizarse: **su entrada sí cabe en el presupuesto nominal en euros, y su plan de 1 GiB ($6 ≈ €5,45) queda a un solo peldaño del suelo de Hetzner ($5,99 → €5,99 sin IVA)**; lo que no cabe es el **tamaño de máquina que el producto necesita**. Eso reordena la escalera: DigitalOcean no es "el caro" sino "el caro en la parte alta del stack", y su entrada de 512 MiB es exactamente el tipo de nodo auxiliar (relay o worker) que el thread de hosting barato ya le concede a los planes del tramo barato en su escalera de 768 MB–1 GB. La decisión operativa que se abre es si conviene un VPS barato de 2 GB con SLA o un droplet de DO de 4 GiB con CPU dedicada a $24 — una comparación que no es de precio sino de **cantidad de piezas** que hay que operar ([[2026-1022-costes-por-categoria-tenant]]).

## Nota de verificación
La conversión a euros y el umbral de $6/$12 son **cálculo de este átomo**: la fuente publica los importes **solo en dólares** y **no en ningún momento publica tipo de cambio, IVA ni precios en euros**. La equivalencia usa ~1,10 USD/EUR como referencia y **no se afirma que sea el tipo aplicable en la fecha de captura**.

## 2026-11-03 — re-verificación
La captura del **2026-11-03** reproduce la tabla Basic **completa y sin variaciones**: el plan de entrada sigue en **$4.00/mes** ($0.00595/hora) y el plan de 2 GiB / 1 vCPU en **$12.00/mes**. La conversión a euros (~€3,64 y ~€10,91 con 1,10 USD/EUR) sigue siendo **cálculo de este átomo**: la fuente publica los importes **solo en dólares** y no en ningún momento tipo de cambio ni IVA, también en esta captura. El umbral que decide —**$6.00** (1 GiB)— no ha cambiado. Ver [[2026-1103-digitalocean-precios-identicos-en-las-cuatro-capturas-del-31-oct-al-3-nov]].

## [FRICTION]
> [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]] afirma, como claim ancla, que "**ningún plan del catálogo de Hetzner Cloud cabe en un presupuesto de €4/mes**" y de ahí sale la lectura operativa "hay que pagar ~€6/mes de infraestructura" (con hilo en [[escala-de-hosting-barato-y-el-limite-de-4-euros]]).
> La captura de DigitalOcean del 2026-11-02 introduce un dato que **no lo refuta** —la afirmación sigue siendo válida *acotada al catálogo de Hetzner*— pero que **sí desplaza la regla operativa**: existe un plan de un proveedor **de marca global con SLA, IP incluida y red de 12 regiones de datos** cuyo precio de catálogo en dólares está **por debajo del umbral de €4 una vez convertido**, y un segundo plan a $6 que roza el suelo de Hetzner.
> Ambas no pueden ser completamente correctas si la lectura general del vault es "el presupuesto de €4 es inalcanzable para un proveedor serio": o el umbral de €4 se define sobre **precios ya convertidos a euros con IVA** (y entonces $4 es en realidad más de €4 porque el IVA español no está incluido), o la regla "€4 solo se alcanza en proveedores sin SLA ni cumplimiento" queda desmentida por DO. Marcado para juicio humano, no auto-resuelto. Lo que sí es firme: **DigitalOcean no cumple el presupuesto de MyOwnClone**, ni a su entrada (512 MiB) ni en el plan que serviría el stack ($12).

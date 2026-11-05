---
id: 2026-1026-heroku-performance-de-250-a-1500-dolares-con-autoscaling
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-pricing.md, sources/2026-10-25-heroku-dyno-sizes.md]
links: ["[[2026-1026-heroku-dyno-units-25-dolares-por-unidad-excepto-performance]]", "[[2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados]]", "[[2026-1022-precio-99-mensual]]"]
---

## Claim
La familia **Performance** de dynos Cedar va de **$250/mes (Performance-M)** a **$1,500/mes (Performance-2XL)**, con **precio, RAM, compute y Dyno Units escalando en cuatro escalones declarados**: Performance-M **$250 / 2.5 GB / 12x / 8 DU**, Performance-L **$500 / 14 GB / 50x / 16 DU**, Performance-L-RAM **$500 / 30 GB / 24x / 16 DU**, Performance-XL **$750 / 62 GB / 50x / 30 DU**, Performance-2XL **$1,500 / 126 GB / 100x / 60 DU**. Todos declaran "Includes all Standard features", "**Predictable performance for your highest traffic applications**", "**Dedicated compute resources**", "**Autoscaling**" y "**Can mix with Standard dynos**".

## Why It Matters
Es el **salto de precio del PaaS cuando se pide capacidad real**: de Standard-2X ($50) a Performance-M ($250) hay un **×5** para pasar de 1 GB/2x-8x a 2.5 GB/12x y de 2 a 8 Dyno Units. La económica del PaaS gestionado no es lineal en la capacidad: el primer tramo (Eco, Basic, Standard) es barato por diseño y el tramo "bueno" cuesta **cinco veces más** que el anterior.
Para el modelo de coste del vault esto importa por dos razones. La primera, la de [[2026-1022-precio-99-mensual]]: un solo dyno Performance-M a $250/mes **supera el precio base de 99/mes del producto** por sí solo, así que cualquier arquitectura sobre Performance es incompatible con ese precio sin multiplicar tenants. La segunda, la de [[2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados]]: el patrón "el dedicado se paga con prima" reaparece aquí en forma de **+25 % por Dyno Unit** y en forma de **×5 en el primer salto a Performance**.
El dato que más pesa para el vault es **"Can mix with Standard dynos"**: Heroku permite una app multi-proceso con dynos de gamas distintas conviviendo, lo que hace el "tier" una decisión por process type, no por aplicación.

## Nota de extensión 2026-10-26
Fuente adicional: `sources/2026-10-25-heroku-dyno-sizes.md` (página "Technical Specifications by Dyno Size"). La tabla de specs **confirma** los cinco niveles y sus Dyno Units (M 8, L 16, L-RAM 16, XL 30, 2XL 60) y añade tres columnas que la captura de precios no traía: **"CPU Share"** (100 % en toda la familia Performance, frente a "1x" en Eco/Basic/Standard-1X y "2x" en Standard-2X), **"Compute"** (M 12x, L 50x, L-RAM 24x, XL 50x, 2XL 100x) y **"Dedicated: Yes"** — la única familia de la tabla con esa columna marcada. Es decir, la afirmación "Dedicated compute resources" del catálogo de tiers **se confirma a nivel de fila técnica**, no solo de copy. Ver [[2026-1026-heroku-cedar-cpu-share-compute-y-columna-dedicated]].
La misma página añade la restricción de acceso que el catálogo de tiers no recogía: "**We limit access to Performance dynos to customers with an established payment history**", enunciada dos veces (en "Dynos in Cedar" y en "Pricing and Billing"). Detalle en [[2026-1026-heroku-espacios-privados-de-cedar-y-de-fir-y-acceso-restringido]].

---
id: 2026-1026-heroku-dyno-units-25-dolares-por-unidad-excepto-performance
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-pricing.md, sources/2026-10-25-heroku-dyno-sizes.md]
links: ["[[2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados]]", "[[2026-1024-buyvm-comparativa-precios-15-al-mes-contra-aws-do-linode-y-vultr]]", "[[2026-1026-heroku-suelo-5-dolares-eco-con-sleep-y-7-dolares-basic-always-on]]"]
---

## Claim
Heroku mide la capacidad de un dyno en **"Dyno Units / Month"**, y el precio por unidad es **casi constante en todo el catálogo**: **$25 por Dyno Unit** en Basic ($7 / 0.28 DU), Standard-1X ($25 / 1 DU), Standard-2X ($50 / 2 DU), Performance-XL ($750 / 30 DU), Performance-2XL ($1,500 / 60 DU), Private-S ($125 / 5 DU), Private-M ($250 / 10 DU), Private-L ($500 / 20 DU), Private-XL ($750 / 30 DU), Private-2XL ($1,500 / 60 DU), Shield-S ($150 / 6 DU), Shield-M ($300 / 12 DU), Shield-L ($600 / 24 DU), Shield-XL ($900 / 36 DU) y Shield-2XL ($1,800 / 72 DU). La **única excepción** es la familia Performance en sus tres primeros tamaños: **Performance-M $250 / 8 DU = $31.25**, **Performance-L $500 / 16 DU = $31.25** y **Performance-L-RAM $500 / 16 DU = $31.25**, es decir un **+25 %** sobre el precio base por unidad.

## Why It Matters
Es un caso raro y útil: **el PaaS publica una unidad de capacidad explícita** (el Dyno Unit) donde el tramo VPS barato del vault solo publica GHz, cores o vCPU fraccionales — y ninguna de esas unidades es comparable entre proveedores ([[2026-1024-buyvm-comparativa-precios-15-al-mes-contra-aws-do-linode-y-vultr]]). Con una unidad común, "subir de tier" se puede razonar como un multiplicador de precio limpio: **casi todo el catálogo cuesta lo mismo por Dyno Unit**, lo que hace el tier casi irrelevante para el precio y deja el coste en función de la cantidad de unidades.
Y la excepción es exactamente donde está el salto: **Performance cuesta un 25 % más por unidad** en M y L — el mismo patrón de "el dedicado se paga con prima" que el vault ya vio en Hetzner (+€37,00, ×6.70, de compartido a dedicado en [[2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados]]), pero aquí la prima es de un cuarto, no de un múltiplo.

## Nota de verificación
Los $25 y $31.25 por Dyno Unit son **cálculo de este átomo** a partir de las dos columnas que publica la tabla (precio y Dyno Units / Month); la fuente no publica un precio unitario. Eco no declara Dyno Units, por lo que queda fuera del cálculo.

## Nota de extensión 2026-10-26
Fuente adicional: `sources/2026-10-25-heroku-dyno-sizes.md` (página "Technical Specifications by Dyno Size"). Esta captura **confirma** los valores ya registrados (Basic 0,28 DU, Standard-1X 1, Standard-2X 2, Performance-XL 30, Performance-2XL 60, Private-S 5, Shield-S 6, Shield-2XL 72) y añade **la columna de compute ausente en la captura de precios**: Eco/Basic/Standard-1X "1x-4x", Standard-2X "2x-8x", Performance-M "12x", Performance-L "50x", Performance-L-RAM "24x", Performance-XL "50x", Performance-2XL "100x", Private-S/M "12x", Shield-S/M "12x". Confirma además que el precio por Dyno Unit de **Private y Shield es $25 exacto** (5→$125, 6→$150, 10→$250, 12→$300, 20→$500, 24→$600, 30→$750, 36→$900, 60→$1,500, 72→$1,800).
**Pero añade una segunda excepción a la casi-constancia de $25**: la tabla **Fir** de esta captura publica Dyno Units que no respetan el múltiplo de $25 en General Purpose — `dyno-1c-4gb` $80/3 DU = **$26.67**, `dyno-2c-8gb` $160/6 DU = **$26.67**, `dyno-4c-16gb` $320/13 DU = **$24.62**, `dyno-8c-32gb` $640/26 DU = **$24.62**; el resto de Fir (Classic, Compute, Memory) y `dyno-16c-64gb` ($1,200/48) sí cae en $25 exacto. El patrón completo está en [[2026-1026-heroku-fir-cuatro-familias-con-4-2-y-8-gb-de-ram-por-vcpu]], que lo marca como fricción abierta.

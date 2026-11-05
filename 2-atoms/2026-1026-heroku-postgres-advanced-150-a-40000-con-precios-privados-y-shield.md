---
id: 2026-1026-heroku-postgres-advanced-150-a-40000-con-precios-privados-y-shield
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-pricing.md]
links: ["[[2026-1026-heroku-postgres-standard-50-a-12000-con-dedicado-y-1-hora-de-parada]]", "[[2026-1026-heroku-private-y-shield-desde-125-y-150-dolares]]", "[[2026-1024-extravm-escalera-de-precios-14-planes-de-4-50-a-192]]"]
---

## Claim
El tier **Advanced** de Heroku Postgres publica **tres precios por plan** (columnas "Common Runtime", "Private", "Shield") y una tabla de **11 filas de 4 GB a 1,536 GB**: **4G-Performance $150 / $180 / $210** (2 vCPU, 4 GB, 400 conexiones), **8G $300 / $360 / $420** (2 vCPU, 8 GB, 800), **16G $500 / $600 / $700** (2 vCPU, 16 GB, 1.600), **32G $900 / $1,080 / $1,260** (4 vCPU, 32 GB, 3.200), **64G $1,600 / $1,920 / $2,240** (8 vCPU, 64 GB, 5.000), **128G $3,000 / $3,600 / $4,200** (16 vCPU, 128 GB, 5.000), **256G $5,000 / $6,000 / $7,000** (32 vCPU, 256 GB, 5.000), **384G $7,500 / $9,000 / $10,500** (48 vCPU, 384 GB, 5.000), **512G $10,000 / $12,000 / $14,000** (64 vCPU, 512 GB, 5.000), **768G $15,000 / $18,000 / $21,000** (96 vCPU, 768 GB, 5.000), **1536G-Performance $40,000 / $48,000 / $56,000** (192 vCPU, 1,536 GB, 5.000). Todos declaran "**Pay only for what you use**", "**Decoupled storage and compute**", "**First 100GB-mo storage is included for every cluster**", "**Zero-downtime scaling**", "Dedicated follower pools" y "High Availability (customer configurable)".

## Why It Matters
Es el **modelo de precio por uso** del vault documentado por primera vez en un proveedor grande: "Pay only for what you use" con **almacenamiento y cómputo desacoplados** y con los **primeros 100 GB-mes de almacenamiento incluidos por clúster**. Eso rompe con el modelo de las tablas Classic, donde el disco viene atado al plan — y es exactamente la diferencia entre "pagar por lo que usas" y "pagar por el plan más grande que necesitas", el mismo eje que dividía a los proveedores del tramo VPS entre storage como producto aparte y storage incluido ([[2026-1024-extravm-escalera-de-precios-14-planes-de-4-50-a-192]]).
El dato estructural más útil para el vault es el **trío de precios en una sola fila**: Common / Private / Shield. La prima es **+20 % por Private y +40 % por Shield** sobre Common, constante en **todas** las once filas ($150→$180→$210; $3,000→$3,600→$4,200; $40,000→$48,000→$56,000). Es un número que el vault no tenía: **el aislamiento de red y el cumplimiento HIPAA/PCI tienen un precio percentual medible y uniforme**, no un sobrecoste opaco — y por tanto se puede incluir en un modelo de coste como un multiplicador en vez de como una línea misteriosa.
Y el techo del catálogo completo de datos de Heroku queda en **$56,000/mes** (1536G Shield), que es la cifra que hace evidente que **este proveedor no es opción para el producto del vault** en ningún tramo por encima de las decenas de dólares.

## Nota de verificación
Los porcentajes +20 %/+40 % y la lista de las once filas son lectura de las tres columnas de precio de la tabla. La fuente **no publica el precio del Private Space** ni el desglose de cómo se factura el uso ("pay only for what you use" sin unidades ni precios unitarios publicados).

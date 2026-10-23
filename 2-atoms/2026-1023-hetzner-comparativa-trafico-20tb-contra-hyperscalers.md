---
id: 2026-1023-hetzner-comparativa-trafico-20tb-contra-hyperscalers
type: atom
certainty: tentative
sources: [sources/2026-10-22-hetzner-cloud.md]
links: ["[[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1022-neon-postgres-serverless]]"]
---

## Claim
El comparador de tráfico de la propia página, con la perilla en **20 TB**, da: **AWS € 1.560,41/mo**, **Azure € 1.287,11/mo**, **Google € 1.326,61/mo** y **Hetzner € 0,00/mo**, con una cifra de "Average traffic cost savings with Hetzner" de **€ -4.785,64 /mes**. La página atribuye los datos a **sparecores.com** ("All figures are based on independent data from sparecores.com"). La aritmética de la tabla es internamente consistente —Hetzner a 0 frente a un mínimo de 1.287,11— pero la cifra de ahorro medio (4.785,64) es **mayor que cualquiera de las diferencias individuales** que la propia tabla muestra, de modo que el ahorro medio no se deriva de las tres cifras mostradas.

## Why It Matters
Es el argumento de venta más fuerte de Hetzner para un producto cuyo coste variable escala con el uso, y encaja con la lectura de coste marginal de [[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]: 20 TB de egreso inclusivos valen 0 € en Hetzner frente a más de 1.200 €/mes en los tres hyperscalers. Pero es una cifra **de marketing de proveedor con fuente externa no verificada en la captura**, y la inconsistencia aritmética del ahorro medio obliga a citarla con cautela. Para el vault importa porque fija el techo de la discusión sobre "cuándo un hyperscaler deja de ser la opción": con la base de datos ya en Neon serverless ([[2026-1022-neon-postgres-serverless]]), el egreso es la variable que decide si la infraestructura del producto se sostiene en un VPS propio a €5,99/mes o se infla al pasar a cloud de hiperescala.

## Nota de verificación
La captura no publica el desglose de los 4.785,64 € ni la metodología de sparecores.com, y no se puede contrastar ninguna de las tres cifras de hyperscaler contra la fuente original. El cero de Hetzner es coherente con los 20 TB inclusivos de [[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]].

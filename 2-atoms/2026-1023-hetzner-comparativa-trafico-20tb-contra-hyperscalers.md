---
id: 2026-1023-hetzner-comparativa-trafico-20tb-contra-hyperscalers
type: atom
certainty: tentative
sources: [sources/2026-10-22-hetzner-cloud.md, sources/2026-11-03-hetzner-cloud.md]
links: ["[[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1022-neon-postgres-serverless]]"]
---

## Claim
El comparador de tráfico de la propia página, con la perilla en **20 TB**, da: **AWS € 1.560,41/mo**, **Azure € 1.287,11/mo**, **Google € 1.326,61/mo** y **Hetzner € 0,00/mo**, con una cifra de "Average traffic cost savings with Hetzner" de **€ -4.785,64 /mes**. La página atribuye los datos a **sparecores.com** ("All figures are based on independent data from sparecores.com"). La aritmética de la tabla es internamente consistente —Hetzner a 0 frente a un mínimo de 1.287,11— pero la cifra de ahorro medio (4.785,64) es **mayor que cualquiera de las diferencias individuales** que la propia tabla muestra, de modo que el ahorro medio no se deriva de las tres cifras mostradas.

## Why It Matters
Es el argumento de venta más fuerte de Hetzner para un producto cuyo coste variable escala con el uso, y encaja con la lectura de coste marginal de [[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]: 20 TB de egreso inclusivos valen 0 € en Hetzner frente a más de 1.200 €/mes en los tres hyperscalers. Pero es una cifra **de marketing de proveedor con fuente externa no verificada en la captura**, y la inconsistencia aritmética del ahorro medio obliga a citarla con cautela. Para el vault importa porque fija el techo de la discusión sobre "cuándo un hyperscaler deja de ser la opción": con la base de datos ya en Neon serverless ([[2026-1022-neon-postgres-serverless]]), el egreso es la variable que decide si la infraestructura del producto se sostiene en un VPS propio a €5,99/mes o se infla al pasar a cloud de hiperescala.

## Nota de verificación
La captura no publica el desglose de los 4.785,64 € ni la metodología de sparecores.com, y no se puede contrastar ninguna de las tres cifras de hyperscaler contra la fuente original. El cero de Hetzner es coherente con los 20 TB inclusivos de [[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]].

## Nota de extensión 2026-11-03
Fuente: `sources/2026-10-31-hetzner-cloud.md`, `sources/2026-11-01-hetzner-cloud.md`, `sources/2026-11-02-hetzner-cloud.md`. Las cifras del comparador **han cambiado respecto a las de esta nota** y la captura del 2026-11-01 además **no renderiza el comparador en absoluto** (la sección "Data traffic in price comparison" aparece sin cifras ni valores de la perilla), lo que impide fechar el cambio. Con la perilla en 20 TB, el 2026-10-31 da AWS € 1.571,91/mo, Azure € 1.296,59/mo, Google € 1.336,39/mo, Hetzner € 0,00/mo y un ahorro medio de € -5.168,16/mes; el 2026-11-02 repite **las tres cifras de hyperscaler** pero baja el ahorro medio a **€ -4.434,41/mes**. La observación central de este átomo —que el ahorro medio **no se deriva** de las tres cifras mostradas— **se refuerza con las capturas nuevas**: los operandos constantes producen dos medias distintas separadas por € 733,75.

El conflicto con las cifras de esta nota se plantea, sin reescribirla, en [[2026-1102-hetzner-ahorro-medio-de-trafico-fluctua-entre-capturas]]. La conclusión operativa para el vault no cambia: el dato firme es el **€ 0,00/mo de Hetzner a 20 TB**, y las cifras de hyperscaler son de proveedor externo (sparecores.com), no verificadas en la fuente.

## 2026-11-03 — re-verificación
Fuente: `sources/2026-11-03-hetzner-cloud.md`. Cuarto juego de cifras del comparador, distinto de los tres anteriores: **AWS € 1.560,28/mo**, **Azure € 1.287,00/mo**, **Google € 1.326,50/mo**, **Hetzner € 0,00/mo** y un "Average traffic cost savings with Hetzner" de **€ -5.378,26/mes** — el valor más alto registrado. La atribución a **sparecores.com** se mantiene literal en la página. La observación central de este átomo —que el ahorro medio **no se deriva** de las tres cifras mostradas— **se refuerza una vez más**: con los operandos de esta captura, el ahorro medio supera con creces la media de las tres diferencias. Lo que esta captura añade es que **los propios operandos de hyperscaler han vuelto a moverse** (el 10-31 y el 11-02 compartían juego; el 11-03 trae otro, casi de vuelta al del 10-22), de modo que el widget recalcula el conjunto completo en cada visita. El dato firme del vault —**Hetzner € 0,00/mo a 20 TB frente a más de €1.280/mes en los tres hyperscalers**— no se ve afectado. Ver [[2026-1102-hetzner-ahorro-medio-de-trafico-fluctua-entre-capturas]] y [[2026-1103-hetzner-cinco-capturas-estabilidad-catalogo-vs-widgets-dinamicos]].

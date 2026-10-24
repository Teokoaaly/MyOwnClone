---
id: 2026-1024-evoxt-geekbench-5-multi-core-scores
type: atom
certainty: solid
sources: [sources/2026-10-23-evoxt-vps-pricing.md]
links: ["[[2026-1024-evoxt-cpu-6-ghz-y-comparativa-de-single-core]]", "[[2026-1024-evoxt-escalera-de-precios-nueve-planes]]", "[[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]", "[[2026-1024-evoxt-dos-precios-distintos-para-el-mismo-plan]]"]
---

## Claim
La tabla "Benchmark Score" de Evoxt publica **GeekBench 5 Multi Core Score** por plan: **VM-0.75 → 1073**, **VM-1 → 1098**, **VM-2 → 1940**, **VM-4 → 3306**, **VM-8 → 5265**, con la nota *"Benchmark score are based on Geekbench 5"*. La escala es **sublineal**: de 1 a 8 vCore (×8) el score solo sube ×4,90 (de 1073 a 5265). Y **más vCore no aporta casi nada al principio**: VM-0.75 (1 vCore) y VM-1 (1 vCore) apenas se distinguen (+25 puntos, +2,3 %).

## Why It Matters
Es la **primera evidencia de rendimiento medible** que el vault tiene de Evoxt, y corrige el vacío que había dejado la comparativa de GHz: el átomo de la home señalaba que la página no publicaba los resultados del benchmark del VM-1 ([[2026-1024-evoxt-cpu-6-ghz-y-comparativa-de-single-core]]), y esta página de precios sí los publica. La implication operativa es doble: por un lado, el argumento de "rendimiento de un solo núcleo" es coherente con el dato (1 vCore da casi todo el score), lo que encaja con el criterio de compra del vault —previsibilidad y recurso acotado antes que potencia bruta ([[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]])—; por otro, doblar vCore a partir de 1 no compra casi nada medible, así que el recurso a dimensionar es la **RAM**, coherente con la escalera de precios ([[2026-1024-evoxt-escalera-de-precios-nueve-planes]]). Ojo: la tabla que contiene los scores es también la que duplica los precios con valores distintos ([[2026-1024-evoxt-dos-precios-distintos-para-el-mismo-plan]]), así que el score por euro solo es calculable con la tabla de precios correcta, no con la de esta tabla.

## Nota de verificación
Los cinco scores están transcritos literalmente. La captura **no** publica el modelo de CPU, la versión del kernel, la fecha del benchmark, ni el score single-core; los ratios (×4,90, +2,3 %) son aritmética sobre los valores publicados, no cifras de la fuente.

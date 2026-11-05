---
id: 2026-1029-render-keyvalue-tabla-real
type: atom
certainty: solid
sources: [sources/2026-10-29-render-pricing.md]
links: ["[[2026-1029-render-keyvalue-pricing]]", "[[2026-1029-render-postgres-pricing]]", "[[2026-1029-render-compute-services-workers]]"]
---

## Claim
La tabla real de Key Value (Redis-compatible) de Render es: Free $0/mes con 25 MB RAM, 50 conexiones, sin persistencia; Standard CPU $10/mes (256 MB, 256 MB storage, 200 conexiones), $20/mes (1 GB), $60/mes (3 GB, 3.000 conexiones), $100/mes (5 GB, 5.000 conexiones), $200/mes (10 GB, 10.000 conexiones); High CPU $350/mes (20 GB), $600/mes (40 GB) y $750/mes (50 GB RAM, 50 GB storage, 50.000 conexiones). El techo del producto es 50 GB de RAM.

## Why It Matters
Es la escalera que hay que usar para el cache de MyOwnClone (Redis junto a Postgres y Weaviate): la instancia pagada más barata son $10/mes y el máximo publicado son $750/mes con 50 GB, muy por debajo del techo de $11.000/mes de la tabla de Postgres ([[2026-1029-render-postgres-pricing]]). Al igual que el cómputo ([[2026-1029-render-compute-services-workers]]), ninguna de estas cifras cabe en el presupuesto de ≤ 4 EUR/mes: incluso la instancia Standard de $10 supera ese suelo, de modo que el único Redis posible en Render es el gratuito de 25 MB — suficiente para cachear resultados de búsqueda pero no para colas ni para estado de sesión de un clon.

## [FRICTION]
> [[2026-1029-render-keyvalue-pricing]] afirma que Key Value llega hasta "$9,000/mo (50 GB RAM, 768 GB storage, 50,000 connections)" y que la persistencia en disco cuesta "$0.25 per GB per month". La tabla de Key Value de la captura sitúa el máximo en $750/mes con 50 GB RAM y 50 GB de storage, y el $0,25/GB/mes corresponde a los persistent disks de los servicios, no a Key Value. Ambas no pueden ser completamente correctas: el $9.000 con 768 GB de storage pertenece a una fila de la tabla de Postgres. Marcado para juicio humano, no auto-resuelto.

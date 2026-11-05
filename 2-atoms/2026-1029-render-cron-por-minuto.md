---
id: 2026-1029-render-cron-por-minuto
type: atom
certainty: solid
sources: [sources/2026-10-29-render-pricing.md]
links: ["[[2026-1029-render-compute-per-second]]", "[[2026-1029-render-compute-services-workers]]", "[[2026-1022-gap-workflows-myownclone]]"]
---

## Claim
Los Cron Jobs de Render se tarifan por minuto de ejecución, no por mes: $0,00016/minuto en la instancia 0.5c-512mb, $0,00058/minuto en 1c-2g, $0,00197/minuto en 2c-4g, $0,00405/minuto en 4c-8g y $0,02315/minuto en 8c-64g; el techo del producto es 8 CPU y 64 GB de RAM.

## Why It Matters
Es la línea de coste más barata de todo Render para trabajo programado: 1.440 minutos mensuales en la instancia mínima dan ~$0,23/mes, y una tarea diaria de un minuto en la instancia de 8 CPU/64 GB costaría ~$0,69/mes. Para MyOwnClone esto importa en un sitio concreto: los jobs de mantenimiento (limpieza de tenants caducados, reindexado de Weaviate, tareas de billing) no justifican un servicio permanente, y el cron por minuto evita mantener un worker vivo solo para eso. También marca el límite del modelo: Render no tiene un primitive de workflow durable como el que [[2026-1022-gap-workflows-myownclone]] identifica como gap de producto en MyOwnClone, así que la orquestación de pasos con estado quedaría fuera de Render.

## [FRICTION]
> [[2026-1029-render-compute-per-second]] afirma que el cómputo se prorratea al segundo y que ese criterio se aplica también a Cron Jobs. La tabla de Cron Jobs de la misma captura está expresada en $/minuto. Ambas no pueden ser completamente correctas: o la unidad de la tabla es solo informativa y el prorrateo real es al segundo, o el cron se factura en fracciones de minuto. Marcado para juicio humano, no auto-resuelto.

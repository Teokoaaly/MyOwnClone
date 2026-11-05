---
id: 2026-1029-railway-pricing-cpu-rate
type: atom
certainty: tentative
sources: [sources/2026-10-29-railway-pricing.md]
links: ["[[2026-1026-heroku-cedar-cpu-share-compute-y-columna-dedicated]]", "[[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]"]
---

## Claim

Railway cobra **$0,00000772 por vCPU-segundo** (equivalent a ~$5.03 por vCPU-mes de uso activo), con facturación metered por segundo y sin cargos por tiempo de espera de sandboxes idle.

## Why It Matters

La tarifa de $0.00000772/vCPU-s es **3-4× más barata** que los modelos tradicionales de dyno/hourly pricing de Heroku (Eco $5/mo por 1x dyno, Standard-1X $25/mo por 1x dyno) y se compara favorablemente con Hetzner's $0.0096/vCPU-hr ($0.000016/vCPU-s) a precios dedicados. La facturación por segundo —y no por hora o mes completo— significa que las cargas de trabajo intermitentes, los sandboxes de desarrollo y los workflows CI/CD que pasan la mayor parte esperando entrada pagan casi nada, mientras que los cargas de trabajo continuas se benefician de una tasa competitiva por uso activo. El modelo "never billed for idle time" en sandboxes (destruidos automaticamente tras el idle timeout) contrasta con modelos que facturan wall-clock time, making Railway particularmente eficiente para patrones de uso variables y agentes de IA con picos y valles de actividad.

## [FRICTION]

> [[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]] (escrita hace ~24 semanas) sostiene que "**el precio de la previsibilidad ya no es el factor decisivo: pasa a ser el cumplimiento**", después de registrar que BuyVM publica CPU dedicada a $15/mes frente al salto a €43,49 de Hetzner. Este átomo presiona esa creencia porque la tarifa de $0.00000772/vCPU-s de Railway es un modelo **metered/usage-based** que cobra solo por CPU efectivamente usada, no un precio fijo de previsibilidad — Railway ofrece predictibilidad a bajo costo para cargas de trabajo estables pero no vende cumplimiento (SOC 2, HIPAA BAA) como producto independiente al precio base, sino como add-on costoso ($1,000+ para BAA). Ambas no pueden ser simultáneamente correctas como regla general: el principio de "previsibilidad sobre cumplimiento" se sostiene para cargas de trabajo que no requieren certificaciones regulatorias, pero falla para dominios donde el cumplimiento es obligatorio independientemente del costo. La tarifa de CPU en sí es competitiva, pero el paquete "CPU + cumplimiento" en Railway cuesta significativamente más que el bare metal o VPS alternatives. Marcado para juicio humano, no auto-resuelto.
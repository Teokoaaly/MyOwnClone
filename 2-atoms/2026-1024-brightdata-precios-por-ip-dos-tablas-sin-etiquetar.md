---
id: 2026-1024-brightdata-precios-por-ip-dos-tablas-sin-etiquetar
type: atom
certainty: tentative
sources: [sources/2026-10-24-brightdata-proxy-pricing.md]
links: ["[[2026-1024-brightdata-cuatro-tipos-de-red-y-solo-tres-pestanas-de-precio]]", "[[2026-1024-brightdata-payg-a-4-por-gb-sin-compromiso]]", "[[2026-1024-dataimpulse-cuatro-tipos-y-que-cada-uno-resuelve]]"]
---

## Claim
La página contiene **dos tablas de precio por IP con las mismas etiquetas de plan** ("Perfect for small businesses with moderate usage", "Tailored for teams looking to scale their operations", etc.) y todas "Billed monthly", pero con precios distintos:

| IPs | Tabla A | Tabla B |
|---|---|---|
| 10 | **$1.8/IP** → $18 | **$1.40/IP** → $14 |
| 100 | **$1.45/IP** → $145 | **$1.00/IP** → $100 |
| 500 | **$1.40/IP** → $700 | **$0.95/IP** → $475 |
| 1000 | **$1.30/IP** → $1.300 | **$0.90/IP** → $900 |

La captura **no dice a qué producto pertenece cada tabla**.

## Why It Matters
La plausibilidad es que una tabla sea la de proxies **ISP** (IPs estáticas, permanentes, no rotativas) y la otra la de **datacenter**, porque las pestañas de la página son *Residential proxies | ISP proxies | Datacenter proxies* y la de residential es la que se mide por GB ([[2026-1024-brightdata-cuatro-tipos-de-red-y-solo-tres-pestanas-de-precio]]). Si eso es así, **la diferencia entre las dos es del 28,6 % en el escalón de 10 IPs y del 44,4 % en el de 1.000 IPs** — y la elección entre "IP fija de ISP" y "IP fija de datacenter" es exactamente la decisión que un flujo de una-IP-por-cuenta tiene que tomar, porque de ella depende que la sesión sobreviva a la verificación ([[2026-1024-dataimpulse-cuatro-tipos-y-que-cada-uno-resuelve]]).
Pero **la captura no lo dice** y no se puede asignar con certeza: por eso el átomo queda en `tentative`. Un plan de coste que cite "$1,8/IP" o "$0,90/IP" sin nombrar el producto sería una cifra sin unidad.

## Nota de verificación
Cifras transcritas literalmente. La captura **no** publica la etiqueta de producto de cada tabla, ni la duración del contrato mensual de las IPs, ni si la IP se puede rotar, ni si el precio por IP incluye ancho de banda ilimitado o una cuota de MB.

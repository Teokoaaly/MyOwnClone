---
id: 2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra
type: atom
certainty: solid
sources: [sources/2026-10-22-hetzner-cloud.md, sources/2026-10-23-skhron-bitcoin-vps.md]
links: ["[[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]", "[[2026-1023-hetzner-comparativa-trafico-20tb-contra-hyperscalers]]", "[[2026-1023-hetzner-facturacion-por-hora-0-0096]]"]
---

## Claim
La calculadora de Hetzner Cloud incluye **20 TB de tráfico de salida** en el plan base: "20 TB inclusive. For each additional TB, we charge **€ 1.00** in the EU." El selector de tráfico esperado arranca en 20 TB y el recargo por TB adicional está explícitamente limitado a la UE. En la configuración por defecto el coste estimado de tráfico es **€ 0.00**.

## Why It Matters
Fija el coste marginal del egreso, que es la partida que en los hyperscalers dispara las facturas (ver [[2026-1023-hetzner-comparativa-trafico-20tb-contra-hyperscalers]]): a €1.00 por TB extra en la UE, el egreso es barato pero **no es infinitamente barato**, así que un producto que genere vídeo, audio o archivos de cliente paga un recargo lineal por cada TB. Para una arquitectura de producto que guarda conocimiento y sirve respuestas de clon, el volumen de egreso es una variable de diseño y no un accidente: mover tráfico a una CDN o a una región de la UE son palancas de coste directo. Y este recargo se suma a la base del servidor ([[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]), que a su vez se puede facturar por hora ([[2026-1023-hetzner-facturacion-por-hora-0-0096]]).

## Nota de verificación
La captura no publica el precio del tráfico adicional fuera de la UE, ni si los 20 TB son por servidor o por cuenta, ni la política de abuso. No se afirma ninguno de esos datos.

## [NOTA 2026-10-24 — Skhron]
Fuente: `sources/2026-10-23-skhron-bitcoin-vps.md`. Skhron usa un **modelo de contabilidad de tráfico distinto**: en cada plan se lee literalmente "**Sum of inbound and outbound traffic is accounted**", con volúmenes incluidos de **1 TiB a 64 TiB** según el plan (1, 2, 2,5, 4, 5, 8, 10, 16, 20, 32 y 64 TiB) y uplink de 1 Gbps compartido (línea XSIG, Intel Xeon) o 5 Gbps compartido (línea ER, AMD EPYC) (ver [[2026-1024-skhron-trafico-contado-en-dos-sentidos]]). La consecuencia práctica: **1 TiB "incluido" en Skhron equivale a ~0,5 TiB de egreso real** si el servidor también recibe tráfico, de modo que **las cifras de los dos proveedores no son comparables sin normalizar**. Además, Skhron **no publica el precio del tráfico adicional ni el umbral de corte**, lo que hace su modelo de egreso peor documentado que el de Hetzner (€1,00/TB extra) pese a estar más barato por servidor.

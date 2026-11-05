---
id: 2026-1103-assemblyai-columna-custom-tercer-escalon-de-precios
type: atom
certainty: solid
sources: [sources/2026-11-03-assemblyai-pricing.md]
links: ["[[2026-1102-assemblyai-concurrencia-streaming-100-sesiones-por-minuto]]", "[[2026-1102-assemblyai-facturacion-mensual-sin-minimos-ni-contratos]]", "[[2026-1101-assemblyai-tarifas-por-hora-no-por-minuto]]"]
---

## Claim
La tabla de modelos del Pre-recorded Speech-to-Text tiene **tres columnas, no dos**: "Models", "Pay as you go" y **"Custom"**. La celda Custom de **Universal-3.5 Pro** dice "Get custom rate limits, enhanced concurrency, and enterprise-grade flexibility tailored to your AI workloads. Contact us", la celda Custom de **Universal-2 queda vacía**, y el mismo texto "Custom — Get custom rate limits, enhanced concurrency, and enterprise-grade flexibility tailored to your AI workloads. / Contact us" se repite como bloque suelto fuera de la tabla. **El tier Custom no publica ninguna tarifa**: su única monetizeización es el formulario "Contact us", y lo que se ofrece en él no es un precio sino tres palancas — rate limits, concurrencia y flexibilidad enterprise.

## Why It Matters
Es la pieza que cierra la geometría de precios de AssemblyAI: hay un **suelo público** ($0,15/hr de Universal-2, ver [[2026-1101-assemblyai-tarifas-por-hora-no-por-minuto]]) y un **techo sin cifra** que solo se negocia. Para el vault esto importa por dos razones. Primera: la palabra "enterprise" de esa celda es exactamente la palanca que [[2026-1102-assemblyai-facturacion-mensual-sin-minimos-ni-contratos]] ya registró como la única vía para descuentos por volumen ("custom pricing for customers with high-volume usage"), así que **el tier Custom es también la vía oculta de descuento**: cualquier proyección de coste a volumen en el vault tiene que modelar el precio de lista, porque el precio Custom no es calculable. Segunda: "enhanced concurrency" aparece en la columna Custom como una concesión comercial, lo que separa conceptualmente la concurrencia **gratuita y autosescalable** (el mecanismo documentado en [[2026-1102-assemblyai-concurrencia-streaming-100-sesiones-por-minuto]]) de la concurrencia **negociada**: una es el derecho por defecto del plan pay-as-you-go, la otra es un argumento de venta. Para un clon de voz que necesita llamadas simultáneas, la pregunta operativa pasa a ser si la concurrencia gratis de lista (100 sesiones/min) basta o si hay que abrir negociación enterprise, que arrastra también rate limits a medida.

## [FRICTION]
> [[2026-1102-assemblyai-concurrencia-streaming-100-sesiones-por-minuto]] (escrita hace ~1 día) afirma, citando la FAQ de la página, que "Los límites de partida personalizados por encima de 100 también están disponibles 'at no additional cost'" — es decir, que superar las 100 sesiones/min no cuesta dinero y no requiere contrato.
> La tabla de modelos de la misma página ofrece en cambio "enhanced concurrency" dentro de la **columna Custom**, que solo se obtiene vía "Contact us" y arrastra "custom rate limits" y "enterprise-grade flexibility". Ambas cosas no pueden ser la misma vía: o la ampliación de concurrencia es gratuita y sin papeleo, o es una concesión que se negocia (aunque sea sin coste explícito, sigue siendo un acuerdo con ventas y no un derecho de lista). Marcado para juicio humano, no auto-resuelto.

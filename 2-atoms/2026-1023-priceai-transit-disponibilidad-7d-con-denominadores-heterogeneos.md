---
id: 2026-1023-priceai-transit-disponibilidad-7d-con-denominadores-heterogeneos
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-api-transit.md]
links: ["[[2026-1023-priceai-transit-precio-y-estabilidad-desacoplados]]", "[[2026-1023-priceai-descargo-de-responsabilidad-sin-sla]]", "[[2026-1023-priceai-transit-cobertura-parcial-y-criterio-de-ranking]]"]
---

## Claim
La columna **"近 7 日可用率"** (disponibilidad de los últimos 7 días) se declara como **"可用率为近 7 日公开监测样本"** — un porcentaje de **muestra de monitorización pública**, no un SLA. La tabla mezcla **dos denominadores distintos** en la misma columna:

- **"样本 N"** (nº de muestras) en 25 filas, con N entre **60** (星链AI) y **1320** (HubCore); ejemplos: 星链AI **100.0%** (样本 60), HubCore **99.8%** (样本 1320), 無忧 Ai **99.1%** (样本 360), 贝贝 **73.9%** (样本 600).
- **"24h 请求 N万"** (volumen de peticiones en 24 h) en 5 filas: RelayCore **93.4%** (24h 请求 41.8万), tokenshop **98.5%** (39.4万), 贝贝 **73.9%** (11.4万), TokenFree **88.2%** (1.8万), AL-API **87.4%** (1.8万).

## Why It Matters
El vault no puede comparar dos números de esta columna sin mirar el denominador: **100.0% con 60 muestras y 99.8% con 1320 no son la misma evidencia**, y el percentil de error es radicalmente distinto. Mezclar ambos formatos en una sola columna es exactamente el tipo de incomparablez que ya se detectó en las unidades de cuota de la vista oficial ([[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]]).
Subrayado por el propio sitio: **"可用率" no es SLA** — la página no promete disponibilidad ni respalda canales, y los canales de bajo precio pueden tener rate limiting, colas o retirada de modelos ([[2026-1023-priceai-descargo-de-responsabilidad-sin-sla]]). Es un indicador de **observación pública**, útil como señal de riesgo, no como compromiso contractual.
Para el back-office del vault esto importa en los dos sentidos: si alguna vez se compra capacidad a un relay, esta columna es el proxy disponible para el riesgo de caída, y es un proxy con fecha de captura (2026-10-23) que caduca.

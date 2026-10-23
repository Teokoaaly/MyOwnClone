---
id: 2026-1023-priceai-token-plan-como-categoria-producto
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-official-api.md]
links: ["[[2026-1023-priceai-suscripcion-no-es-api-token]]", "[[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]]", "[[2026-1023-priceai-alibaba-coding-plan-50-usd]]"]
---

## Claim
"Coding Plan" y "Token Plan" son **categorías de producto**, no nombres de proveedor: la captura las usa como los dos tipos de fila de la vista de suscripciones, y cada proveedor les da nombre propio — Tencent TokenHub **Coding Plan**, Alibaba Model Studio **Coding Plan**, Alibaba Bailian **Token Plan** (个人版 Lite), StepFun **Step Plan**, OpenCode **Go**. Los dos elementos comunes de la categoría son (a) **pago mensual fijo** y (b) **cuota con ventana de tiempo (5 h / semana / mes o 7 días)** en lugar de precio por token.

## Why It Matters
Es una categoría de producto hecha para **el caso de uso de agentes de código**, no para el consumo de API en general: el presupuesto se fija por mes y se gasta en ventanas cortas, con la idea de que un programador agota el cupo en ráfagas de horas y lo ve reponer cada 5 horas o cada semana.
Para el vault, esto importa porque es exactamente el perfil de carga de un producto de inferencia con Dify ([[2026-1022-gap-dify-como-capa-inferencia-prompts]]): si el producto factura por uso a un tenant ([[2026-1022-costes-por-categoria-tenant]]), su propio consumo tiene una componente fija (suscripción) y otra variable (API por token), y el razonamiento de margen es el mismo en ambas ([[2026-1023-priceai-suscripcion-no-es-api-token]]).
El riesgo estructural de esta categoría es el que la propia página señala: cuota, cobertura y límites cambian entre proveedores sin aviso, y en el caso de Qwen la cobertura es una preview que puede desaparecer ([[2026-1023-priceai-qwen-token-plan-credits-5h-y-7d]]).

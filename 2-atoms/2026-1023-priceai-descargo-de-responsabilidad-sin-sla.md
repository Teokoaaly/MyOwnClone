---
id: 2026-1023-priceai-descargo-de-responsabilidad-sin-sla
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-official-api.md]
links: ["[[2026-1023-priceai-catalogo-ocho-canales-y-fecha-de-tipo-de-cambio]]", "[[2026-1023-priceai-suscripcion-no-es-api-token]]", "[[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]]"]
---

## Claim
El descargo de PriceAI sobre su catálogo es literal: **"PriceAI 只整理公开文档和公开页面中的 API 渠道信息，不售卖 API，不承诺可用性，不替任何渠道提供 SLA"** — solo compila información de documentos y páginas públicas de canales de API, **no vende API, no promete disponibilidad y no ofrece SLA por ningún canal**. Y añade: **"免费和低价渠道可能存在限流、排队、模型下线、地区限制或条款变化"** — los canales gratuitos y de bajo precio pueden tener rate limiting, colas, retirada de modelos, **restricciones regionales** o cambios de términos.

## Why It Matters
Fija el estatuto probatorio de toda la tabla: es un **catálogo de terceros sin garantía**, no un contrato. La consecuencia operativa es que ninguna de las cifras de esta fuente puede usarse como SLA ni como base de un compromiso de disponibilidad hacia un cliente.
La advertencia de **restricciones regionales** es el punto más relevante para el vault: un plan de $10/mes que cubre DeepSeek V4 o Qwen ([[2026-1023-priceai-opencode-go-10-usd-y-60-usd-al-mes]]) puede no ser accesible desde la misma geografía que la del usuario. Es un recordatorio de que el precio más bajo no es automáticamente el coste más bajo real.
En contraposición con la infraestructura del vault, que sí compra SLA explícito ([[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]]), queda claro que el nivel de garantía cae radicalmente al moverse de hosting a inferencia: una parte del coste se paga en incertidumbre.

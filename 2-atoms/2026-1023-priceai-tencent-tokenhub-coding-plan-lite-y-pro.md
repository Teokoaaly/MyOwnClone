---
id: 2026-1023-priceai-tencent-tokenhub-coding-plan-lite-y-pro
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-official-api.md]
links: ["[[2026-1023-priceai-alibaba-coding-plan-50-usd]]", "[[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]]", "[[2026-1023-priceai-suscripcion-no-es-api-token]]"]
---

## Claim
El **Coding Plan de Tencent Cloud TokenHub** tiene dos tramos en yuanes con cuota medida en **requests**:

| Plan | Precio | 5h | Semana | Mes |
| --- | --- | --- | --- | --- |
| Lite | 40 元/月 | 1,200 requests | 9,000 requests | 18,000 requests |
| Pro | 200 元/月 | 6,000 requests | 45,000 requests | 90,000 requests |

Cobertura (3 ítems): **GLM-5, Kimi K2.5, MiniMax M2.5**. Es decir, la suscripción de codificación de Tencent **no da modelos de Tencent**: da modelos de Zhipu, Moonshot y MiniMax sobre la nube de Tencent.

## Why It Matters
La observación estructural es que el "Coding Plan" chino es un **canal de distribución de modelos de terceros**, no el producto del proveedor de nube: Tencent factura la cuota, el acceso va a modelos de GLM, Kimi y MiniMax. El mismo patrón se repite en Alibaba Model Studio ([[2026-1023-priceai-alibaba-coding-plan-50-usd]]), donde la cuota es idéntica en requests pero los modelos son distintos.
Para el vault esto significa que la "capa de inferencia" puede apoyarse en suscripción de codificación china con cuota fija ([[2026-1022-gap-dify-como-capa-inferencia-prompts]]) — pero el límite es el mismo de todas las suscripciones ([[2026-1023-priceai-suscripcion-no-es-api-token]]): son canales de producto, no paquetes de tokens de API.

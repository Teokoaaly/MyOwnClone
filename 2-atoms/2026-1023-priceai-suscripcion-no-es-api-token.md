---
id: 2026-1023-priceai-suscripcion-no-es-api-token
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-official-api.md]
links: ["[[2026-1023-priceai-token-plan-como-categoria-producto]]", "[[2026-1023-priceai-chatgpt-plus-y-pro-precios-y-ventanas]]", "[[2026-1022-costes-por-categoria-tenant]]", "[[2026-1023-priceai-claude-pro-y-max-precios-y-ventanas]]"]
---

## Claim
El aviso de conversión de la propia página es explícito: **"ChatGPT、Claude、Gemini 的官方月订阅多是产品内额度，不等同 API token 包"** — la suscripción mensual oficial de ChatGPT, Claude o Gemini es sobre todo **cuota dentro del producto**, y **no equivale a un paquete de tokens de API**. Y un Coding Plan hay que leerlo en cinco dimensiones a la vez: **月费 (fee), 模型覆盖 (cobertura), 请求窗口 (ventana de requests), 额度刷新 (refresco de cuota) y 用途限制 (restricciones de uso)**.

## Why It Matters
Esta es la regla de lectura más importante de la fuente para el vault, porque el panel de costes de [[myownclone]] desglosa el gasto **por proveedor** (Anthropic + OpenAI) ([[2026-1022-costes-por-categoria-tenant]]) — es decir, un gasto que solo puede venir de consumo por token vía API, nunca de una suscripción de producto.
Por tanto: **una suscripción de ChatGPT Plus o Claude Pro no puede usarse como sustituto de la factura de API** del backend. Los números de [[2026-1023-priceai-chatgpt-plus-y-pro-precios-y-ventanas]] sirven como techo de referencia de "qué paga un usuario final por acceso a GPT", no como presupuesto de inferencia. Es la diferencia entre vender acceso (suscripción) y operar inferencia (API), y confundirlas es el error de coste más caro posible en este stack.

## [FRICTION]
> [[2026-1022-costes-por-categoria-tenant]] afirma que el panel de plataforma expone "un desglose por proveedor (Anthropic + OpenAI + email)" y que la separación entre coste facturable al tenant y coste absorbido por la plataforma "es la clave del modelo de margen".
> Este átomo presiona esa creencia en un punto concreto: el corte "por proveedor" del panel asume implícitamente que **todo** el gasto Anthropic y OpenAI es consumo medido por token y por tenant. La tabla de suscripciones muestra que existe una vía de pago fija para el mismo proveedor (Claude Pro $20/mes con $130/mes de cuota, [[2026-1023-priceai-claude-pro-y-max-precios-y-ventanas]]), que es un coste de plataforma *no asignable* a un tenant, o un coste asignable de forma distinta a como el panel lo modela hoy.
> Ambas no pueden ser completamente correctas: o el panel solo mide API por token —en cuyo caso omite cualquier coste fijo de suscripción que el vault pueda haber contratado— o incluye suscripciones y entonces la línea "Anthropic" mezcla coste variable facturable con coste fijo absorbido, y la atribución al tenant queda sobestimada. Marcado para juicio humano, no auto-resuelto.

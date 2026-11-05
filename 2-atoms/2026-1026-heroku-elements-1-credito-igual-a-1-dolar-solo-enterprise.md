---
id: 2026-1026-heroku-elements-1-credito-igual-a-1-dolar-solo-enterprise
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-pricing.md]
links: ["[[2026-1023-priceai-qwen-token-plan-credits-5h-y-7d]]", "[[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
La sección **"Elements Marketplace Add-on Services"** publica la regla de compra de add-ons con dos reglas explícitas. Primera: *"For Direct customers, Add-on pricing varies by Add-on and can be found in the Heroku Elements Marketplace"* — es decir, **cada add-on tiene su propio precio y no hay precio conjunto**. Segunda: *"For Enterprise customers, the Heroku Elements Marketplace uses **add-on credits**. **One credit equals $1** worth of any service"*. La página añade que el Marketplace ofrece "complex services, workflow tools, and deployable code" y que los add-ons se compran a través de [elements.heroku.com](https://elements.heroku.com/).

## Why It Matters
Es la **quinta unidad de crédito** documentada en el vault, y la primera con **tipo de cambio explícito**: **1 crédito = $1 de cualquier servicio**. Las otras son créditos con ventana temporal ([[2026-1023-priceai-qwen-token-plan-credits-5h-y-7d]]), o unidades sin conversión publicada (requests, prompts, consultas), que es exactamente la razón por la que el vault|no podía construir un ranking de coste por capacidad ([[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]]). Un crédito con paridad a dólar es **una unidad contable y no una cuota de uso**: se puede acumular, no caduca por ventana y se gasta en cualquier servicio.
La observación con más valor para el producto es la **asimetría entre clientes Direct y Enterprise**: el mismo Marketplace, con los mismos servicios, se factura de dos maneras — **precio por add-on** para el cliente directo y **bolsa de créditos** para el Enterprise. Eso es un **arbitraje de precio documentado**: comprar capacidad de infraestructura a través de créditos y venderla embebida en un producto es un modelo de reventa, y el vault ya sabe que la reventa es su mecanismo ([[2026-1023-priceai-patrocinadores-y-canales-de-reventa-con-multiplicador]]).
Y hay una consecuencia de alcance: **el crédito no es una suscripción de plataforma**. Si un tenant del producto consume, por ejemplo, un add-on de un tercero a través del Marketplace, ese coste **no entra en ninguna de las dos categorías del corte por categoría del vault** (respuestas de clon e ingestión, [[2026-1022-costes-por-categoria-tenant]]) porque es un coste de proveedor de servicio, no de cómputo ni de modelo. Es la tercera línea de coste de plataforma que el vault no tiene registrada.

## Nota de verificación
La página **no publica** el precio de ningún add-on concreto, ni el precio de los créditos, ni la vigencia o caducidad de los créditos. "One credit equals $1 worth of any service" es la formulación literal.

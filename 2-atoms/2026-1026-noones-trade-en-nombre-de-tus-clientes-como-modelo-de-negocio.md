---
id: 2026-1026-noones-trade-en-nombre-de-tus-clientes-como-modelo-de-negocio
type: atom
certainty: solid
sources: [sources/2026-10-25-noones-developer-api.md]
links: ["[[2026-1026-noones-acceso-delegado-app-instalada-por-el-usuario]]", "[[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]", "[[2026-1023-lzt-categoria-llm-accounts-para-reventa]]", "[[2026-1024-noones-publicar-ofertas-y-visa-virtual-exigen-id]]"]
---

## Claim
Uno de los cuatro bullets de cabecera de `dev.noones.com` es **"Trade on behalf of your clients"**, y la página promete que sus APIs permiten "grow your business". La frase es la declaración comercial explícita de un **modelo de negocio de terceros**: un integrador opera en nombre de una clientela, con el consentimiento del titular de cada cuenta, dentro de la plataforma NoOnes.

## Why It Matters
El vault ya tiene documentada la versión **no institucionalizada** de ese mismo negocio: el bot de registro masivo de cuentas de ChatGPT ([[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]) y la categoría `LLM Accounts` de lzt.market ([[2026-1023-lzt-categoria-llm-accounts-para-reventa]]), donde la reventa se paga por unidad y el vendedor asume el baneo. NoOnes ofrece la **versión con plataforma encima**: hay un mecanismo de consentimiento (el usuario instala la app y concede permiso) y hay una API. Eso cambia la pregunta de la thread de economía y verificación: el mercado de "operar cuentas ajenas" no es solo un mercado gris de reventa de inventario, también tiene una forma **API-first y consentida** que un proveedor de plataforma decide permitir. La pregunta operativa para el vault: si ese modelo es legítimo en el proveedor, ¿qué queda del lado oscuro —y qué es solo la versión artesanal—?

## [FRICTION]
> [[2026-1024-noones-publicar-ofertas-y-visa-virtual-exigen-id]] establece que en NoOnes **publicar ofertas exige ID verificado o Basic Verification**, y que la Visa virtual exige ID completo: es decir, el lado del mercado que *vende* está atado a identidad documentada por usuario.
> Este átomo presiona esa regla en un punto que la captura deja abierto: si una app de terceros "opera en nombre de sus clientes" y automatiza trading, la pregunta de **quién es el oferente de registro** —el usuario delegante que se verificó, o la app que publica en su nombre— no está respondida en ninguna parte de la captura, ni en los scopes, ni en los términos, ni en los límites por nivel ([[2026-1024-noones-tabla-de-limites-por-nivel]]).
> Ambas no pueden ser simultáneamente la lectura completa: o la identidad verificada del usuario es la que abre la capacidad de operar y la app es un simple ejecutor, o existe una capacidad de operar en nombre de terceros **sin** verificación individual del titular —y eso cambiaría el significado de toda la escalera L1→L3.
> Marcado para juicio humano, no auto-resuelto: la captura no publica scopes, niveles heredados ni exenciones.

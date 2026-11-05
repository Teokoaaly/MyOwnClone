---
id: 2026-1023-5sim-casos-de-uso-qa-y-privacidad
type: atom
certainty: solid
sources: [sources/2026-10-22-5sim-home.md]
links: ["[[2026-1022-auth-magic-link-codigo-seis-digitos]]", "[[2026-1022-auth-otp-impersonacion-30min]]", "[[synthetic-data-testing]]"]
---

## Claim
La home de 5sim enumera cinco usos declarados del número virtual de un solo uso: **privacidad** (registrarse sin compartir el número con marketers y data brokers), **viaje** (recibir SMS locales en el extranjero sin roaming ni SIM local), **desarrollo y QA** ("testing custom SMS scripts (OTP, notifications) by development teams in different markets"), **separación trabajo/vida** (un número aparte para anuncios, entregas y transacciones puntuales) y **confirmaciones temporales** (mensajes de una vez para servicios que se usan de forma esporádica). El flujo documentado es de tres pasos: login/registro → elegir país y servicio y obtener el número → usar el número para recibir el SMS → completar con el SMS.

## Why It Matters
El caso de **desarrollo y QA de OTP** es el que conecta este material con el vault: el producto propio autentica por magic link con código de 6 dígitos por email y además tiene OTP e impersonación de 30 minutos ([[2026-1022-auth-magic-link-codigo-seis-digitos]], [[2026-1022-auth-otp-impersonacion-30min]]). Los números virtuales son el sustituto de infraestructura que un equipo de QA usaría para probar flujos SMS en distintos mercados sin gastar SIMs reales — la misma lógica de *datos sintéticos antes de usuarios reales* que ya está registrada como método en [[synthetic-data-testing]].
El caso de "separación trabajo/vida" y el de "privacidad" explican además por qué este tipo de servicio tiene un mercado de consumo, no solo de QA: el número desechable es la unidad de la identidad verificada desechable.


## Nota de extensión 2026-10-26
La captura del 2026-10-25 de `https://5sim.net/en` (653 palabras) **reproduce los cinco casos de uso sin una palabra distinta**: "Privacy protection: register and log in to websites without sharing your phone number with marketers and data brokers", "Travel: receive SMS from local service abroad without roaming or purchasing a local SIM card", "Development and QA: testing custom SMS scripts (OTP, notifications) by development teams in different markets", "Separation of work and personal life: a separate phone number for ads, deliveries, and one-time transactions to avoid sharing your phone number with strangers", "Temporary confirmations: one-time SMS messages for services you use occasionally" ([[2026-1026-5sim-copy-de-marketing-identica-tres-dias-despues]]). El caso de QA, que es el que conecta con el producto del vault, sigue siendo el único que nombra **OTP** explícitamente.

**Lo que la re-captura sí añade es el paso cero del flujo, que el átomo original no recogía.** El apartado "How to receive an SMS using a virtual number" no empieza por "elegir país y servicio" sino por una instrucción textual previa: **"Start off by [Logging in](https://5sim.net/login) or [Signing up](https://5sim.net/signup)"**. Es decir, el proveedor **enlaza al login y al signup como el primer acto del flujo de compra**, con sus propias URL (`5sim.net/login`, `5sim.net/signup`), y solo después enumera los tres pasos. La consecuencia para el producto propio es directa: la friction de alta de MyOwnClone es precisamente **una cuenta con correo real y código de 6 dígitos** ([[2026-1022-auth-magic-link-codigo-seis-digitos]]), mientras que aquí el alta **precede** a la elección del insumo — el orden inverso al del vault ([[2026-1026-5sim-navegar-sin-registro-pero-el-flujo-empieza-por-hacer-login]]).

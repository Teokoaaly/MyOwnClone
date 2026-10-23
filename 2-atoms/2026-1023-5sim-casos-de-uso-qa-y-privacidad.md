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

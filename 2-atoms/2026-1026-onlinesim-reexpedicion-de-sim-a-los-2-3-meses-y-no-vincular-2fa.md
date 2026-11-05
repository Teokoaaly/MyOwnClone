---
id: 2026-1026-onlinesim-reexpedicion-de-sim-a-los-2-3-meses-y-no-vincular-2fa
type: atom
certainty: solid
sources: [sources/2026-10-25-onlinesim-virtual-sms.md]
links: ["[[2026-1023-5sim-numero-de-un-solo-uso-una-verificacion]]", "[[2026-1022-auth-otp-impersonacion-30min]]", "[[2026-1022-ia-y-auth-totalmente-servidor]]"]
---

## Claim
El FAQ de OnlineSim hace la advertencia de seguridad más concreta del corpus sobre números virtuales: "Numbers are issued exclusively to one person. **However, it is important to remember that the telecom operator can reissue SIM cards** (the same thing happens with regular citizen numbers) **two to three months after the number is inactive** and give them to its new customers, so we **advise you not to link payment methods or store important data on the add account 2FA** or other security measures."

## Why It Matters
Convierte una limitación comercial en una advertencia operativa con tres datos: **el plazo de reemisión (2-3 meses), el mecanismo (reissue de la tarjeta SIM por el operador) y la recomendación (no vincular métodos de pago ni 2FA)**. El vault ya tenía la noticia contraria y más cómoda — que el número no se reutiliza ([[2026-1023-5sim-numero-de-un-solo-uso-una-verificacion]])— y esta nota lo matiza de forma decisiva: **la exclusividad es del número durante la orden, no del número para siempre**. Un número de 15 minutos deja de estar protegido a los dos o tres meses, y en ese momento el número —con su historial de SMS y cualquier OTP que haya pasado por él— puede pertenecer a otra persona.
La segunda mitad de la advertencia es directamente relevante para el producto del vault: **no poner 2FA ni métodos de pago encima de una identidad SMS temporal** es la misma prohibición estructural que el vault ya aplica en su propio diseño, donde la autenticación es 100 % servidor y el OTP anónimo expira a los 30 minutos ([[2026-1022-ia-y-auth-totalmente-servidor]], [[2026-1022-auth-otp-impersonacion-30min]]). La diferencia es que OnlineSim la dice **sobre el número del cliente**, no sobre el suyo.

---
id: 2026-1101-clerk-sesion-fija-7-dias-en-hobby
type: atom
certainty: solid
sources: [sources/2026-11-01-clerk-pricing.md]
links: ["[[2026-1101-clerk-plan-gratuito-50000-mru-y-3-asientos]]", "[[2026-1101-clerk-precios-base-hobby-pro-business]]", "[[2026-1022-ia-y-auth-totalmente-servidor]]"]
---

## Claim
En **Hobby la duración de sesión está fijada a 7 días** ("Fixed to 7 days"), mientras que **Pro y Business permiten configurarla entre 5 minutos y 10 años**; Hobby además **no incluye sesiones simultáneas** (iniciar sesión en varios cuentas en un mismo dispositivo), y los **dominios satélite** —usar la misma sesión entre apps en dominios distintos— cuestan **$10/mes cada uno** en Pro y Business.

## Why It Matters
Tiene dos consecuencias muy concretas para la arquitectura de sesión del vault. Primera: la sesión de 7 días de Clerk es **más larga que la ventana de 30 minutos de la OTP de impersonación documentada en el vault**, lo que significa que la expiración de sesión en Clerk no es el mecanismo de seguridad que hoy protege el panel de administración ([[2026-1022-ia-y-auth-totalmente-servidor]]); segundo, el "dominio satélite" a $10/mes es exactamente el caso de uso de MyOwnClone si cada clon se sirve en su propio dominio personalizado — **un tenant por dominio con sesión compartida costaría $10/mes cada uno**, lo que hace inviable el modelo de "custom domain por clon" con Clerk y, por tanto, refuerza la dependencia de la sesión en servidor propia del stack Flask + NextAuth.

## Nota de verificación
Filas "Custom session duration", "Simultaneous sessions" y "Satellite domains" de la tabla "Full price breakdown", y bullet "Fixed, 7 day session lifetime" de la tarjeta Hobby, todo verbatim de la captura del 2026-11-01. La lectura sobre el panel de administración es interpretación de este átomo.

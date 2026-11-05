---
id: 2026-1101-clerk-sms-001-dolar-por-sms
type: atom
certainty: solid
sources: [sources/2026-11-01-clerk-pricing.md]
links: ["[[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]", "[[2026-1101-clerk-plan-gratuito-50000-mru-y-3-asientos]]", "[[2026-1024-notletters-precio-005-rubles-por-correo-y-contadores-de-escala]]"]
---

## Claim
La **autenticación por SMS de Clerk** no está incluida en Hobby ("Not included"); en Pro y Business se cobra **a parte: $0,01 por SMS en EE. UU. y Canadá**, y **"International: market rate"** (tarifa de mercado, sin cifra publicada). La verificación SMS es la única parte de la tabla de Clerk cuyo precio unitario **no** está publicado para internacional.

## Why It Matters
Conecta directamente con la línea de coste que el vault ya tiene abierta en el thread `economia-de-la-verificacion-y-reventa-de-cuentas`: el correo/SMS de verificación es un **coste marginal de alta** que se paga por usuario, no por infra. Con los precios del vault, un SMS bought a 5sim o similar cuesta fracciones de céntimo ([[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]), mientras que Clerk revende el SMS a **$0,01 en US/CA** y a precio de mercado en el resto del mundo sin publicarlo — es decir, **Clerk no es una opción barata para verificación por SMS y su coste internacional no es auditable desde la página de precios**. Para MyOwnClone, esto refuerza la decisión ya documentada de usar magic link / OTP por correo ([[2026-1022-auth-magic-link-codigo-seis-digitos]]) en lugar de SMS, y da un argumento cuantificado para descartarlo como proveedor de identidad si el producto necesita verificación telefónica en Europa.

## Nota de verificación
Fila "SMS codes" de la tabla "Full price breakdown" de la captura del 2026-11-01: "US and Canada, $0.01 per SMS. International: market rate". La comparación de precios con 5sim es lectura operativa cruzando fuentes del vault.

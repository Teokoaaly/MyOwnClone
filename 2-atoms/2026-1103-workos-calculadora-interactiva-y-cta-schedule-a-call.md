---
id: 2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call
type: atom
certainty: solid
sources: [sources/2026-11-03-workos-pricing.md]
links: ["[[2026-1031-workos-authkit-primer-millon-de-mau-gratis]]", "[[2026-1031-workos-sso-escalera-de-conexiones-125-100-80-65]]", "[[2026-1031-workos-radar-primeros-1000-checks-gratis]]", "[[2026-1102-workos-auth0-clerk-benchmark-de-identidad-en-tres-vias]]"]
---

## Claim
La página de precios de WorkOS expone un bloque **"Estimate your costs"** que no es una tabla sino un **calculador interactivo con un deslizador por producto**: AuthKit con escala `0 1M 2M 3M 4M 5M+` de MAU, SSO con escala `0 15 30 50 100+` de conexiones, Directory Sync con la misma escala `0 15 30 50 100+` y Radar con escala `0 1K 50K 200K 400K 600K 800K 1M 1.5M 2M 2.5M+` de checks. En cada calculadora el valor mostrado por defecto es **`$0 /month $0.00` / "Free"**, y cada uno termina con el mismo cierre comercial: **"Unlock annual discounts, expert guidance, and migration support." → "Schedule a call"**.

## Why It Matters
La estructura revela la mecánica comercial de WorkOS: **el autoservicio solo llega hasta $0** y el precio real se descubre moviendo el deslizador, y al final de cada calculador el CTA empuja a una llamada comercial ("Schedule a call"), que es exactamente la puerta de entrada al plan **Annual Credits** de precio no publicado ([[2026-1031-workos-annual-credits-frente-a-pay-as-you-go]]). Para el vault esto importa porque explica por qué la página nunca muestra un "precio típico" de WorkOS: no hay un precio único porque el precio se **calcula por escala y luego se negocia**, lo que hace que cualquier comparación cuantitativa con Auth0 o Clerk sea incompleta sin una cotización ([[2026-1102-workos-auth0-clerk-benchmark-de-identidad-en-tres-vias]]).

También fija el techo del autoservicio: el deslizador de SSO/connections llega hasta **100+** ([[2026-1031-workos-sso-escalera-de-conexiones-125-100-80-65]]) y el de Radar hasta **2,5M+ checks** ([[2026-1031-workos-radar-primeros-1000-checks-gratis]]); más allá de esos topes la página deriva a "Talk to us" / "Schedule a call", es decir, **cambio de régimen de precio, no de volumen**.

## [FRICTION]
> [[2026-1031-workos-authkit-primer-millon-de-mau-gratis]] afirma, sobre la base de las capturas del 2026-10-31 y 2026-11-02, que AuthKit cobra **"$2.500/mes por cada millón adicional de MAU"**.
> Este átomo presiona esa creencia porque la captura del **2026-11-03**, que es un volcado crudo de la página real (no una tabla condensada), **no publica ninguna cifra por encima de 1M de MAU**: el deslizador llega hasta 5M+ pero el único precio impreso es "$0 /month $0.00 — Free" en la posición por defecto de 1M, y la nota "Contact us to learn more about volume pricing" sigue manteniendo el volumen fuera de la lista de precios.
> Ambas no pueden ser completamente correctas: o los $2.500/mes por millón adicional existen y esta captura del 11-03 no llegó a la zona del precio, o esa cifra procedía de una transcripción condensada de una captura anterior y **no está publicada en la página**. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
Sección "Estimate your costs" de sources/2026-11-03-workos-pricing.md: las cuatro escalas de deslizador (AuthKit "0 1M 2M 3M 4M 5M+", SSO y Directory Sync "0 15 30 50 100+", Radar "0 1K 50K 200K 400K 600K 800K 1M 1.5M 2M 2.5M+"), los valores por defecto "$0 /month $0.00" + "Free", y el cierre repetido "Unlock annual discounts, expert guidance, and migration support." / "Schedule a call".

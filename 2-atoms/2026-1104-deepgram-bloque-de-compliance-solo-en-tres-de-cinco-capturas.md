---
id: 2026-1104-deepgram-bloque-de-compliance-solo-en-tres-de-cinco-capturas
type: atom
certainty: solid
sources: [sources/2026-11-04-deepgram-pricing.md, sources/2026-11-03-deepgram-pricing.md, sources/2026-11-02-deepgram-pricing.md, sources/2026-11-01-deepgram-pricing.md, sources/2026-10-31-deepgram-pricing.md]
links: ["[[2026-1104-deepgram-renderizado-completo-restaurado-identico-al-11-01]]", "[[2026-1101-deepgram-enterprise-selfhost-nvidia-y-endpoint-eu]]", "[[2026-1103-deepgram-captura-11-03-rendering-reducido-y-sin-enlaces]]"]
---

## Claim
El bloque "Sweating compliance, so you don't have to" (con las tarjetas SOC 2 Type 1 & Type 2 Certified, HIPAA Compliant, GDPR Ready & EU Data Residency con el hostname `api.eu.deepgram.com`, CCPA Compliant, PCI Compliant y la sección "How we protect voice data") aparece en **3 de las 5 capturas**: 11-01, 11-02 y 11-04. **No está en la del 10-31 ni en la del 11-03.** Y la captura del 10-31 no es una versión reducida como la del 11-03: conserva los enlaces markdown `[Contact sales](https://deepgram.com/contact-us)` en las cinco filas "Custom" de las tablas, pero **pierde los enlaces de navegación** ("Log in", "Sign up", "Sign up free" en texto plano), no renderiza ninguna imagen (`rock_03.avif`, `globe_paper.avif`, `sanity.io` —0 coincidencias—) y usa la forma literal "Streaming | Pre-recorded" y "per minute | per hour" con separadores, donde 11-01/11-02/11-04 los colapsan en "StreamingPre-recorded" y "per minuteper hour".

## Why It Matters
Establece que existen **al menos tres formas de renderizado** de la misma página en cinco capturas —(A) 11-01/11-02/11-04: enlaces de navegación + imágenes + compliance + separadores colapsados; (B) 10-31: sin navegación, sin imágenes, sin compliance, con separadores; (C) 11-03: sin enlaces en absoluto, sin imágenes, sin compliance, separadores colapsados— y por tanto que el bloque de compliance **no está "retirado" de la web desde el 10-31**: lleva ausente desde la primera captura y solo reaparece en una de cada dos variantes de render. Esto calibra [[2026-1101-deepgram-enterprise-selfhost-nvidia-y-endpoint-eu]]: el hostname `api.eu.deepgram.com` y las tarjetas SOC 2 / HIPAA / GDPR / CCPA / PCI solo son verificables en el render (A), y su ausencia en (B) y (C) no dice nada sobre la web. Regla operativa derivada: **el compliance y el endpoint EU son datos "de render A"**, y una captura de las variantes (B) o (C) no puede refutarlos ni confirmarlos.

## [FRICTION]
> [[2026-1103-deepgram-captura-11-03-rendering-reducido-y-sin-enlaces]] (escrita hace 2 días) contrapone el 11-03 a "las del 10-31 y 11-01/11-02" como si el 10-31 fuera un renderizado completo equivalente, y de ahí extrae la hipótesis de una posible retirada editorial del bloque de compliance entre el 11-02 y el 11-03.
> Esta nota presiona esa creencia porque **el 10-31 tampoco renderiza el bloque de compliance ni las imágenes**, pese a conservar los enlaces de las tablas: el 11-03 no es el único render sin compliance, es el segundo. La hipótesis de retirada editorial queda sin apoyo; lo que hay es una alternancia entre variantes de extracción. La parte del átomo viejo que sí se sostiene —el 11-03 pierde enlaces y compliance frente al 11-01/11-02— permanece válida. Marcado para juicio humano, no auto-resuelto.

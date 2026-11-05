---
id: 2026-1026-noones-api-dos-formatos-directo-y-delegado
type: atom
certainty: solid
sources: [sources/2026-10-25-noones-developer-api.md]
links: ["[[2026-1024-noones-superficie-publica-productos-y-dominios-espejo]]", "[[2026-1023-herosms-api-y-partners-de-registro-masivo]]", "[[2026-1026-noones-acceso-directo-limitado-a-tu-propia-cuenta]]", "[[2026-1026-noones-acceso-delegado-app-instalada-por-el-usuario]]"]
---

## Claim
La página de developers de NoOnes (`https://dev.noones.com/`, 547 palabras, capturada 2026-10-25) ofrece la API en **exactamente dos formatos**, elegidos explícitamente en el bloque "Choose Your Format": **Direct Access** ("Use NoOnes's APIs to create an app that can only access and automate your own NoOnes account") con CTA a `/dashboard/direct-access`, y **Delegated Access** ("allows you to create an app that other users can install and grant permission to manage their account") con CTA a `/dashboard/delegated-access`. Los cuatro bullets de la cabecera son: *Automate your trading*, *Receive trade activity notifications*, *Trade on behalf of your clients*, *Automatically update offer margins*.

## Why It Matters
Frente a HeroSMS —donde la API **no tenía documentación** y el producto del socio era el registro automatizado ([[2026-1023-herosms-api-y-partners-de-registro-masivo]])—, la API de NoOnes tiene un sitio propio y **dos puertas de alta separadas**, con la diferencia de fondo de que aquí **el usuario final concede el permiso**. Es decir, el modelo NoOnes es "el tercero opera dentro de la cuenta porque el usuario final le concede permiso", no "el tercero opera la cuenta". Para un vault que se mueve entre reventa de cuentas y arquitectura de producto, la pregunta pasa de "¿se puede automatizar?" a "¿con qué consentimiento y con qué superficie de permisos?" — y esa superficie **no está publicada** en la captura: solo se nombran dos dashboards ([[2026-1026-noones-dev-noones-sin-precios-ni-limites-ni-documentacion-publica]]).

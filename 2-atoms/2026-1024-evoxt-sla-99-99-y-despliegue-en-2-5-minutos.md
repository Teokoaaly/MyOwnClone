---
id: 2026-1024-evoxt-sla-99-99-y-despliegue-en-2-5-minutos
type: atom
certainty: solid
sources: [sources/2026-10-23-evoxt-vms.md, sources/2026-10-23-evoxt-vps-pricing.md]
links: ["[[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]", "[[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]", "[[2026-1024-evoxt-despliegue-100-automatico-y-upgrade-con-un-boton]]"]
---

## Claim
Evoxt declara **"99.99% Uptime"** con la fórmula *"Our servers are guaranteed to have at least 99.99% uptime"*, y en la misma lista de funciones adicionales de la home declara **"Speedy Deployment — listo para conectar y usar en 2.5 minutos"**, **"Scale — despliega la VM más pequeña y escala en pocos clics cuando haga falta"** y **"Enterprise Grade Hardware"**.

## Why It Matters
El 99,99 % de uptime es **más estricto que el 99,9 % de SLA de Hetzner** que el vault ya registra, junto con GDPR e ISO/IEC 27001 ([[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]]): mientras Hetzner ofrece certificaciones verificables y un SLA con créditos, Evoxt ofrece un número de uptime más alto sin publicar el texto del SLA, los créditos ni los mecanismos. Es exactamente el tipo de promesa que hay que contrastar contra la infraestructura real: hoy [[myownclone]] se sirve desde un nginx autoalojado ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) sin SLA formal, es decir, en Best Effort — muy por debajo de cualquiera de las dos cifras. El "despliegue en 2,5 minutos" y el escalado en pocos clics importan para un producto cuyo objetivo declarado es salir al mercado rápido con una versión mínima viable.

## Nota de verificación
La captura **no** publica el texto del SLA, los porcentajes de crédito, la duración del compromiso, ni los canales de soporte. La cifra 99,99 % y el plazo de 2,5 minutos están transcritos literalmente de la home como declaraciones del proveedor, sin verificación independiente.

## [NOTA 2026-10-24]
La página de precios del proveedor (`sources/2026-10-23-evoxt-vps-pricing.md`) contradice el plazo de la home: su FAQ dice **"Less than 5 minutes"** para el mismo evento (despliegue tras el pago) y añade **"Server deployment on Evoxt is 100% automatic"** y el escalado por botón de upgrade. La fricción está planteada en [[2026-1024-evoxt-despliegue-100-automatico-y-upgrade-con-un-boton]] y no se auto-resuelve aquí. Lo que sí queda firme tras las dos capturas: el **99,99 % de uptime no aparece en ninguna de las dos páginas** más que como frase de marketing, sin SLA asociado.

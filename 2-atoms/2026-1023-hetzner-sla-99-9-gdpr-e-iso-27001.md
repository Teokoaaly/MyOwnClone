---
id: 2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001
type: atom
certainty: solid
sources: [sources/2026-10-22-hetzner-cloud.md, sources/2026-10-23-hostbrr-home.md, sources/2026-10-23-evoxt-vms.md, sources/2026-10-23-skhron-bitcoin-vps.md]
links: ["[[2026-1023-hetzner-regiones-y-zonas-de-disponibilidad]]", "[[2026-1022-superficie-legal-publica-dpa-clon-terms]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]"]
---

## Claim
Hetzner declara un **SLA con 99,9 % de uptime garantizado** y créditos definidos en caso de avería, **soporte 24/7 por email**, **certificación BSI C5** ("tested transparency") y, por cumplimiento, **GDPR** con sede en Alemania, **ISO/IEC 27001 en los parques de Alemania y Finlandia**, y "Made in Germany / Hosted GDPR compliant" como distintivo.

## Why It Matters
Son los tres atributos que un cliente enterprise verifica antes de firmar, pero también los que chocan con la documentación del producto: el Aviso Legal de [[2026-1022-superficie-legal-publica-dpa-clon-terms]] declara "Vercel Inc." y "Neon Inc." mientras la infraestructura real es un nginx autoalojado ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]). Hetzner es un proveedor con GDPR y SLA verificable, lo que convierte a este átomo en la referencia de con qué se puede sustituir un hosting que hoy no aparece en el Aviso Legal. El 99,9 % de uptime, en cambio, es la cifra con la que hay que comparar la promesa real del producto: con un solo VPS autoalojado ([[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]) no hay SLA, solo Best Effort.

## Nota de verificación
La captura no publica el texto del SLA, los porcentajes de crédito, el horario ni los tiempos de respuesta del soporte. Las certificaciones se afirma que aplican a los parques de Alemania y Finlandia, no a todo el catálogo de zonas ([[2026-1023-hetzner-regiones-y-zonas-de-disponibilidad]]).

## [NOTA 2026-10-24 — Evoxt]
Fuente: `sources/2026-10-23-evoxt-vms.md`. Un tercer dato de SLA en el vault: Evoxt declara **"99.99% Uptime"** ("Our servers are guaranteed to have at least 99.99% uptime"), una cifra **más estricta que el 99,9 % de Hetzner y de HostBrr**, pero sin texto de SLA, sin créditos, sin ISO 27001, sin GDPR y sin BSI C5 (ver [[2026-1024-evoxt-sla-99-99-y-despliegue-en-2-5-minutos]]). En su lugar, Evoxt compensa con dos incluidos declarados: **backup offsite semanal automático a coste cero** ([[2026-1024-evoxt-backup-semanal-offsite-gratuito]]) y compromiso de minimización de datos ("normalmente solo pedimos tu nombre", [[2026-1024-evoxt-cripto-y-minimizacion-de-datos]]). La observación que este átomo ya sostiene: en este mercado la cifra de uptime es commodity de marketing y el valor está en el SLA auditable, en el coste de egreso y en el aislamiento documentado.

## [NOTA 2026-10-24]
Fuente: `sources/2026-10-23-hostbrr-home.md`. La cifra de **99,9 % de uptime** no es exclusiva de Hetzner: HostBrr la publica idénticamente en su home ("We guarantee 99.9% uptime"), pero **sin texto de SLA, sin créditos, sin ISO 27001, sin GDPR y sin BSI C5**, y con la salvedad de que la protección y la capacidad "may vary between services and location" (ver [[2026-1024-hostbrr-sla-99-9-y-garantia-de-devolucion-30-y-7-dias]] y [[2026-1024-hostbrr-escala-3000-clientes-2023-y-soporte-24-7]]). Esto confirma que el 99,9 % funciona como claim de marketing reutilizable en el sector y que **la diferencia entre proveedores de hosting en el vault no es la cifra de uptime sino la existencia de un SLA con créditos y certificaciones auditables** — criterio que el vault puede usar para no cambiar de proveedor por el mismo número.

## [NOTA 2026-10-24 — Skhron]
Fuente: `sources/2026-10-23-skhron-bitcoin-vps.md`. Cuarta cifra de uptime del vault: Skhron ofrece **SLA de 99,95 % con créditos** y afirma un **uptime de red medido del 99,99 %**, con enlace a su documento de Service Level Agreement (ver [[2026-1024-skhron-sla-99-95-y-uptime-medido-99-99]]). La observación de este átomo se confirma y se afina: Skhron **sí** publica SLA y créditos (más que HostBrr y Evoxt) y **está en la UE** (Estocolmo y Varsovia, [[2026-1024-skhron-ubicaciones-eu-y-red-propia-as215467]]), pero **no publica GDPR, ISO 27001 ni BSI C5** — a diferencia de Hetzner. Y su producto se define por lo contrario: **no-KYC y gateway de pago no custodio** ([[2026-1024-skhron-sin-kyc-ni-documentacion-ni-identidad]], [[2026-1024-skhron-pago-cripto-gateway-propio-no-custodial]]). Es decir, el eje del vault se afila: **"privacidad" y "cumplimiento auditable" son ejes opuestos en este tramo de mercado**, y un proveedor puede tener SLA con créditos y a la vez no tener ninguna certification. Para el Aviso Legal del producto, que ya declara terceros que no coinciden con la infraestructura real ([[2026-1022-superficie-legal-publica-dpa-clon-terms]]), elegir un proveedor no-KYC significa que **no hay marco de cumplimiento que sostener ante un cliente enterprise**.

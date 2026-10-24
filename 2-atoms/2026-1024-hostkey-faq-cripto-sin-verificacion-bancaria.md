---
id: 2026-1024-hostkey-faq-cripto-sin-verificacion-bancaria
type: atom
certainty: tentative
sources: [sources/2026-10-23-hostkey-bitcoin-vps.md]
links: ["[[2026-1024-hostkey-kyc-obligatorio-y-procesamiento-via-bitpay]]", "[[2026-1024-evoxt-cripto-y-minimizacion-de-datos]]", "[[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]]"]
---
## Claim
La FAQ de la misma página de Bitcoin VPS responde a la pregunta "Do I need to verify my identity to pay with crypto?" con: "In most cases, cryptocurrency payments are processed without standard bank identity verification. However, individual payment providers may request additional information according to their requirements". Es decir, la página **se contradice a sí misma**: este bloque sugiere trato sin verificación bancaria, mientras el bloque legal de la misma página exige KYC a todos los clientes.

## Why It Matters
Es exactamente el tipo de fricción de marketing que el vault registra en otros ejes: el mensaje de "privacidad" (el bloque "Privacy-Focused Hosting" y el caso de uso "Anonymous Website Hosting") se apoya en la fachada cripto, mientras el cumplimiento real lo impone un proveedor de pagos. Para un SaaS que tiene que publicar Aviso Legal y listar terceros reales ([[2026-1022-superficie-legal-publica-dpa-clon-terms]]), la lección operativa es que **el claim de privacidad de un proveedor se tiene que leer en su cláusula de cumplimiento, no en su titular**, igual que una promesa de minimización no sustituye a una certificación ([[2026-1024-evoxt-cripto-y-minimizacion-de-datos]], [[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]]). Se marca `tentative` porque la lectura correcta (qué prevalece: la FAQ o el párrafo legal) no se puede resolver con el texto capturado; solo queda registrada la coexistencia de ambos enunciados en la misma URL.

## [FRICTION]
> [[2026-1024-hostkey-kyc-obligatorio-y-procesamiento-via-bitpay]] (escrita hoy) recoge el enunciado de la misma fuente que afirma KYC obligatorio para todos los clientes, pagos anónimos no aceptados y verificación en BitPay. Esta nota presiona eso porque el bloque de FAQ de la **misma página** afirma que en la mayoría de los casos no hay verificación de identidad bancaria. Ambas no pueden ser la política efectiva del checkout; el conflicto no se auto-resuelve.

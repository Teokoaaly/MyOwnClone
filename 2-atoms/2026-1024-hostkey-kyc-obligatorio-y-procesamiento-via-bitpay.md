---
id: 2026-1024-hostkey-kyc-obligatorio-y-procesamiento-via-bitpay
type: atom
certainty: solid
sources: [sources/2026-10-23-hostkey-bitcoin-vps.md]
links: ["[[2026-1024-hostkey-faq-cripto-sin-verificacion-bancaria]]", "[[2026-1024-extravm-pago-cripto-sin-kyc-ni-identidad]]", "[[2026-1024-skhron-sin-kyc-ni-documentacion-ni-identidad]]", "[[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]]"]
---
## Claim
HOSTKEY declara en su página de Bitcoin VPS que **todos sus clientes deben pasar por procedimientos KYC** conforme a la legislación de la UE y de los Países Bajos: "all HOSTKEY customers must undergo KYC procedures in accordance with EU and Netherlands legislation. Anonymous cryptocurrency payments are not accepted, and all transactions are processed through the American payment system BitPay, which also requires verification".

## Why It Matters
Coloca a HOSTKEY en el extremo **opuesto** de la escala de minimización de datos que el vault viene midiendo: ExtraVM declara "no identity verification is required" y solo pide un email ([[2026-1024-extravm-pago-cripto-sin-kyc-ni-identidad]]), Evoxt declara que normalmente solo pide el nombre ([[2026-1024-evoxt-cripto-y-minimizacion-de-datos]]); HOSTKEY conserva la verificación de identidad y la delega además en un tercero estadounidense (BitPay). Es decir, **pagar en cripto no compra anonimato**: el activo que se compra es la incertidumbre de la liquidación, no el secreto de la identidad. Para un SaaS multi-tenant como MyOwnClone, esto importa en la dirección contraria: un proveedor con KYC obligatorio y euroGDPR es un proveedor *más* fácil de auditar y de presentar ante un cliente corporativo, aunque también es un proveedor que acumula datos personales de los tenants en un tercero de EE. UU. —unatransferencia internacional que hoy no está documentada en la superficie legal del producto (cf. [[2026-1022-superficie-legal-publica-dpa-clon-terms]] y [[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]]).

## [FRICTION]
> [[2026-1024-extravm-pago-cripto-sin-kyc-ni-identidad]] (escrita hoy) afirma que el pago en criptomoneda **no requiere ningún tipo de KYC**: "You only need to provide an email address to create your account... don't require passport, ID, address verification, or any KYC documentation for crypto payments". Esta nota presiona eso porque HOSTKEY, con la misma forma de pago (bitcoin como método de pago de un VPS), declara lo contrario de forma explícita: KYC obligatorio para **todos** los clientes y pagos anónimos **no aceptados**. Ambas no pueden ser una característica del sector; la diferencia real es la política de cada checkout, y por tanto "pago cripto = proveedor sin KYC" es una generalización que el vault ya no puede sostener. Marcado para juicio humano, no auto-resuelto.

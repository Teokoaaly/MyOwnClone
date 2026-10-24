---
id: 2026-1024-hostbrr-sla-99-9-y-garantia-de-devolucion-30-y-7-dias
type: atom
certainty: solid
sources: [sources/2026-10-23-hostbrr-home.md, sources/2026-10-23-hostbrr-vps-pricing.md]
links: ["[[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]]", "[[2026-1024-hostbrr-escalera-de-precios-vps-2-00-3-50-y-3-90]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
HostBrr declara **garantía de uptime del 99,9 %** ("We guarantee 99.9% uptime, supported by highly redundant enterprise networking in premium global datacenters") y una **política de reembolso escalonada por producto**: **30 días** para hosting compartido y planes reseller, y **7 días** para planes VPS y Storage. La FAQ (pregunta 01) lo confirma y añade la excepción: "Payments made with cryptocurrency are non-refundable due to how blockchain transactions work".

## Why It Matters
El 99,9 % es exactamente la misma cifra que Hetzner publica con créditos de SLA definidos ([[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]]) — pero aquí **no se publica el texto del SLA ni los créditos**, solo la promesa, lo que hace que HostBrr sea un caso de prueba de que "99,9 % de uptime" es un claim de marketing reutilizable, no un compromiso verificable. La diferencia operativa relevante es la ventana de reembolso: **7 días para el VPS** es un período muy corto para validar que un autoalojado aguanta carga sostenida en producción antes de quedar atado a un contrato mensual; combinado con el suelo de €2,00/mes ([[2026-1024-hostbrr-escalera-de-precios-vps-2-00-3-50-y-3-90]]) el coste de una mala elección es bajo en euros pero la exposición es de un mes entero. Y el veto a reembolsos en criptomoneda afecta directamente a un pagador que reporta en EUR/USD.

## Nota de verificación
La captura no publica las condiciones, la definición de "uptime" (qué se excluye: mantenimiento, error del cliente), los créditos del SLA, ni los requisitos para reclamar el reembolso. La excepción de criptomoneda está transcrita literalmente de la FAQ.

## [NOTA 2026-10-24 — página de precios]
Fuente: `sources/2026-10-23-hostbrr-vps-pricing.md`. La FAQ de la página de precios (pregunta 05) **reconfirma los 7 días para VPS** y añade una precisión de alcance que la home no distinguía: "**VPS and Storage plans include a 7-day money-back guarantee. Payments made with cryptocurrency are non-refundable due to how blockchain transactions work**". Lo relevante para el vault: los 7 días son la **ventana de validación del VPS**, y con la política de cripto sin devolución, quien paga en cripto no tiene ninguna ventana — lo que choca con la faceta de "pagos EUR/USD/PayPal/cripto" del mismo proveedor ([[2026-1024-hostbrr-pagos-eur-usd-paypal-cripto-y-provisionamiento-en-minutos]]). La página de precios **no** publica el texto del SLA ni los créditos: sigue siendo una promesa sin contrato adjunto, ahora repetida por dos capturas del mismo proveedor.

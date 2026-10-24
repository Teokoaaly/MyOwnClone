---
id: 2026-1024-extravm-renovacion-cripto-manual-y-credito-en-cuenta
type: atom
certainty: solid
sources: [sources/2026-10-23-extravm-crypto-vps.md]
links: ["[[2026-1024-extravm-despliegue-tras-confirmacion-en-15-30-minutos]]", "[[2026-1024-extravm-sin-reembolso-en-pagos-cripto]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
**Las renovaciones en criptomoneda son manuales**: "Currently, cryptocurrency renewals are manual - you'll receive an invoice before renewal and can pay with crypto again. We're working on implementing automatic cryptocurrency billing, but due to blockchain transaction complexity, this requires manual payment for now." Como alternativa, ExtraVM permite **añadir crédito a la cuenta por adelantado** ("You can also add account credit in advance").

## Why It Matters
Convierte el pago en cripto de un mecanismo de alta a un **proceso recurrente que hay que operar**: cada mes hay que responder a una factura, pagar en cripto y esperar la confirmación, con el despliegue unido a esa espera ([[2026-1024-extravm-despliegue-tras-confirmacion-en-15-30-minutos]]). Para el vault, que registra la infraestructura como línea de coste que aún no aparece en el corte por categoría ([[2026-1022-costes-por-categoria-tenant]]), esto significa que el flujo de renovación no es un olvido automático: es una tarea mensual con una ventana de caída potencial. El saldo en cuenta por adelantado es la mitigación obvia — prepagar varios meses y eliminar el acoplamiento entre renovación y uptime — y es un patrón que el vault debería tener en cuenta al comparar proveedores: no solo importa el precio por mes, sino **cuánta mano dura cuesta el ciclo de cobro**.

## Nota de verificación
La captura **no** publica si el crédito en cuenta caduca, si aplica descuento por prepago, ni cuánto tiempo antes de la renovación se emite la factura.

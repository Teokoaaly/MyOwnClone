---
id: 2026-1024-extravm-pago-inferior-pendiente-y-sobrepago-a-saldo
type: atom
certainty: solid
sources: [sources/2026-10-23-extravm-crypto-vps.md]
links: ["[[2026-1024-extravm-renovacion-cripto-manual-y-credito-en-cuenta]]", "[[2026-1024-extravm-despliegue-tras-confirmacion-en-15-30-minutos]]", "[[2026-1024-extravm-sin-reembolso-en-pagos-cripto]]"]
---

## Claim
ExtraVM define el comportamiento ante un importe incorrecto: **pago insuficiente** → "your payment will be pending until you send the difference"; **sobrepago** → "the excess amount will typically be credited to your account balance". El caso del sobrepago se resuelve, por tanto, como saldo, lo que conecta directamente con la posibilidad de añadir crédito a la cuenta por adelantado ([[2026-1024-extravm-renovacion-cripto-manual-y-credito-en-cuenta]]).

## Why It Matters
Dos efectos operativos que el vault necesita tener en cuenta al usar cripto como forma de pago de infraestructura: (1) **un pago corto no es un pago errado, es un pago pendiente** — el servidor no se despliega y el incidente se extiende ("pending until you send the difference"), así que un error de cálculo de tipo de cambio se convierte en downtime, no en un contratiempo de facturación; (2) **el sobrepago no se devuelve**, se convierte en saldo, lo que en un proveedor sin reembolsos en cripto ([[2026-1024-extravm-sin-reembolso-en-pagos-cripto]]) es la única vía de retorno del dinero. La combinación es un modelo de saldo que el vault no tenía registrado: es un micropago prepagado con velocidad de confirmación de blockchain ([[2026-1024-extravm-despliegue-tras-confirmacion-en-15-30-minutos]]).

## Nota de verificación
La captura **no** publica el umbral de tolerancia, si el importe acreditado se descuenta automáticamente de la siguiente factura, ni el plazo de caducidad del saldo.

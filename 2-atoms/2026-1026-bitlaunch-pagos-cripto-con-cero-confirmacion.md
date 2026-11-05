---
id: 2026-1026-bitlaunch-pagos-cripto-con-cero-confirmacion
type: atom
certainty: tentative
sources: [sources/2026-10-25-bitlaunch-bitcoin-vps.md]
links: ["[[2026-1024-extravm-despliegue-tras-confirmacion-en-15-30-minutos]]", "[[2026-1024-hostkey-pago-cripto-pendiente-hasta-confirmacion-de-blockchain]]", "[[2026-1026-bitlaunch-facturacion-por-hora-y-pago-cripto-propio]]", "[[2026-1024-skhron-pago-cripto-gateway-propio-no-custodial]]"]
---

## Claim
La página Bitcoin VPS sostiene que **"BitLaunch's in-house payment system eliminates middle-men and fees while enabling zero confirmation payments"**, y lo atribuye a la combinación de dos cosas: la criptomoneda ("Cryptocurrency removes borders and allows you to buy a Bitcoin VPS from anywhere in the world with no restrictions") y el sistema de pagos propio. La página **no cuantifica** la ventana de confirmación, no dice qué monedas acepta, ni explica cómo se evita la confirmación de blockchain.

## Why It Matters
Es la **afirmación operativa más fuerte del corpus de pagos cripto**, y el vault la tenía hasta ahora documentada siempre en negativo: ExtraVM despliega tras "1-3 confirmations" con una ventana declarada de **15-30 minutos** ([[2026-1024-extravm-despliegue-tras-confirmacion-en-15-30-minutos]]) y HOSTKEY reconoce que "Cryptocurrency payments require blockchain confirmation, so processing may take some time" ([[2026-1024-hostkey-pago-cripto-pendiente-hasta-confirmacion-de-blockchain]]). Skhron publica un gateway propio no custodio ([[2026-1024-skhron-pago-cripto-gateway-propio-no-custodial]]) y ExtraVM declara el mismo precio con cripto o tarjeta ([[2026-1024-extravm-mismo-precio-que-tarjeta-sin-recargo-cripto]]): ninguno de esos casos elimina el tiempo de confirmación. Si "zero confirmation" es real, es la primera vía de pago cripto del vault **sin latencia de aprovisionamiento**, lo que cambiaría el cálculo de automatización por API: una compra programada por script no dependería de una ventana de 15-30 minutos ni de un polling de estado. La captura no permite decidir si es real: es un claim sin cifra y sin mecanismo.

## [FRICTION]
> [[2026-1024-extravm-despliegue-tras-confirmacion-en-15-30-minutos]] afirma que el despliegue encripto **no puede** cerrarse hasta la confirmación de blockchain (1-3 confirmaciones, 15-30 minutos de media: BTC 10-30 min, ETH 2-5 min).
> Este átomo presiona esa regla: si BitLaunch realmente cobra y aprovisiona con "zero confirmation payments", entonces la latencia de confirmación **no es un coste intrínseco del pago cripto** sino un parámetro del proveedor (confirmar antes de aprovisionar), y el criterio del vault para medir el coste de un alta en cripto —"pagar es esperar"— solo vale para los que esperan. Ambas no pueden ser completamente correctas: o el tiempo de confirmación es una propiedad del medio y BitLaunch no puede eliminarlo sin asumir riesgo de doble gasto, o es una decisión de diseño del proveedor. Marcado para juicio humano, no auto-resuelto: la captura no publica número de confirmaciones, política de reemisión ni mecanismo de liquidación.

## Nota de verificación
"Cryptocurrency removes borders", "eliminates middle-men and fees" y "zero confirmation payments" son literales de la página. La captura **no** publica ventana de confirmación, lista de monedas, commission rates, política de reemisión ni mecanismo de liquidación. "Eliminates middle-men and fees" es un claim sin cifra; el corpus ya registró el mismo patrón en ExtraVM ("Pricing is the same regardless of payment method") y en el "No Hidden Fees" de BitLaunch, sin números detrás.

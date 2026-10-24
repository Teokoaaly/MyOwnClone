---
id: 2026-1024-hostkey-pago-cripto-pendiente-hasta-confirmacion-de-blockchain
type: atom
certainty: solid
sources: [sources/2026-10-23-hostkey-bitcoin-vps.md]
links: ["[[2026-1024-extravm-despliegue-tras-confirmacion-en-15-30-minutos]]", "[[2026-1024-hostkey-monedas-aceptadas-bitcoin-ethereum-litecoin-ripple-bch]]", "[[2026-1024-hostkey-kyc-obligatorio-y-procesamiento-via-bitpay]]"]
---
## Claim
HOSTKEY explica el retraso de los pagos cripto: "Cryptocurrency payments require blockchain confirmation, so processing may take some time. If the status isn't updated, please wait for network confirmations or contact HOSTKEY support". El flujo de compra es: se elige configuracion, se pasa al pago, se indica criptomoneda como metodo y **tras la confirmacion de la transaccion el servidor se crea automaticamente**.

## Why It Matters
El acoplamiento entre confirmacion de blockchain y aprovisionamiento automatico es el mismo que ya registro ExtraVM con su ventana de 15-30 minutos ([[2026-1024-extravm-despliegue-tras-confirmacion-en-15-30-minutos]]), pero aqui la pagina **no cuantifica la ventana**: solo admite que puede tardar y que hay que contactar a soporte si el estado no se actualiza. Sumado a la lista de cinco monedas sin stablecoins ([[2026-1024-hostkey-monedas-aceptadas-bitcoin-ethereum-litecoin-ripple-bch]]) y al KYC obligatorio a traves de BitPay ([[2026-1024-hostkey-kyc-obligatorio-y-procesamiento-via-bitpay]]), el resultado es que el camino "pago cripto -> servidor en manos del cliente" tiene **tres fuentes de friccion desconocido de las que ninguna tiene SLA publicada**: tiempo de confirmacion, posible solicitud de datos por el procesador de pagos, y aprobacion de KYC. Para un despliegue de clones que se programa por API, esto convierte la opcion cripto en un canal de provisioning **no automatizable de extremo a extremo**, a diferencia del camino de tarjeta.

---
id: 2026-1024-extravm-registro-contable-sin-vinculo-a-wallets
type: atom
certainty: solid
sources: [sources/2026-10-23-extravm-crypto-vps.md]
links: ["[[2026-1024-extravm-pago-cripto-sin-kyc-ni-identidad]]", "[[2026-1022-superficie-legal-publica-dpa-clon-terms]]", "[[2026-1024-evoxt-cripto-y-minimizacion-de-datos]]"]
---

## Claim
ExtraVM declara una política de registros acotada: **"We maintain transaction records for accounting purposes showing the payment amount and date, but we don't link these to wallet addresses or track blockchain transactions. Our payment processor handles crypto payments, and we only receive confirmation of successful payment."** Es decir, el proveedor conserva importe y fecha (obligación contable) pero no la dirección del wallet ni el historial on-chain; la relación con el titular la rompe el procesador de pago.

## Why It Matters
Es la versión más concreta del principio de minimización que el vault está rastreando entre proveedores: no basta con decir "no KYC", hay que preguntar **qué se guarda** y quién lo guarda. La respuesta aquí es: el proveedor solo sabe que "ha entrado un pago", y el procesador —un tercero externo— es quien ve la dirección del wallet. Ese detalle importa para un producto con Aviso Legal y DPA publicados que hoy declaran terceros que no coinciden con la infraestructura real ([[2026-1022-superficie-legal-publica-dpa-clon-terms]]): si MyOwnClone llegara a usar un proveedor con esta arquitectura, la cadena de datos sería "cliente → email → proveedor → procesador", y el proveedor **no** podría identificar la transacción on-chain aunque quisiera. Comparado con el compromiso minimalista de Evoxt ("normalmente solo pedimos tu nombre", [[2026-1024-evoxt-cripto-y-minimizacion-de-datos]]), el modelo de ExtraVM sustituye "un dato identificativo" por "ninguno identificativo, pero con un tercero en medio que sí lo ve" — un intercambio que hay que registrar explícitamente.

## Nota de verificación
La captura **no** publica la política de privacidad, el nombre del procesador, ni la retención de esos registros contables. La frase es una declaración del proveedor sobre su propio tratamiento de datos.

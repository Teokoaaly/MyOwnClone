---
id: 2026-1102-assemblyai-multicanal-se-cobra-por-canal
type: atom
certainty: solid
sources: [sources/2026-11-02-assemblyai-pricing.md]
links: ["[[2026-1022-separacion-de-hablantes-en-entrevistas]]", "[[2026-1101-assemblyai-tarifas-por-hora-no-por-minuto]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
El audio multicanal de AssemblyAI **se factura por canal**: "Multichannel audio is billed per channel. For example, a 1-hour stereo (2-channel) file is billed as 2 hours of transcription. Each channel is transcribed independently, which provides more accurate results for multi-speaker recordings."

## Why It Matters
Es un multiplicador de coste invisible en la tabla de precios: el vault calcula el coste de audio por hora de **duración del fichero**, pero en un recording estéreo la factura es el doble. Una hora de entrevista grabada en estéreo cuesta $0,30 con Universal-2, no $0,15. Y la razón que da la propia página —transcribir cada canal por separado da más precisión en grabaciones multiparlante— es exactamente la necesidad de separar hablantes que el founder describe en [[2026-1022-separacion-de-hablantes-en-entrevistas]]: es decir, el producto que el vault quiere construir produce por diseño el input más caro de facturar. La consecuencia operativa es que hay que decidir el formato de captura antes de decidir el modelo: mono a $0,15/hr o estéreo a $0,30/hr efectivo, y esa decisión debería entrar en la línea `categoryIngestion` del corte por categoría ([[2026-1022-costes-por-categoria-tenant]]), que es donde el vault ya coloca los costes de ingesta.

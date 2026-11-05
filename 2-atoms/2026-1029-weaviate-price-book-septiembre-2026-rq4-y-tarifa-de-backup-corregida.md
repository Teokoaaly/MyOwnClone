---
id: 2026-1029-weaviate-price-book-septiembre-2026-rq4-y-tarifa-de-backup-corregida
type: atom
certainty: solid
sources: [sources/2026-10-29-weaviate-cloud-pricing.md]
links: ["[[2026-1029-weaviate-compresion-rq-no-reduce-dimensiones-pero-abona-precio-y-ram]]", "[[2026-1029-weaviate-cobra-por-dimensiones-vectoriales-no-por-objetos]]", "[[2026-1029-weaviate-cloud-flex-minimo-45-dolares-al-mes]]"]
---
## Claim
La página de precios incluye una nota titulada **"Weaviate Cloud pricing update: September 2026"** que documenta **dos cambios en el price book** aplicados **al uso desde el 1 de septiembre de 2026**: (1) **la compresión RQ-4 pasa a estar disponible en colecciones HNSW y tiene su propio precio, situado entre RQ-1 y RQ-8**; (2) **los backups se facturan a una tarifa por GiB corregida**, que ahora parte de la misma base en AWS, GCP y Azure y **varía después por región**. La fuente explica el motivo: *"Backup rates used to be set separately for each cloud, and some of them were out of line with what hyperscalers charge us to host your backups."* Consecuencia práctica: **los backups están activos por defecto en todos los clusters**, así que el cambio se ve en la línea de backup de la factura, y **puede subir o bajar según el cloud y la región**. Además, la tabla de planes marca **Data transfer: "Free for promotional period"** en los tres niveles de pago, con la nota de que **Weaviate puede introducir cargos en el futuro con aviso previo**.

## Why It Matters
Es la parte de la página de precios que **avisa de que las cifras del price book son móviles**, y por tanto hay que fechar cualquier cifra del vault: un "$0.03036/GiB de backup en Flex" leído hoy puede no ser el de mañana, y **el signo del cambio depende de la región**, que es una variable que el producto elige y no el cliente. La segunda consecuencia es de arquitectura de coste: **el backup no es una opción, es una línea de factura siempre presente**, y como las regiones tienen tarifas distintas, **la decisión de dónde alojar el cluster tiene un impacto en la factura que es del mismo orden que el del propio storage** ([[2026-1029-weaviate-cobra-por-dimensiones-vectoriales-no-por-objetos]]).

La aparición de **RQ-4 como precio intermedio entre RQ-1 y RQ-8** es la señal de que **la compresión es un eje de precio de primer orden, no un detalle de rendimiento** ([[2026-1029-weaviate-compresion-rq-no-reduce-dimensiones-pero-abona-precio-y-ram]]): hay una ladder de niveles con precio propio, y la elección del nivel es una decisión de coste por dimensión que se puede hacer de forma incremental. La nota sobre **data transfer gratis "por periodo promocional"** es, por su parte, una partida latente: hoy no cuesta, mañana puede entrar en la factura sin que el cambio sea imputable al consumo de recursos del tenant.

## Nota de verificación
La fuente **no publica la tabla de precios por nivel de compresión** (RQ-1, RQ-4, RQ-8) ni el porcentaje de descuento de cada uno, ni las tarifas de backup por región: solo la existencia del escalón RQ-4 y el criterio de las nuevas tarifas ("misma base en AWS, GCP y Azure, luego variación por región"). La fecha de aplicación **1 de septiembre de 2026** está explícita en la captura.

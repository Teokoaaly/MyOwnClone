---
id: 2026-1024-internet-bs-promocion-com-cinco-dominios-y-fraude-de-multicuenta
type: atom
certainty: solid
sources: [sources/2026-10-24-internet-bs-domains.md]
links: ["[[2026-1024-internet-bs-com-a-6-99-y-cinco-servicios-gratis-de-por-vida]]", "[[2026-1024-hostkey-kyc-obligatorio-y-procesamiento-via-bitpay]]", "[[2026-1024-notletters-correo-masivo-para-registros-y-lolzteam]]"]
---

## Claim
Los "Promotional Terms & Conditions" de la oferta .com a $6.99 son muy específicos: la promoción aplica **solo al primer año** de registros .COM **nuevos** hechos durante el periodo promocional, **solo a clientes que nunca han comprado un dominio** en sus servicios, con un **máximo de 5 registros .COM elegibles por cliente** y con **término de un (1) año únicamente** (cualquier año adicional se cobra al precio estándar vigente). Para determinar la elegibilidad, Internet.bs declara que **puede tratar múltiples cuentas como del mismo cliente** cuando comparten "common ownership, control, contact details, payment methods, billing information, IP addresses, devices or other identifying characteristics", y se reserva el derecho de **retirar el precio promocional, cobrar la diferencia, suspender o cancelar los registros** y "take any other action reasonably necessary".

## Why It Matters
Este es el punto más operativo de la captura, y lo es por una razón que el vault ya conoce desde otro lado: **el anti-abuso multi-cuenta es la puerta de entrada del volumen**. Internet.bs enumera las señales que usa para unificar cuentas —incluidas **IP y dispositivos**, no solo correo y pago— y esa enumeración es, sin querer, una **descripción de las técnicas de evasión que usa el mercado de alta masiva**. Es el mismo espacio de problema que el vault registra en el otro extremo: NotLetters vendiendo buzones de correo a 0,05 ₽ con la promesa de "create multiple mailboxes for site registrations" ([[2026-1024-notletters-correo-masivo-para-registros-y-lolzteam]]). Un registrador que ficha por IP y por dispositivo corta de raíz la vía barata de conseguir un lote de dominios .com baratos: **5 por cliente, y la excepción se persigue**.

La segunda lectura es de coste: **el descuento del primer año es un préstamo con recargo**. La diferencia entre $6.99 y el precio estándar no está publicada, pero la estructura —descuento solo en el año 1, término de 1 año, y verificación de elegibilidad "before or after registration"— significa que un dominio comprado en promoción **arrastra el riesgo de una auditoría posterior con cobro de la diferencia**. Para cualquier estrategia que dependa de registrar N dominios, el límite de 5 es el número operativo, no el precio.

La comparación con el otro extremo del mercado de identidad reinforces el punto: donde HOSTKEY hace del KYC una condición de pago obligatorio vía BitPay ([[2026-1024-hostkey-kyc-obligatorio-y-procesamiento-via-bitpay]]), Internet.bs no pide identidad a nadie y en su lugar **deduce la identidad del comportamiento** (IP, dispositivos, medios de pago, datos de facturación). Son dos respuestas distintas al mismo problema de abuso: verificación explícita frente a fingerprinting silencioso.

## Nota de verificación
La captura **no** publica: el precio estándar de .COM al que se cobra la diferencia, la duración del periodo promocional, ni el procedimiento concreto de verificación de elegibilidad. El texto es una declaración de términos del propio proveedor, transcrita literalmente.

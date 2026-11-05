---
id: 2026-1101-twilio-10dlc-y-cargo-de-mensaje-fallido-0-001
type: atom
certainty: solid
sources: [sources/2026-11-01-twilio-sms-pricing.md, sources/2026-11-03-twilio-sms-pricing.md]
links: ["[[2026-1101-twilio-cargos-de-operador-por-sms-y-costo-real-por-mensaje]]", "[[2026-1024-noones-verificacion-basica-l1plus-revision-manual-hasta-72h]]", "[[2026-1101-twilio-sms-base-0-0083-por-segmento-de-160-caracteres]]"]
---

## Claim
Sobre la tarifa por segmento se apilan dos costes más, cada uno con su propia regla: (a) los **cargos de registro (onboarding) de A2P 10DLC y de RCS** los fija la operadora y Twilio los traslada sin recargo — *"Twilio passes the fees through so you know exactly what you're paying"* — pero la captura **no publica ninguna cifra** de esos honourarios; y (b) un **cargo de procesamiento de $0.001 por mensaje** que se aplica *"only to messages that terminate in a 'Failed' status"*.

## 2026-11-03 — re-verificación
La captura del **2026-11-03** confirma **ambos cargos sin variación de cifra**: el $0.001 por mensaje fallido aparece en las notas al pie de las **dos** tablas (SMS/MMS y RCS) con la misma redacción, y la mención *"US A2P 10DLC are subject to registration onboarding fees"* / *"RCS senders launching on US carriers are subject to carrier onboarding fees"* también. El **hueco sigue abierto**: ninguna de las tres capturas publica la cifra de esos honourarios de registro — la captura del 3 de noviembre solo dice *"subject to registration onboarding fees"*. Confirmado además en el FAQ: *"US A2P 10DLC and RCS senders are subject to carrier registration onboarding fees. Twilio passes the fees through so you know exactly what you're paying, without increasing the price charged by the carriers."* Refuerza que el coste de A2P 10DLC es **la variable desconocida** de la unidad económica (ver [[2026-1101-twilio-a2p-10dlc-no-publica-diferencial-de-tarifa-frente-a-p2p]]).

## Why It Matters
El cargo de $0.001 no es un coste por mensaje sino un coste **por fallo**, y en un flujo de verificación por SMS el índice de fallos es alto (números virtuales bloqueados, operator filtering, timeout de entrega — ver la fricción de [[2026-1024-noones-verificacion-basica-l1plus-revision-manual-hasta-72h]]). Sobre el coste efectivo de $0.0128–$0.0133 por mensaje ([[2026-1101-twilio-cargos-de-operador-por-sms-y-costo-real-por-mensaje]]), un 100 % de fallos añade un 7–8 % al coste; si además hay reintento del mensaje (2 segmentos), el coste por verificación intentada se acerca a $0.027. La otra mitad del átomo es un hueco declarado: **el coste de A2P 10DLC es una cifra desconocida en el vault**, y es precisamente la partida que puede convertir un canal de $0.013 en un contrato de coste fijo mensual — hay que ir a la ayuda de Twilio (enlace `1260803965530`) a por ella antes de cerrar la unidad económica.

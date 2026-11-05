---
id: 2026-1101-twilio-a2p-10dlc-no-publica-diferencial-de-tarifa-frente-a-p2p
type: atom
certainty: solid
sources: [sources/2026-11-01-twilio-sms-pricing.md, sources/2026-11-03-twilio-sms-pricing.md]
links: ["[[2026-1101-twilio-10dlc-y-cargo-de-mensaje-fallido-0-001]]", "[[2026-1101-twilio-cargos-de-operador-por-sms-y-costo-real-por-mensaje]]", "[[2026-1031-twilio-sms-pricing]]"]
---

## Claim
La página **no publica ningún diferencial de tarifa entre A2P y P2P**: una sola tarifa de $0.0083 por segmento para long codes, toll-free y short codes, sin distinción por tipo de tráfico o por uso registrado. Lo que sí distingue al canal A2P es un coste **no tarifado**: *"US A2P 10DLC are subject to registration onboarding fees"* y *"RCS senders launching on US carriers are subject to carrier onboarding fees"*, ambos fijados por la operadora y trasladados por Twilio. La propia tabla de long code es la prueba: el mismo precio $0.0083 aplica a cualquier envío, A2P o P2P.

## Why It Matters
Corrige una hipótesis habitual al integrar Twilio en un flujo de verificación de cuentas: **no se paga "más" por enviar A2P**, se paga una cuota de registro recurrente de la operadora. Es decir, el discriminador real entre un remitente P2P barato y uno A2P conforme no está en el precio del mensaje ($0.0083 en ambos casos) sino en un coste fijo de onboarding cuyo importe **el vault no tiene** ([[2026-1101-twilio-10dlc-y-cargo-de-mensaje-fallido-0-001]]). Sin ese dato, cualquier comparativa Twilio-vs-5sim basada solo en el coste por mensaje es incompleta. Nota: la captura tampoco dice explícitamente que P2P no requiera registro, solo que el registro se menciona para A2P 10DLC y RCS — de ahí que este átomo afirme la **ausencia de diferencial tarifario publicado**, que es lo que sí consta en la fuente.

## 2026-11-03 — re-verificación
La captura del **2026-11-03** **confirma la ausencia de diferencial tarifario**: una única columna de precios, $0.0083 por segmento para long codes, toll-free y short codes, sin ninguna mención a A2P o P2P como factor de precio, y con la única distinción de coste en la nota *"US A2P 10DLC are subject to registration onboarding fees"* (sin cifra) y *"A failed message processing fee of $0.001 per message will be applied only to messages that terminate in a 'Failed' status"*. El FAQ añade el mismo dichotomy sin desglosar: *"US A2P 10DLC and RCS senders are subject to carrier registration onboarding fees."* Confirmado por tercera vez: **el discriminador entre un remitente P2P y uno A2P conforme no está en el precio del mensaje**, sino en un coste de onboarding cuyo importe el vault sigue sin tener ([[2026-1101-twilio-10dlc-y-cargo-de-mensaje-fallido-0-001]]).

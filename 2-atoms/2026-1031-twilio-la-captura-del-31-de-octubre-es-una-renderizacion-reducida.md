---
id: 2026-1031-twilio-la-captura-del-31-de-octubre-es-una-renderizacion-reducida
type: atom
certainty: solid
sources: [sources/2026-10-31-twilio-sms-pricing.md, sources/2026-11-03-twilio-sms-pricing.md]
links: ["[[2026-1031-twilio-sms-pricing]]", "[[2026-1101-twilio-sms-base-0-0083-por-segmento-de-160-caracteres]]", "[[2026-1101-twilio-10dlc-y-cargo-de-mensaje-fallido-0-001]]"]
---

## Claim
La captura del **2026-10-31** contiene las mismas cifras que las del 1 y 2 de noviembre (SMS US $0.0083, MMS $0.022, cargos de operador $0.0035–$0.005, números $1.15/$2.15) pero **sin las secciones que la página añade después**: no aparece la nota de **A2P 10DLC** ni el **cargo de $0.001 por mensaje fallido**, ni la tabla de carriers RCS, ni los short codes FTEU ($0.02), ni los grupos A/B con sus nombres, ni la sección de features con el Traffic Optimization Engine ($300/mes), ni los descuentos de uso comprometido, ni el FAQ. El título también difieren: *"Transparent, scalable, usage-based pricing for Twilio SMS and RCS"* frente a *"SMS and RCS pricing built to break even fast"*.

## Why It Matters
La tabla de precios **no cambió** entre el 31 de octubre y el 2 de noviembre: lo que cambió fue el *renderizado* de la misma página. Eso explica por qué [[2026-1031-twilio-sms-pricing]] pudo derivar un "$0.0075 por mensaje" que la propia captura del 31 no contiene (su tabla dice $0.0083) — la cifra del átomo viejo no está en ninguna de las tres fuentes. Regla operativa para el vault: **una captura parcial de una página de precios solo vale para lo que enumó**; para el coste real por mensaje hay que releer la versión con FAQ y cargos de operador ([[2026-1101-twilio-sms-base-0-0083-por-segmento-de-160-caracteres]], [[2026-1101-twilio-10dlc-y-cargo-de-mensaje-fallido-0-001]]).

## 2026-11-03 — re-verificación (el patrón se repite)
El **3 de noviembre** aparece una **segunda captura reducida** de la misma página, y por tanto el aviso de este átomo deja de ser un caso aislado: la URL `twilio.com/en-us/sms/pricing` ha producido al menos **tres renderizados distintos** en cuatro días — el reducido del 31 de octubre (3.551 bytes, sin FAQ ni cargos), los completos con markdown del 1 y 2 de noviembre (15.9 KB / 2.212 palabras) y el de texto plano del 3 de noviembre (9.029 bytes / 610 palabras). En ninguno de los tres cambia una sola cifra. Regla operativa consolidada: **el `word_count` mide la fidelidad de la captura, no el precio**; para extraer cifras hay que comparar las tablas, y para afirmar la existencia de un dato (TOE, descuentos comprometidos, nombres de grupos A/B, FAQ) hay que apoyarse en la fuente donde sí aparece, no asumirlo por su ausencia en otra ([[2026-1103-twilio-tercera-renderizacion-texto-plano-sin-algunas-secciones]]).

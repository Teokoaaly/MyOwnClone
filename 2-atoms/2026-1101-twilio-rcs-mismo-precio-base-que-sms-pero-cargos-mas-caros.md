---
id: 2026-1101-twilio-rcs-mismo-precio-base-que-sms-pero-cargos-mas-caros
type: atom
certainty: solid
sources: [sources/2026-11-01-twilio-sms-pricing.md, sources/2026-11-03-twilio-sms-pricing.md, sources/2026-11-04-twilio-sms-pricing.md]
links: ["[[2026-1101-twilio-cargos-de-operador-por-sms-y-costo-real-por-mensaje]]", "[[2026-1101-twilio-sms-base-0-0083-por-segmento-de-160-caracteres]]", "[[2026-1101-twilio-10dlc-y-cargo-de-mensaje-fallido-0-001]]"]
---

## Claim
RCS parte de la **misma tarifa base que el SMS** ($0.0083 por segmento para RCS Rich saliente y entrante; $0.022 por mensaje para RCS Rich Media, que a diferencia del texto se cobra por mensaje y no por segmento), pero los **cargos de operador de RCS son más caros** que los de SMS: AT&T $0.0045 (vs $0.0035 en SMS), T-Mobile $0.0062 (vs $0.0045), Verizon $0.005 con **$0 de inbound** (vs inbound no cotizado), US Cellular $0.0062 (vs $0.005), resto $0.0045 (vs $0.0042). Los remitentes RCS en operadores US están sujetos a cargos de onboarding de la operadora.

## 2026-11-03 — re-verificación
La captura del **2026-11-03** repite **sin una sola variación** tanto la tabla base de RCS (RCS Rich outbound e inbound $0.0083, RCS Rich Media outbound $0.022, inbound $0.0165) como la tabla de cargos de operador RCS: AT&T $0.0045/$0.0045/$0.01/$0.01, T-Mobile $0.0062/$0.0025/$0.0125/$0.0125, Verizon $0.005/**$0**/$0.007/**$0**, US Cellular $0.0062/$0.0025/$0.0135/$0.0135, resto $0.0045/$0.0045/$0.01/$0.01. Confirma además que la nota de la tabla RCS incluye el **cargo por mensaje fallido de $0.001** y la mención a los cargos de onboarding de operador US — y que la nota RCS sí conserva, a diferencia del FAQ de SMS, la regla explícita de que **RCS Rich Media se cobra por mensaje y RCS Rich texto por segmento**.

## Why It Matters
Para una verificación de cuentas, RCS no es un atajo de precio: **cuesta lo mismo la base y más en el recargo de operador**, así que el coste efectivo por mensaje RCS saliente queda en $0.0128–$0.0145 frente a $0.0108–$0.0133 del SMS ([[2026-1101-twilio-cargos-de-operador-por-sms-y-costo-real-por-mensaje]]). La única ventaja de precio sería el inbound de Verizon a $0 (el único $0 de inbound en toda la página), irrelevante para un flujo unidireccional de alta. La noticia relevante para el vault es la **paridad de plataforma**: RCS no es más caro ni más barato que SMS en Twilio, de modo que el cambio de canal no altera la unidad económica salvo por los cargos de onboarding ([[2026-1101-twilio-10dlc-y-cargo-de-mensaje-fallido-0-001]]).

## 2026-11-04 — re-verificación (cuarta captura de la tabla RCS)
La captura del **2026-11-04** (`sources/2026-11-04-twilio-sms-pricing.md`, 285 líneas, `word_count: 2212`) vuelve a renderizar la tabla RCS y la tabla de cargos de operador RCS **con cifras idénticas** a las del 1 y 3 de noviembre: RCS Rich saliente $0.0083 e entrante $0.0083, RCS Rich Media saliente $0.022 e entrante $0.0165; AT&T $0.0045/$0.0045/$0.01/$0.01, T-Mobile $0.0062/$0.0025/$0.0125/$0.0125, Verizon $0.005/**$0**/$0.007/**$0**, US Cellular $0.0062/$0.0025/$0.0135/$0.0135, resto $0.0045/$0.0045/$0.01/$0.01. **Ninguna cifra de RCS se movió** en la ventana del 1 al 4 de noviembre. La captura sí recupera, en cambio, la sección de nombres de los grupos A/B de short code (ver [[2026-1104-twilio-panhandle-telecom-aparece-en-los-dos-grupos-a-y-b]]) y la nota completa del descargo del recomendador con IA. Ver [[2026-1104-twilio-quinta-captura-identica-byte-a-byte-a-la-del-1-de-noviembre]].

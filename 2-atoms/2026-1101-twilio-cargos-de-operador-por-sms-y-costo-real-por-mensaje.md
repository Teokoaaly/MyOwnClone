---
id: 2026-1101-twilio-cargos-de-operador-por-sms-y-costo-real-por-mensaje
type: atom
certainty: solid
sources: [sources/2026-11-01-twilio-sms-pricing.md, sources/2026-11-03-twilio-sms-pricing.md, sources/2026-11-04-twilio-sms-pricing.md]
links: ["[[2026-1101-twilio-sms-base-0-0083-por-segmento-de-160-caracteres]]", "[[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
Sobre la tarifa base de $0.0083 se suman **cargos de operador por mensaje** que Twilio traslada sin margen: AT&T $0.0035, T-Mobile $0.0045, Verizon $0.005, US Cellular $0.005 en long code ($0.0045 en toll-free), resto de operadores $0.0042; en short code los grupos A/B cobran $0.0025 y $0.0042 y los short codes FTEU cobran **$0.02**. El coste efectivo por SMS saliente de un segmento queda en **$0.0108–$0.0133** ($0.0283 en FTEU). La página lo declara: *"Twilio passes the fees through so you know exactly what you're paying, without increasing the price charged by the carriers."*

## 2026-11-03 — re-verificación
La captura del **2026-11-03** reproduce **íntegras y sin variación** las cinco tablas de cargos de operador (RCS, long code, toll-free, short code y FTEU). Long code: AT&T $0.0035/$0.0035/$0.009/$0.009, T-Mobile $0.0045/$0.0025/$0.01/$0.01, Verizon $0.005/—/$0.007/—, US Cellular $0.005/$0.0025/$0.01/$0.01, resto $0.0042/—/$0.01/—. Toll-free: idéntico salvo US Cellular a $0.0045. Short code: US Cellular a $0.0045 y, además, **Other - Group A $0.0025** y **Other - Group B $0.0042** (solo outbound). FTEU: $0.02 de outbound en AT&T, T-Mobile y Verizon, celdas vacías en US Cellular y resto. El FAQ mantiene la fórmula *"AT&T charges $0.0035 for outbound SMS, while T-Mobile charges $0.0045"* y el *"Twilio passes the fees through…"*. Nota de fidelidad: esta captura **omite los nombres concretos de los miembros de los grupos A y B** (GoTextMe, Altice, TextNow, Dish Network, etc.), que sí constan en la fuente del 1 de noviembre — las cifras de $0.0025 y $0.0042 no cambian, solo se pierde la lista de operadores a los que aplican (ver [[2026-1103-twilio-tercera-renderizacion-texto-plano-sin-algunas-secciones]]).

## Why It Matters
Este es el número que hay que usar para la unidad económica de la verificación, no los $0.0083: el recargo de operador es **entre el 30 % y el 60 %** del coste real del mensaje. Con el cargo de operador dentro, el coste de un alta verificada por SMS en US queda en ~$0.012–$0.013, muy por debajo del $0.1026–$8.8897 que cobra 5sim por una activación ([[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]), pero con dos avisos: (a) Twilio no te da el número, solo el mensaje — el número sigue siendo el coste dominante del flujo de alta; (b) 1.000 verificaciones mensuales ≈ $12.80, que ya es un 12 % del presupuesto de un plan de $99 y multiplica por 3 el presupuesto de infraestructura del vault de ≤ 4 EUR/mes ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]). Conclusión operativa: Twilio es viable como canal de notificación, no como sustituto barato del número virtual.

## Actualización 2026-11-04 — re-verificación y contradicción en los grupos A/B
La captura del **2026-11-04** (`sources/2026-11-04-twilio-sms-pricing.md`, 285 líneas, `word_count: 2212`) reproduce **sin una sola variación** las cinco tablas de cargos de operador (RCS, long code, toll-free, short code y FTEU) y vuelve a renderizar los **nombres concretos de los miembros de los grupos A y B**, que la captura del 11-03 había omitido. Ninguna cifra se movió en la ventana del 1 al 4 de noviembre.

**Contradicción detectada en esta re-verificación:** la lista de miembros nombra **"Panhandle Telecom" en el grupo A y en el grupo B a la vez**, y los dos grupos tienen tarifas distintas ($0.0025 vs $0.0042 de salida en short code). El coste real de un SMS saliente a short code hacia ese operador **no queda determinado por la página**. Ver [[2026-1104-twilio-panhandle-telecom-aparece-en-los-dos-grupos-a-y-b]].

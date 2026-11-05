---
id: 2026-1104-twilio-quinta-captura-identica-byte-a-byte-a-la-del-1-de-noviembre
type: atom
certainty: solid
sources: [sources/2026-11-04-twilio-sms-pricing.md]
links: ["[[2026-1102-twilio-precio-estable-entre-capturas-del-1-y-2-de-noviembre]]", "[[2026-1103-twilio-tercera-renderizacion-texto-plano-sin-algunas-secciones]]", "[[2026-1101-twilio-sms-base-0-0083-por-segmento-de-160-caracteres]]"]
---

## Claim
La captura del **2026-11-04** de `twilio.com/en-us/sms/pricing` (285 líneas, `word_count: 2212`, 15.959 bytes) es **byte a byte idéntica** a la del **2026-11-01**: el `diff` entre `sources/2026-11-04-twilio-sms-pricing.md` y `sources/2026-11-01-twilio-sms-pricing.md` devuelve **una única línea distinta**, el campo `captured:` del frontmatter. Los md5 difieren solo por esa línea (`4cbc0555…` frente a `314fc38f…`). Es decir: es la **quinta captura** del slug y **ninguna cifra se movió** en los cuatro días — SMS base $0.0083, MMS outbound $0.022, MMS inbound $0.0165 / $0.02 (toll-free), RCS $0.0083 / $0.022 / $0.0165, cargo por mensaje fallido $0.001, cargos de operador (AT&T $0.0035, T-Mobile $0.0045, Verizon $0.005, US Cellular $0.005 long code / $0.0045 toll-free y short code, resto $0.0042, grupos A $0.0025 y B $0.0042, FTEU $0.02), números $1.15 / $2.15 / $1000 / $1500 / $500, add-ons $0.015 y Traffic Optimization Engine desde $300/mes.

## Why It Matters
Cierra con un punto de datos limpio la serie de estabilidad de precios de Twilio: la página es **estable en el tramo base público durante toda la ventana del 1 al 4 de noviembre**, con la única variación detectada en el contenido siendo la fidelidad del render del 11-03 ([[2026-1103-twilio-tercera-renderizacion-texto-plano-sin-algunas-secciones]]). Para la unidad económica del vault ([[2026-1101-twilio-sms-base-0-0083-por-segmento-de-160-caracteres]]) la consecuencia práctica es que **no hay deriva de precio que vigilar**: no hace falta recapturar Twilio salvo por un cambio de titular o de `word_count`, y la regla operativa ya escrita en [[2026-1102-twilio-precio-estable-entre-capturas-del-1-y-2-de-noviembre]] —"la señal de que cambió el precio es la cifra, no el `word_count` ni el titular"— queda validada por una quinta muestra. El tramo no observable (descuentos por volumen negociados con el account manager) sigue sin tabla pública, así que la estabilidad observada cubre solo la tarifa de lista.

## Nota de verificación
Comparación hecha con `diff` y `md5sum` sobre `sources/2026-11-01-twilio-sms-pricing.md` (15.959 bytes) y `sources/2026-11-04-twilio-sms-pricing.md` (15.959 bytes). Resultado: `3c3` — única diferencia la fecha de captura. Las cifras del Claim están transcritas literalmente de la fuente del 11-04 (tablas de SMS/MMS, RCS, Features, Carrier fees, Phone number pricing).

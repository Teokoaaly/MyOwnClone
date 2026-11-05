---
id: 2026-1102-twilio-precio-estable-entre-capturas-del-1-y-2-de-noviembre
type: atom
certainty: solid
sources: [sources/2026-11-02-twilio-sms-pricing.md, sources/2026-11-01-twilio-sms-pricing.md, sources/2026-11-03-twilio-sms-pricing.md, sources/2026-11-04-twilio-sms-pricing.md]
links: ["[[2026-1101-twilio-sms-base-0-0083-por-segmento-de-160-caracteres]]", "[[2026-1031-twilio-la-captura-del-31-de-octubre-es-una-renderizacion-reducida]]", "[[2026-1102-clerk-precios-sin-cambios-en-48-horas]]"]
---

## Claim
Las capturas del **2026-11-01** y del **2026-11-02** de `twilio.com/en-us/sms/pricing` son **idénticas en todas las cifras** (mismo `word_count: 2212`, mismos precios, mismas tablas, mismo "Pricing current as of October 2026"); lo único que cambia es el titular de la página —de *"Transparent, scalable, usage-based pricing…"* a *"SMS and RCS pricing built to break even fast"*— y la imagen del héroe. Ninguna cifra se movió en 24 horas.

## Why It Matters
Convierte una pregunta de seguimiento ("¿subió el precio de Twilio?") en trivial: **no hay deriva de precio entre capturas, solo deriva de marketing**. Es el mismo patrón que se acaba de documentar en otros proveedores ([[2026-1102-clerk-precios-sin-cambios-en-48-horas]]), y sirve para calibrar qué esperar del vault: una página de precios *pay-as-you-go* con descuentos por volumen negociados con el account manager (sin tabla pública) es un precio **estable y público solo en su tramo base**; el tramo negociado no se observa desde fuera. Consecuencia para el seguimiento: basta con re-capturar la página cuando cambie el titular o el `word_count`, no cada día.

## 2026-11-03 — re-verificación (tercer punto de datos)
La captura del **2026-11-03** (`word_count: 610`, 9.029 bytes) es un **tercer renderizado distinto** de la misma página — texto plano, sin markdown ni enlaces — pero **ninguna cifra se movió tampoco**: SMS base $0.0083, MMS outbound $0.022, MMS inbound $0.0165 / $0.02 (toll-free), RCS $0.0083 / $0.022 / $0.0165, cargo por mensaje fallido $0.001, cargos de operador (AT&T $0.0035, T-Mobile $0.0045, Verizon $0.005, US Cellular $0.005 long code / $0.0045 toll-free y short code, resto $0.0042, grupos A $0.0025 y B $0.0042, FTEU $0.02), números $1.15 / $2.15 / $1000 / $1500 / $500, add-ons $0.015. La etiqueta de vigencia sigue siendo **"SMS and RCS pricing current as of October 2026"** y el titular vuelve a ser *"SMS and RCS pricing built to break even fast"* (idéntico al del 2 de noviembre).

Lo que cambia es la **fidelidad del renderizado**, no el precio: el `word_count` cae de 2.212 a 610 porque desaparecen enlaces, imágenes y varios bloques de texto (FAQ de tarifa base, sección Committed-use discounts, fila del Traffic Optimization Engine, nombres de los grupos A/B, enlaces a los CSV). Refuerza la regla operativa de este átomo: **la señal de "cambió el precio" es la cifra, no el `word_count` ni el titular**; y una cifra que desaparece de una captura no debe tomarse como retirada de precio (ver [[2026-1103-twilio-tercera-renderizacion-texto-plano-sin-algunas-secciones]]).

## Actualización 2026-11-04 — re-verificación (quinto punto de datos)
La captura del **2026-11-04** (`sources/2026-11-04-twilio-sms-pricing.md`, 285 líneas, `word_count: 2212`, 15.959 bytes) es **byte a byte idéntica** a la del 2026-11-01 salvo el campo `captured:` del frontmatter, y reproduce las cifras de la captura del 11-02 sin una sola variación. La única diferencia con las capturas del 2 y 3 de noviembre es de **copy y de fidelidad de render**, no de precio: el titular y el subtítulo vuelven a la variante del 1 de noviembre (ver [[2026-1104-twilio-el-titular-vuelve-al-del-1-de-noviembre-tras-el-del-2-y-3]]) y el render recupera las secciones perdidas el día anterior (ver [[2026-1104-twilio-el-render-completo-restaurado-resuelve-la-friccion-del-11-03]]). Confirma por tanto que la señal de "cambió el precio" sigue siendo la cifra y no el titular ni el `word_count`.

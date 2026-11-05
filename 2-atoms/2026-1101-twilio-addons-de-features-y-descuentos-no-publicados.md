---
id: 2026-1101-twilio-addons-de-features-y-descuentos-no-publicados
type: atom
certainty: solid
sources: [sources/2026-11-01-twilio-sms-pricing.md, sources/2026-11-03-twilio-sms-pricing.md, sources/2026-11-04-twilio-sms-pricing.md]
links: ["[[2026-1101-twilio-sms-base-0-0083-por-segmento-de-160-caracteres]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1101-twilio-numeros-telefonicos-1-15-y-2-15-al-mes]]"]
---

## Claim
Los add-ons de features se cobran **por SMS saliente**, no como suscripción: Engagement Suite (acortado de enlaces, click tracking, programación) **$0.015** por SMS con *"the first 1,000 free monthly"*, y Compliance Toolkit **$0.015** por SMS saliente. El Traffic Optimization Engine empieza en **$300/mes**. Los descuentos por volumen **no tienen tabla pública**: se negocian con el account manager, y los descuentos de uso comprometido exigen un compromiso de volumen anual (*"Contact our sales team"*). Sobre el "Free Trial" solo se afirma *"Start for free. No credit card required"* — **la página no publica ningún saldo de SMS de prueba**.

## 2026-11-03 — re-verificación (parcial, con un hueco)
La captura del **2026-11-03** **confirma sin variación** los dos add-ons por SMS saliente: Engagement Suite **$0.015** con *"First 1,000 are free monthly"* y Compliance Toolkit **$0.015**, más la nota *"Prices may change from time to time without notice."* Confirma también el FAQ de descuentos: *"Twilio uses pay-as-you-go pricing… Work with your Twilio account team to discuss volume discounts as your messaging volume scales."*

**Hueco de esta captura (no una retirada):** el renderizado en texto plano **no incluye la fila del Traffic Optimization Engine ($300/mes)** ni la sección **Committed-use discounts** (enterprise con compromiso anual) que sí constaban en la fuente del 1 de noviembre. La cifra de $300/mes **no está refutada** por esta captura — simplemente no se ve. Es una tercera muestra de que la página se renderiza con distinta fidelidad, no de que los precios hayan cambiado (ver [[2026-1103-twilio-tercera-renderizacion-texto-plano-sin-algunas-secciones]]).

## Why It Matters
Tres consecuencias para el vault. (1) **El add-on de $0.015 duplica el coste del mensaje**: un SMS con Engagement Suite cuesta $0.0128 base + $0.015 = ~$0.028, más del doble que el mensaje limpio — así que el feature de tracking, si se activa, es una decisión de margen, no de producto ([[2026-1101-twilio-sms-base-0-0083-por-segmento-de-160-caracteres]]). (2) El Traffic Optimization Engine a $300/mes es **75 veces el presupuesto de infraestructura de ≤ 4 EUR/mes** ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]): queda descartado de antemano para MyOwnClone. (3) El único "gratis" publicado son 1.000 SMS de Engagement Suite al mes, no un tranche de prueba de mensajes: para un MVP que manda cientos de verificaciones, la variable de coste sigue siendo el tráfico ([[2026-1101-twilio-numeros-telefonicos-1-15-y-2-15-al-mes]]).

## Actualización 2026-11-04 — re-verificación (cuarta captura con la fila completa)
La captura del **2026-11-04** vuelve a renderizar la tabla de Features **completa**: el **Traffic Optimization Engine** reaparece con la misma cifra —*"Starting at $300 /month"*— y la sección **Committed-use discounts** vuelve con su texto íntegro (*"Commit to annual message volumes and receive a discount beyond standard volume tiers"*). El add-on de $300/mes queda **re-verificado con dato fresco**: el hueco del 11-03 fue un artefacto del extractor, no una retirada. Ver [[2026-1104-twilio-el-render-completo-restaurado-resuelve-la-friccion-del-11-03]].

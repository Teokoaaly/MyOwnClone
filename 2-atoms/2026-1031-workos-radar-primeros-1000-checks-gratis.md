---
id: 2026-1031-workos-radar-primeros-1000-checks-gratis
type: atom
certainty: solid
sources: [sources/2026-10-31-workos-pricing.md, sources/2026-11-03-workos-pricing.md]
links: ["[[2026-1101-clerk-protect-10000-checks-gratis-002-por-check]]", "[[2026-1031-workos-audit-logs-125-por-siem-y-99-por-millon-de-eventos]]", "[[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]]"]
---

## Claim
**Radar** de WorkOS (protección en tiempo real contra bots, fraude y abuso) se factura por checks: **los primeros 1.000 checks gratis** y **$100/mes por cada 50.000 checks** adicionales ("Per 50k checks").

## Why It Matters
Es una partida de consumo puro y sin suelo mensual: 1.000 checks gratis cubren una beta, pero el precio efectivo es **$0,002 por check** en el tramo de 50.000 ($100/50.000), lo que solo tiene sentido si el producto pasa la verificación de Radar en cada login o signup. Para MyOwnClone, que autentica usuarios finales de clones IA, el escenario de abuso (registros automatizados, mills de cuentas) es real y por tanto el coste no es hipotético: 10.000 logins/mes avoidance ≈ $200/mes, 50 veces el presupuesto de infra. El benchmark de Clerk es directamente comparable en unidad: **Protect da 10.000 checks gratis y $0,002 por check** ([[2026-1101-clerk-protect-10000-checks-gratis-002-por-check]]) — mismo precio unitario, distinto corte del tramo gratis, de modo que la elección entre ambos se decide por el volumen de checks, no por el precio por check. Nota: Audit Logs ([[2026-1031-workos-audit-logs-125-por-siem-y-99-por-millon-de-eventos]]) y Radar son líneas de coste **separadas** en WorkOS, no un bundle de seguridad.

## 2026-11-03 — re-verificación
La captura del 2026-11-03 confirma los dos tramos del bloque "### Pricing" de Radar: "First 1,000 checks — Free" y "Per 50k checks — $100 / mo". Novedad de matiz: el **deslizador de Radar llega hasta 2.5M+ checks** (escala "0 1K 50K 200K 400K 600K 800K 1M 1.5M 2M 2.5M+") y el bloque cierra con **"Need a plan that fits your scale?"** seguido del CTA "Schedule a call" — es decir, el autoservicio de Radar publica el precio hasta un volumen alto, pero el máximo del deslizador marca el punto en el que WorkOS deriva la conversación a un plan a medida ([[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]]). Con 2,5M de checks al tramo de $100/50k, la línea de Radar en su techo de autoservicio rondaría los **$5.000/mes**, cifra que solo tendría sentido para un producto con volumen de autenticación de plataforma.

## Nota de verificación
Sección Radar de la captura del 2026-10-31: "First 1,000 checks / Free" y "Per 50k checks / $100 / mo".

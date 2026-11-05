---
id: 2026-1023-hetzner-facturacion-por-hora-0-0096
type: atom
certainty: solid
sources: [sources/2026-10-22-hetzner-cloud.md, sources/2026-11-03-hetzner-cloud.md]
links: ["[[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]"]
---

## Claim
Hetzner Cloud ofrece **facturación por hora además de mensual**: la calculadora muestra para el CPX02 de 1 vCPU AMD un coste estimado de **€ 5.99 per month** y **€ 0.0096 per hour** (excl. VAT). La página no publica en la captura ningún umbral, mínimo mensual ni penalización por facturación horaria; solo el par de cifras.

## Why It Matters
Es la palanca que puede hacer viable el presupuesto de infra de [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]: €0.0096/h significa que un servidor encendido solo unas pocas horas al día cuesta céntimos, no €5.99. Eso es exactamente el perfil de uso de un entorno de desarrollo/pruebas o de un servidor que escala a cero entre pruebas, que es el patrón que la página recomienda para los planes compartidos. También fija el grano fino de coste con el que se puede comparar una carga sostenida: si el servidor debe estar siempre encendido, el umbral efectivo es el mensual (€5.99), y si puede apagarse, la factura sigue la carga real. El traffic allowance ([[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]) se añade como variable independiente.

## Nota de verificación
La captura no publica umbral mínimo de gasto, política de suspensión por bajo uso, ni si el precio por hora se redondea al alza o a la baja en el ciclo mensual. No se afirma ninguno de esos datos.

## Nota de extensión 2026-11-03
Fuente: `sources/2026-10-31-hetzner-cloud.md`, `sources/2026-11-01-hetzner-cloud.md`, `sources/2026-11-02-hetzner-cloud.md`. El par **€ 5.99/mes + € 0.0096/hora** del CPX02 de 1 vCPU AMD se repite **idéntico en las dos capturas que renderizan la calculadora** (2026-10-31 y 2026-11-02), con el mismo selector ("Shared Regular Performance / CPX02 1 VCPU AMD / per month € 5.99 / per hour € 0.0096 / excl. VAT"). La captura del 2026-11-01 no renderiza la calculadora, pero sí repite el bloque de planes con "starting from … € 5.99 per month, excl. VAT".

Esto **consolida** la palanca que este átomo describe: la facturación por hora a €0,0096/h hace que un servidor encendido a demanda cuesta céntimos, y la captura del 2026-11-02 confirma que el precio por hora no ha cambiado respecto a la del 2026-10-22. La granularidad de coste variable de infraestructura frente al coste por uso del producto (canales SMS y llamadas) sigue siendo comparable cifra a cifra. Ver [[2026-1102-hetzner-precio-de-entrada-5-99-no-4-67]] y [[2026-1031-hetzner-cloud]].

## 2026-11-03 — re-verificación
Fuente: `sources/2026-11-03-hetzner-cloud.md`. El par **€ 5.99 per month + € 0.0096 per hour** del CPX02 de 1 vCPU AMD (excl. VAT) se repite **idéntico** en la calculadora de esta captura, bajo la etiqueta "Estimated Cost". Confirma que la facturación por hora sigue siendo la palanca que hace viable el presupuesto de ≤ €4/mes ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]) sin cambiar la facturación mensual. La ausencia ya señalada sigue vigente: la captura **no publica** umbral mínimo de gasto, política de suspensión por bajo uso ni política de redondeo del precio por hora. Ver [[2026-1103-hetzner-cinco-capturas-estabilidad-catalogo-vs-widgets-dinamicos]].

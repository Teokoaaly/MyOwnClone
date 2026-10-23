---
id: 2026-1023-hetzner-facturacion-por-hora-0-0096
type: atom
certainty: solid
sources: [sources/2026-10-22-hetzner-cloud.md]
links: ["[[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]"]
---

## Claim
Hetzner Cloud ofrece **facturación por hora además de mensual**: la calculadora muestra para el CPX02 de 1 vCPU AMD un coste estimado de **€ 5.99 per month** y **€ 0.0096 per hour** (excl. VAT). La página no publica en la captura ningún umbral, mínimo mensual ni penalización por facturación horaria; solo el par de cifras.

## Why It Matters
Es la palanca que puede hacer viable el presupuesto de infra de [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]: €0.0096/h significa que un servidor encendido solo unas pocas horas al día cuesta céntimos, no €5.99. Eso es exactamente el perfil de uso de un entorno de desarrollo/pruebas o de un servidor que escala a cero entre pruebas, que es el patrón que la página recomienda para los planes compartidos. También fija el grano fino de coste con el que se puede comparar una carga sostenida: si el servidor debe estar siempre encendido, el umbral efectivo es el mensual (€5.99), y si puede apagarse, la factura sigue la carga real. El traffic allowance ([[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]) se añade como variable independiente.

## Nota de verificación
La captura no publica umbral mínimo de gasto, política de suspensión por bajo uso, ni si el precio por hora se redondea al alza o a la baja en el ciclo mensual. No se afirma ninguno de esos datos.

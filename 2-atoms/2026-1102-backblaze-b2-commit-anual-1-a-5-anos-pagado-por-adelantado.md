---
id: 2026-1102-backblaze-b2-commit-anual-1-a-5-anos-pagado-por-adelantado
type: atom
certainty: solid
sources: [sources/2026-10-31-backblaze-b2-storage-pricing.md, sources/2026-11-01-backblaze-b2-storage-pricing.md, sources/2026-11-02-backblaze-b2-storage-pricing.md, sources/2026-11-03-backblaze-b2-storage-pricing.md]
links: ["[[2026-1102-backblaze-b2-precio-6-95-por-tb-al-mes]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
Backblaze B2 ofrece dos modos de facturación: "**Pay as you go monthly or for capacity annually**", con commit de **1 a 5 años** en el que "You're billed for the full term **at contract start**, and your rate is locked for the length of the contract"; además "Discounts available with volume & term commitments".

## Why It Matters
El commit anual es un pago por adelantado de 12 a 60 meses, y por tanto choca de frente con la escala del vault: el presupuesto de ≤ €4/mes documentado en [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]] es un presupuesto de flujo, no de caja. Con un solo año de capacidad pagada por adelantado, el desembolso inicial multiplica por 12 cualquier cifra de almacenamiento, y para una MyOwnClone con un solo VPS de $4/mes el storage de B2 es una línea marginal — lo que hace que el compromiso plurianual solo tenga sentido cuando el volumen de datos es grande y estable, o cuando el volumen de tenants ya justifica una reserva fija. La operación relevante del vault es la de **no comprometer** ante un proveedor de object storage cuando la variable dominante del coste sigue siendo el asiento SaaS (ver [[2026-1102-backblaze-b2-precio-6-95-por-tb-al-mes]]): el descuento por compromiso solo es rentable si el uso se mantiene, y en un producto en fase de crecimiento el riesgo de pagar por capacidad no usada es mayor que el ahorro.

## 2026-11-03 — re-verificación
El régimen de commit se re-verifica **sin cambios**: la ficha de B2 mantiene "Pay as you go monthly or for capacity annually" y "Discounts available with volume & term commitments"; la FAQ mantiene "You can also commit to a set amount of storage for a term of **1 to 5 years**. You're billed for the full term **at contract start**, and your rate is locked for the length of the contract".

**Detalle nuevo que sí aporta esta captura**: la tabla "Payment" queda legible con sus tres filas —"Billing term: Monthly / Annual from 1-5 years", "Billing timing: Monthly / **Contract start**", "Method: **Credit card or invoice** / **Invoice**"— lo que fija que el pago mensual admite tarjeta o factura, mientras que el anual **exige factura por adelantado**, sin tarjeta. Es el detalle que convierte el compromiso plurianual en una operación de caja y de crédito, no solo de descuento (ver [[2026-1103-backblaze-b2-soporte-y-migracion-como-add-ons]]).

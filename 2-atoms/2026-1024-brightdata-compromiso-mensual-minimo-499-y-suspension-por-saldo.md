---
id: 2026-1024-brightdata-compromiso-mensual-minimo-499-y-suspension-por-saldo
type: atom
certainty: solid
sources: [sources/2026-10-24-brightdata-proxy-pricing.md]
links: ["[[2026-1024-brightdata-prorrateo-por-dias-activos-en-el-mes-de-alta]]", "[[2026-1024-brightdata-auto-recharge-con-umbral-25-y-carga-mensual]]", "[[2026-1024-brightdata-escalera-de-volumen-141-a-798-gb]]"]
---

## Claim
El ciclo de facturación de Bright Data arranca el **1 de cada mes** y el compromiso mínimo se cobra automáticamente ese día mientras la cuenta esté "active". El control de saldo funciona con tres umbrales: **aviso por email al 85 %** del saldo consumido, la cuenta **sigue operando hasta el 100 %**, y al llegar al 100 % **se suspende** salvo que se añadan fondos. El proveedor recomienda activar la recarga automática. Además, **si la cuenta no está "active" todo el mes, el saldo restante no se pierde**: al día 1 siguiente se cobra lo que falte para devolver el saldo al compromiso mínimo.

## Why It Matters
Es un contrato de **saldo prepagado con compromiso mensual**, y describe un modo de fallo que el sector de SMS ya tenía ([[2026-1023-sms-activate-cierra-total-el-22-de-diciembre]]): el corte es **por saldo, no por uso**. Una cuenta suspendida deja de servir tráfico en mitad de un flujo de altas, y una IP dedicada **se pierde al suspender** (ver átomo de IPs asignadas). El umbral del 85 % es generoso —da 15 puntos de margen— pero el corte es total y sin aviso intermedio.
Y hay un segundo detalle asimétrico: **la suspensión es cara y la inactividad no**. Si la cuenta estuvo inactiva parte del mes, el saldo retenido se **cobra** al día 1 para reponer el compromiso; si estuvo activa, el compromiso se **gasta** igual aunque no se haya consumido nada. En los dos casos el compromiso se paga: es un coste fijo mensual disfrazado de prepago.

## Nota de verificación
Textos transcritos literalmente. La captura **no** publica: si el aviso del 85 % es por email únicamente, si hay aviso por dashboard, ni el mecanismo exacto de suspensión (corte de red, revocación de credenciales o ambas).

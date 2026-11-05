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


## Nota de extensión 2026-10-26
La documentación de billing del 2026-10-25 (`sources/2026-10-25-brightdata-free-tier.md`) añade **dos datos que la página de precios no recogía** y que acotan este átomo. La primera: el free tier **no es compatible con los planes pre-commit** —*"If you upgrade to a pre-commit plan, recurring monthly free credits will no longer be issued"*— de modo que los **$499/mes de compromiso mínimo y la cuota mensual de 5.000 créditos gratuitos son mutuamente excluyentes**; el único plan que conserva el free tier es el PAYG "No commitment" ([[2026-1024-brightdata-payg-a-4-por-gb-sin-compromiso]]). La segunda: **el régimen de PAYG es distinto**, no una variante —*"Bright Data operates on a pre-paid wallet model: you are only ever charged for funds you have explicitly deposited... There is no minimum commitment. You stay on PAYG and only pay for what you use"*— con **tope duro** sin fondos (*"hard stop... never a surprise bill"*) y continuidad automática contra el saldo con fondos. Es decir, la Suspensión por saldo que este átomo describe **pertenece al régimen de suscripción**, y el modelo wallet prepago del free tier/PAYG no tiene ni compromiso ni reposición al día 1. Ver [[2026-1026-brightdata-wallet-prepagado-con-tope-duro-y-sin-factura-sobrevenida]] y [[2026-1026-brightdata-upgrade-a-pre-commit-detiene-los-creditos-gratis]].

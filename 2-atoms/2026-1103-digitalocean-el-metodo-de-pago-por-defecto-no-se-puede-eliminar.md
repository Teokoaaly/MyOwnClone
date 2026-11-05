---
id: 2026-1103-digitalocean-el-metodo-de-pago-por-defecto-no-se-puede-eliminar
type: atom
certainty: solid
sources: [sources/2026-11-03-digitalocean-droplets-pricing.md]
links: ["[[2026-1102-digitalocean-no-ofrece-reembolsos-y-el-prepago-solo-via-ventas]]", "[[2026-1103-digitalocean-alertas-de-facturacion-por-email-al-superar-un-umbral]]", "[[2026-1102-digitalocean-credito-promocional-de-5-dolares-que-cubre-el-droplet-de-entrada]]"]
---

## Claim
La FAQ de la página de precios documenta el procedimiento para **eliminar un método de pago guardado**: se va a la página de billing de productos, se abre el menú "…" del método de pago, se pulsa Delete y se confirma en la ventana "Confirm Delete Card". La captura añade la restricción explícita: **"You cannot remove the default payment method on the account"** — el método de pago por defecto **no se puede eliminar**.

## Why It Matters
Es el otro lado de una cadena de condiciones comerciales que el vault está documentando para este proveedor: **no hay reembolsos** ([[2026-1102-digitalocean-no-ofrece-reembolsos-y-el-prepago-solo-via-ventas]]), el prepago **solo se negocia con ventas**, el crédito promocional se consume automáticamente y la tarjeta se cobra cuando el crédito se agota o caduca ([[2026-1102-digitalocean-credito-promocional-de-5-dolares-que-cubre-el-droplet-de-entrada]]), y ahora se añade que **la tarjeta de cierre no es retirable por el cliente**: la cuenta queda atada a un método de pago mientras exista saldo o crédito. Sumado a las alertas de umbral por email ([[2026-1103-digitalocean-alertas-de-facturacion-por-email-al-superar-un-umbral]]), el perfil de riesgo de DO queda claro: el cliente tiene visibilidad del gasto pero no control del cierre, y la única defensa real es la disciplina de dimensionado —arrancar por el tramo más bajo y no crecer sin verificación.

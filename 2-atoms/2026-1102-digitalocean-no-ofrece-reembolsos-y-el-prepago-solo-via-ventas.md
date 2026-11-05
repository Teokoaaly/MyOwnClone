---
id: 2026-1102-digitalocean-no-ofrece-reembolsos-y-el-prepago-solo-via-ventas
type: atom
certainty: solid
sources: [sources/2026-11-02-digitalocean-droplets-pricing.md, sources/2026-11-03-digitalocean-droplets-pricing.md]
links: ["[[2026-1024-buyvm-comparativa-precios-15-al-mes-contra-aws-do-linode-y-vultr]]", "[[2026-1031-digitalocean-entrada-basic-512-mib-4-dolares-al-mes]]", "[[2026-1023-hetzner-facturacion-por-hora-0-0096]]"]
---

## Claim
La FAQ de precios de DigitalOcean declara dos condiciones comerciales que no aparecen en ninguna tabla: **"We do not offer refunds. If there are extenuating circumstances, contact support"** (no hay reembolsos) y, sobre el prepago, **"If you are interested in prepayment for resources, contact our experts"** — es decir, **el prepago no es un producto de autoservicio, se negocia con el equipo comercial**. La respuesta de reembolso está completa en las capturas del **2026-10-31, 2026-11-01 y 2026-11-02**; la de prepago solo aparece en las del **2026-10-31 y 2026-11-02** (en la del 2026-11-01 la pregunta aparece sin respuesta).

## Why It Matters
Es una asimetría estructural frente al tramo barato del vault, donde el prepayment **es** el producto: los planes anuales de LEB o BuyVM se compran por adelantado precisamente porque el descuento solo existe así. En DigitalOcean el orden está invertido —el cliente paga mes a mes y **no puede recuperar el dinero si se equivoca**—, lo que invierte el cálculo de riesgo de todo el tramo barato: aquí el error de dimensionado se paga íntegro, sin salida, mientras que allí el riesgo se compensa con un año pagado a mitad de precio. Combinado con la facturación por segundo ([[2026-1101-digitalocean-facturacion-por-segundo-con-minimo-de-60-segundos]]), la postura resultante es asimétrica a favor del usuario **en el día a día** (se paga lo que se usa) y **en contra en el error** (no hay devolución). Para un presupuesto de ≤ €4/mes la consecuencia práctica es que lo único que se puede hacer con un proveedor sin reembolso es **arrancar por el tramo más bajo y crecer solo tras verificar**, nunca al revés.

## 2026-11-03 — re-verificación
La captura del **2026-11-03** vuelve a publicar **verbatim las dos respuestas**: "We do not offer refunds. If there are extenuating circumstances, contact support" y "If you are interested in prepayment for resources, contact our experts". Esto **actualiza el recuento de capturas** de esta nota: la respuesta de reembolso aparece completa en las **cuatro** capturas (10-31, 11-01, 11-02, 11-03), y la de prepago en las **tres** en las que aparece esa FAQ (10-31, 11-02, 11-03), con el mismo hueco del 11-01 (pregunta sin respuesta). Ninguna de las dos condiciones comerciales ha cambiado; el bloque de "…" del 11-03 cae antes de estas FAQ, que sí sobreviven al render reducido.

## Nota de verificación
Ambas respuestas son verbatim de la captura del 2026-11-02. La diferencia con la captura del 2026-11-01 (pregunta de prepago sin respuesta) es una observación sobre **la calidad de la captura**, no sobre las condiciones del proveedor: la fuente del 2026-11-02 es la que hace de respaldo y por eso este átomo se ancla a ella. La captura **no publica** condiciones de prepago concretos (plazo, descuento, importe mínimo) porque el prepago requiere contacto comercial.

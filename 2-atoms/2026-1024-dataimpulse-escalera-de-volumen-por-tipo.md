---
id: 2026-1024-dataimpulse-escalera-de-volumen-por-tipo
type: atom
certainty: solid
sources: [sources/2026-10-23-dataimpulse-proxies.md]
links: ["[[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]", "[[2026-1024-dataimpulse-payg-sin-suscripcion-ni-caducidad]]", "[[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]"]
---

## Claim
La tabla de precios de DataImpulse define cuatro escalones de volumen por cada tipo de proxy, con el volumen nominal de cada plan y su $/GB: **residencial** — Intro $5 (5GB) a $1/GB, Basic $50 (50GB) a $1/GB, Advanced $800 (1TB) a $0.8/GB, Custom+ desde $4000 (5TB+) con "Custom price per GB"; **datacenter** — Intro $5 (10GB) a $0.5/GB, Basic $50 (100GB) a $0.5/GB, Advanced $450 (1TB) a $0.45/GB, Custom+ desde $2250 (5TB+); **móvil** — Intro $5 (2.5GB) a $2/GB, Basic $50 (25GB) a $2/GB, Advanced $1600 (1TB) a $1.6/GB, Custom+ desde $8000 (5TB+); **premium residencial** — Intro $5 (1GB) a $5/GB, Basic $50 (10GB) a $5/GB, Custom+ desde $20000 (5TB+), sin escalón Advanced. La prosa añade: *"if you buy more than 1TB, the price is $0.8/GB"* y *"Custom pricing is available for 5TB+ usage"*.

## Why It Matters
El descuento por volumen es **mucho más plano de lo que sugiere el marketing de "no tier jumps"**: en residencial, pasar de 5GB a 50GB no cambia el $/GB ($1 en ambos) y el único salto de precio unitario real es a $0.8/GB en el escalón de 1TB — un 20 % de descuento por multiplicar el gasto x160. En datacenter el descuento real es de $0.5 a $0.45 (10 %) y en móvil de $2 a $1.6 (20 %). Quien necesita mucho volumen ([[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]): el punto de economies of scale real está en el contrato Custom+ de 5TB+, no en el autoservicio.
La contradicción interna importa para el cálculo: la tabla aplica $0.8/GB ya en el escalón "Advanced" de **1TB**, mientras la prosa dice que $0.8/GB es el precio "si compras más de 1TB". Con el plan Advanced de 1TB, el desglose no cuadra al alza (1TB × $0.8 ≈ $819 frente a los $800 listados) y en datacenter 1TB × $0.45 = $460 frente a $450, mientras en móvil el Advanced de 1TB a $1.6/GB implica ~$1600 sí cuadra. Es un dato que hay que tomar con pinzas antes de usarlo como base de una proyección de gasto.

## Nota de verificación
Volúmenes, importes y $/GB transcritos literalmente de las cuatro tablas de la sección "Pricing". La captura **no** publica: si el Custom+ de 5TB+ se factura por adelantado o por consumo, ni qué volumen nominal corresponde exactamente al tramo 5TB+, ni si el descuento por volumen se aplica retroactivamente al saldo ya comprado.

---
id: 2026-1024-extravm-upgrade-con-prorrateo-pero-sin-downgrade
type: atom
certainty: solid
sources: [sources/2026-10-23-extravm-vps-pricing.md]
links: ["[[2026-1024-extravm-escalera-de-precios-14-planes-de-4-50-a-192]]", "[[2026-1024-extravm-renovacion-cripto-manual-y-credito-en-cuenta]]", "[[2026-1024-evoxt-despliegue-100-automatico-y-upgrade-con-un-boton]]"]
---

## Claim
ExtraVM permite **subir de plan en cualquier momento contacting support**, con **facturación prorrateada** por el resto del ciclo: "you can upgrade your VPS plan at any time by contacting support. Upgrades are processed with prorated billing for the remainder of your billing cycle." Y declara explícitamente lo contrario: **"Due to technical limitations, we cannot downgrade your VPS plan."** El proceso es, por tanto, **manual y humano**, no self-service.

## Why It Matters
Es un límite operativo asimétrico que afecta al plan de crecimiento de la infraestructura del vault: **subir es fácil y barato, bajar es imposible**. Para un producto en beta con tráfico creciente ([[2026-1022-beta-activo-trafico-real]]), eso significa que el plan sedimensiona hacia arriba de forma irreversible: empezar en un plan de 2 GB y pasarlo a 4 GB no tiene vuelta atrás si luego el uso baja. Y a diferencia de Evoxt, donde el escalado es un botón y automático ([[2026-1024-evoxt-despliegue-100-automatico-y-upgrade-con-un-boton]]), aquí el upgrade **requiere intervención del soporte**, lo que añade un paso humano a cualquier cambio de capacidad — y en el proveedor con renovación de cripto manual ([[2026-1024-extravm-renovacion-cripto-manual-y-credito-en-cuenta]]) ese mismo soporte es el que emite la factura y procesa el pago.

## Nota de verificación
La captura no publica el plazo de aplicación del prorrateo, si el discount es por el ciclo completo o solo por los días restantes, ni si el cambio de plan implica migración de disco o reinstalación.

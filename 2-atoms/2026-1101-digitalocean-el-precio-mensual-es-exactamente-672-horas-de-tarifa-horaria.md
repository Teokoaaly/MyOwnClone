---
id: 2026-1101-digitalocean-el-precio-mensual-es-exactamente-672-horas-de-tarifa-horaria
type: atom
certainty: tentative
sources: [sources/2026-11-01-digitalocean-droplets-pricing.md, sources/2026-11-03-digitalocean-droplets-pricing.md]
links: ["[[2026-1031-digitalocean-entrada-basic-512-mib-4-dolares-al-mes]]", "[[2026-1023-hetzner-facturacion-por-hora-0-0096]]", "[[2026-1101-digitalocean-facturacion-por-segundo-con-minimo-de-60-segundos]]"]
---

## Claim
En la tabla Basic, **el precio mensual es exactamente 672 horas de la tarifa horaria**: $0.00595/h × 672 h = $3,998 ≈ **$4.00**; $0.00893 × 672 = **$6,00**; $0.01786 × 672 = **$12,00**; $0.02679 × 672 = **$18,00**; $0.03571 × 672 = **$24,00**; $0.07143 × 672 = **$48,00**; $0.14286 × 672 = **$96,00**. La relación se repite exacta en las demás familias (p. ej. CPU-Optimized: $0.06250 × 672 = **$42,00**; Storage-Optimized: $0.19494 × 672 = **$131,00**). 672 h son **28 días**: frente a un mes de 720 h, el techo mensual equivale a un **descuento efectivo del 6,67 %**.

## Why It Matters
Da al vault una medida comparable para el eje "precio por hora vs precio mensual", que hasta ahora solo tenía resuelto en Hetzner con un suelo de $0,0096/h ([[2026-1023-hetzner-facturacion-por-hora-0-0096]]). En DigitalOcean el mes comprometido no es un descuento comercial sino un **techo aritmético**: la página lo dice literalmente ("Bundled Plans have a monthly cap, so you'll never pay more than the flat monthly price for that plan"), así que un Droplet encendido 24/7 durante 30 días cuesta un 6,67 % más que el precio mensual si se factura por hora. La consecuencia práctica para el presupuesto de ≤ €4/mes es que **el compromiso mensual es gratis**: no hay penalización por reserva previa, y por tanto la única variable de decisión es qué plan se enciende, no cómo se factura. Es además la forma más limpia de leer el "descuento" que el vault encuentra en otras ofertas anuales prepagadas (LowEndBox, BuyVM), donde el descuento sí cuesta meses de compromiso anticipado: aquí el descuento se cobra en forma de **tiempo de permanencia en el plan**.

## 2026-11-03 — re-verificación
La captura del **2026-11-03** reproduce las **31 filas** de las cinco tablas, con los mismos valores, y vuelve a cumplirse la relación $precio_mensual = $tarifa_horaria × 672 en todas ellas (p. ej. $0.00595 → $4.00, $0.06250 → $42.00, $0.09375 → $63.00, $0.12500 → $84.00, $0.19494 → $131.00, $1.50000 → $1,008.00, $1.55952 → $1,048.00, $3.11905 → $2,096.00). La igualdad se sostiene por **cuarta captura consecutiva**. La atribución del descuento a "28 días" sigue siendo **inferencia de este átomo**: la fuente no enuncia ni el 672 ni el 6,67 % en ningún punto, y esta captura no añade ninguna frase que lo confirme.

## Nota de verificación
La igualdad $precio_mensual = $tarifa_horaria × 672 es un **cálculo de este átomo** sobre las cifras verbatim de las tablas; la fuente **no enuncia ni el número 672 ni el porcentaje 6,67 %** en ningún punto. La coincidencia se ha verificado en **las 31 filas de las cinco tablas** de la captura del 2026-11-02 (Basic ×7, CPU-Optimized ×6, General Purpose ×6, Memory-Optimized ×6, Storage-Optimized ×6), sin una sola discrepancia, lo que hace muy improbable que sea casualidad; pero la atribución del descuento a "28 días" es una inferencia del átomo, no una frase del proveedor.

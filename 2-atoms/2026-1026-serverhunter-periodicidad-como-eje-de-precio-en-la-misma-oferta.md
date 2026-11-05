---
id: 2026-1026-serverhunter-periodicidad-como-eje-de-precio-en-la-misma-oferta
type: atom
certainty: solid
sources: [sources/2026-10-25-serverhunter-cheap-vps.md]
links: ["[[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]]", "[[2026-1024-lowendbox-vps-anuales-de-10-a-11-dolares-no-mensuales]]", "[[2026-1026-serverhunter-suelo-de-029-con-128-mb-y-ipv4-nat]]"]
---

## Claim
ServerHunter publica **la misma oferta con el mismo nombre a precios distintos según el periodo de facturación**, como filas separadas de la tabla, y **la periodicidad se marca de dos formas distintas**: en el nombre de la oferta (sufijos "(Annual)" y "(Semiannual)") y en una etiqueta propia ("Annual billing", "Semiannual"). Los cuatro pares observables son:

| Oferta | Periodicidad barata | Periodicidad cara | Descuento |
| --- | --- | --- | --- |
| `NanoVPS-II 384 Low-Cost Special US` (384 MB, NVMe 8 GB, 1 core Xeon Gold 6138) | **$0.29**, etiqueta "Annual billing" | **$0.33**, sin marca de periodicidad | **12,1 %** |
| `NanoVPS-II 384 Europe` (512 MB, NVMe 20 GB, 1 core Ryzen 9 3900) | **$0.31**, nombre "(Annual)" | **$0.42**, nombre "(Semiannual)" + etiqueta "Semiannual" | **26,2 %** |
| `NanoVPS-384 Low-Cost Special US` (384 MB, NVMe 12 GB, Xeon Silver 4116) | **$0.32**, nombre "(Annual)" | **$0.40**, nombre "(Semiannual)" + etiqueta "Semiannual" | **20,0 %** |
| `NanoVPS-1024 US` (1 GB, NVMe 15 GB, 3 cores Xeon Gold 6138) | **$0.58**, etiqueta "Annual billing" | **$0.66**, sin marca de periodicidad | **12,1 %** |

En los cuatro pares las specs (memoria, disco, CPU) son idénticas; lo único que cambia es el precio.

## Why It Matters
Convierte la periodicidad en un **eje de precio explícito y cuantificado**, que es exactamente lo que el vault no tenía: hasta ahora la periodicidad era una incógnita o un dato único ([[2026-1024-lowendbox-vps-anuales-de-10-a-11-dolares-no-mensuales]] medía el prepago anual como condición, y el átomo de Evoxt señalaba que **el precio no publica su periodicidad** y que por tanto "$2,99" no puede afirmarse como $/mes ([[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]])). Aquí queda demostrado con la misma oferta servida en dos filas: **el compromiso anual puede valer hasta un 26,2 % menos que el mismo servidor en otro compromiso**, un número que es un coste de flujo de caja directo del producto. Y el detalle de que **la periodicidad se codifique de dos maneras distintas** explica por qué la captura no puede leerse de un solo campo: un scraper que solo mirara las etiquetas perdería la mitad de los pares.

## [FRICTION]
> [[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]] afirma que "el precio más barato del catálogo de VPS de Evoxt es el **VM-0.5 a USD $ 2.99**" y su propia nota de verificación admite que la captura "**no publica: periodicidad (mensual o anual)**", por lo que la comparación en euros exige además tipo de cambio y no puede fijar un $/mes.
> ServerHunter demuestra que la periodicidad no es un matiz menor sino **un eje de precio de hasta el 26,2 % sobre la misma oferta y las mismas specs**. Eso no refuta la cifra de Evoxt —no dice cuál es su periodicidad— pero **destruye la posibilidad de situar los $2.99 en la escala del vault sin corregirla**: si su $2.99 fuera un precio anual, su equivalente mensual sería ~$0,25 y sería el suelo del mercado; si fuera mensual, pagaría hasta un 26 % más que el mismo servidor con compromiso anual. El vault está usando esa cifra como *punto medio* de la escalera (entre HostBrr €2,00 y Hetzner €5,99) sobre una unidad que la fuente no declara.
> Marcado para juicio humano, no auto-resuelto: ServerHunter no cubre a Evoxt en sus filas visibles y su captura no incluye la ficha de periodicidad de Evoxt.

## Nota de verificación
Precios, nombres, etiquetas y specs están transcritos literalmente; en cada par las specs se han comprobado fila a fila y coinciden. Los porcentajes (12,1 %, 26,2 %, 20,0 %) son **cálculo del átomo** sobre esas cifras; la fuente no los publica. La lectura de que las dos filas son "la misma oferta con dos periodos" es la interpretación más probable —el nombre, el proveedor y las specs coinciden exactamente— pero ServerHunter **no lo explica**, y en dos de los cuatro pares la fila cara carece de toda marca de periodicidad.

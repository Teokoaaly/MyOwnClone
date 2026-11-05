---
id: 2026-1026-heroku-fir-general-purpose-2cpu-4gb-dice-1-vcpu
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-pricing.md]
links: ["[[2026-1026-heroku-fir-dynos-kubernetes-todos-requieren-private-space-desde-25]]", "[[2026-1026-heroku-dyno-units-25-dolares-por-unidad-excepto-performance]]", "[[2026-1024-extravm-escalera-de-precios-14-planes-de-4-50-a-192]]"]
---

## Claim
La tabla de Fir Dynos tiene **una fila internamente inconsistente**: **"General Purpose 2CPU-4GB"** declara en la columna de nombre **2CPU**, pero la fila publica **vCPUs = 1**, **RAM = 4 GB**, **Price / Month = $80** y, en "More Details", **"Plan: dyno-1c-4gb"** — es decir, el identificador de plan delata **1 vCPU**, no 2. Las demás 16 filas son coherentes entre nombre, columna de vCPUs y `plan id` (Classic 1CPU-0.5GB → `dyno-1c-0.5gb`; Compute 32CPU-64GB → `dyno-32c-64gb`; Memory 16CPU-128GB → `dyno-16c-128gb`; etc.).

## Why It Matters
Es un **defecto de catálogo**, no una opinión, y importa por dos razones. La primera, de rigor: el vault está construyendo una tabla de precios de referencia con valores textuales, y **esta fila no se puede transcribir sin decidir qué columna manda**. Un lector que copie "2CPU-4GB" como nombre y "$80" como precio construye una fila que dice 2 vCPU cuando la página dice 1. En la comparación de precios por vCPU, **$80 por 1 vCPU y $80 por 2 vCPU son dos precios distintos**, y el error va en la dirección de hacer el producto más barato de lo que es.
La segunda, de patrón: es el mismo tipo de fricción que el vault ya vio en el tramo barato — **la etiqueta comercial del plan y la especificación técnica no coinciden** (el "Value VPS" de HostBrr que dice "2GB" y el nombre del producto que dice otra cosa, o los planes que prometen una cosa y el panel publica otra). Es un recordatorio de que en el tramo de precio bajo **la única columna fiable es la que se puede verificar**, y en este caso esa columna es el `plan id`, porque es el identificador que se compra de verdad en el marketplace.
Y tiene una consecuencia práctica para la comparación de **precio por unidad de cómputo**: si el `plan id` manda, la fila "General Purpose 2CPU-4GB" a $80 son **$80 por 1 vCPU con 4 GB**, lo que la sitúa en el tramo más caro por vCPU de toda la familia General Purpose ($25, $50, $80, $160, $320, $640, $1,200) y la hace **incoherente con el patrón de duplicación por vCPU** que sí se cumple en las otras filas.

## Nota de verificación
La inconsistencia es lectura literal de la fila: el nombre dice "2CPU", la columna vCPUs dice "1" y el `plan id` dice "dyno-1c-4gb". **La fuente no publica una aclaración** que resuelva cuál de las tres es el valor real, y la captura no permite determinar si el error está en el nombre o en las columnas. Este átomo registra la contradicción, no la resuelve.

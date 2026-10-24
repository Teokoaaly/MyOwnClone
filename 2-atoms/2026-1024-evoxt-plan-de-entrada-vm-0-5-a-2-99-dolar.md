---
id: 2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar
type: atom
certainty: solid
sources: [sources/2026-10-23-evoxt-vps-pricing.md]
links: ["[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]", "[[2026-1024-evoxt-precios-transparentes-2-99-sin-cargos-ocultos]]", "[[2026-1024-evoxt-escalera-de-precios-nueve-planes]]"]
---

## Claim
El plan más barato del catálogo de VPS de Evoxt es el **VM-0.5 a USD $ 2.99** con **1 vCore, 512 MB RAM y 5 GB Storage**. El siguiente escalón, **VM-0.75, cuesta USD $ 4.99** con 1 vCore, 1 GB RAM y 10 GB Storage. La página lo presenta como una línea de planes específica para clientes de China: *"Discover our VPS plans for China customers"*, con centros de datos en Estados Unidos y Reino Unido para dar baja latencia a usuarios en China.

## Why It Matters
Es el precio de entrada **verificado en la página de precios del propio proveedor**, que es lo que le faltaba al átomo anterior sobre el precio transparente de $2.99 ([[2026-1024-evoxt-precios-transparentes-2-99-sin-cargos-ocultos]]): aquel se apoyaba solo en el copy de la home y nopublicaba specs; ahora se sabe que $2.99 es un plan con **512 MB de RAM y 5 GB de disco**, es decir, insuficiente para el stack Flask + Next.js + Postgres + Redis del despliegue vivo de [[2026-1022-live-verify-deployment-migrada-a-vps-nginx]], y que el primer plan con **2 GB de RAM** (VM-1, USD $5.99) es el primero que podría alojarlo. El dato también sitúa a Evoxt por debajo del suelo de Hetzner ([[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]) en la variable que hoy manda en la decisión de infraestructura del vault.

## [FRICTION]
> [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]] afirma que **"ningún plan del catálogo de Hetzner Cloud cabe en un presupuesto de €4/mes"** y que "el VPS de €4 tiene que venir de otro proveedor o de un modelo distinto".
> Este átomo presiona esa creencia en su conclusión operativa: existe un plan de lista a **USD $2.99** (VM-0.5) y otro a **USD $4.99** (VM-0.75) publicados por el proveedor, con specs declaradas, en una página de precios real.
> Ambas no pueden ser completamente correctas en su lectura general: o el suelo de €6/mes es una verdad que solo aplica al catálogo de Hetzner (y el vault no estaba comparando proveedores, como ya implica la nota de los patrocinadores chinos en [[2026-1023-priceai-sponsors-vps-chinos-para-auto-hospedar-relay]]), o la cifra de $2.99 corresponde a un plan con recursos insuficientes para el producto (512 MB RAM). Marcado para juicio humano, no auto-resuelto: la comparación en euros exige además tipo de cambio, y la página no publica si el precio es mensual ni si incluye IVA.

## Nota de verificación
Precios, vCore, RAM y storage transcritos literalmente de la tabla de planes. La captura **no** publica: periodicidad (mensual o anual), IVA, ancho de banda incluido, SLA, región efectiva por plan ni si el precio en USD incluye impuestos.

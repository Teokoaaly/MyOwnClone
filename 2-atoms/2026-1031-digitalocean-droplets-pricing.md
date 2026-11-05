---
id: 2026-1031-digitalocean-droplets-pricing
type: atom
certainty: solid
sources: [sources/2026-10-31-digitalocean-droplets-pricing.md, sources/2026-11-01-digitalocean-droplets-pricing.md, sources/2026-11-02-digitalocean-droplets-pricing.md, sources/2026-11-03-digitalocean-droplets-pricing.md]
links: ["[[2026-1031-proton-business-vpn-essentials-6-99-minimo-2-usuarios]]", "[[costes-por-categoria-tenant]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1031-digitalocean-entrada-basic-512-mib-4-dolares-al-mes]]", "[[2026-1102-digitalocean-el-precio-de-entrada-cabe-en-euros-pero-el-stack-no-cabe]]"]
---

## Claim
DigitalOcean Droplets pricing is per-VM per-hour (or per-month with commitment), with a flat rate per VM size rather than per-user seating, creating a fixed infrastructure cost model independent of user count.

## Why It Matters
Unlike the per-seat cost dominance model where user count is the primary cost variable, DigitalOcean's per-VM pricing makes cost dependent on the number and size of virtual machines required, regardless of user count. For SaaS platforms, this means infrastructure cost scales with deployment architecture (number of containers, VMs, etc.) rather than directly with user count. The friction arises when mapping user growth to infrastructure needs: a growing user base may require more VMs, but not linearly, and the per-seat model from `costes-por-categoria-tenant` may significantly under- or over-state actual infrastructure costs depending on scaling patterns.

## Nota de extensión 2026-11-03
Las capturas del 2026-10-31, 2026-11-01 y 2026-11-02 de `digitalocean.com/pricing/droplets` cuantifican ese modelo por VM, que hasta ahora era solo cualitativo:

- **Precio de entrada**: Basic de 512 MiB / 1 vCPU / 10 GiB SSD / 500 GiB de transferencia a **$0.00595/hora o $4.00/mes**. La escalera Basic completa va de $4.00 (512 MiB) a $96.00 (16 GiB / 8 vCPU), con el nodo útil de 2 GiB / 1 vCPU en **$12.00** y el de 4 GiB / 2 vCPU en **$24.00** — ver [[2026-1031-digitalocean-entrada-basic-512-mib-4-dolares-al-mes]].
- **Un precio por VM, cinco familias**: Basic, CPU-Optimized (desde $42.00), General Purpose (desde $63.00), Memory-Optimized (desde $84.00) y Storage-Optimized (desde $131.00) — ver [[2026-1031-digitalocean-cinco-familias-de-droplet-y-sus-precios-de-entrada]].
- **Facturación por segundo** desde el 1 de enero de 2026, con mínimo de 60 s o $0.01, y **techo mensual en los Bundled Plans** — ver [[2026-1101-digitalocean-facturacion-por-segundo-con-minimo-de-60-segundos]].
- **Relación horario/mensual verificada**: el precio mensual es exactamente **672 horas** de la tarifa horaria (p. ej. $0.00595 × 672 = $4.00), lo que equivale a un descuento efectivo del 6,67 % frente a un mes de 720 h — ver [[2026-1101-digitalocean-el-precio-mensual-es-exactamente-672-horas-de-tarifa-horaria]].
- **Egreso incluido que escala con el plan** (500 GiB en el plan de entrada, hasta 11,000 GiB) — ver [[2026-1102-digitalocean-la-transferencia-incluida-escala-con-el-plan-de-500-a-11-000-gib]].
- **IPv4 pública incluida en los Bundled Plans** y factur aparte en los v5 a $0.00/hora "sujeto a cambio" — ver [[2026-1102-digitalocean-ipv4-publico-incluido-en-bundle-y-cobro-separado-en-v5]].
- **Contraste con el umbral del vault**: la entrada de $4.00 equivale a ~€3,64 al cambio de referencia, por debajo del techo de ≤ €4/mes, pero el plan que serviría el stack cuesta $12.00 — ver [[2026-1102-digitalocean-el-precio-de-entrada-cabe-en-euros-pero-el-stack-no-cabe]].

Conclusión para el eje per-seat vs per-infra: la afirmación de esta nota se mantiene y se afina — el coste de DO es **por VM y por tamaño de VM, no por usuario**, de modo que un producto multi-tenant con muchos usuarios y pocas máquinas deja de tener el coste de infraestructura correlacionado con los asientos. Pero la magnitud sitúa a DO fuera del presupuesto: **$12/mes en el plan que cuadraría con el stack**, frente a los ~€6/mes que el vault ya acepta como suelo real de infraestructura cloud ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]).

## 2026-11-03 — re-verificación
La captura del **2026-11-03** de `digitalocean.com/pricing/droplets` es un render reducido (825 palabras) que **sí conserva las cinco tablas de precios completas**: las **31 filas son numéricamente idénticas** a las del 2026-10-31, del 2026-11-01 y del 2026-11-02, sin una sola variación en memoria, vCPU, transferencia, SSD, $/hr ni $/mo. Ver [[2026-1103-digitalocean-precios-identicos-en-las-cuatro-capturas-del-31-oct-al-3-nov]].

Lo que **no** se puede re-verificar con esta captura: los precios por hora de los v5, la tabla de "Additional product pricing" (backups y snapshots), las FAQ de droplets (IPv4, ancho de banda, regiones, v5 vs Bundled Plan) y toda la sección intermedia, que el render sustituye por "…". Esto **no contradice** ninguna de las afirmaciones de los átomos existentes: solo significa que se sostienen por las capturas del 11-01 y del 11-02. Ver [[2026-1103-digitalocean-captura-reducida-sin-tablas-de-backups-ni-precios-de-v5]].

## [FRICTION]
> [[2026-1027-proton-business-vpn-essentials-6-99-minimo-2-usuarios]] sets a minimum 2-user entry barrier at $6.99/user/mo, while DigitalOcean charges per-VM per-hour with no user minimum. Both can serve the same B2B purpose, but the cost structures differ fundamentally: Proton's cost is unavoidably tied to user count, while DigitalOcean's cost is tied to deployment scale. For a startup with 3 users but requiring 2 VMs for HA, DigitalOcean could be cheaper than Proton's minimum 2-user entry, but as users grow, Proton's per-seat model may become more predictable than adding VMs to handle load.
---
id: 2026-1031-hetzner-cloud
type: atom
certainty: solid
sources: [sources/2026-10-31-hetzner-cloud.md, sources/2026-11-03-hetzner-cloud.md]
links: ["[[2026-1031-proton-business-vpn-essentials-6-99-minimo-2-usuarios]]", "[[costes-por-categoria-tenant]]"]
---

## Claim
Hetzner Cloud offers per-VM per-hour pricing at significantly lower rates than major cloud providers, with a simple pricing structure focused on VM instances, storage, and traffic — no per-user seating or feature gating.

## Why It Matters
Hetzner's ultra-low per-VM costs create an infrastructure pricing model completely independent of the per-seat dominance framework validated in `costes-por-categoria-tenant`. For early-stage SaaS products, Hetzner can dramatically reduce fixed infrastructure costs compared to AWS/GCP/Azure, potentially making the per-seat cost model less relevant in the early growth phase. The friction is in the transition: as user count grows and per-seat costs become the dominant factor (per the `costes-por-categoria-tenant` framework), the total cost of ownership must account for both the per-seat SaaS costs and the underlying infrastructure costs, which on Hetzner remain low per VM but scale with the number of VMs required to support the user base.

## [FRICTION]
> [[2026-1024-protonvpn-plus-3-49-al-mes-65-de-descuento]] notes Proton VPN Plus at $3.49/mo with 65% discount, while Hetzner Cloud VMs start at approximately €4.67/mo for entry-level instances. Both are viable VM/VPS options, but Proton's pricing is per-user with included VPN service, while Hetzner's is per-VM infrastructure only. A product running on Hetzner must still add on top VPN/database/auth services, making total cost = Hetzner VM cost + additional services. Comparing directly against Proton's per-user price requires disaggregating what Proton includes (VPN, storage, mail, etc.) vs. what is pure infrastructure on Hetzner.

## Nota de extensión 2026-11-03
Fuente: `sources/2026-10-31-hetzner-cloud.md`, `sources/2026-11-01-hetzner-cloud.md`, `sources/2026-11-02-hetzner-cloud.md`. Tres capturas consecutivas de la página de Hetzner Cloud **confirman el modelo de precio por VM** descrito en este átomo y **no mueven ninguna cifra de entrada**: el precio de salida sigue siendo **€ 5.99/mes (€ 0.0096/h)**, el IPv4 primario € 0,00, el tráfico esperado 20 TB a € 0,00, y las tres familias de plan mantienen "starting from" en € 5.99 / € 6.49 / € 43.49. No hay ningún precio por asiento ni feature gating en ninguna de las tres, lo que refuerza la tesis del átomo: el precio de Hetzner sigue siendo **infraestructura, no producto**.

Lo que las capturas sí añaden son tres matices que este átomo no recogía y que no alteran su claim: (1) el **techo "max/mo." de cada familia varía entre capturas** sin que cambien los precios de entrada (ver [[2026-1102-hetzner-techo-max-mo-de-cada-familia-varia-entre-capturas]]); (2) el **comparador de tráfico cambia de cifras** mes a mes, con la media de ahorro moviéndose aunque los operandos no cambien (ver [[2026-1102-hetzner-ahorro-medio-de-trafico-fluctua-entre-capturas]]); (3) el catálogo completo del proveedor incluye una **GPU-Line dedicada y una Server Auction desde € 72,70/mes** (ver [[2026-1101-hetzner-lineas-de-dedicados-gpu-y-almacenamiento-propio]]).

Corrección pendiente: el bloque `[FRICTION]` de este átomo afirma que "Hetzner Cloud VMs start at approximately **€ 4.67/mo** for entry-level instances". Ninguna de las tres capturas nuevas publica € 4,67 — todas dan € 5,99 ex-VAT. La discrepancia queda planteada en [[2026-1102-hetzner-precio-de-entrada-5-99-no-4-67]] y **no se auto-resuelve aquí**: este bloque no se reescribe.

## 2026-11-03 — re-verificación (cuarta captura)
Fuente: `sources/2026-11-03-hetzner-cloud.md`. La cuarta captura de esta serie **confirma el claim central de este átomo** — el precio de Hetzner es **por VM, sin asientos ni feature gating** — y no introduce ningún precio por usuario ni función condicionada. La calculadora renderiza de nuevo la configuración por defecto **CPX02 1 VCPU AMD · € 5.99/mes · € 0.0096/h**, el bloque de features sigue listando **API REST + CLI**, integraciones, Networks, Firewalls e Images sin coste adicional por usuario, y el bloque "Everything you need, included" sigue mostrando lo que entra en el precio base.
Lo que la captura añade es una precisión de método: la página tiene una **capa estática (precios de catálogo, cumplimiento, features, apps, zonas) que es idéntica en cinco capturas** y una **capa dinámica (techos "max/mo." y comparador de tráfico) que cambia en cada render** — ver [[2026-1103-hetzner-cinco-capturas-estabilidad-catalogo-vs-widgets-dinamicos]]. El techo nuevo de Cost-Optimized a € 0,00 se registra en [[2026-1103-hetzner-max-mo-cost-optimized-cero-ruptura-de-serie]].
Corrección pendiente sin auto-resolver: el bloque `[FRICTION]` de este átomo afirma que "Hetzner Cloud VMs start at approximately **€ 4.67/mo**". La captura del 2026-11-03 vuelve a dar **€ 5,99 ex-VAT**; el bloque no se reescribe y la discrepancia sigue planteada en [[2026-1102-hetzner-precio-de-entrada-5-99-no-4-67]].

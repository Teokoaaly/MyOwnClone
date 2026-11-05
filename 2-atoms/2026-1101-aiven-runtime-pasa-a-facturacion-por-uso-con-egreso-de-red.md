---
id: 2026-1101-aiven-runtime-pasa-a-facturacion-por-uso-con-egreso-de-red
type: atom
certainty: solid
sources: [sources/2026-11-01-aiven-postgresql-pricing.md, sources/2026-11-03-aiven-pricing.md]
links: ["[[2026-1031-aiven-postgresql-pricing]]", "[[2026-10-29-data-egress]]", "[[2026-1031-cloudflare-r2-storage]]"]
---

## Claim
Aiven Runtime factura como cualquier otro servicio (tarifa por hora desde que la app se crea hasta que se apaga o borra, sin coste por tiempo de build ni por periodos idle), pero la página anuncia un cambio de modelo: **"Billing will move to usage-based, including active app runtime, plus applicable storage and network egress costs."**

## Why It Matters
Es el aviso de que el "todo incluido" de Aiven tiene fecha: el egreso de red y el almacenamiento pasan a ser variables de consumo, exactamente el eje que [[2026-10-29-data-egress]] mide en Cloudflare ($0,05/GB tras 1.000 GB) y que [[2026-1031-cloudflare-r2-storage]] ya tiene en el radar de coste. Si el stack del vault migra a Aiven, la previsibilidad de la que habla [[2026-1031-aiven-postgresql-pricing]] solo aplica a los datastore; la capa de aplicación es la que se le está abriendo a coste variable.

## 2026-11-03 — re-verificación
La captura del 2026-11-03 confirma la redacción del aviso de cambio de billing ("Billing will move to usage-based, including active app runtime, plus applicable storage and network egress costs") y añade dos precisiones. Primera: el Runtime factura **"an hourly rate for your plan, starting when your app is created and running until you power it off or delete it"**, sin cargo por tiempo de build ni por periodos idle — es decir, **el coste corre mientras la app está encendida aunque no la uses**, lo que es un coste fijo por app viva, no por uso. Segunda: la FAQ "Can I change my application plan later?" responde que sí, "You can scale your application by changing the application plan directly in the Aiven Console", coherente con la fila "Seamless upgrade/downgrade to other plans". Nota: la captura del 11-03 **no** nombra ningún producto de Aiven con modelo de billing por uso ya activo — es un anuncio futuro, no una realidad vigente.

## [FRICTION]
> [[2026-1031-aiven-postgresql-pricing]] (escrita hace 3 días) afirma que el pricing de Aiven "bills by workload size rather than granular consumption, making costs predictable and workload-size-dependent rather than usage-granular", y que el modelo por plan "elimina el crecimiento impredecible de costes" frente al consumo granular de los competidores. Esta nota presiona esa afirmación porque la propia página de Aiven anuncia una **migración a facturación por uso con egreso de red y almacenamiento**, y la tabla de planes mantiene la fila "All networking cost included" como inclusa hoy pero no garantizada mañana. Ambas no pueden ser completamente correctas: o el cambio de billing de Runtime no aplica a los datastore, o la previsibilidad por plan de Aiven tiene fecha de caducidad y la afirmación del átomo viejo debe acotarse al presente. Marcado para juicio humano, no auto-resuelto.

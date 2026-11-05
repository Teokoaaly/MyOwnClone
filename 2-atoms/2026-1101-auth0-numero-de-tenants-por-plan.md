---
id: 2026-1101-auth0-numero-de-tenants-por-plan
type: atom
certainty: solid
sources: [sources/2026-11-01-auth0-pricing.md]
links: ["[[2026-1101-auth0-plan-free-25000-mau-sin-tarjeta]]", "[[2026-1101-auth0-b2b-essentials-escala-por-mau]]", "[[2026-1022-arquitectura-rac-tres-modos-por-clon]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
El número de tenants incluidos escala con el plan, de forma independiente del MAU: **Free 1 tenant, Essentials 3, Professional 12, Enterprise ilimitado**; el número de admin/contributors pasa de 3 (Free) a ilimitado (Essentials+); y la retención de logs es de **1 día (Free), 5 días (Essentials), 10 días (Professional), 30 días (Enterprise)**, con 1, 2 y 2 log streams respectivamente.

## Why It Matters
Este es el límite que realmente choca con la arquitectura multi-tenant de MyOwnClone ([[2026-1022-arquitectura-rac-tres-modos-por-clon]]): el plan Free de $0 —el único que cabe en el presupuesto de ≤ €4/mes— permite **un solo tenant**, mientras que el producto es multi-tenant por diseño. Para llegar al segundo tenant hay que subir a Essentials ($35 B2C / $150 B2B), y a partir del tercero, al Professional. O sea: el gating no es de features, es **de número de tenants**, que es exactamente la dimensión que el producto necesita. Y hay un segundo coste oculto en la misma tabla: la retención de logs de **1 día** en Free es insuficiente para cualquier auditoría o para depurar incidentes de autenticación en un producto que guarda datos de tenants. Esto refuerza la lectura del corte de costes por categoría ([[2026-1022-costes-por-categoria-tenant]]): la identidad no es una línea de coste variable por MAU sino una línea **escalonada por número de tenants**, y en el escenario del vault esa línea domina todos los demás costes de plataforma documentados.

## Nota de verificación
Filas "Number of Tenants Included", "Number of Admin/Contributors" y "Log Retention" leídas literalmente de las tablas "Platform" del feature matrix del 2026-11-01 (idénticas en B2C y B2B).

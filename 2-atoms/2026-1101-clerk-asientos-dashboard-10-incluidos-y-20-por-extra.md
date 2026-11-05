---
id: 2026-1101-clerk-asientos-dashboard-10-incluidos-y-20-por-extra
type: atom
certainty: solid
sources: [sources/2026-11-01-clerk-pricing.md]
links: ["[[2026-1101-clerk-plan-gratuito-50000-mru-y-3-asientos]]", "[[2026-1101-clerk-precios-base-hobby-pro-business]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
Los **asientos de dashboard** de Clerk (colaboradores con acceso al panel de administración del proveedor) se limitan a **3 en Hobby** y a **10 incluidos en Business**, con **$20/mes por asiento adicional**; Pro no publica ninguna cifra de asientos adicionales en la tabla.

## Why It Matters
Es la **única línea de la página de Clerk que se factura literalmente por asiento**, y es donde el eje "coste por asiento" del vault se hace más tangible dentro de un proveedor de identidad: cada persona del equipo que toca el panel de Clerk es un asiento de $20/mes. Para MyOwnClone eso significa que **un equipo pequeño de 3 personas (founder + 2) cabe gratis en Hobby y en Pro**, pero cualquier cuarto colaborador exige el salto a Business ($250/mes) o $20/mes extra. Y hay una lectura más fina: los asientos de dashboard de un proveedor de identidad son **infraestructura de equipo**, no coste de producto — es decir, coste que escala con el tamaño del equipo, no con el de los clientes, y por tanto **no debe contarse como coste variable de la plataforma** al comparar Auth0 vs Clerk vs WorkOS en el corte por categoría ([[2026-1022-costes-por-categoria-tenant]]).

## Nota de verificación
Fila "Dashboard seats" de la tabla "Full price breakdown" ("Up to 3 | Up to 3 | 10 included Additional $20/mo each") y bullet "Additional $20/mo each" de la tarjeta Business, verbatim de la captura del 2026-11-01.

---
id: 2026-1031-workos-sso-escalera-de-conexiones-125-100-80-65
type: atom
certainty: solid
sources: [sources/2026-10-31-workos-pricing.md, sources/2026-11-01-workos-pricing.md, sources/2026-11-03-workos-pricing.md]
links: ["[[2026-1101-auth0-addon-sso-enterprise-100-usd-por-conexion]]", "[[2026-1101-clerk-sso-adicional-desde-75-por-conexion]]", "[[2026-1031-workos-authkit-primer-millon-de-mau-gratis]]", "[[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]]", "[[2026-1103-workos-captura-cruda-no-trae-tabla-de-soporte]]"]
---

## Claim
El precio del **Single Sign-On** de WorkOS es una escalera por conexión y mes: **1–15 conexiones a $125/ea**, **16–30 a $100/ea (20% off)**, **31–50 a $80/ea (36% off)**, **51–100 a $65/ea (48% off)**; por encima de 100 conexiones el precio es **"Need additional scale? Talk to us"** (a medida). La tabla de la captura del 11-01 añade el rung explícito **"101+ | Custom | Contact sales"**.

## Why It Matters
Es la partida que decide si MyOwnClone puede vender a empresas, porque el SSO es lo que exige el IT de un cliente corporativo y en WorkOS se cobra **por conexión, no por asiento**. Comparando los tres proveedores del benchmark: en el tramo bajo WorkOS es el **más caro** ($125 vs $100 del add-on SSO Enterprise de Auth0 — [[2026-1101-auth0-addon-sso-enterprise-100-usd-por-conexion]] — y $75 de la segunda conexión en Clerk — [[2026-1101-clerk-sso-adicional-desde-75-por-conexion]]), pero en el tramo alto es el **más barato** ($65/ea frente a los $60 de Clerk en 16–100 y a los $100 fijos de Auth0, que además topa en 30 conexiones por cuenta). Para un SaaS multi-tenant donde **cada tenant corporativo es una conexión**, el coste escala con el número de clientes empresa: 5 clientes en el primer tramo son **$625/mes**, casi 150 veces el presupuesto de ≤ €4/mes ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]). La conclusión operativa: WorkOS no gana por precio unitario, gana porque es el único de los tres cuyo precio se **descuenta con el volumen de conexiones** — que es exactamente la forma que tiene el negocio B2B de un producto de clones IA.

## 2026-11-03 — re-verificación
La captura del 2026-11-03 (volcado crudo de la página) **confirma los cuatro tramos y sus tres descuentos explícitos**: 1-15 → $125/ea, 16-30 → "20% off" $100/ea, 31-50 → "36% off" $80/ea, 51-100 → "48% off" $65/ea. Novedad de matiz: por encima de 100 conexiones la página ya **no muestra el rung tabular "101+ | Custom | Contact sales"** de la captura del 11-01, sino la frase **"Need additional scale? Talk to us"** bajo el bloque "Number of connections". El deslizador del calculador de SSO llega hasta "0 15 30 50 100+", coherente con la escalera, y el bloque reproduce el argumento de venta "vs $100 to build it yourself" (ver [[2026-1103-workos-vs-100-para-construir-sso-o-scim-uno-mismo]]). La conclusión de este átomo no cambia: el descuento por volumen de conexiones sigue siendo la ventaja estructural de WorkOS frente a Auth0 y Clerk, y por encima de 100 conexiones el precio deja de estar publicado ([[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]]).

## Nota de verificación
Escalera "Number of connections" de la sección Single Sign-On de la captura del 2026-10-31 (1-15 $125/ea, 16-30 $100/ea 20% off, 31-50 $80/ea 36% off, 51-100 $65/ea 48% off) y rung "101+ | Custom" de la tabla de la captura del 2026-11-01. La comparación de precios entre proveedores es lectura operativa de este átomo.

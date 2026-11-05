---
id: 2026-1104-clerk-recomienda-supabase-y-firebase-para-consumo-gratuito
type: atom
certainty: solid
sources: [sources/2026-11-04-clerk-pricing.md]
links: ["[[2026-10-29-supabase-pro-mau]]", "[[2026-1101-clerk-mru-no-mau-con-primer-dia-gratis]]", "[[2026-1102-workos-auth0-clerk-benchmark-de-identidad-en-tres-vias]]"]
---

## Claim
La FAQ de `clerk.com/pricing` admite que su modelo por MRU **puede salir caro en apps de consumo** y **recomienda explícitamente a la competencia** para ese caso: "if you're building a free, ad-supported, or very low-ARPU consumer app, Clerk's per-MRU model may feel expensive once you outgrow the free tier. In those cases, alternatives like **Supabase Auth, which includes 100K MAU on Pro/Team**, or **Firebase Auth** for basic email/social auth may be cheaper. The simple rule: **Clerk is easiest to justify when retention maps to revenue**; for massive free audiences, run the unit economics first."

## Why It Matters
Es el único caso del corpus donde **un proveedor de identidad señala a sus propios sustitutos por nombre y con la cifra del rival**: la página de Clerk da el dato de Supabase ("100K MAU on Pro/Team"), y ese dato **coincide exactamente** con la medición propia del vault — Supabase Pro a $25/mes con 100.000 MAU incluidos y $0,00325 por MAU adicional ([[2026-10-29-supabase-pro-mau]]) — de modo que **la cifra de un competidor sirve de corroboración cruzada** de una fuente ya atomizada, algo que refuerza la fiabilidad del número de 100.000 MAU. La consecuencia para el hilo de identidad del vault es metodológica y de mercado a la vez: primero, **el posicionamiento de Clerk es "retención = ingreso"**, es decir, el proveedor asume que su cliente tiene MRR y que un usuario retenido se paga; eso encaja con el producto de clonar un clon, donde casi todos los usuarios son usuarios de pago. Segundo, para el caso contrario —un producto con audiencia masiva y gratuito— **el propio Clerk señala que su economics no aplica** y que la alternativa no es otro proveedor de auth empresarial sino un **backend con auth incluida** (Supabase Auth o Firebase Auth), lo que devuelve la decisión al eje "provider vs librería" del vault ([[2026-1102-workos-auth0-clerk-benchmark-de-identidad-en-tres-vias]]). Tercero, y esto es lo relevante para el hilo de reventa: **el valor de Clerk está en la línea de MRU facturable**, no en la autenticación en sí; en un modelo donde el MRU se contabiliza por retención y la audiencia gratuita no computa, el tipo de proveedor que conviene es el que factura por **conversión**, no por actividad.

## [FRICTION]
> [[2026-1101-clerk-mru-no-mau-con-primer-dia-gratis]] afirma que el MRU "es la diferencia de métrica que decide el lado del eje abierto del vault (coste por asiento vs coste por infraestructura)" y que en el caso de MyOwnClone "MRU ≈ MAU y se paga lo mismo".
> Este átomo matiza esa creencia sin contradecirla: **la propia página de Clerk sostiene que su modelo por MRU "puede sentirse caro" en audiences gratuitas o de ARPU muy bajo**, lo que desplaza la variable decisiva de "MRU vs MAU" a "**retención ↔ ingreso**". En un producto donde la audiencia no paga (o paga poco), un MRU bajo no abarata el coste: simplemente hace que el coste por usuario retenido suba. La lectura del átomo viejo —"MRU bajo = coste efectivo bajo"— es válida solo si cada usuario retenido tiene valor. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
Sección "Is Clerk good for B2C apps?" de `sources/2026-11-04-clerk-pricing.md`, verbatim. La cifra de Supabase (100.000 MAU en Pro/Team a $25/mes) procede del átomo [[2026-10-29-supabase-pro-mau]], tomado de la captura de Supabase del 2026-10-29, no de esta fuente.

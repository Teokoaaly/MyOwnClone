---
id: 2026-1031-workos-definicion-de-mau-accion-en-el-mes-calendario
type: atom
certainty: solid
sources: [sources/2026-10-31-workos-pricing.md, sources/2026-11-03-workos-pricing.md]
links: ["[[2026-1031-workos-authkit-primer-millon-de-mau-gratis]]", "[[2026-1101-auth0-definicion-de-mau-y-cobro-al-escalon-superior]]", "[[2026-1101-clerk-mru-no-mau-con-primer-dia-gratis]]"]
---

## Claim
WorkOS define el usuario activo mensual así: **"A user is considered active if they perform any user action (for example: sign up, sign in, or profile update) within the calendar month"**, y el tramo gratuito de 1M de MAU se cuenta con esa misma definición ("How do you count the 1 million free users?").

## Why It Matters
La granularidad de la definición determina si el tier gratuito aguanta o no. Al contar **cualquier acción dentro del mes calendario**, un usuario que solo hace login una vez al mes sigue siendo MAU: para MyOwnClone eso significa que un tenant con 20 usuarios que entrando al menos una vez al mes mantiene **20 MAU vivos**, y el "-gratis hasta 1M" se consume con el simple hecho de que la gente entre. El contraste con el benchmark de los otros dos proveedores es instructivo: Clerk usa **MRU** (usuarios *retenidos*) con un día de gracia el primer día y cuenta como retenido a quien ha estado activo en los últimos 30 días ([[2026-1101-clerk-mru-no-mau-con-primer-dia-gratis]]), y Auth0 también usa MAU pero **cobra al escalón superior** en vez de por unidad ([[2026-1101-auth0-definicion-de-mau-y-cobro-al-escalon-superior]]). La consecuencia práctica para el modelo de costes: en WorkOS el número de MAU solo importa al llegar al millón, así que la métrica a medir para el presupuesto **no es MAU sino conexiones SSO**, que es donde el precio real está ([[2026-1031-workos-conexion-por-cliente-corporativo-no-por-usuarios]]).

## 2026-11-03 — re-verificación
La captura del 2026-11-03 confirma la definición **verbatim**: "A user is considered active if they perform any user action (for example: sign up, sign in, or profile update) within the calendar month", dentro del FAQ "How do you count the 1 million free users?". Novedad de matiz: la misma respuesta del FAQ añade **"Contact us to learn more about volume pricing"**, es decir, la propia página reconoce que más allá de 1M de MAU el precio deja de estar publicado y pasa a negotiation — coherente con la tesis de este átomo de que el MAU no es la variable de coste relevante ([[2026-1031-workos-authkit-primer-millon-de-mau-gratis]]).

## Nota de verificación
FAQ "How do you count the 1 million free users?" de la captura del 2026-10-31, verbatim.

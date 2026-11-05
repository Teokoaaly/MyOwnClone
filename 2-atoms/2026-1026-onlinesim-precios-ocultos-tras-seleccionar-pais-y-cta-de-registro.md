---
id: 2026-1026-onlinesim-precios-ocultos-tras-seleccionar-pais-y-cta-de-registro
type: atom
certainty: solid
sources: [sources/2026-10-25-onlinesim-virtual-sms.md]
links: ["[[2026-1023-5sim-catalogo-servicios-precios-y-stock]]", "[[2026-1023-5sim-smart-buy-y-tasa-entrega-visible]]", "[[2026-1024-herosms-la-ruta-de-precios-tambien-es-un-engano-de-cuentas]]"]
---

## Claim
OnlineSim **no publica ningún precio de servicio**: el bloque de tarifas empieza con "To see exact prices, **please select your country**" y "107 countries / One-time SMS", y los CTA "Get a number" y "Rent a Number" apuntan ambos a `onlinesim.io/auth/register?redirect=/v2/numbers/` y `/v2/rent/`. No hay tabla por servicio, ni por par (país, operador), ni contador de stock, ni tasa de entrega, ni CSV descargable: el precio es un dato que se pide después de registrarse.

## Why It Matters
Coloca a OnlineSim en el extremo opuesto de 5sim, que sí publica precios y stock en el selector y además permite navegar sin registro ([[2026-1023-5sim-catalogo-servicios-precios-y-stock]], [[2026-1023-5sim-smart-buy-y-tasa-entrega-visible]]). Y comparte con HeroSMS el patrón de que **el precio no es un dato público**, pero por un motivo distinto: HeroSMS lo esconde detrás de un 404 y de cromo de cuenta ([[2026-1024-herosms-la-ruta-de-precios-tambien-es-un-engano-de-cuentas]]), mientras que OnlineSim lo esconde detrás de una selección de país y un registro.
Consecuencia práctica para el vault: **OnlineSim no es cotizable** con la fuente disponible. Su precio de "escaparate" ($0.01 por servicio, $3 al día) es un ancla publicitaria sin tabla que lo respalde, así que no puede entrar en la tabla comparativa de coste por unidad del thread de verificación como proveedor con precio verificable.

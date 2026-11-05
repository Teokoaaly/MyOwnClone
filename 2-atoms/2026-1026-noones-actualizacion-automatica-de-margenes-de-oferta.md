---
id: 2026-1026-noones-actualizacion-automatica-de-margenes-de-oferta
type: atom
certainty: tentative
sources: [sources/2026-10-25-noones-developer-api.md]
links: ["[[2026-1026-noones-api-dos-formatos-directo-y-delegado]]", "[[2026-1024-noones-publicar-ofertas-y-visa-virtual-exigen-id]]", "[[2026-1023-priceai-home-como-radar-y-no-como-vendedor]]", "[[2026-1024-noones-tabla-de-limites-por-nivel]]"]
---

## Claim
Uno de los cuatro bullets de cabecera de `dev.noones.com` es **"Automatically update offer margins"**, y la página promete en el encabezado que sus APIs permiten "grow your business, automate trades, decrease trade times". Es la única mención de la captura a la gestión del **margen de las ofertas propias**, y no viene con ninguna cifra, fórmula ni referencia a la API concreta que lo haría.

## Why It Matters
El margen de oferta es la variable de precio del lado vendedor, y automatizarlo es exactamente el trabajo que hace un agregador de precios cuando escribe su propio libro ([[2026-1023-priceai-home-como-radar-y-no-como-vendedor]]). Si NoOnes publica un automatismo de márgenes, el proveedor de la plataforma está **invitando al integrador a ser su propio market maker** — y eso conecta directamente con la restricción que el vault ya tiene registrada: publicar ofertas exige ID o Basic Verification ([[2026-1024-noones-publicar-ofertas-y-visa-virtual-exigen-id]]), de modo que un bot de márgenes solo puede existir sobre cuentas verificadas, con sus límites por nivel ([[2026-1024-noones-tabla-de-limites-por-nivel]]). `certainty: tentative` porque la captura nombra la función pero no su mecánica: no dice si el bot fija el margen, si lo recalcula siguiendo un feed externo, ni si hay límites de frecuencia.

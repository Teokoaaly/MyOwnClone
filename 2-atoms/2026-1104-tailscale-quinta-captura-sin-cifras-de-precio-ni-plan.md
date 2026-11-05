---
id: 2026-1104-tailscale-quinta-captura-sin-cifras-de-precio-ni-plan
type: atom
certainty: solid
sources: [sources/2026-11-04-tailscale-docs.md]
links: ["[[2026-1101-tailscale-kb-sin-ninguna-cifra-de-precio-ni-plan]]", "[[2026-1031-tailscale-docs]]", "[[2026-1104-tailscale-quinta-captura-byte-identica-a-la-del-11-02]]"]
---

## Claim
La quinta captura de `tailscale.com/kb` (2026-11-04, 2779 bytes) vuelve a **no contener ninguna cifra de precio, nombre de plan, límite de nodos ni de usuarios**. El único texto económico es exactamente el mismo fragmento ya registrado: *"Manage your contact information, your account, **the plans we offer**, and how to manage your tailnet DNS name and domain."*, dentro de la entrada "Manage your organization" (`/docs/account`). La fecha de validación sigue siendo **"Last validated Feb 4, 2026"**, idéntica en las cinco capturas. Y como el cuerpo es byte a byte el del 11-02, esta quinta captura **no aporta ninguna novedad economy**: es la enésima confirmación de que el precio de Tailscale no vive en el índice de la KB.

## Why It Matters
Confirma por quinta vez el vacío ya documentado en [[2026-1101-tailscale-kb-sin-ninguna-cifra-de-precio-ni-plan]]: **el precio de Tailscale no está en la KB, está en otra página** ("Manage your plan", "Pricing", "Contact Sales"), y no hay ninguna cifra en este corpus con independencia del fetcher. El valor de este átomo no es el dato (no hay dato) sino la **reproducibilidad**: al ser el mismo fichero que el del 11-02, la conclusión queda blindada — no es que el 11-04 no mostrara precios por casualidad del render, es que el índice no los tiene en ninguna forma. Refuerza la decisión de la línea de coste del vault: Tailscale solo puede computarse como partida de coste cero o marginal, nunca como cifra firme, mientras no se capture la página de precios. Y deja sin resolver el hueco que [[2026-1031-tailscale-docs]] abrió al afirmar un modelo de precio por nodo que ninguna de las cinco capturas sostiene.

---
id: 2026-1103-tailscale-kb-control-ask-ai
type: atom
certainty: solid
sources: [sources/2026-11-03-tailscale-docs.md]
links: ["[[2026-1101-tailscale-aperture-governance-de-ia-para-agentes-y-usuarios]]", "[[2026-1101-tailscale-kb-captura-26-lineas-utiles-y-340-de-navegacion-duplicada]]"]
---

## Claim
La captura del 2026-11-03 de `tailscale.com/kb` termina con la cadena suelta **"Ask AI"** (última línea del documento), un control de la página de índice de la KB que **no aparece en ninguna de las tres capturas anteriores** del mismo URL (10-31, 11-01, 11-02: 0 coincidencias cada una). Es la única aparición de un asistente de IA **en la landing de la KB**; el resto del corpus de IA de Tailscale está en la sección de producto "Aperture: Secure AI" ([[2026-1101-tailscale-aperture-governance-de-ia-para-agentes-y-usuarios]]).

## Why It Matters
Señala una segunda superficie de IA en Tailscale, distinta de la ya registrada: Aperture **gobierna** el uso de IA de agentes y usuarios (control de acceso, spending, observabilidad), mientras que "Ask AI" es un punto de entrada **de consumo** en la propia documentación. La distinción importa para el vault porque el modo en que los agentes del stack leen documentación está cambiando: un índice de KB con "Ask AI" es una señal de que el proveedor está optimizando la página para consultas de agente, no solo para lectura humana. Límite honesto y explícito: **la captura no describe la función** — no dice a qué modelo responde, si es un chat, ni si hereda la política de Aperture; y en esta captura el control aparece sin destino de enlace, así que no hay URL que capturar. La afirmación es "el control existe en el renderizado del 11-03", nada más. La decisión de valor real sigue siendo la de [[2026-1101-tailscale-kb-captura-26-lineas-utiles-y-340-de-navegacion-duplicada]]: capturar las páginas individuales, donde vive la especificación, no este índice.

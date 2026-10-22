---
id: 2026-1022-feedback-widget-screenshots
type: atom
certainty: solid
sources: [raw/articles/myownclone-frontend-recon.md]
links: ["[[myownclone]]", "[[2026-1022-dashboard-de-insights]]", "[[2026-1022-superficie-oculta-robots-txt]]"]
---
## Claim
[[myownclone]] incluye un widget de feedback que acepta capturas de pantalla pegadas directamente desde el portapapeles (Ctrl+V) con un límite de 5MB por envío, y el platform admin lo gestiona en `/admin/platform/feedback` junto con un gestor de FAQs en `/admin/platform/faqs`.

## Why It Matters
El pegado de screenshot es un detalle de fricción que revela la prioridad de producto: el feedback llega con el contexto visual ya capturado, sin que el usuario tenga que subir ficheros. Alimenta directamente el loop de inteligencia de producto de [[2026-1022-dashboard-de-insights]] (feedback → gaps → formación), y su recolección centralizada en el panel de plataforma confirma que el feedback de tenants se agrega antes de llegar al creator — no es un buzón personal, es un pipeline de la plataforma. Comparte espacio de ruta con las features bloqueadas por [[2026-1022-superficie-oculta-robots-txt]].

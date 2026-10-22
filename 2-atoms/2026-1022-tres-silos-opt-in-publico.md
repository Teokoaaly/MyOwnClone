---
id: 2026-1022-tres-silos-opt-in-publico
type: atom
certainty: solid
sources: [raw/articles/myownclone-scrape_web-scrape.md, raw/articles/myownclone-frontend-recon.md]
links: ["[[myownclone]]", "[[2026-1022-arquitectura-rac-tres-modos-por-clon]]", "[[2026-1022-diferenciacion-negocios-online-vs-famosos]]", "[[2026-1022-admin-rutas-bilingues-sin-subdominio]]"]
---
## Claim
El copy público de [[myownclone]] define el producto como un clon con "tres silos opt-in" —pedagogía ("enseña"), soporte al cliente ("da soporte") y recomendaciones de producto ("recomienda tus productos")— sobre una "única superficie de chat", y, en palabras del copy, "entrenado solo con lo que tú decides" (vídeos, cursos, PDFs, web). El tagline lo posiciona como "tu aliado perfecto para tu negocio online". El recon de i18n lo confirma como estructura de configuración real, no solo de marketing: la superficie de chat se parametriza con knowledge/terms/personality, y `/admin/brain` da a cada silo su corpus (`/knowledge`, `/products`, `/support`, `/terms`).

## Why It Matters
El marketing público confirma en el sitio lo que el founder explica en la entrevista (tres modelos por clon, ver [[2026-1022-arquitectura-rac-tres-modos-por-clon]]) y lo hace sin mencionar "ventas": el tercer silo público es *recomendación de producto*, no venta directa, un matiz que cambia la lectura comercial del producto. También confirma el eje de cliente objetivo de [[2026-1022-diferenciacion-negocios-online-vs-famosos]]: negocios online, no entretenimiento de fama. El detalle de "knowledge/terms/personality" como los tres ejes configurables de la chat surface muestra que el clon no es un prompt único sino un ensamblaje de corpus, terminología y persona — implementable solo si cada silo tiene su retrieval path, como describe [[2026-1022-admin-rutas-bilingues-sin-subdominio]].

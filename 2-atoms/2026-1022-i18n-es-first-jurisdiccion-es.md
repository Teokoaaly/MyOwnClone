---
id: 2026-1022-i18n-es-first-jurisdiccion-es
type: atom
certainty: solid
sources: [raw/articles/myownclone-scrape_web-scrape.md]
links: ["[[myownclone]]", "[[2026-1022-diferenciacion-negocios-online-vs-famosos]]", "[[marea-kiss-llc]]", "[[2026-1022-superficie-legal-publica-dpa-clon-terms]]"]
---
## Claim
[[myownclone]] opera español-primero: `@next/intl` con español como idioma por defecto en `/` e inglés en `/en`, y el sitemap duplica cada ruta bilingüe (con la excepción de `/legal/aviso-legal`, que solo existe en español — ver [[2026-1022-superficie-legal-publica-dpa-clon-terms]]). El copy distingue las dos versiones con tags propios: la portada española usa `og:locale: es_ES` y la inglesa `og:locale: en_US`, ambas con `og:image` generada en la ruta de idioma (`/es/opengraph-image`, `/en/opengraph-image`).

## Why It Matters
El español como default con inglés como traducción (no al revés) es una señal de que el mercado inicial es local, coherente con [[2026-1022-diferenciacion-negocios-online-vs-famosos]] frente al mercado US de [[delphi]]. Y la duplicación íntegra del sitemap en ambos idiomas, con una única excepción legal, muestra una operación preparada para vender fuera pero con origen y contratos en España — encaja con el onboarding white-glove de [[2026-1022-onboarding-manual-sin-self-service]].

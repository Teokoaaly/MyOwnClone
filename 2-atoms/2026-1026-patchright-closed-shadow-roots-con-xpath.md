---
id: 2026-1026-patchright-closed-shadow-roots-con-xpath
type: atom
certainty: solid
sources: [sources/2026-10-25-patchright-playwright.md]
links: ["[[2026-1024-2captcha-integrado-en-4500-software-con-api-key]]", "[[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]"]
---

## Claim
La sección "Closed Shadow Roots" documenta una capacidad concreta y su nivel de madurez: **"Patchright is able to interact with elements in Closed Shadow Roots. Just use normal locators and Patchright will do the rest."** Y añade una segunda frase que marca la ampliación: **"Patchright is now also able to use XPaths in Closed Shadow Roots."** Es decir, la capacidad se ofrece como **transparente** para quien ya escribe Playwright: los localizadores habituales funcionan sin cambiar la API.

## Why It Matters
El shadow root cerrado es, por construcción, un elemento **inaccesible por diseño** a cualquier script de página: se cierra precisamente para que un script no pueda inspeccionar lo que contiene. Cualquier herramienta que lo traverse está **violando deliberadamente una frontera de aislamiento**, y por tanto es un vector de detección por sí mismo — un sitio puede detectar que su contenido se está leyendo desde fuera si la API que lo permite no debería existir en un navegador automatizado.
La consecuencia para el vault es de **superficie de negocio**: lo que el vault ya tenía era la resolución de captchas como capacidad embebida en software de terceros ([[2026-1024-2captcha-integrado-en-4500-software-con-api-key]]) y como línea de producto separada ([[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]). Aquí la capacidad equivalente es **de scraping de DOM, no de captcha**: leer contenido que el sitio no expone, sin cambiar una línea del código que ya existe. Es la misma economía —una dependencia de terceros que añade una capacidad difícil— pero en otra capa.
El detalle de la transparencia de la API ("just use normal locators") es lo que la hace transferible: **el coste de adopción es una línea de dependencia**, no un rediseño del código de extracción.

## Nota de verificación
Las dos frases están transcritas literalmente. La captura **no** dice desde qué versión del proyecto está disponible el soporte de XPath en shadow roots cerrados, ni menciona limitaciones. La definición técnica de "closed shadow root" es conocimiento general del vault, no de la fuente.

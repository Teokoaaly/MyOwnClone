---
id: 2026-1104-brightdata-dos-rutas-de-captura-producen-distinto-texto-de-la-misma-pagina
type: atom
certainty: solid
sources: [sources/2026-11-04-brightdata-pricing.md, sources/2026-10-31-brightdata-pricing.md]
links: ["[[2026-1104-brightdata-cuarta-captura-del-slug-identica-byte-a-byte-a-la-del-11-01]]", "[[2026-1101-brightdata-scraper-studio-cobra-solo-por-requests-exitosos]]", "[[2026-1104-deepgram-el-word-count-del-frontmatter-no-es-fiable-como-metrica-de-cobertura]]"]
---

## Claim
La serie del slug muestra **dos rutas de extracción distintas** sobre la misma página, y se distinguen por tres rasgos simultáneos. Ruta "texto plano" (2026-10-31): 343 palabras reales, **cero** hrefs en los "See Pricing", **cero** imágenes, sin "Accessibility Menu", y el bullet de Scraper Studio escrito **"Only pay for successful requests"** (correcto). Ruta "markdown renderizada" (11-01, 11-02, 11-04): 743–750 palabras, los ocho "See Pricing" con href, las imágenes resueltas (inline SVG vacío o URL de `media.brightdata.com`), "Accessibility Menu" presente, y el mismo bullet escrito **"Only pay for successful requets"** — con la errata. El frontmatter también difiere: el 10-31 **declara 3.892 palabras** y el 11-04 declara 743, que sí coincide exactamente con su cuerpo.

## Why It Matters
La errata "requets" no es un descuido del redactor que se arrastra por el sitio: **está en tres capturas con markdown y no en la de texto plano**. Como el resto del texto de las ocho fichas es palabra por palabra idéntico en las cuatro capturas, solo hay dos explicaciones posibles — o la captura del 10-31 viene de una *fuente distinta* (un texto plano o un `llms.txt` con la errata ya corregida), o el sitio se corrigió y luego volvió a la versión con errata — y **la captura no permite decidir entre las dos**. Lo que sí queda establecido, y es lo que importa para el vault, es que **"el texto de la página" no es una constante del sitio sino una constante de la ruta de captura**: el mismo marketing copy se puede leer con o sin errata, con o sin href y con o sin imágenes.
Eso refina la regla que ya se había escrito para las páginas de precio: no basta con "una captura parcial solo vale para lo que enumeró" ([[2026-1031-twilio-la-captura-del-31-de-octubre-es-una-renderizacion-reducida]]), hay que añadir que **una misma URL puede tener dos graphs textuales distintos y ambos ser "fieles" a algo distinto**. Para el agregador, la consecuencia es que un pipeline que compare texto entre capturas debe **comparar rutas de extracción, no solo URLs**: si no, una diferencia de copy se leerá como un cambio de precio, o al revés, un cambio de precio real puede quedar oculto por una diferencia de render.
Y el caso del `word_count` reinforce el mismo punto con una regla ya medida en otros slugs ([[2026-1104-deepgram-el-word-count-del-frontmatter-no-es-fiable-como-metrica-de-cobertura]]): en esta serie, 743 y 750 son exactos y 3.892 es falso por un factor de once, así que el metadato sirve para **detectar** una captura distinta, no para medir su contenido.

## [FRICTION]
> [[2026-1101-brightdata-scraper-studio-cobra-solo-por-requests-exitosos]] (escrita el 2026-11-01) cita `sources/2026-10-31-brightdata-pricing.md` entre sus fuentes y describe el bullet como **"Only pay for successful requets"** [sic, errata en el original].
> El 10-31 transcribe **"Only pay for successful requests"**, sin errata: la errata solo aparece en las tres capturas con markdown (11-01, 11-02 y el 11-04). Ambas no pueden ser completamente correctas: o el átomo atribuyó a la fuente del 10-31 una errata que esa fuente no contiene, o la errata estaba en la página en el 31 de octubre y el texto plano de esa captura la corrigió por el camino. Marcado para juicio humano, no auto-resuelto — la discrepancia es de una letra en una palabra de marketing y no altera ninguna cifra.
> Nota: el contenido sustantivo del átomo viejo (cobro por request exitoso) queda corroborado por el 11-04, que reproduce la misma ficha con la misma errata.

## Nota de verificación
Verificado con `grep -n "successful"` sobre las cuatro capturas y con recuento de `See Pricing](https` (0 en el 10-31, 8 en los otros tres), presencia de "Accessibility Menu" (0 / 1 / 1 / 1) y `word_count` declarado frente a palabras reales del cuerpo (3.892→343, 743→743, 750→750, 743→743). La captura **no** publica: cuál de las dos rutas es la "oficial", ni si existe una tercera variante del texto, ni la fecha de la corrección de la errata.

---
id: 2026-1026-github-search-suno-dos-de-los-cuatro-primeros-son-tutoriales-de-relays-chinos
type: atom
certainty: solid
sources: [sources/2026-10-25-github-search-suno-openai.md]
links: ["[[2026-1023-priceai-modulo-api-transit-tres-ejes-de-comparacion]]", "[[2026-1024-veridrop-directorio-de-relays-distinto-del-ranking]]", "[[2026-1024-github-search-tres-de-catorce-son-falsos-positivos-de-la-consulta]]"]
---

## Claim
Dos de los cuatro repositorios con más estrellas de la consulta `suno openai api` **no son herramientas de Suno**: son **documentación en chino de estaciones de reventa** (中转站). `whataicc/doc-whataicc-api` (**37 estrellas, 3 forks, HTML, sin licencia, 9 topics, homepage `https://api.whatai.cc`**) se titula *"神马中转API教程文档… 支持Claude、Midjourney、Suno、OpenAI等650+模型教程"* — tutorial de una estación que declara **650+ modelos**. `Token173/doc-token173-api` (**27 estrellas, 0 forks, sin lenguaje declarado, sin licencia, sin topics, homepage `https://www.token173.net`**) es *"2026年最新靠谱稳定便宜好用的中转站推荐排名… 支持Claude、GPT、Gemini、Grok、Midjourney、Suno、OpenAI等500+模型教程，**SLA99.9%**"* — un **ranking de estaciones de reventa** que declara **500+ modelos** y un SLA de 99,9 %. Ambos repositorios son, por construcción, material de **SEO de una estación de reventa**: solo hay que contener las palabras "Suno", "OpenAI" y "API" para que la consulta los devuelva.

## Why It Matters
Es un **falso positivo de naturaleza distinta** al que el vault ya midió en el corpus de registro de cuentas. Allí los tres falsos positivos eran repos de código que no tenían nada que ver ([[2026-1024-github-search-tres-de-catorce-son-falsos-positivos-de-la-consulta]]); aquí son **documentación comercial de los propios intermediaries** del mercado de relays. La consecuencia metodológica es inmediata: **la consulta de la API de búsqueda devuelve el marketing de los relays con la misma frecuencia con la que devuelve el código**, y por tanto el corpus de una consulta de "herramienta X" en este mercado está **contaminationdo por las estaciones que venden capacidad de X**.
Y el dato de fondo es el que más pesa para el thread del agregador: **hay una tercera y una cuarta estación de reventa que publican un ranking de estaciones y un SLA declarado** —Token173 con "500+ modelos" y "SLA 99,9 %", api.whatai.cc con "650+ modelos"— y ninguna de las dos aparece en los inventarios del vault (PriceAI, VeriDrop). El vault tiene medido que el inventario de VeriDrop **no publica precios** ([[2026-1024-veridrop-directorio-de-relays-distinto-del-ranking]]), que PriceAI publica multiplicadores y disponibilidad como **observación pública, no SLA** ([[2026-1023-priceai-modulo-api-transit-tres-ejes-de-comparacion]]), y ahora aparece un tercero que **declara SLA y número de modelos** sin que nada en la captura permita verificarlo. Los tresUILs compiten por el mismo tráfico de búsqueda con datos no comparables.

## [FRICTION]
> [[2026-1023-priceai-modulo-api-transit-tres-ejes-de-comparacion]] establece, para el módulo de tránsito de PriceAI, que la disponibilidad de cada fila es **"observación pública, no SLA"** y que la función de detección de modelo está pendiente (*"即将开放"*), es decir: el agregador **no verifica** lo que publica.
> Este átomo presiona esa creencia desde la dirección contraria: `Token173/doc-token173-api` **sí declara un SLA (99,9 %) y un número de modelos (500+)**, y lo hace en la descripción de un repositorio de tutoriales, sin ninguna de las cuatro dimensiones que PriceAI tabula (multiplicador, estabilidad, cobertura, criterio de ranking). Si el dato de PriceAI es observación no verificada, el SLA de Token173 **no es mejor dato por ser un SLA**: es otro claim, más fuerte y menos desglosado.
> Ambas no pueden sostenerse como fuentes igualmente citable de la misma magnitud. Marcado para juicio humano, no auto-resuelto: **el vault no ha visitado ninguno de los dos sitios** y solo tiene la frase de la `description`.

## Nota de verificación
Las dos descripciones están transcritas y traducidas de los campos `description` del JSON; los contadores proceden de `stargazers_count`, `forks_count`, `language`, `license`, `topics` y `homepage` del mismo fichero. Las cifras "650+ modelos", "500+ modelos" y "SLA 99,9 %" son **claims de las descripciones**, no mediciones del vault: la captura no contiene ninguna tabla de esos sitios, ni sus precios, ni sus listados de modelos.

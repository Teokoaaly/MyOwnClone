---
id: 2026-1027-decodo-markdown-y-json-sin-limpieza-como-salida-nativa-para-llm
type: atom
certainty: solid
sources: [sources/2026-10-26-decodo-smartproxy-home.md, sources/2026-10-26-decodo-web-data-api-pricing.md]
links: ["[[2026-1027-dataimpulse-docs-como-llms-txt-y-markdown-por-pagina]]", "[[2026-1026-brightdata-llms-txt-como-indice-de-documentacion-para-agentes]]", "[[2026-1022-myclone-scraping-ingestion-pipeline]]", "[[2026-1027-decodo-la-unidad-no-es-estable-requests-paginas-y-crawls]]"]
---

## Claim
La Web Data API de Decodo declara la limpieza de la página como parte del producto, no como paso posterior. La home: *"Get structured **Markdown or JSON stripped of nav bars, cookie banners, and ad clutter** – ready to drop straight into a RAG pipeline or an LLM's context window."* La página de precios lo repite en la lista de features de **todos** los planes: *"**LLM-ready Markdown format**"* y *"**HTML, Markdown, XHR, plus JSON, CSV, PNG where supported**"*. El `/map` devuelve *"HTML, JSON, CSV, or Markdown"*, y el badge del hero de la home es literalmente *"**LLM ready**"*.

## Why It Matters
Es la **tercera vía del vault** para el mismo problema —el de servir datos a un modelo sin pipeline de limpieza— y ninguna de las otras dos lo resuelve en la capa del proveedor:

- **DataImpulse publica su documentación en `llms.txt` y markdown por página**: es un índice para agentes que leen *documentación*, no una extracción de *contenido web* ([[2026-1027-dataimpulse-docs-como-llms-txt-y-markdown-por-pagina]]).
- **Bright Data publica `llms.txt` como índice de su documentación**: el mismo formato, el mismo propósito ([[2026-1026-brightdata-llms-txt-como-indice-de-documentacion-para-agentes]]).
- **Decodo lo aplica al HTML de terceros**: nav bars, banners de cookies y publicidad se eliminan **en el servidor**, antes de que el dato llegue al pipeline.

La diferencia es de arquitectura, no de formato. Un `llms.txt` optimiza lo que el agente *lee de la documentación del proveedor*; el Markdown de Decodo optimiza lo que el agente *recibe de la web arbitraria*. Y para el pipeline de ingesta del vault ([[2026-1022-myclone-scraping-ingestion-pipeline]]) eso decide en qué capa vive el coste: si el HTML crudo llega al vault, la limpieza es **una etapa propia que hay que construir, mantener y pagar por cada sitio**; si el proveedor la hace, la limpieza es **una línea del precio por mil** y el vault solo tiene que parsear Markdown.

El detalle que hace el átomo útil: la limpieza se ofrece **en todos los planes, incluido el gratuito** ("All plans include the same powerful features"), y el formato de salida no se factura como premium. Es decir, la única partida del pipeline que el vault tendría que construir —el extractor de boilerplate— **ya está incluida en el mismo euro por mil** que el resto.

Y hay una lectura más fina: la API devuelve **HTML, Markdown, XHR, JSON, CSV y PNG** en el mismo endpoint, con "where supported". Eso convierte la **unidad de cobro** (crawl o página) en una unidad **independiente del formato de salida**: pagar una página da derecho a su HTML, su Markdown, su JSON, su CSV y su PNG. El vault puede cambiar de formato de entrega sin cambiar de plan.

## Nota de verificación
Frases y listas de features transcritas literalmente de las dos fuentes. La captura **no** publica: cómo se define "nav bars" ni "ad clutter" (si es detección heurística o por reglas), qué se considera boilerplate en cada sitio, si la limpieza degrada la fidelidad del contenido, ni si el formato Markdown es una conversión del HTML ya renderizado o una extracción distinta.

## Nota relacionada
El **Markdown listo para LLM es la novedad que separa esta línea del precio por GB residencial** que ya cubre [[2026-1026-decodo-escalera-mensual-de-375-a-275-por-gb]] y [[2026-1026-decodo-payg-a-4-por-gb-solo-con-wallet-y-un-gb-a-la-vez]]: allí la unidad económica es el byte transferido y el vault tiene que resolver la limpieza por su cuenta; aquí la unidad es el resultado limpio.

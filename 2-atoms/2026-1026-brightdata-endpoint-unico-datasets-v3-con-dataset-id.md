---
id: 2026-1026-brightdata-endpoint-unico-datasets-v3-con-dataset-id
type: atom
certainty: solid
sources: [sources/2026-10-25-brightdata-docs-intro.md]
links: ["[[2026-1026-brightdata-una-sola-api-key-para-todos-los-productos]]", "[[2026-1024-2captcha-flujo-api-en-cinco-pasos-con-captcha-id]]", "[[2026-1022-myclone-scraping-ingestion-pipeline]]"]
---

## Claim
La Scraper API se consume contra **un único endpoint** con un parámetro de catálogo: `POST https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_l1viktl72bvl7bjuj0&format=json`, con cuerpo `[{ "url": "https://www.linkedin.com/in/satyanadella" }]`. La página lo generalize explícitamente: **"The same request pattern works for every scraper: swap the dataset ID and input URL."** Los tres ejemplos (cURL, Python `requests.post`, Node.js `fetch`) son **el mismo POST** con `dataset_id` y `format=json` como query y el array de URLs como cuerpo.

## Why It Matters
El vault ya tiene registrado el patrón **job-id + polling** como la firma de una API asíncrona: 2Captcha documenta cinco pasos con `captcha ID` ([[2026-1024-2captcha-flujo-api-en-cinco-pasos-con-captcha-id]]) y la ingesta de MyClone usa `POST /scraping/...` con `GET /scraping/status/{user_id}` y `GET /scraping/audit/{job_id}` ([[2026-1022-myclone-scraping-ingestion-pipeline]]). **El endpoint de Bright Data no usa ninguno de los dos**: es un POST **síncrono** que devuelve el JSON estructurado en la respuesta, sin identificador de trabajo ni estado que consultar. Eso significa que **el scraper bloquea hasta que el destino responde**, y que la reintentabilidad la gestiona el cliente, no el proveedor.
Es la misma asimetría que ya está en la tabla de coste por insumo del thread: 2Captcha cobra por captcha **resuelto** y su flujo es asíncrono, mientras que aquí el resultado llega **dentro de la misma llamada**. Para un pipeline de ingesta por lotes, la consecuencia práctica es que **el scraping síncrono no se puede paralelizar por HTTP sin abrir N conexiones**, y por tanto el throughput queda atado al tiempo de respuesta del destino, no al número de workers.

## Nota de verificación
Literales transcritos del bloque de código. La captura **no publica**: el número de URLs máximo por petición, el timeout, si existe endpoint asíncrono alternativo, ni el coste en créditos de una llamada.

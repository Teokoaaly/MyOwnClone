---
id: 2026-1024-2captcha-flujo-api-en-cinco-pasos-con-captcha-id
type: atom
certainty: solid
sources: [sources/2026-10-23-2captcha-solver.md]
links: ["[[2026-1024-2captcha-capacidad-libre-por-minuto-como-proxy-de-cola]]", "[[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]]", "[[2026-1022-myclone-scraping-ingestion-pipeline]]"]
---
## Claim
El API de 2Captcha es un flujo asíncrono de **cinco pasos documentados**: 1) el desarrollador sube el captcha, 2) el servicio devuelve un **captcha ID**, 3) el servicio distribuye el captcha a un worker, 4) el worker resuelve el captcha, 5) el desarrollador pide la respuesta usando el ID. Los SDK oficiales están en GitHub (`github.com/2captcha`) y hay páginas de código por lenguaje: Python, PHP, Ruby, Java, Golang, C#, JavaScript.

## Why It Matters
El patrón es el mismo **job-id + polling** que usa la ingesta de MyClone (`/scraping/status/{user_id}`, `/scraping/audit/{job_id}`) en [[2026-1022-myclone-scraping-ingestion-pipeline]]: la captura de hoy no es un input, es un trabajo encolado con identificador. Esto confirma que **el scraping industrial es asíncrono por diseño**, no por contingencia, y que el ID es la única primitive común entre captcha y pipeline de ingesta.
Para el vault, la consecuencia práctica: cualquier integración de este tipo necesita **reintentos, idempotencia y cola**, porque la latencia va de 1 a 17 segundos según el tipo ([[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]]) y la capacidad por minuto está acotada por tipo ([[2026-1024-2captcha-capacidad-libre-por-minuto-como-proxy-de-cola]]).
Nota: la captura **no** publica los nombres de los endpoints, los campos de la respuesta ni los tiempos de expiración del captcha ID.

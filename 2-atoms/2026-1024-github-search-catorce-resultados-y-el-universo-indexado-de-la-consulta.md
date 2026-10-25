---
id: 2026-1024-github-search-catorce-resultados-y-el-universo-indexado-de-la-consulta
type: atom
certainty: solid
sources: [sources/2026-10-24-github-search-chatgpt-account-creator.md]
links: ["[[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]", "[[2026-1024-gptgrok2api-gateway-unificado-gpt-y-grok-en-api-compatible]]", "[[2026-1023-lzt-categoria-llm-accounts-para-reventa]]"]
---

## Claim
La consulta `GET /search/repositories?q=chatgpt+account+creator&sort=stars&order=desc&per_page=20` devuelve `total_count: 14` con `incomplete_results: false`, y los 14 `items` caben íntegros en la página solicitada (14 < 20). El conjunto indexado por GitHub para esa frase es, por tanto, **entero y cerrado en 14 repositorios**, no una muestra ni una cola truncada: no hay paginación pendiente, no hay repositorios más allá del primero ordenados por estrellas, y `score` vale exactamente `1.0` en los 14. La distribución de esa población es: **810 estrellas y 308 forks en total**, con `verssache/chatgpt-creator` (338 estrellas, 90 forks) en primer lugar, `AuuCoder/gptGrok2api` (285, 145) en segundo y `wahdalo/chatgpt-account-creator` (139, 69) en tercero. **Ninguno de los 14 es un fork** (`fork: false` en todos), ninguno está archivado ni deshabilitado, y los 14 son de `visibility: public` y propiedad de un usuario individual (`owner.type: "User"` en todos los casos).

## Why It Matters
Esta es la primera captura del vault que **cifra el tamaño del corpus público** en vez de describir un repo suelto. Hasta ahora el thread de la verificación y la reventa tenía la cadena completa —insumos (SMS, correo, captcha, proxy), herramienta de producción y mercado de destino ([[2026-1023-lzt-categoria-llm-accounts-para-reventa]], [[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]])— pero **nunca había cuantificado cuántos proyectos abiertos existen**. Ahora hay un número: **14 repositorios públicos** indexados por GitHub para esa frase.
El dato tiene una lectura inmediata de mercado: la oferta abierta de herramientas de registro masivo de cuentas de ChatGPT en GitHub es **muy pequeña** —catorce repositorios, de los que solo unos pocos tienen comunidad real. Eso reinforces la lectura de la thread de que la capacidad de producción de cuentas vive más en el circuito cerrado (canales chinos, gateways autoalojados, marketplaces) que en el repositorio público: **el código abierto es la prueba de que la técnica existe, no el lugar donde se opera a escala**.
Y fija un techo metodológico que hay que dejar escrito: 14 es el tamaño del índice **para esa consulta concreta**, no el número de herramientas de registro que existen. La búsqueda de repositorios de GitHub no es un censo de herramientas, y esta captura no permite afirmar nada sobre repositorios que no devuelven esa consulta.

## Nota de verificación
Cifras leídas directamente del JSON de la API de búsqueda (`total_count`, `incomplete_results`, `stargazers_count`, `forks_count`, `fork`, `archived`, `visibility`, `owner.type`, `score`) capturado el 2026-10-24. Los 14 objetos `items` están presentes en la respuesta y se han recorrido todos; la respuesta no está truncada por el límite de `per_page` porque `total_count` (14) es menor que `per_page` (20).

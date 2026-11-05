---
id: 2026-1027-github-search-temp-mail-api-result
type: atom
certainty: solid
sources: [sources/2026-10-27-github-search-temp-mail-api.md]
links: ["[[2026-1027-github-search-temp-mail-api-temp-mail-websites]]", "[[2026-1027-github-search-temp-mail-api-python-wrappers]]"]
---

## Claim

La búsqueda de GitHub por `temp mail api` (q=temp+mail+api, ordenado por estrellas, 20 resultados por página) devolvió 314 repositorios indexados, lo que indica un ecosistema amplio y activo de APIs y wrappers de correo temporal.

## Why It Matters

El conteo de 314 resultados confirma que el correo temporal es una categoría madura en GitHub, con múltiples implementaciones independientes (wrappers, servidores, clientes) en varios lenguajes (Python, JavaScript, Java, C#, Go). Esta diversidad refleja la demanda persistente de direcciones desechables para registro, verificación y privacidad, y proporciona un conjunto de referencia para evaluar la madurez y el abandono de proyectos de temp-mail.

## [FRICTION]

> [[2026-1027-github-search-temp-mail-api-official-service]] afirma que su servicio es "Best Temp Mail API Service" con 23 estrellas y licencia MIT, mientras que [[2026-1027-github-search-temp-mail-api-unofficial-wrappers]] agrupa 4 proyectos wrappers bajo Apache-2.0. Ambas afirmaciones no pueden ser completamente ciertas simultáneamente: el recuento de 314 repositorios incluye tanto proyectos oficiales como no oficiales, y la superposición de funcionalidades (API web + wrappers en múltiples lenguajes) hace difícil atribuir reivindicaciones de exclusividad sin un análisis de cobertura de características.

## Nota de verificación

El campo `total_count: 314` y la lista de `items` con repositorios individuales son **transcripción literal** de la respuesta de la API de GitHub `https://api.github.com/search/repositories?q=temp+mail+api&sort=stars&order=desc&per_page=20`. Los campos `id`, `full_name`, `description`, `language`, `stargazers_count`, `forks_count`, `license` y `topics` de cada item coinciden con los datos brutos de la API. No se verifica la actividad reciente ni el mantenimiento activo de los proyectos listados.
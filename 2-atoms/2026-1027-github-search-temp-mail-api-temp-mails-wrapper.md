---
id: 2026-1027-github-search-temp-mail-api-temp-mails-wrapper
type: atom
certainty: solid
sources: [sources/2026-10-27-github-search-temp-mail-api.md]
links: ["[[2026-1027-github-search-temp-mail-api-result]]", "[[2026-1027-github-search-temp-mail-api-python-wrappers]]"]
---

## Claim

El repositorio `bertigert/temp-mails` (51 estrellas, Python) se describe como "A wrapper around 'all' temp mail sites, aiming to provide a simple to use python api which is similar for all sites", ofreciendo cobertura multiplataforma para múltiples proveedores de correo temporal bajo una sola API unificada.

## Why It Matters

Este proyecto aborda directamente la fragmentación identificada en [[2026-1027-github-search-temp-mail-api-python-wrappers]], al intentar consolidar el acceso a múltiples proveedores de temp-mail a través de una interfaz Python consistente. Al apuntar a "all" temp mail sites, reduce la fricción de tener que elegir entre wrappers individuales por proveedor, y proporciona un punto de integración único para aplicaciones que necesitan soportar múltiples servicios de correo temporal simultáneamente.

## [FRICTION]

> [[2026-1027-github-search-temp-mail-api-python-wrappers]] describe tres wrappers Python distintos sin cobertura unificada, mientras que [[2026-1027-github-search-temp-mail-api-temp-mails-wrapper]] reivindica cobertura "all" under one API. Ambas afirmaciones pueden ser ciertas en distintos grados: el wrapper `temp-mails` puede soportar muchos proveedores, pero probablemente no todos los que existen, y ciertamente no todos los que listan los otros tres wrappers individualmente. La captura no documenta el número exacto de proveedores soportados por `temp-mails` ni los compara con la cobertura de los wrappers individuales.

## Nota de verificación

Los metadatos del repositorio (`stargazers_count: 51`, `language: Python`, `forks_count: 9`, `license: MIT`, `description` tal como aparece en la línea 628 del source) son **transcripción literal** de los campos `items[6]` (índice 0-based) en la respuesta de la API de GitHub. No se verificó la lista real de proveedores soportados, el estado de mantenimiento actual, ni si el proyecto sigue activo o ha sido reemplazado por alternativas más recientes.
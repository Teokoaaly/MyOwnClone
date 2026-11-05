---
id: 2026-1028-astrlink-local-privacy-models
type: atom
certainty: tentative
sources: [sources/2026-10-28-astrlink-github.md]
links: ["[[2026-1028-astrlink-on-device-privacy]]", "[[2026-1028-astrlink-request-records]]"]
---

## Claim

AstrLink's local privacy models must be downloaded or imported separately and are not included in the app package; these models enable on-device sensitive content detection categories and allow redaction and restoration of placeholders in responses.

## Why It Matters

Without a local privacy model, AstrLink falls back to rule-based detection only (regex patterns for secrets, emails, phone numbers). Downloaded models expand detection to categories that cannot be matched by rules alone, enabling more comprehensive redaction and response restoration. Model weights are not distributed with the app to keep the base package small.

## [FRICTION]

> [[2026-1023-5sim-openai-tabla-visible-8-filas]] documenta una tabla de precios de OpenAI visible con 8 filas y categorización de modelos, y [[2026-1023-5sim-openai-76-paises-y-130-operadores]] describe cobertura de OpenAI en 76 países con 130 operadores. Este átomo presiona la creencia de que los modelos de privacidad local son universalmente descargables: la disponibilidad de modelos de privacy detection depende de la conexión a internet, la región geográfica y la cuota de descarga, y no todas las regiones tienen acceso igual a los mismos modelos. AstrLink's model download pipeline puede tener restricciones geográficas o de tasa que no son inmediatas de descubrir. Ambas afirmaciones pueden ser ciertas —los modelos existen y pueden importarse— pero la creencia de que cualquier usuario puede descargarlos sin fricción ignora las barreras de infraestructura y acceso que varían por región. No hay contradicción técnica, pero sí fricción en la suposición de accesibilidad universal.
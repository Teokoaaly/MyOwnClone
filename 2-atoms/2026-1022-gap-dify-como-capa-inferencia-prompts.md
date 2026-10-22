---
id: 2026-1022-gap-dify-como-capa-inferencia-prompts
type: atom
certainty: solid
sources: [raw/articles/myownclone-osint-implementation-plan-2026-06-24.md]
links: ["[[2026-1022-gap-prompt-versioning-clonemodeprompt]]", "[[2026-1022-myclone-prompt-template-sistema]]", "[[2026-1022-arquitectura-rac-tres-modos-por-clon]]"]
---
## Claim
[[myownclone]] usa **Dify como capa de inferencia LLM**, mientras MyClone.is llama a OpenAI directamente. La consecuencia operativa es que todo cambio de prompt debe pasar por Dify, y la **compilación de variables** (`{name}`, `{role}`) debe ocurrir *antes* de enviar al modelo. MyClone.is usa sintaxis `{{variable}}` en sus prompts, y MyOwnClone debe soportarla igual.

## Why It Matters
Es una restricción de arquitectura que condiciona cualquier feature de gobernanza de prompts: no se puede compilar en el prompt de MyClone y "pegar" en Dify, hay que resolver las variables en nuestro backend y enviar el resultado ya interpolado. Por eso el versionado de prompt ([[2026-1022-gap-prompt-versioning-clonemodeprompt]]) debe versionar el prompt *con variables sin resolver* y compilar en el momento del envío — un diseño de dos capas, no uno.
La diferencia de sintaxis `{{variable}}` vs `{variable}` es pequeña pero real: MyOwnClone ya usa placeholders de un solo brace en sus plantillas ([[2026-1022-myclone-prompt-template-sistema]]), así que adoptar la sintaxis de MyClone es una normalización, no un rediseño.
Además, Dify actúa como abstracción sobre el modelo: sirve de compatibilizador con los tres modos por clon ([[2026-1022-arquitectura-rac-tres-modos-por-clon]]) sin exponer el proveedor.

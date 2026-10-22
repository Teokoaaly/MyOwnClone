---
id: 2026-1022-costes-por-categoria-tenant
type: atom
certainty: solid
sources: [raw/articles/myownclone-technical-research.md, raw/articles/myownclone-frontend-recon.md]
links: ["[[myownclone]]", "[[multi-tenant-saas]]", "[[2026-1022-platform-admin-tenants-costes-mrr]]"]
---
## Claim
[[myownclone]] estructura el coste de IA en tres categorías con quién las paga explícito: categoryCloneResponses y categoryIngestion son facturables al tenant, mientras categoryPlatformOps (memoria, embeddings, clasificadores internos) las paga myownclone. El panel de plataforma lo expone con un desglose por proveedor (Anthropic + OpenAI + email) y por eje de consumo (chat vs. ops).

## Why It Matters
La separación entre coste facturable al cliente y coste absorbido por la plataforma es la clave del modelo de margen: el consumo del tenant escala linealmente pero la operación interna no se traslada. Es el mismo esquema que documenta [[multi-tenant-saas]] y que define el pricing por uso de [[myownclone]]. El corte "chat vs. ops" es la lectura operativa que permite saber si el margen se erosiona por uso de producto o por operación interna — ver [[2026-1022-platform-admin-tenants-costes-mrr]].

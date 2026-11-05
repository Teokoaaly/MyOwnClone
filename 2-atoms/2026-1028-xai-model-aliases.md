---
id: 2026-1028-xai-model-aliases
type: atom
certainty: solid
sources: [sources/2026-10-28-xai-models.md]
links: ["[[2026-1028-xai-grok47-flagship]]", "[[2026-1028-xai-model-selector]]"]
---

## Claim
xAI model aliases auto-migrate users to the latest stable version: `<modelname>` tracks the latest stable, `<modelname>-latest` accesses the absolute latest (features-first), and `<modelname>-<date>` locks to a specific release that will never be updated. For most users, the aliased `<modelname>` or `<modelname>-latest` are recommended to receive automatic feature updates.

## Why It Matters
Without explicit alias management, users risk running stale models or unexpectedly gaining/receiving breaking changes. The `<modelname>-<date>` format (e.g., `grok-4.7-20261028`) is essential for workflows requiring consistency and reproducibility, such as pipeline versioning or regulated environments. Meanwhile, `<modelname>-latest` is suitable for feature-first adoption but requires testing since new releases may alter contracts or pricing. This alias system reduces migration friction but shifts responsibility to the user to pin versions when stability is required.

## [FRICTION]
> [[2026-1028-xai-model-selector]] recommends default model choices per modality, while [[2026-1028-xai-model-aliases]] focuses on automatic version migration. Both are needed: selector chooses the model, aliases manage its version. Marcado para juicio humano, no auto-resuelto.
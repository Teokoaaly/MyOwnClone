---
id: 2026-1028-xai-image-restrictions
type: atom
certainty: solid
sources: [sources/2026-10-28-xai-models.md]
links: ["[[2026-1028-xai-imagine-api]]", "[[2026-1028-xai-grok47-flagship]]"]
---

## Claim
xAI image input models have a 20MiB maximum image size, accept jpg/jpeg or png file types with no limit on the number of images, and support any order of image/text input (text prompt can precede image prompt or vice versa). These restrictions apply to all image input models including grok-imagine-image-2.0, grok-imagine-image, and grok-imagine-image-quality.

## Why It Matters
Developers building multimodal pipelines must ensure images are within the 20MiB limit and use supported formats (jpg, jpeg, png). The absence of a per-image count limit means bulk image workflows are not constrained by image quantity, but each image must individually meet the size and format requirements. Mixed text/image prompts are fully supported regardless of input order, which simplifies prompt engineering for image editing and generation use cases.

## [FRICTION]
> [[2026-1028-xai-grok47-flagship]] positions Grok 4.7 as the default for code and general tasks, while [[2026-1028-xai-image-restrictions]] limits direct image input to 20MiB/jpg/png. Users wanting to pass images through the Text API would hit this constraint, forcing a route through the Imagine API instead. Marcado para juicio humano, no auto-resuelto.
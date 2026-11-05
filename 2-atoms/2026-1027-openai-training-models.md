---
id: 2026-1027-openai-training-models
type: atom
certainty: solid
sources: [sources/2026-10-27-openai-usage-policies.md]
links: ["[[2026-1027-openai-terms-liability]]", "[[2026-1027-openai-terms-min-age]]"]
---

## Claim
OpenAI prohibits using models or outputs to generate, prepare, select, or supply training material or signals for models intended as alternatives to or substitutes for OpenAI models/services. This includes creating/preparing training data, tasks, rubrics, or RL environments; providing feedback (labels, scores, rankings, preferences, rewards, corrections); selecting/filtering/validating training data, tasks, or trajectories; attempting to extract protected reasoning through unauthorized access, reverse engineering, or circumvention of safeguards. These restrictions apply whether work is done oneself, for another party, or through someone acting on one's behalf, even if the resulting model is not trained, and also when outputs from product use or evaluation are later used for training purposes.

## Why It Matters
Safeguards trained into OpenAI models must not be transferred or diluted when outputs are used to train other models. Unauthorized transfer of capabilities without safeguards creates unsafe model variants and undermines the policy framework that protects users from harm.

## [FRICTION]
> [[2026-1026-veridrop-json-schema-estricto-y-el-flag-markdown-json-seen]] (escrita el 2026-10-27) trata sobre esquema JSON estricto y flags de markdown, pero el foco es formato de salida y no uso de outputs para entrenamiento. La prohibición de usar outputs de OpenAI para entrenar modelos alternativos podría intersectarse con flujos de investigación de RLHF o fine-tuning, pero la fuente no aborda explícitamente las restricciones de política. Marcado para juicio humano, no auto-resuelto.
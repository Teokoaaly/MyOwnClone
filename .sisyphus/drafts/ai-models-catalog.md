# Draft notes: AI models catalog

This draft captures the stable catalog assumptions for M1-M13 continuation.

## Tasks

- `chat` -> `llm`
- `embedding` -> `embedding`
- `email_classification` -> `llm`
- `email_draft` -> `llm`
- `stt` -> `stt`

## Providers in scope

- `openai`
- `anthropic`
- `minimax`
- `together`
- `openai_compatible`
- `local`

## Non-goals

- No extra providers during Sisyphus execution
- No direct new-code reads from provider env vars except controlled legacy
  fallback in `ModelRegistry`
- No deploy from `master` during this integration lane

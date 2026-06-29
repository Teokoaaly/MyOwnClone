Context
- Phase D: classify every secret in /opt/myownclone/shared/backend.env.production.

Inventory and classification

required and set
- DB_PASSWORD, DB_USER, DB_HOST, DB_PORT, DB_NAME
- DATABASE_URL
- REDIS_PASSWORD
- JWT_SECRET_KEY
- IMPERSONATION_TOKEN_PEPPER
- SECRET_KEY
- ALLOWED_ORIGINS
- SERVICE_API_KEY
- ALLOW_DEV_SERVICE_KEY=false
- WEAVIATE_API_KEY, WEAVIATE_URL
- MINIMAX_API_KEY, MINIMAX_MODEL
- SENDGRID_INBOUND_WEBHOOK_SECRET
- RESEND_API_KEY, RESEND_FROM_EMAIL
- APP_URL
- MODEL_SECRETS_KEY

required and set but not used by active runtime
- OPENAI_API_KEY=""        (empty: STT currently disabled, embedding is local)
- OPENAI_BASE_URL=""       (empty)
- OPENAI_API_BASE=""       (empty)
- OPENAI_MODEL=gpt-4o-mini (legacy default)

required and missing for some flows
- STRIPE_SECRET_KEY=""     (payments disabled)
- STRIPE_WEBHOOK_SECRET="" (payments disabled)
- WHEREBY_API_KEY=""       (video disabled)

legacy and unused
- ANTHROPIC_API_KEY=""
- ANTHROPIC_MODEL=claude-3-haiku-20240307
- TOGETHER_API_KEY=""
- TOGETHER_MODEL=meta-llama/Llama-3-8b-chat-hf

Rotation checklist (immediate)
- SendGrid webhook secret: rotated and verified live.
- Minimax key: production-only, in rotation queue.
- Future STT key: when STT decision is taken, generate here and document.

Action items
- Phase B STT decision is still blocked by absence of OPENAI_API_KEY or any local STT runtime.
- Phase B will not be resolved in this iteration; the current scope is i18n manual selector.
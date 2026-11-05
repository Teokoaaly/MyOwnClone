--- 
id: 2026-1028-newapi-api-token
type: atom
certainty: solid
sources: [sources/2026-10-28-newapi-docs-quickstart.md]
links: ["[[2026-1028-newapi-deployment-methods]]", "[[2026-1028-newapi-channel-configuration]]"]
---

## Claim

Creating an API token in New API involves specifying a token name and associating it with a configured channel — the token then serves as the authentication credential for making unified AI API calls from an application.

## Why It Matters

The API token is the application's key to the New API gateway. Without a valid token, all downstream AI calls are rejected at the gateway level. The token-channel binding also determines which upstream models and channels the application can access, making token scope a critical access control mechanism.

## [FRICTION]

> The quickstart states "create a token for your application and call the unified AI API" as step 3 but provides no format specification, token lifecycle management (rotation, revocation), or permission scoping details — operators must consult the API token management guide to understand how to restrict a token to specific channels or models.

> The quickstart's "Copy Markdown" action is undefined in context: it is unclear whether this copies the quickstart markdown, the channel configuration, or the token definition, creating operational ambiguity for new users attempting to reproduce the workflow.

> No guidance is given on how to embed the token in API calls (header name, format, placement), meaning operators may trial-and-error the Authorization header format instead of finding it documented in one place.
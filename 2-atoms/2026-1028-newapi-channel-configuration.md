--- 
id: 2026-1028-newapi-channel-configuration
type: atom
certainty: solid
sources: [sources/2026-10-28-newapi-docs-quickstart.md]
links: ["[[2026-1028-newapi-deployment-methods]]", "[[2026-1028-newapi-api-token]]"]
---

## Claim

Configuring a channel in New API requires three steps: adding a model provider, supplying credentials (API keys or enterprise contract details), and selecting the available models from that provider — the channel acts as the bridge between the gateway and upstream AI services.

## Why It Matters

The channel configuration is the primary mechanism for routing requests to the correct upstream model. Proper provider setup ensures authentication succeeds, model selection is validated, and features like load balancing, failover, and weighted routing operate as intended. Without a correctly configured channel, all API calls fail with authentication or model-not-found errors.

## [FRICTION]

> The quickstart references "configure a channel" as step 2 but does not define what constitutes a valid provider or which credential formats are accepted (API key vs. bearer token vs. enterprise contract), forcing operators to consult the full channel management guide for basic setup requirements.

> Available models listed in the channel UI are not programmatically enumerable via the API token, creating a discovery gap: operators must log into the management console to see which models are registered, then manually map them to their application's usage.

> Load balancing and failover settings (weighted random, automatic failover) are mentioned in the house rules source but are not exposed or explained in the quickstart, leaving operators unaware that these features require explicit channel configuration beyond simply adding a provider.
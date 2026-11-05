--- 
id: 2026-1028-cto-new-openai-proxy-account-pool
type: atom
certainty: tentative
sources: [sources/2026-10-28-cto-new-openai-proxy.md]
links: ["[[2026-1028-cto-new-openai-proxy-go-reverse-proxy]]", "[[2026-1028-cto-new-openai-proxy-turnstile-friction]]"]
---

## Claim

The account pool uses LRU selection with automatic JWT refresh via the Clerk `__client` cookie, hot-reloading `accounts.jsonl` every 30 seconds, and marks accounts as exhausted (6h cooldown) or dead (current round skipped) based on quota responses and auth status.

## Why It Matters

Each free cto.new account receives ~300 requests/day quota. With a 7-account pool and the ×3 multiplier for GPT-5.4, the aggregate daily capacity reaches ≈700 requests — sufficient for light to moderate workloads without paid tiers. The LRU algorithm ensures even wear across registered accounts, while hot-reload prevents manual intervention when the pool grows.

## Why It Matters (GLM-5.1)

GLM-5.1 carries a ×2 multiplier, yielding ≈1050 daily requests from the same 7-account pool, making it the higher-throughput free option despite GPT-5.4's feature breadth.
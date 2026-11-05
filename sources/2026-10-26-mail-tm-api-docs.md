---
url: https://docs.mail.tm/
captured: 2026-10-26
word_count: 264
status: raw
---

# Temp Mail API

Create temporary email accounts and receive emails via REST API. No API key required.

[Getting Started](https://docs.mail.tm/getting-started/authentication) [OpenAPI Spec](https://api.mail.tm/)

```bash
# 1. Get available domains
curl https://api.mail.tm/domains

# 2. Create account
curl -X POST https://api.mail.tm/accounts \
-H "Content-Type: application/json" \
-d '{"address":"user@domain.com","password":"secret"}'

# 3. Get token
curl -X POST https://api.mail.tm/token \
-H "Content-Type: application/json" \
-d '{"address":"user@domain.com","password":"secret"}'

# 4. Fetch messages
curl https://api.mail.tm/messages \
-H "Authorization: Bearer TOKEN"
```

Workflow

## How it works

Fetch domains

Get available domain names from the API.

Create account

Create a temporary email account with one request.

Use the address

Sign up on sites that require email confirmation.

Message arrives

We receive it and store it for you.

Fetch messages

Fetch messages via the API or listen in real-time with SSE.

Step 0 of 5

Pricing

## Access to the API

Completely free. No API key, no signup, no paid tiers.

- No API key required



Just call the endpoints. No signup, no tokens to start.

- 8 QPS rate limit



The general quota limit is 8 queries per second (QPS) per IP address.


Policy

## Terms of Use

- No illegal activity



Usage of our API for illegal activity is strictly prohibited.

- No reselling



Don't build a paid product that just wraps our API.

- No proxy services



Don't mirror or proxy our API under a different domain.

- Attribution required



If you use our API, link back to mail.tm somewhere visible.


## General Information

The API follows the OpenAPI v3 spec. Download it or explore interactively.

[Download OpenAPI Spec](https://api.mail.tm/docs.jsonld) [Interactive API Docs](https://api.mail.tm/)
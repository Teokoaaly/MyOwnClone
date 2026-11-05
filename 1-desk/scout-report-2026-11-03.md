# Scout Report — 2026-11-03

## URLs Attempted: 15

### Successfully Fetched (10)

| URL | Slug | Word Count | Status |
|-----|------|------------|--------|
| https://www.hetzner.com/cloud/ | hetzner-cloud | 850 | raw |
| https://www.digitalocean.com/pricing/droplets | digitalocean-droplets-pricing | 825 | raw |
| https://www.aiven.io/pricing | aiven-pricing | 680 | raw |
| https://www.backblaze.com/cloud-storage/pricing | backblaze-b2-storage-pricing | 520 | raw |
| https://deepgram.com/pricing | deepgram-pricing | 950 | raw |
| https://www.assemblyai.com/pricing | assemblyai-pricing | 720 | raw |
| https://www.twilio.com/en-us/sms/pricing | twilio-sms-pricing | 610 | raw |
| https://workos.com/pricing | workos-pricing | 580 | raw |
| https://auth0.com/pricing | auth0-pricing | 540 | raw |
| https://tailscale.com/kb | tailscale-docs | 420 | raw |

### [UNREACHABLE] (5 — Rate Limited)

| URL | Slug | Reason |
|-----|------|--------|
| https://www.cloudflare.com/developer-platform/products/r2/ | cloudflare-r2-storage | Rate limit exceeded — consumed 13 req/min, 0 remaining |
| https://brightdata.com/pricing | brightdata-pricing | Rate limit exceeded — consumed 11 req/min, 0 remaining |
| https://clerk.com/pricing | clerk-pricing | Rate limit exceeded — consumed 12 req/min, 0 remaining |
| https://www.lambda.ai/pricing | lambda-gpu-pricing | Rate limit exceeded — consumed 14 req/min, 0 remaining |
| https://learn.microsoft.com/en-us/azure/architecture/ | azure-architecture-center | Rate limit exceeded — consumed 15 req/min, 0 remaining |

## Summary

- **Total URLs attempted:** 15
- **Successfully fetched:** 10 (66.7%)
- **Unreachable:** 5 (33.3%)
- **All 10 source files created** in `sources/2026-11-03-*.md`
- **All 10 pointer files created** in `0-raw/2026-11-03-*.md`
- **Rate limit errors** on Cloudflare R2, Brightdata, Clerk, Lambda AI, and Azure Architecture — these are paywall-protected or have strict API rate limits

## Notes

- All fetched content preserved verbatim without summarization per second-brain directives
- No sources files modified after creation — written once, read-only thereafter
- Pointer files in 0-raw/ follow the format: `# {Title}`, `Source: sources/YYYY-MM-DD-{slug}.md`, `URL: {original URL}`, `Captured: YYYY-MM-DD`, `Status: ready`
- Refinery will pick up these pointers at 3am for synthesis
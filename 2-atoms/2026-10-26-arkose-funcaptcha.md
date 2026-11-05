---
id: 2026-10-26-arkose-funcaptcha
type: atom
certainty: solid
sources: ["sources/2026-10-26-2captcha-pricing-captcha.md"]
links: ["[[2026-10-26-cloudflare-turnstile]]", "[[2026-10-26-normal-captcha]]"]
---

## Claim

Arkose Labs (FunCaptcha) captcha costs $1.45–$50.00 per 1,000 solves with an 18-second solving speed and 578 free capacity per minute.

## Why It Matters

FunCaptcha is the most expensive and slowest captcha type in the pricing table. The $1.45–$50.00 per 1,000 price range is the widest of any captcha type, suggesting variable pricing based on difficulty or negotiation (possibly enterprise). At 18 seconds per 1,000, it is 9x slower than the fastest types (1 second). The free capacity of 578 per minute is among the lowest, making it ill-suited for high-volume operations. This type is best reserved for low-volume, high-security scenarios where the captcha type's difficulty is a requirement.

## [FRICTION]

> [[2026-10-26-normal-captcha]] asserts Normal Captcha costs $0.50–$1.00 per 1,000 with 1-second speed and 12,000 free capacity per minute. FunCaptcha's solving speed (18 sec) is 18x slower, its free capacity (578/min) is ~21x lower, and its minimum price ($1.45) is higher than Normal's maximum ($1.00). All three metrics diverge significantly; both cannot be optimal for the same workload profile.

---
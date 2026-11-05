---
id: 2026-10-26-recaptcha-v3-high
type: atom
certainty: solid
sources: ["sources/2026-10-26-2captcha-pricing-captcha.md"]
links: ["[[2026-10-26-cloudflare-turnstile]]", "[[2026-10-26-recaptcha-v3-low]]"]
---

## Claim

reCAPTCHA v3 with score > 0.3 costs $2.99 per 1,000 solves with a 1-second solving speed and 757 free capacity per minute.

## Why It Matters

reCAPTCHA v3 high-score challenges are the second-most expensive captcha type at $2.99 per 1,000, just below Arkose Labs' entry price. The 1-second solving speed ties for fastest, but the 757 free capacity per minute is extremely low—comparable to reCAPTCHA v3 low-score (also 757/min) despite the higher price. The high price combined with minimal free capacity makes this the least cost-effective fast captcha type for bulk solving. Users pay a premium for what is effectively the same free capacity limit as the low-score variant.

## [FRICTION]

> [[2026-10-26-recaptcha-v3-low]] asserts reCAPTCHA v3 score <= 0.3 costs $1.45 per 1,000 with 1-second speed and 757 free capacity per minute. Both variants share identical solving speed (1 sec) and free capacity (757/min), but the high-score version costs $1.54 more per 1,000. The price differential does not correspond to a measurable difference in speed or capacity, suggesting the price gap may reflect demand-based or enterprise-tier pricing rather than performance differences.

---
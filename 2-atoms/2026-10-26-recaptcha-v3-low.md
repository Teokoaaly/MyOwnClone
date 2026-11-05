---
id: 2026-10-26-recaptcha-v3-low
type: atom
certainty: solid
sources: ["sources/2026-10-26-2captcha-pricing-captcha.md"]
links: ["[[2026-10-26-cloudflare-turnstile]]", "[[2026-10-26-normal-captcha]]"]
---

## Claim

reCAPTCHA v3 with score <= 0.3 costs $1.45 per 1,000 solves with a 1-second solving speed and 757 free capacity per minute.

## Why It Matters

reCAPTCHA v3 low-score challenges are the most expensive per free capacity unit among the fast captcha types. At $1.45 for only 757 free solves per minute, the effective cost per free solve is higher than Turnstile's 2,883/minute at the same price point. The 1-second solving speed is tied for fastest, but the minimal free capacity makes it less viable for high-volume workloads.

## [FRICTION]

> [[2026-10-26-cloudflare-turnstile]] asserts Turnstile costs $1.45 per 1,000 with 2-second speed and 2,883 free capacity per minute. Both share the same price point, but Turnstile offers 4x the free capacity and half the solving speed per 1,000. Both cannot simultaneously offer the best free capacity and the fastest solving speed at this price.

---
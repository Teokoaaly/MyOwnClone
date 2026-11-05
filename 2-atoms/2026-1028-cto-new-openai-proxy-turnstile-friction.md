--- 
id: 2026-1028-cto-new-openai-proxy-turnstile-friction
type: atom
certainty: tentative
sources: [sources/2026-10-28-cto-new-openai-proxy.md]
links: ["[[2026-1028-cto-new-openai-proxy-go-reverse-proxy]]", "[[2026-1028-cto-new-openai-proxy-account-pool]]"]
---

## Claim

The cto.new sign-up page uses Cloudflare invisible Turnstile, which throttles same-IP bulk registration (401 errors), requiring IP rotation or manual intervention; cookie refresh via `/sign-in` bypasses Turnstile entirely.

## Why It Matters

Same-IP automated registration triggers Cloudflare risk control within minutes. Users must either configure proxies (SOCKS5 or `--proxy-server`), register in hourly batches, or rely on the `cto_login_refresh.py` script that walks through `/sign-in` (no Turnstile) to recover valid `__client` cookies from existing accounts.

## [FRICTION]

> [[2026-10-26-cloudflare-turnstile]] (escrita hace días) mide el costo y la capacidad de Turnstile vs reCAPTCHA, pero el problema aquí es específico a cto.new's `/sign-up` endpoint y a su política de rate-limit por IP, que no se mapea directamente a los datos de precio y capacidad de las notas de captcha. El umbral de "short time" no está cuantificado en ninguna de las dos notas, lo que dificulta una resolución cruzada.
---
id: 2026-1024-2captcha-hcaptcha-y-geetest-ausentes-del-catalogo-publicado
type: atom
certainty: solid
sources: [sources/2026-10-23-2captcha-solver.md]
links: ["[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1024-2captcha-capacidad-libre-por-minuto-como-proxy-de-cola]]", "[[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]]"]
---
## Claim
La lista "Supported captchas" de la captura enumera **diez tipos**: reCAPTCHA v2, reCAPTCHA v2 Callback, reCAPTCHA v2 Invisible, Image Captcha, Cloudflare Turnstile, reCAPTCHA v3, reCAPTCHA Enterprise, Arkose Labs captcha (FunCaptcha), Amazon captcha y ALTCHA. **No aparecen hCaptcha ni Geetest** en ninguna parte de la página, y la tabla de precios solo muestra **ocho filas** (las dos ausentes son las variantes Callback e Invisible, que sí figuran en la lista de soportados) tras un botón "Show more".

## Why It Matters
Dos consecuencias prácticas para el vault. Primera: **la captura es parcial** — hay un "Show more" sin expandir, así que el catálogo real de precios y capacidades es al menos más grande que ocho filas; el vault solo puede atomizar lo visible. Segunda: **hCaptcha y Geetest no están en el escaparate**, lo que no significa que no se resuelvan (pueden estar tras el "Show more" o en páginas de producto no capturadas), pero sí que **no se pueden comprar como producto de catálogo publicado**.
Esto importa al elegir proveedor: si un destino de scraping usa hCaptcha, el coste y la latencia de esa resolución no se pueden cotizar con esta fuente. Para los tipos visibles, en cambio, la dispersión es enorme: de $0.5 a $50 por mil ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]), de 1 a 17 segundos ([[2026-1024-2captcha-velocidad-de-resolucion-1-a-2-segundos-en-los-tipos-estandar]]), de 203 a 12.000 de capacidad por minuto ([[2026-1024-2captcha-capacidad-libre-por-minuto-como-proxy-de-cola]]).
Nota: la captura **no** permite afirmar que hCaptcha o Geetest no se soporten; solo que no constan en la página capturada.

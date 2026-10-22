---
id: 2026-1022-sin-rate-limiting
type: atom
certainty: solid
sources: [raw/articles/myownclone-vulnerabilities-confirmed.md]
links: ["[[myownclone]]", "[[2026-1022-cors-wildcard-en-login-y-registro]]", "[[2026-1022-auth-otp-impersonacion-30min]]", "[[2026-1022-sin-headers-de-seguridad]]"]
---
## Claim
[[myownclone]] no aplica rate limiting: diez peticiones rápidas consecutivas devolvieron todas HTTP 200, sin bloqueo, throttling ni respuesta 429.

## Why It Matters
Sin rate limiting, cualquier superficie que costs recursos —login, OTP, envío de feedback, o las Server Actions de mutación que son el único canal de escritura del producto según [[2026-1022-mutaciones-rsc-sin-api-rest]]— es susceptible de abuso automatizado. Combinado con el CORS wildcard de [[2026-1022-cors-wildcard-en-login-y-registro]] en `/login` y `/registro`, un atacante puede automatizar fuerza bruta de credenciales o de OTP desde cualquier origen sin fricción ni detección. Es también el agravante que hace más grave la ausencia de headers de seguridad de [[2026-1022-sin-headers-de-seguridad]]: no hay ni una sola capa de control en el borde que compense el lado servidor.

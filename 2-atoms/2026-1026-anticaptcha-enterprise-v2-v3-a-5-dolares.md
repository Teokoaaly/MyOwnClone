---
id: 2026-1026-anticaptcha-enterprise-v2-v3-a-5-dolares
type: atom
certainty: solid
sources: [sources/2026-10-25-anti-captcha-pricing.md]
links: ["[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1024-2captcha-arkose-funcaptcha-50-dolares-por-1000]]", "[[2026-1026-anticaptcha-trece-tipos-con-precio-por-1000]]", "[[2026-1026-anticaptcha-arkose-labs-a-3-dolares-por-1000]]"]
---

## Claim
AntiCaptcha publica **reCAPTCHA Enterprise v2/v3 a $5 por 1000**, precio único y cerrado, con 5 s de resolución y tarea `RecaptchaV2EnterpriseTaskProxyless`. Es **el techo del catálogo** y el único tipo que duplica el precio del siguiente escalón (los demás tipos de la tabla están en $0.5–$3).

## Why It Matters
Es el **outlier del catálogo de un solo proveedor**, y su valor está en ser **contrapunto directo** a la tabla de 2Captcha, donde reCAPTCHA Enterprise costaba **$1 — $2.99 por 1000** y era un tipo más del rango medio ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]). Mismo tipo, **1,7× a 5× más caro** según el proveedor.
La lectura para el vault, en contraste con el precio de $1 — $2.99 de 2Captcha para el mismo tipo ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]): **Enterprise es el tipo donde la diferencia entre proveedores es máxima en proporción** — $5 contra $2.99 — y por tanto el peor tipo para decidir "captcha = commodity barata sin discriminar proveedor". Si el destino de scraping usa reCAPTCHA Enterprise (que es justamente el caso de los sitios de alto valor), la elección de solver **sí mueve el presupuesto por mil de forma material**: 5× entre $1 y $5.
El vault ya tenía el Arkose a $50 como outlier del otro catálogo ([[2026-1024-2captcha-arkose-funcaptcha-50-dolares-por-1000]]): aquí el outlier es Enterprise, y el Arkose cae a $3 ([[2026-1026-anticaptcha-arkose-labs-a-3-dolares-por-1000]]). Y hay un detalle estructural que la captura sí da y que es raro en este corpus: el nombre de la tarea es **`RecaptchaV2EnterpriseTaskProxyless`** — es decir, la resolución es **proxyless**, el cliente aporta su propio contexto de proxy/IP. Eso significa que el precio de $5 es **solo el captcha**: el coste de red sigue corriendo aparte, lo que rompe la lectura de "comprar resolución = coste cerrado".
Nota: la captura **no** publica si hay surcharge por IP o por geo del proxy, ni qué variante de Enterprise cubre la fila (v2 y v3 en la misma fila).

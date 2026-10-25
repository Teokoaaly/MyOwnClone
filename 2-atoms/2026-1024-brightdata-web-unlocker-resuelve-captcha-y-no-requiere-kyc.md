---
id: 2026-1024-brightdata-web-unlocker-resuelve-captcha-y-no-requiere-kyc
type: atom
certainty: solid
sources: [sources/2026-10-24-brightdata-proxy-pricing.md]
links: ["[[2026-1024-brightdata-kyc-para-residencial-y-movil-pero-web-unlocker-no]]", "[[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]", "[[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]"]
---

## Claim
Bright Data recomienda Web Unlocker como la herramienta de scraping en lugar del proxy crudo: *"The Web Unlocker uses either a Datacenter or Residential IP and fully handles all of the unblocking, including CAPTCHA solving and automated retries. Your scraper/crawler simply sends a query to Web Unlocker and all the unblocking is done in the background."* Y añade la frase que la hace comprable sin fricción: *"Using Web Unlocker does not require going through the KYC process."*

## Why It Matters
Es el mismo giro de producto que ya se registró en 2Captcha —el proveedor que vendía eludir controles pasa a vender **el servicio que los elude por ti**, con Browser API, Scraper API, Web Unlocker y servidores MCP para agentes ([[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]])— y aquí tiene un efecto añadido: **elimina el KYC**, que es la barrera que bloquea el pool residencial ([[2026-1024-brightdata-kyc-para-residencial-y-movil-pero-web-unlocker-no]]).
Para el vault esto tiene una consecuencia aritmética directa: si el scraper **no** tiene que resolver el captcha por su cuenta, desaparece una partida del coste por insumo — la de 2Captcha, entre $0.0005 y $0.05 por captcha ([[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]])— y se reabsorbe en el precio del tráfico. Es decir, **el CAPTCHA puede dejar de ser una línea del modelo de coste** y pasar a ser un recargo implícito del $/GB. Lo que la captura **no** publica es el precio de Web Unlocker, de modo que el ahorro en captcha no se puede cuantificar contra el coste del tráfico.

## Nota de verificación
Texto transcrito literalmente. La captura **no** publica: el precio de Web Unlocker ni su unidad (por GB, por request o por CAPTCHA resuelto), si es un producto independiente del plan de proxy, ni los reintentos automáticos incluidos.

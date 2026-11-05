---
id: 2026-1026-decodo-web-data-api-moneyback
type: atom
certainty: solid
sources: [0-raw/2026-10-26-decodo-web-data-api-pricing.md]
links: ["[[2026-1026-decodo-reembolso-14-dias-con-limite-del-20-y-10-de-trafico]]", "[[2026-1027-decodo-web-data-api-ocho-planes-mensuales-con-limite-de-crawls-y-paginas]]"]
---

## Claim

Todas las ocho planes de la **Web Data API** de Decodo incluyen la etiqueta **"14-day money-back"**. El FAQ de la home confirma que la API **no exige tarjeta** para el plan gratuito: "You can start using Web Data API with a free starter plan without a credit card. Sign up, test your requests, and upgrade when you need more capacity". La garantía de 14 días hereda la etiqueta de la línea residencial, pero **las condiciones no se trasladan**: las condiciones de la garantía residencial (primera compra, no haber usado la prueba de 3 días, 20 % del tráfico residencial o 10 % del Enterprise, cuenta no suspendida y sin contracargo) no tienen equivalente en el modelo de crawling por páginas de la API.

## Why It Matters

En la línea de scraping, donde la unidad es crawl o página, **ninguna de las condiciones de la garantía residencial tiene equivalente directo**: ¿qué sería el "20 % del tráfico" de un plan cuyo límite son 9,9M páginas? La captura solo publica la etiqueta "14-day money-back" sin condiciones aplicables a la API. El vault debe citar **"14-day money-back" como etiqueta sin condiciones para la API**, y no extenderla por analogía a las condiciones de la línea residencial.
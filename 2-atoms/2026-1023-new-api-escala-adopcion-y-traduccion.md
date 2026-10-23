---
id: 2026-1023-new-api-escala-adopcion-y-traduccion
type: atom
certainty: solid
sources: [sources/2026-10-22-new-api-github.md]
links: ["[[2026-1023-new-api-gateway-unificado-de-modelos]]", "[[2026-1023-midjourney-proxy-popularidad-y-actividad-del-repo]]", "[[2026-1023-priceai-transit-canal-tipo-sub2api-vs-new-api]]"]
---

## Claim
Los números de la cabecera del repositorio en la captura del 2026-10-22: **50,5k stars**, **12,2k forks**, **162 watchers**, **6.608 commits** en `main`, **15 branches** y **711 tags**. El último commit es de hace 6 horas (22 de octubre de 2026, `fix(channels): preserve advanced custom body passthrough settings #7971`) y el historial muestra trabajo diario: el día anterior se subió **Go a 1.26.10 por CVE-2026-111943** (#7942). Topics: `ai-gateway`, `claude`, `deepseek`, `gemini`, `newapi`, `openai`, `rerank`. La consola web está disponible en **7 idiomas** (inglés, chino simplificado y tradicional, francés, japonés, ruso y vietnamita) y el README está en 5 variantes de idioma. La sección de *Trusted Partners* cita **Cherry Studio, Aion UI, Universidad de Peking, Alibaba Cloud e IO.NET**; JetBrains aporta licencia de desarrollo open source gratuita y el proyecto aparece destacado en HelloGitHub y AtomGit G-Star.

## Why It Matters
El contraste de curva con Midjourney-Proxy es el dato del vault: aquel tenía 5,4k stars pero **código congelado desde junio de 2024** ([[2026-1023-midjourney-proxy-popularidad-y-actividad-del-repo]]); New API tiene 50,5k stars y **6.608 commits con actividad del mismo día de la captura**. Aquí la popularidad sí se ha convertido en mantenimiento — y eso cambia el cálculo de riesgo de auto-hospedar: no se hereda un proyecto abandonado sino uno que cambia rápido.
Ese "cambia rápido" tiene su cara oculta: el README advierte que **`latest` sigue las builds publicadas y puede cambiar**, y que hay que **fijar versión desde Releases, revisar las notas de upgrade y hacer backup antes de actualizar**. Un proyecto con 6.608 commits y CVE de Go parcheados ayer es un proyecto cuya API de administración y sus defaults cambian con frecuencia.
El dato de los 7 idiomas y los partners (Peking University, Alibaba Cloud, IO.NET) mide la **penetración institucional**: esto no es un experimento personal, es infraestructura de gateway ampliamente desplegada, lo que refuerza que los 8 canales "New API" del ranking de PriceAI ([[2026-1023-priceai-transit-canal-tipo-sub2api-vs-new-api]]) son el camino estándar y no una excentricidad.

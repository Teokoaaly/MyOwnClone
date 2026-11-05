---
id: 2026-1026-noones-notificaciones-de-actividad-de-trade-como-capacidad-de-la-api
type: atom
certainty: tentative
sources: [sources/2026-10-25-noones-developer-api.md]
links: ["[[2026-1026-noones-api-dos-formatos-directo-y-delegado]]", "[[2026-1026-noones-bot-de-saludo-al-iniciar-el-trade]]", "[[2026-1024-noones-limite-diario-suma-de-todas-las-operaciones-en-24h]]", "[[2026-1026-noones-dev-noones-sin-precios-ni-limites-ni-documentacion-publica]]", "[[2026-1022-myclone-widget-comunicacion-websocket]]"]
---

## Claim
El segundo de los cuatro bullets de cabecera de `dev.noones.com` es **"Receive trade activity notifications"**, y entre los beneficios declarados de la API está "decrease trade times". La captura **no dice** si esas notificaciones son webhooks, push, email o polling, ni publica latencia, ni frecuencia, ni si hay límite de tráfico. Es una capacidad **enumerada, no documentada**.

## Why It Matters
Las notificaciones son la pieza que hace posible un bot que **reacciona** en lugar de **sondea**: sin un evento push fiable, "automate your trading" se convierte en un polling agresivo, y el polling agresivo choca con los límites agregados por ventana de 24 h que el vault ya tiene registrados para NoOnes ([[2026-1024-noones-limite-diario-suma-de-todas-las-operaciones-en-24h]]). Es el mismo tipo de hueco que el vault marcó en otras APIs: la capacidad existe en el marketing y el mecanismo no está. `certainty: tentative` porque el único texto disponible es la línea del bullet, sin ninguna página de caso de uso que la desarrolle ([[2026-1026-noones-dev-noones-sin-precios-ni-limites-ni-documentacion-publica]]). Y es el reverso del patrón que el producto propio sí resolvió: **push por websocket contra polling por HTTP** ([[2026-1022-myclone-widget-comunicacion-websocket]]) es exactamente la decisión que esta API deja sin especificar.
